from PIL import Image

for p in [4, 5, 6, 7]:
    hdr = Image.open(f'assets/extracted/page{p}_header.jpg').convert('L')
    # ASCII of header
    t = hdr.resize((60, 10))
    chars = ' .:-=+*#%@'
    print(f'=== Page {p} Header ===')
    for y in range(10):
        print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(60)))

