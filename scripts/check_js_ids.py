import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

ids = re.findall(r'document\.getElementById\([\'"]([^\'"]+)[\'"]\)', js)
print(f'Total getElementById calls: {len(ids)}')
for i in set(ids):
    if f'id="{i}"' not in html and f"id='{i}'" not in html:
        print(f'MISSING ID IN HTML: {i}')

