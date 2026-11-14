import re

# 1. Update js/app.js
with open('js/app.js', 'r', encoding='utf-8') as f:
    js = f.read()

target_sec6 = '// 6. MOBILE & TABLET NAVIGATION DRAWER CONTROLLER'
idx = js.find(target_sec6)
assert idx != -1, 'Could not find section 6 in app.js'

new_sec6 = '''// 6. MOBILE & TABLET NAVIGATION DRAWER CONTROLLER
  // =========================================================================
  const mobileToggle = document.getElementById('mobileMenuToggle');
  const mobileDrawer = document.getElementById('mobileNavDrawer');
  const drawerCloseBtn = document.getElementById('drawerCloseBtn');
  const drawerBackdrop = document.getElementById('drawerBackdrop');

  function openMobileMenu(e) {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (e && typeof e.stopPropagation === 'function') e.stopPropagation();
    const drawer = mobileDrawer || document.getElementById('mobileNavDrawer');
    const toggle = mobileToggle || document.getElementById('mobileMenuToggle');
    if (!drawer) return;
    drawer.classList.add('is-open');
    drawer.setAttribute('aria-hidden', 'false');
    if (toggle) {
      toggle.classList.add('is-active');
      toggle.setAttribute('aria-expanded', 'true');
    }
    document.body.classList.add('menu-locked');
  }

  function closeMobileMenu(e) {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (e && typeof e.stopPropagation === 'function') e.stopPropagation();
    const drawer = mobileDrawer || document.getElementById('mobileNavDrawer');
    const toggle = mobileToggle || document.getElementById('mobileMenuToggle');
    if (!drawer) return;
    drawer.classList.remove('is-open');
    drawer.setAttribute('aria-hidden', 'true');
    if (toggle) {
      toggle.classList.remove('is-active');
      toggle.setAttribute('aria-expanded', 'false');
    }
    document.body.classList.remove('menu-locked');
  }

  function toggleMobileMenu(e) {
    if (e && typeof e.preventDefault === 'function') e.preventDefault();
    if (e && typeof e.stopPropagation === 'function') e.stopPropagation();
    const drawer = mobileDrawer || document.getElementById('mobileNavDrawer');
    if (!drawer) return;
    if (drawer.classList.contains('is-open')) {
      closeMobileMenu(e);
    } else {
      openMobileMenu(e);
    }
  }

  // Global window bindings for instant onclick safety
  window.openMobileMenu = openMobileMenu;
  window.closeMobileMenu = closeMobileMenu;
  window.toggleMobileMenu = toggleMobileMenu;

  if (mobileToggle) {
    mobileToggle.addEventListener('click', toggleMobileMenu);
  }

  if (drawerCloseBtn) {
    drawerCloseBtn.addEventListener('click', closeMobileMenu);
  }

  if (drawerBackdrop) {
    drawerBackdrop.addEventListener('click', closeMobileMenu);
  }

  drawerNavLinks.forEach(link => {
    link.addEventListener('click', closeMobileMenu);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && mobileDrawer && mobileDrawer.classList.contains('is-open')) {
      closeMobileMenu();
    }
  });

  window.addEventListener('resize', () => {
    if (window.innerWidth > 1024 && mobileDrawer && mobileDrawer.classList.contains('is-open')) {
      closeMobileMenu();
    }
  });

});
'''

js_updated = js[:idx] + new_sec6
with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(js_updated)
print('Updated js/app.js with bulletproof mobile drawer handlers!')

# 2. Update index.html
with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# Update header brand logo to horizontal clean logo
html = re.sub(
    r'<a href="#hero" class="geo-brand" aria-label="Negizhi Industries Home">\s*<img src="assets/logo\.png"[^>]*>\s*</a>',
    '<a href="#hero" class="geo-brand" aria-label="Negizhi Industries Home"><img src="assets/logo-horizontal-clean.png" alt="Negizhi Industries - Precision Engineering Plastic Components" class="geo-brand-logo" /></a>',
    html
)

# Update mobile toggle button with onclick
old_btn = '<button class="geo-mobile-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu" aria-expanded="false" type="button">'
new_btn = '<button class="geo-mobile-toggle" id="mobileMenuToggle" aria-label="Toggle navigation menu" aria-expanded="false" type="button" onclick="window.toggleMobileMenu ? window.toggleMobileMenu(event) : toggleMobileMenu(event)">'
html = html.replace(old_btn, new_btn)

# Update drawer close button and backdrop
old_close = '<button class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close navigation menu" type="button">'
new_close = '<button class="drawer-close-btn" id="drawerCloseBtn" aria-label="Close navigation menu" type="button" onclick="window.closeMobileMenu ? window.closeMobileMenu(event) : closeMobileMenu(event)">'
html = html.replace(old_close, new_close)

old_backdrop = '<div class="drawer-backdrop" id="drawerBackdrop"></div>'
new_backdrop = '<div class="drawer-backdrop" id="drawerBackdrop" onclick="window.closeMobileMenu ? window.closeMobileMenu(event) : closeMobileMenu(event)"></div>'
html = html.replace(old_backdrop, new_backdrop)

# In drawer logo, use clean logo
html = re.sub(
    r'<img src="assets/logo\.png" alt="Negizhi Industries Logo" class="drawer-logo" />',
    '<img src="assets/logo-horizontal-clean.png" alt="Negizhi Industries Logo" class="drawer-logo" />',
    html
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)
print('Updated index.html with inline handlers and clean horizontal branding!')

