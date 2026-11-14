from PIL import Image

im = Image.open('assets/inspect_master/crop_pc_region.jpg').convert('L')
t = im.resize((65, 18))
chars = ' .:-=+*#%@'
print('=== crop_pc_region ===')
for y in range(18):
    print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(65)))

