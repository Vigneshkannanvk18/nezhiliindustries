with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

count = html.count('scroll-step')
print(f'scroll-step occurrences: {count}')

# Check .step-card occurrences
print(f'step-card occurrences: {html.count("step-card")}')

