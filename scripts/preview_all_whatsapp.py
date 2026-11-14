import glob
from PIL import Image

files = sorted(glob.glob('WhatsApp Image*.jpeg'))
for f in files:
    im = Image.open(f)
    print(f'=== {f} ===')
    print(f'Size: {im.size}')
    # save preview in assets/inspect_master/
    base = f.replace(' ', '_').replace('(', '').replace(')', '').replace('@', '')
    im.resize((300, int(300 * im.height / im.width))).save(f'assets/inspect_master/{base}.png')
print('Previews saved for all WhatsApp images')

