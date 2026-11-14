import os
from PIL import Image

im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size

# Let's test a few crops around the optical cover:
crops = [
    # (x1, y1, x2, y2) in 0..1
    ('opt_v1', (0.58, 0.22, 0.84, 0.48)),
    ('opt_v2', (0.56, 0.20, 0.86, 0.50)),
    ('opt_v3', (0.59, 0.23, 0.82, 0.46)),
    ('opt_v4', (0.55, 0.18, 0.85, 0.52)),
]

for name, cr in crops:
    x1, y1, x2, y2 = int(cr[0]*w), int(cr[1]*h), int(cr[2]*w), int(cr[3]*h)
    crop = im.crop((x1, y1, x2, y2))
    crop.save(f'assets/inspect_master/{name}.jpg')
    print(f'{name}: {crop.size}')

