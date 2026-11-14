import os, re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

srcs = re.findall(r'(?:src|srcset)="([^"]+)"', html)
missing = []
found = []
for s in srcs:
    clean = s.split('?')[0].split(',')[0].strip().split(' ')[0]
    if clean.startswith('http') or clean.startswith('data:'):
        continue
    if os.path.exists(clean):
        found.append(clean)
    else:
        missing.append(clean)

print(f'Total local image assets found: {len(found)}')
for f in sorted(set(found)):
    print(f'  [OK] {f}')
if missing:
    print('MISSING ASSETS:', set(missing))
else:
    print('ALL ASSET REFERENCES EXIST ON DISK! 100% OK')

