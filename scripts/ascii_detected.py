from PIL import Image

for i in [17, 18, 19, 22, 23]:
    fn = f'assets/detected_parts/part_{i:02d}.jpg'
    im = Image.open(fn).convert('L')
    t = im.resize((50, 15))
    chars = ' .:-=+*#%@'
    print(f'=== Part {i:02d} ===')
    for y in range(15):
        print(''.join(chars[t.getpixel((x, y)) * (len(chars)-1) // 255] for x in range(50)))

