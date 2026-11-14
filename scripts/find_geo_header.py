with open('css/styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:300]):
    if 'geo-header' in l:
        for j in range(max(0, i-2), min(len(lines), i+15)):
            print(f'{j+1}: {lines[j].rstrip()}')
        break

