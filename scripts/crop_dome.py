from PIL import Image

im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size

# In crop_pc_region, x was 800 to 1400, y was 200 to 600
# Let's crop tighter around the dome: x in [850, 1350], y in [220, 580]
dome_crop = im.crop((850, 220, 1350, 580))
dome_crop.save('assets/inspect_master/meter_cover_candidate.jpg')

print('Saved meter_cover_candidate.jpg:', dome_crop.size)

