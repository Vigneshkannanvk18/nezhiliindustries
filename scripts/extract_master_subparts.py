import os
from PIL import Image

im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size
print(f'Master size: {w}x{h}')

# Let's save a fine grid of 5 columns and 4 rows (20 sub-regions)
os.makedirs('assets/master_subparts', exist_ok=True)
gw = w // 5
gh = h // 4
for r in range(4):
    for c in range(5):
        crop = im.crop((c * gw, r * gh, (c + 1) * gw, (r + 1) * gh))
        crop.save(f'assets/master_subparts/part_r{r}_c{c}.jpg')

print('Saved 20 subparts to assets/master_subparts/')

