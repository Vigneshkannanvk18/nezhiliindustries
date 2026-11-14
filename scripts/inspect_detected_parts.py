import cv2
import numpy as np

for i in [12, 17, 18, 10, 19, 21, 22, 23, 15, 20]:
    fn = f'assets/detected_parts/part_{i:02d}.jpg'
    img = cv2.imread(fn)
    if img is not None:
        mean_bgr = img.mean(axis=(0,1)).round(1)
        # convert to RGB
        mean_rgb = [mean_bgr[2], mean_bgr[1], mean_bgr[0]]
        print(f'Part {i:02d}: shape={img.shape}, mean_rgb={mean_rgb}')

