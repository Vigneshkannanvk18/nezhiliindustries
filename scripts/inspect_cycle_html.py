import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Extract the sequence section
seq_match = re.search(r'<section[^>]*id=["\']moulding-cycle["\'][^>]*>(.*?)</section>', html, re.DOTALL)
if seq_match:
    print('Found moulding-cycle section!')
    lines = seq_match.group(0).splitlines()
    print(f'Total lines: {len(lines)}')
    for i in range(min(50, len(lines))):
        print(f'{i+1}: {lines[i]}')
else:
    print('moulding-cycle section not found!')

