with open('js/app.js', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if 'geo-nav-link' in line or 'IntersectionObserver' in line or 'scroll' in line.lower() and 'nav' in line.lower():
        for j in range(max(0, i-5), min(len(lines), i+15)):
            print(f'{j+1}: {lines[j]}', end='')
        print('---')

