import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check elements with fixed widths
for m in re.finditer(r'([^{]+)\{([^}]+)\}', css):
    sel = m.group(1).strip()
    body = m.group(2).strip()
    # Check width: XXXpx where XXX > 320
    w_match = re.search(r'(?<!max-)(?<!min-)width:\s*(\d+)px', body)
    if w_match:
        w_val = int(w_match.group(1))
        if w_val > 300 and not any(k in sel for k in ['container', 'modal', 'canvas', 'svg', 'ambient']):
            print(f'Fixed width {w_val}px in selector: {sel}')

