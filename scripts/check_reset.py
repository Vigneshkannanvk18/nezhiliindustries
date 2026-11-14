with open('css/styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:30]):
    print(f'{i+1}: {l.rstrip()}')

