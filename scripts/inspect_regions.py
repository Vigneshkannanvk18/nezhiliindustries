import os
from PIL import Image
import numpy as np

# In WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg:
# Let's see what objects exist.
im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size

# Let's check color clusters or features of objects
# The background is white/light grey table.
# Any object has colors or shadows.
# Let's print out what is at various regions:
# top-left, top-mid, top-right, mid-left, center, mid-right, bottom-left, bottom-mid, bottom-right
regions = [
    ('top-left', 0.05, 0.20, 0.35, 0.50),
    ('top-mid', 0.35, 0.20, 0.65, 0.50),
    ('top-right', 0.65, 0.20, 0.95, 0.50),
    ('mid-left', 0.05, 0.45, 0.35, 0.75),
    ('mid-center', 0.35, 0.45, 0.65, 0.75),
    ('mid-right', 0.65, 0.45, 0.95, 0.75),
    ('bot-left', 0.05, 0.70, 0.35, 0.95),
    ('bot-mid', 0.35, 0.70, 0.65, 0.95),
    ('bot-right', 0.65, 0.70, 0.95, 0.95),
]

for name, x1, y1, x2, y2 in regions:
    crop = im.crop((int(x1*w), int(y1*h), int(x2*w), int(y2*h)))
    crop.save(f'assets/inspect_master/reg_{name}.jpg')
    arr = np.array(crop)
    # Check non-background pixels (darker than 190 or colored)
    non_bg = np.sum((arr[:,:,0] < 180) | (arr[:,:,1] < 180) | (arr[:,:,2] < 180))
    print(f'{name:12}: non_bg pixels = {non_bg} / {crop.width * crop.height}')

