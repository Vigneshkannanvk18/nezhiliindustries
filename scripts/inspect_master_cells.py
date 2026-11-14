import os
from PIL import Image

# Inspect WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg in detail
im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size
print(f'Master image size: {w}x{h}')

# Let's save 6 horizontal slices and 6 vertical slices to understand the layout of components
os.makedirs('assets/inspect_master', exist_ok=True)
# Save 4x4 sub-images
gw, gh = w // 4, h // 4
for r in range(4):
    for c in range(4):
        crop = im.crop((c * gw, r * gh, (c + 1) * gw, (r + 1) * gh))
        crop.save(f'assets/inspect_master/cell_{r}_{c}.jpg')

print('Saved 16 cells in assets/inspect_master/')

