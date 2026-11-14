import os
from PIL import Image
import numpy as np

for name in ['top-left', 'top-mid', 'top-right', 'mid-left', 'mid-center', 'mid-right', 'bot-left', 'bot-mid', 'bot-right']:
    fn = f'assets/inspect_master/reg_{name}.jpg'
    im = Image.open(fn)
    arr = np.array(im)
    # Check dominant colors
    r, g, b = arr[:,:,0].astype(float), arr[:,:,1].astype(float), arr[:,:,2].astype(float)
    # Saturation / color identification
    is_yellow = (r > 150) & (g > 130) & (b < 100)
    is_orange_red = (r > 150) & (g < 100) & (b < 80)
    is_black_dark = (r < 70) & (g < 70) & (b < 70)
    is_white_clear = (r > 190) & (g > 190) & (b > 190)
    is_blue = (b > 120) & (b > r + 30)
    
    print(f'=== {name} ===')
    print(f'  Yellow: {np.sum(is_yellow)}, Red/Orange: {np.sum(is_orange_red)}, Dark/Black: {np.sum(is_black_dark)}, White/High: {np.sum(is_white_clear)}, Blue: {np.sum(is_blue)}')

