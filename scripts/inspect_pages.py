import os
from PIL import Image

for i in [2, 3, 4, 5, 6, 8]:
    f = f'assets/extracted/page{i}_body.jpg'
    if os.path.exists(f):
        im = Image.open(f)
        print(f'Page {i} body: {im.size}')
        # Check if there are sub-images or components inside
        # Save crops of left and right of page body
        left = im.crop((0, 0, im.width//2, im.height))
        right = im.crop((im.width//2, 0, im.width, im.height))
        left.save(f'assets/inspect_master/page{i}_left.jpg')
        right.save(f'assets/inspect_master/page{i}_right.jpg')

