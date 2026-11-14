import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

classes = set(re.findall(r'class="([^"]+)"', html))
all_classes = set()
for c in classes:
    for item in c.split():
        all_classes.add(item)

print(f'Total unique classes in index.html: {len(all_classes)}')

missing = []
for c in sorted(all_classes):
    pattern = r'\.' + re.escape(c) + r'(?:[:\s{,.\[]|$)'
    if not re.search(pattern, css):
        missing.append(c)

print(f'Classes found in CSS: {len(all_classes) - len(missing)}')
print(f'Classes not directly matched: {len(missing)}')
if missing:
    print('Unmatched classes:', missing)

