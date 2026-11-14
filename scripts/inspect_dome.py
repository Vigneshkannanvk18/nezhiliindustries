from PIL import Image
import numpy as np

im = Image.open('assets/inspect_master/meter_cover_candidate.jpg')
arr = np.array(im)
print('Shape:', arr.shape)
print('Min RGB:', arr.min(axis=(0,1)))
print('Max RGB:', arr.max(axis=(0,1)))
print('Mean RGB:', arr.mean(axis=(0,1)).round(1))

t = im.convert('L').resize((60, 20))
chars = ' .:-=+*#%@'
print('=== meter_cover_candidate ===')
for y in range(20):
    print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(60)))

