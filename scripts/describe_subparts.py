import os
from PIL import Image
import numpy as np

for r in range(4):
    for c in range(5):
        fn = f'assets/master_subparts/part_r{r}_c{c}.jpg'
        im = Image.open(fn)
        arr = np.array(im)
        mean_val = arr.mean(axis=(0,1)).round(1)
        # Check standard deviation (texture/detail)
        std_val = arr.std(axis=(0,1)).round(1)
        # If std_val is high, there is a prominent object
        if np.mean(std_val) > 15:
            print(f'r{r}_c{c}: mean={mean_val}, std={std_val}')

