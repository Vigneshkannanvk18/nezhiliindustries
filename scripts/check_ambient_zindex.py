with open('css/styles.css', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines[:140]):
    if 'ambient' in l or 'vignette' in l or 'pattern' in l or 'z-index' in l:
        print(f'{i+1}: {l.rstrip()}')

