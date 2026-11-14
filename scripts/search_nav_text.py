import os

for root, dirs, files in os.walk('.'):
    if '.git' in root or 'node_modules' in root:
        continue
    for file in files:
        if file.endswith(('.js', '.html', '.css')):
            path = os.path.join(root, file)
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                content = f.read()
                for phrase in ['Process Cycle', 'Tool Room', 'Quality Lab']:
                    if phrase in content:
                        print(f'{path}: contains "{phrase}"')

