import os
from PIL import Image

for name in ['r1_c0', 'r1_c1', 'r1_c2', 'r3_c0', 'r3_c1', 'r3_c3', 'r3_c4']:
    fn = f'assets/master_subparts/part_{name}.jpg'
    im = Image.open(fn).convert('L')
    thumb = im.resize((50, 14))
    chars = ' .:-=+*#%@'
    print(f'==={name}===')
    for y in range(14):
        print(''.join(chars[thumb.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(50)))

