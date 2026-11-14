import re

with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

by_id = set(re.findall(r'getElementById\([\'"]([^\'"]+)[\'"]\)', js))
print(f"Total IDs accessed via getElementById: {len(by_id)}")

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

missing = []
for el_id in sorted(by_id):
    pattern1 = f'id="{el_id}"'
    pattern2 = f"id='{el_id}'"
    if pattern1 not in html and pattern2 not in html:
        missing.append(el_id)

print(f"Missing IDs in index.html ({len(missing)}):", missing)

