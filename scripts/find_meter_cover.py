import re
from PIL import Image

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

cards = re.findall(r'<article class="product-card"[^>]*>(.*?)</article>', text, re.DOTALL)
print(f'Total product cards: {len(cards)}')
for i, card in enumerate(cards):
    title = re.search(r'<h3 class="product-title">(.*?)</h3>', card)
    img = re.search(r'<img[^>]+src="([^"]+)"', card)
    t_str = title.group(1) if title else 'Unknown'
    i_str = img.group(1) if img else 'Unknown'
    print(f'Card {i+1}: {t_str} -> {i_str}')

