with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

for term in ['sequence-pills-row', 'seq-pills-bar', 'scroll-step', 'sequence-scroll-track', 'sequence-sticky-container', 'scroll-sequence-wrapper']:
    print(f'{term}: {css.count(term)} times in css')

