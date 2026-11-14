with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

import re
matches = re.findall(r'.*preselectMaterial.*', js)
for m in matches:
    print(m)

