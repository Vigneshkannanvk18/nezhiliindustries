import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

selectors = ['.geo-header', '.geo-nav-container', '.geo-brand', '.geo-brand-logo', '.geo-nav-menu', '.geo-nav-list', '.geo-nav-link', '.geo-header-actions', '.btn-geo-ghost', '.btn-geo-primary']

for sel in selectors:
    for m in re.finditer(r'([^{]*' + re.escape(sel) + r'[^{]*\{[^}]*\})', css):
        # only print if selector matches closely
        first_line = m.group(0).split('{')[0].strip()
        if sel in first_line:
            print(m.group(0))
            print()

