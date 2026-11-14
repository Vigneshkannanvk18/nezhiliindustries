from PIL import Image

im = Image.open('assets/inspect_master/cover_detail.jpg').convert('L')
t = im.resize((60, 20))
chars = ' .:-=+*#%@'
print('=== cover_detail ===')
for y in range(20):
    print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(60)))

