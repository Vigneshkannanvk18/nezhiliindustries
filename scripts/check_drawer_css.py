with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

import re
for m in re.finditer(r'([^{]*\.geo-mobile-drawer[^{]*\{[^}]*\})', css):
    print(m.group(0))

