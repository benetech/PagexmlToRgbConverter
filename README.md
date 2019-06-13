# Overview
This script was written to facilitate converting the [PRImA Layout Analysis Dataset](https://www.primaresearch.org/datasets/Layout_Analysis) into an RGB masked format compatible with training the [dhSegment](https://github.com/dhlab-epfl/dhSegment) model. The dataset is comprised of 478 individual pages masked off into various region types specified by the PAGE XML specification. I would think this script could be more generally applied to convert most datasets comprised of images + PAGE XML metadata into RGB masked images suitable for training.

# Map of colors to region types
The basic map is defined at lines 16-27 and can be modified to suit. For example if you want to combine multiple region types into a single color you simple modify the map accordingly and the script should do the right thing (hopefully).

Peace out and good luck,

Ron