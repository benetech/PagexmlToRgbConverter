# Overview
This script was written to facilitate converting the [PRImA Layout Analysis Dataset](https://www.primaresearch.org/datasets/Layout_Analysis) into an RGB masked format compatible with training various image segmentation models. The dataset is comprised of 478 individual pages images in TIF format and associated masking metadata in PAGE XML format alongside the images.

# System Requirements
This script has only ever been tested on Ubuntu 18.04 but I would expect it would probably work on other *nix platforms (and who knows, maybe even Windows?)
* Python 3.6
* BeautifulSoup 4
* Pillow

# Mapping of colors to region types
The basic map is defined at lines 16-27 of converter.py and can be modified to suit. Colors are described in RGB notation. For example if you want to combine multiple region types into a single color you simple modify the map accordingly and the script should do the right thing (hopefully).

## The default color to region type mapping
| Region Type | Region Color Code |
|-------------|-------------------|
|ChartRegion|255,0,0|
|DrawingRegion|0,255,0|
|FrameRegion|0,0,255|
|GraphicRegion|255,255,0|
|ImageRegion|0,255,255|
|MathsRegion|255,138,0|
|NoiseRegion|255,0,255|
|SeparatorRegion|150,0,255|
|TableRegion|0,100,25|
|TextRegion|128,128,128|

# Region outlines
If you would like to have an outline drawn around the RGB masked regions you'll want to set the region_outline variable to a three digit RGB tuple for the color you want to use for the outline in converter.py.

# How to run the converter.py script
The converter.py script expects to be provided three directories as input arguments. Additionally it also operates under the assumption that ground truth images and their associated PAGE XML metadata files will share the same base name. For example if you have a ground truth image called coolpic.jpg converter.py will expect the associated PAGE XML metadata to be called coolpic.xml.

## converter.py args
1. Directory containing ground truth images
2. Directory containing ground truth metadata in PAGE XML format
3. Directory where output images with RGB masks applied should be stored

## converter.py usage example
./converter.py /path/to/ground_truth_images /path/to/ground_truth_pagexml /path/to/output_rgb_masked_images