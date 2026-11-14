import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def enhance_optical_meter_cover():
    input_file = 'WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg'
    im = Image.open(input_file).convert('RGB')
    w, h = im.size
    
    # Coordinates of the optical polycarbonate meter cover
    # Centered around the dome:
    crop_norm = (0.56, 0.20, 0.86, 0.50)
    x1 = int(crop_norm[0] * w)
    y1 = int(crop_norm[1] * h)
    x2 = int(crop_norm[2] * w)
    y2 = int(crop_norm[3] * h)
    
    cropped = im.crop((x1, y1, x2, y2))
    cw, ch = cropped.size
    
    arr = np.array(cropped, dtype=np.float32)
    
    # Background whitening
    top_strip = arr[:int(ch*0.08), :]
    bg_val = float(np.percentile(top_strip, 85))
    if bg_val < 140:
        bg_val = 180
    scale = 250.0 / bg_val
    arr_scaled = np.clip(arr * scale, 0, 255)
    
    # Smooth tone curve: lifts reflections and clarifies clear polycarbonate
    x = arr_scaled / 255.0
    # Lift highlights and keep deep shadows crisp
    y = np.where(x < 0.45, x * 1.14, 1.0 - (1.0 - x)**1.22 * 0.88)
    y = np.clip(y * 255.0, 0, 255).astype(np.uint8)
    
    res = Image.fromarray(y)
    
    # Slight contrast and color boost
    res = ImageEnhance.Color(res).enhance(1.15)
    res = ImageEnhance.Contrast(res).enhance(1.14)
    res = res.filter(ImageFilter.UnsharpMask(radius=1.2, percent=125, threshold=2))
    
    # Aspect ratio 4:3 padding with clean studio background (#fcfcfc)
    target_aspect = 4/3
    rw, rh = res.size
    cur_aspect = rw / rh
    if cur_aspect < target_aspect:
        new_w = int(rh * target_aspect)
        new_h = rh
        padded = Image.new('RGB', (new_w, new_h), (252, 252, 254))
        px = (new_w - rw) // 2
        padded.paste(res, (px, 0))
        res = padded
    elif cur_aspect > target_aspect:
        new_w = rw
        new_h = int(rw / target_aspect)
        padded = Image.new('RGB', (new_w, new_h), (252, 252, 254))
        py = (new_h - rh) // 2
        padded.paste(res, (0, py))
        res = padded
        
    final = res.resize((1000, 750), Image.Resampling.LANCZOS)
    
    out_dir = 'assets/products'
    os.makedirs(out_dir, exist_ok=True)
    jpg_path = os.path.join(out_dir, 'optical-meter-cover.jpg')
    webp_path = os.path.join(out_dir, 'optical-meter-cover.webp')
    
    final.save(jpg_path, 'JPEG', quality=95, optimize=True)
    final.save(webp_path, 'WEBP', quality=92, method=6)
    print(f'Successfully generated {jpg_path} ({os.path.getsize(jpg_path)} bytes)')
    print(f'Successfully generated {webp_path} ({os.path.getsize(webp_path)} bytes)')

enhance_optical_meter_cover()

