import re, os

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

matches = re.findall(r'(?:src|href|srcset)=["\']([^"\'\s,]+\.(?:png|jpg|jpeg|webp|svg|pdf|css|js))', html)
print(f"Total referenced assets including srcset: {len(matches)}")
unique_assets = sorted(set(matches))
print(f"Unique referenced assets ({len(unique_assets)}):")
for u in unique_assets:
    exists = os.path.exists(u)
    print(f"  [{'EXISTS' if exists else 'MISSING'}] {u}")
