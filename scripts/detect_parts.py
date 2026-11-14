import cv2
import numpy as np
import os

img = cv2.imread('WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
h, w = gray.shape

# The table is light grey (~170-190).
# Threshold to find non-table components
thresh = cv2.adaptiveThreshold(gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 51, 10)
# Find contours
contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

os.makedirs('assets/detected_parts', exist_ok=True)
parts = []
idx = 0
for cnt in contours:
    x, y, cw, ch = cv2.boundingRect(cnt)
    area = cw * ch
    if area > 10000 and cw > 60 and ch > 60:
        idx += 1
        crop = img[max(0, y-15):min(h, y+ch+15), max(0, x-15):min(w, x+cw+15)]
        cv2.imwrite(f'assets/detected_parts/part_{idx:02d}.jpg', crop)
        parts.append((idx, x, y, cw, ch, area))

print(f'Detected {len(parts)} significant parts')
for p in sorted(parts, key=lambda x: x[1]): # sort left to right
    print(f'Part {p[0]:02d}: pos=({p[1]}, {p[2]}), size={p[3]}x{p[4]}, area={p[5]}')

