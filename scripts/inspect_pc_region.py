from PIL import Image

im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size

# Let's crop:
# (800, 200, 1400, 600)
crop1 = im.crop((800, 200, 1400, 600))
crop1.save('assets/inspect_master/crop_pc_region.jpg')

# Let's also check (200, 450, 700, 850)
crop2 = im.crop((200, 450, 700, 850))
crop2.save('assets/inspect_master/crop_midleft_region.jpg')

# Let's inspect what colors and shapes are in crop_pc_region
print('Saved crop_pc_region.jpg and crop_midleft_region.jpg')

