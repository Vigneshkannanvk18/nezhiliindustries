import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

for m in re.finditer(r'([^{]*menu-locked[^{]*\{[^}]*\})', css):
    print(m.group(0))

