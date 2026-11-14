import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Check for fixed widths or properties that often cause mobile overflow
findings = []

# 1. Elements with fixed width > 320px outside media queries or in general
for m in re.finditer(r'([^{]+)\{([^}]+)\}', css):
    sel = m.group(1).strip()
    body = m.group(2)
    
    # check min-width or width > 350px (excluding max-width)
    w_matches = re.findall(r'(?<!max-)(?:min-)?width:\s*(\d+)px', body)
    for w in w_matches:
        if int(w) > 340 and not any(k in sel for k in ['container', '@media', 'modal', 'canvas']):
            findings.append((sel, f'fixed width {w}px'))
            
    # check grid-template-columns with fixed px columns
    if 'grid-template-columns' in body and 'repeat' not in body:
        px_cols = re.findall(r'\d+px', body)
        if len(px_cols) >= 2:
            findings.append((sel, f'grid with px cols: {px_cols}'))

print(f'Total findings: {len(findings)}')
for s, reason in findings[:25]:
    print(f'  {s[:50]}: {reason}')

