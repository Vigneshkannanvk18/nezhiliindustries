import cv2
import numpy as np
from PIL import Image

im = Image.open('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
w, h = im.size

# In WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg:
# Let's inspect coordinates (900, 220, 1300, 560):
cover = im.crop((920, 240, 1320, 540))
cover.save('assets/inspect_master/cover_detail.jpg')

# Let's also check if there is an optical cover in WhatsApp Image 2026-11-13 at 2.02.58 PM (1).jpeg, etc.
print('Cover crop size:', cover.size)

