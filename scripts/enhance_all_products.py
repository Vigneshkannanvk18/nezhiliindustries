import os
from PIL import Image, ImageEnhance, ImageFilter
import numpy as np

def enhance_product_smooth(
    input_file,
    crop_norm,           # (x1, y1, x2, y2) in 0..1
    output_basename,
    target_aspect=4/3,
    contrast=1.12,
    saturation=1.18,
    shadow_lift=1.16,
    sharpness=1.25,
    target_res=(1000, 750)
):
    if not os.path.exists(input_file):
        print(f'Missing input: {input_file}')
        return

    im = Image.open(input_file).convert('RGB')
    w, h = im.size
    
    # Crop
    x1 = max(0, int(crop_norm[0] * w))
    y1 = max(0, int(crop_norm[1] * h))
    x2 = min(w, int(crop_norm[2] * w))
    y2 = min(h, int(crop_norm[3] * h))
    cropped = im.crop((x1, y1, x2, y2))
    cw, ch = cropped.size
    
    arr = np.array(cropped, dtype=np.float32)
    
    # Sample top margin for background level
    top_strip = arr[:int(ch*0.08), :]
    bg_val = float(np.percentile(top_strip, 82))
    if bg_val < 140:
        bg_val = 180
    
    # Scale background towards 248
    scale = 248.0 / bg_val
    arr_scaled = np.clip(arr * scale, 0, 255)
    
    # Smooth tone curve: lifts shadows for engineering plastics, smoothly compresses highlights to 255
    x = arr_scaled / 255.0
    y = np.where(x < 0.4, x * shadow_lift, 1.0 - (1.0 - x)**1.25 * 0.88)
    y = np.clip(y * 255.0, 0, 255).astype(np.uint8)
    
    res = Image.fromarray(y)
    
    if saturation != 1.0:
        res = ImageEnhance.Color(res).enhance(saturation)
    if contrast != 1.0:
        res = ImageEnhance.Contrast(res).enhance(contrast)
        
    res = res.filter(ImageFilter.UnsharpMask(radius=1.2, percent=int(sharpness*100), threshold=2))
    
    # Aspect ratio padding with pure white
    rw, rh = res.size
    cur_aspect = rw / rh
    if cur_aspect < target_aspect:
        new_w = int(rh * target_aspect)
        new_h = rh
        padded = Image.new('RGB', (new_w, new_h), (255, 255, 255))
        px = (new_w - rw) // 2
        padded.paste(res, (px, 0))
        res = padded
    elif cur_aspect > target_aspect:
        new_w = rw
        new_h = int(rw / target_aspect)
        padded = Image.new('RGB', (new_w, new_h), (255, 255, 255))
        py = (new_h - rh) // 2
        padded.paste(res, (0, py))
        res = padded
        
    final = res.resize(target_res, Image.Resampling.LANCZOS)
    
    out_dir = 'assets/products'
    os.makedirs(out_dir, exist_ok=True)
    jpg_path = os.path.join(out_dir, f'{output_basename}.jpg')
    webp_path = os.path.join(out_dir, f'{output_basename}.webp')
    
    final.save(jpg_path, 'JPEG', quality=94, optimize=True)
    final.save(webp_path, 'WEBP', quality=92, method=6)
    print(f'-> Enhanced: {output_basename}.jpg & .webp')

ITEMS = [
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.01 PM (3).jpeg',
        'crop': (0.12, 0.06, 0.88, 0.90),
        'name': 'gear-delrin-helical',
        'contrast': 1.14, 'saturation': 1.15, 'shadow_lift': 1.22, 'sharpness': 1.30
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.02.59 PM.jpeg',
        'crop': (0.01, 0.26, 0.99, 0.92),
        'name': 'motor-cooling-fan-family',
        'contrast': 1.16, 'saturation': 1.10, 'shadow_lift': 1.25, 'sharpness': 1.30
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.02.58 PM.jpeg',
        'crop': (0.04, 0.20, 0.96, 0.95),
        'name': 'motor-fan-cowl-detail',
        'contrast': 1.16, 'saturation': 1.10, 'shadow_lift': 1.22, 'sharpness': 1.30
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.02.58 PM (1).jpeg',
        'crop': (0.04, 0.20, 0.96, 0.95),
        'name': 'motor-fan-cowl-frontal',
        'contrast': 1.16, 'saturation': 1.10, 'shadow_lift': 1.22, 'sharpness': 1.30
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.02.59 PM (1).jpeg',
        'crop': (0.18, 0.36, 0.92, 0.92),
        'name': 'bearing-rollers-overmoulded',
        'contrast': 1.12, 'saturation': 1.25, 'shadow_lift': 1.18, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.02.59 PM (2).jpeg',
        'crop': (0.24, 0.40, 0.76, 0.98),
        'name': 'switchgear-terminal-enclosure',
        'contrast': 1.12, 'saturation': 1.05, 'shadow_lift': 1.25, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.00 PM.jpeg',
        'crop': (0.26, 0.10, 0.78, 0.98),
        'name': 'brass-insert-bracket',
        'contrast': 1.16, 'saturation': 1.20, 'shadow_lift': 1.22, 'sharpness': 1.30
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.00 PM (1).jpeg',
        'crop': (0.28, 0.44, 0.96, 0.88),
        'name': 'threaded-pipe-caps',
        'contrast': 1.10, 'saturation': 1.20, 'shadow_lift': 1.12, 'sharpness': 1.20
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.00 PM (2).jpeg',
        'crop': (0.04, 0.56, 0.96, 0.98),
        'name': 'fluidic-connectors-plugs',
        'contrast': 1.15, 'saturation': 1.28, 'shadow_lift': 1.18, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.01 PM (2).jpeg',
        'crop': (0.02, 0.26, 0.99, 0.92),
        'name': 'pu-spider-couplings-family',
        'contrast': 1.15, 'saturation': 1.26, 'shadow_lift': 1.16, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.01 PM.jpeg',
        'crop': (0.12, 0.32, 0.88, 0.92),
        'name': 'pu-spider-coupling-single',
        'contrast': 1.15, 'saturation': 1.30, 'shadow_lift': 1.16, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.01 PM (1).jpeg',
        'crop': (0.10, 0.54, 0.95, 0.94),
        'name': 'alignment-bullet-pins',
        'contrast': 1.15, 'saturation': 1.25, 'shadow_lift': 1.15, 'sharpness': 1.25
    },
    {
        'file': 'WhatsApp Image 2026-11-13 at 2.03.02 PM.jpeg',
        'crop': (0.01, 0.18, 0.99, 0.96),
        'name': 'master-component-showcase',
        'target_aspect': 16/9,
        'contrast': 1.16, 'saturation': 1.22, 'shadow_lift': 1.20, 'sharpness': 1.25,
        'target_res': (1280, 720)
    }
]

for item in ITEMS:
    enhance_product_smooth(
        input_file=item['file'],
        crop_norm=item['crop'],
        output_basename=item['name'],
        target_aspect=item.get('target_aspect', 4/3),
        contrast=item.get('contrast', 1.12),
        saturation=item.get('saturation', 1.18),
        shadow_lift=item.get('shadow_lift', 1.16),
        sharpness=item.get('sharpness', 1.25),
        target_res=item.get('target_res', (1000, 750))
    )
