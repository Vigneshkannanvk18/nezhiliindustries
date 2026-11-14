from PIL import Image

for p in [4, 5, 6, 7]:
    im = Image.open(f'assets/extracted/page{p}_img1_Im0.jpg')
    print(f'Page {p}: size={im.size}')
    # In these pages (1152x648), where are the images?
    # Usually the top 100-200px is header/title, middle is image, bottom is description or specs
    # Let's crop middle 50%
    mid = im.crop((100, 100, 1052, 548))
    mid.save(f'assets/inspect_master/page_{p}_mid.jpg')

