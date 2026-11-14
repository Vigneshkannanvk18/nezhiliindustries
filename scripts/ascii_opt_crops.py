from PIL import Image

for name in ['opt_v1', 'opt_v2', 'opt_v3']:
    im = Image.open(f'assets/inspect_master/{name}.jpg').convert('L')
    t = im.resize((60, 16))
    chars = ' .:-=+*#%@'
    print(f'=== {name} ===')
    for y in range(16):
        print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(60)))

