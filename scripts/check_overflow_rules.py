with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

print('html overflow-x:', 'html' in css and 'overflow-x' in css)

# Find all occurrences of overflow-x
import re
for m in re.finditer(r'([^{]+)\{([^}]*overflow-x[^}]*)\}', css):
    print(m.group(1).strip(), '->', m.group(2).strip())

