import re

# 1. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Replace Card 7 SVG with picture tag
card7_old = '''          <!-- Product 7: Optical PC Meter Cover -->
          <article class="product-card" data-cat="electrical">
            <div class="product-media-wrap">
              <img src="assets/products/optical-meter-cover.svg?v=2" alt="Optical Grade Polycarbonate Meter Cover" class="product-img" loading="lazy" />
              <span class="product-tag-badge">OPTICAL &amp; IMPACT PROOF</span>
            </div>'''

card7_new = '''          <!-- Product 7: Optical PC Meter Cover -->
          <article class="product-card" data-cat="electrical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/optical-meter-cover.webp" type="image/webp" />
                <img src="assets/products/optical-meter-cover.jpg" alt="Optical Polycarbonate (PC) Meter Covers" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">OPTICAL &amp; IMPACT PROOF</span>
            </div>'''

if card7_old in html:
    html = html.replace(card7_old, card7_new)
    print('Updated Card 7 in index.html to real image!')
else:
    print('Warning: Card 7 pattern not directly found, searching regex...')
    html = re.sub(
        r'<img src="assets/products/optical-meter-cover\.svg[^"]*" alt="[^"]*" class="product-img" loading="lazy" />',
        '<picture><source srcset="assets/products/optical-meter-cover.webp" type="image/webp" /><img src="assets/products/optical-meter-cover.jpg" alt="Optical Polycarbonate (PC) Meter Covers" class="product-img" loading="lazy" /></picture>',
        html
    )
    print('Regex replaced Card 7 image.')

# Update footer brand logo in index.html
footer_old = '''      <div class="footer-col-brand">
        <img src="assets/logo.png" alt="Negizhi Industries Logo" class="footer-logo" />
        <p class="footer-tagline">CRAFTING QUALITY : SHAPING TOMORROW</p>'''

footer_new = '''      <div class="footer-col-brand">
        <a href="#hero" class="footer-brand-link" aria-label="Negizhi Industries">
          <img src="assets/logo-horizontal-clean.png" alt="Negizhi Industries - Crafting Quality : Shaping Tomorrow" class="footer-logo" width="220" height="43" loading="lazy" />
        </a>
        <p class="footer-tagline">CRAFTING QUALITY : SHAPING TOMORROW</p>'''

if footer_old in html:
    html = html.replace(footer_old, footer_new)
    print('Updated footer logo in index.html to clean horizontal logo lockup!')
else:
    print('Warning: Footer old pattern not found directly, checking regex...')
    html = re.sub(
        r'<img src="assets/logo\.png" alt="Negizhi Industries Logo" class="footer-logo" />',
        '<a href="#hero" class="footer-brand-link" aria-label="Negizhi Industries"><img src="assets/logo-horizontal-clean.png" alt="Negizhi Industries - Crafting Quality : Shaping Tomorrow" class="footer-logo" width="220" height="43" loading="lazy" /></a>',
        html
    )
    print('Regex replaced footer logo.')

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Saved updated index.html')

