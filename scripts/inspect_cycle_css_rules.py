import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

terms = ['scroll-step', 'sequence-scroll-track', 'step-card', 'sequence-sticky-container', 'scroll-sequence-wrapper', 'sequence-pills-row']

for m in re.finditer(r'([^{]+)\{([^}]+)\}', css):
    sel = m.group(1).strip()
    body = m.group(2).strip()
    if any(t in sel for t in terms):
        print('=== ' + sel + ' ===')
        print(body)
        print()

