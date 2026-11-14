import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Let's find each media query block and its starting line
for m in re.finditer(r'@media\s*\([^)]+\)\s*\{', css):
    start = m.start()
    # Find line number
    line_no = css[:start].count('\n') + 1
    # Find matching brace
    brace_count = 0
    end = start
    for idx in range(start, len(css)):
        if css[idx] == '{':
            brace_count += 1
        elif css[idx] == '}':
            brace_count -= 1
            if brace_count == 0:
                end = idx + 1
                break
    mq_text = css[start:end]
    mq_header = m.group(0)
    print(f'Line {line_no:4d}: {mq_header[:40]}... (length {len(mq_text)} chars)')

