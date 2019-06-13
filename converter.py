#!/usr/bin/env python3.6

import os
import pprint
import sys

from glob import glob
from pathlib import Path
from bs4 import BeautifulSoup
from PIL import Image, ImageDraw

images_dir = "/home/rkeiii/tmp/coolds/primabig/PRImA Layout Analysis Dataset/Images"
xml_dir = "/home/rkeiii/tmp/coolds/primabig/PRImA Layout Analysis Dataset/XML"
masked_images_dir = "/home/rkeiii/tmp/coolds/primabig/PRImA Layout Analysis Dataset/RGB Masked Images"

region_type_to_color = {
    "ChartRegion":      (255,0,0), # red
    "DrawingRegion":    (0,255,0), # green
    "FrameRegion":      (0,0,255), # blue
    "GraphicRegion":    (255,255,0), # yellow
    "ImageRegion":      (0,255,255), # cyan
    "MathsRegion":      (255,138,0), # orange 
    "NoiseRegion":      (255,0,255), # pink
    "SeparatorRegion":  (150,0,255), # purple
    "TableRegion":      (0,100,25), # dark green
    "TextRegion":       (128,128,128) # grey
}

image_count = 1

# iterate over each original image file
for imagef in os.listdir(images_dir):
    basename = imagef.split(".")[0]

    print("%d) processing base name %s" % (image_count, basename))

    with Image.open("%s/%s" % (images_dir, imagef)) as image:
        # create a new image with the same dimensions as the original and a white background
        new_image = Image.new('RGB', image.size, color = 'white')
        draw = ImageDraw.Draw(new_image)

        # find the XML file associated with this image
        for xmlf in glob("%s/*%s*" % (xml_dir, basename)):
            # open associated PAGE XML file for parsing
            with open(xmlf) as file:
                soup = BeautifulSoup(file, 'lxml')
            
                # search XML for each region type
                for region_type in region_type_to_color.keys():
                    # iterate over region tags for the specified type
                    # bs4 likes to deal with lower case tag names
                    for region_tag in soup.find_all(region_type.lower()):
                        points = region_tag.findChildren("point", recursive=True)
                        coordinate_array = []

                        # iterate over each point in the polygon
                        for point in points:
                            coordinate_array.append((int(point["x"]), int(point["y"])))

                        # if we have coordinates draw our polygon
                        if len(coordinate_array) > 1:
                            draw.polygon(coordinate_array, fill=region_type_to_color[region_type])
        
        # write out the image
        new_image.save("%s/%s.png" % (masked_images_dir, basename), "PNG")

        image_count += 1
