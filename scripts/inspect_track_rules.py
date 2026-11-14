with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
rules = re.findall(r'(\.sequence-scroll-track[^{]*\{[^}]*\})', css)
for r in rules:
    print(r)

rules2 = re.findall(r'(\.scroll-step[^{]*\{[^}]*\})', css)
for r in rules2:
    print(r)

