import re

with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

seq_match = re.search(r'<section[^>]*id=["\']moulding-cycle["\'][^>]*>(.*?)</section>', html, re.DOTALL)
if seq_match:
    lines = seq_match.group(0).splitlines()
    for i in range(50, len(lines)):
        print(f'{i+1}: {lines[i]}')

