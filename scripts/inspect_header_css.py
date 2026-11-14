import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

for sel in ['.geo-header', '.geo-nav-container', '.geo-header-actions', '.btn-geo-primary', '.geo-brand']:
    for m in re.finditer(r'([^{]+)\{([^}]+)\}', css):
        s = m.group(1).strip()
        b = m.group(2).strip()
        if s == sel:
            print(f'=== {s} ===')
            print(b)
            print()

