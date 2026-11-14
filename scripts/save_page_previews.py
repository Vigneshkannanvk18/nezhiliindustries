import os
from PIL import Image

for i in [2, 3, 4, 5, 6, 8]:
    fn = f'assets/extracted/page{i}_body.jpg'
    if os.path.exists(fn):
        im = Image.open(fn)
        # downsample and save to inspect
        im.resize((500, int(500 * im.height / im.width))).save(f'assets/inspect_master/page{i}_body_preview.jpg')

print('Saved body previews')

