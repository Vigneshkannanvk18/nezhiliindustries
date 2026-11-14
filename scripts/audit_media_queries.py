import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Find all @media queries
media_queries = re.findall(r'@media[^{]+\{', css)
print(f'Total @media queries in css/styles.css: {len(media_queries)}')
for mq in set(media_queries):
    print('  ', mq.strip().rstrip('{').strip())

