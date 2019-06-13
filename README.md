# Overview
This script was written to facilitate converting the [PRImA Layout Analysis Dataset](https://www.primaresearch.org/datasets/Layout_Analysis) into an RGB masked format compatible with training the [dhSegment](https://github.com/dhlab-epfl/dhSegment) model. The dataset is comprised of 478 individual pages masked off in the PAGE XML format alongside the images. I would think this script could be more generally applied to convert most datasets comprised of images + PAGE XML metadata into RGB masked images suitable for training.

# Map of colors to region types
The basic map is defined at lines 16-27 of converter.py and can be modified to suit. For example if you want to combine multiple region types into a single color you simple modify the map accordingly and the script should do the right thing (hopefully).

## The current color -> region type map as a table
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

Peace out and good luck,

Ron