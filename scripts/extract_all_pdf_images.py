import pypdf
import os

reader = pypdf.PdfReader('NEGIZHII.pdf')
print(f'Total pages: {len(reader.pages)}')

os.makedirs('assets/pdf_images', exist_ok=True)
count = 0
for page_num, page in enumerate(reader.pages):
    print(f'Page {page_num + 1} images:')
    for img_name, img_obj in page.images.items():
        count += 1
        safe_name = img_name.replace('/', '_').replace('\\', '_')
        ext = os.path.splitext(img_obj.name)[1] if hasattr(img_obj, 'name') and img_obj.name else '.png'
        if not ext:
            ext = '.png'
        out_name = f'assets/pdf_images/p{page_num + 1}_{safe_name}{ext}'
        with open(out_name, 'wb') as fp:
            fp.write(img_obj.data)
        print(f'  Saved {out_name}: len={len(img_obj.data)}')

print(f'Total extracted images from PDF: {count}')
