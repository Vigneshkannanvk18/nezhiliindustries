import re

# 1. Update css/styles.css
with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# Update html and body reset
html_reset_old = '''html {
  scroll-behavior: smooth;
  color-scheme: dark;
}

body.geometric-industrial-theme {
  background-color: var(--geo-bg-deep);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  min-height: 100vh;
  overflow-x: hidden;
  position: relative;
  -webkit-font-smoothing: antialiased;
}'''

html_reset_new = '''html {
  scroll-behavior: smooth;
  color-scheme: dark;
  overflow-x: clip;
  width: 100%;
  max-width: 100%;
}

body.geometric-industrial-theme {
  background-color: var(--geo-bg-deep);
  color: var(--text-primary);
  font-family: var(--font-body);
  font-size: 16px;
  line-height: 1.6;
  min-height: 100vh;
  overflow-x: clip;
  width: 100%;
  max-width: 100%;
  position: relative;
  -webkit-font-smoothing: antialiased;
}

@supports not (overflow-x: clip) {
  html, body.geometric-industrial-theme {
    overflow-x: hidden;
  }
}'''

if html_reset_old in css:
    css = css.replace(html_reset_old, html_reset_new)
    print('Updated html/body overflow-x reset to clip!')
else:
    print('Notice: html_reset_old not matched exactly, replacing via regex...')
    css = re.sub(
        r'html\s*\{[^}]*scroll-behavior:[^}]*\}\s*body\.geometric-industrial-theme\s*\{[^}]*\}',
        html_reset_new,
        css
    )

# Update Mobile Drawer CSS
drawer_css_old = '''.geo-mobile-drawer {
  position: fixed;
  inset: 0;
  z-index: 9999;
  visibility: hidden;
  transition: visibility 0.3s ease;
}

.geo-mobile-drawer.is-open {
  visibility: visible;
}

.drawer-backdrop {
  position: absolute;
  inset: 0;
  background: rgba(2, 4, 10, 0.8);
  backdrop-filter: blur(8px);
  opacity: 0;
  transition: opacity 0.3s ease;
}

.geo-mobile-drawer.is-open .drawer-backdrop {
  opacity: 1;
}

.drawer-content {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 85%;
  max-width: 360px;
  background: #090e1a;
  border-left: 1px solid rgba(0, 229, 255, 0.2);
  box-shadow: -10px 0 40px rgba(0, 0, 0, 0.8);
  display: flex;
  flex-direction: column;
  padding: 24px 20px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  transform: translateX(100%);
  transition: transform 0.35s cubic-bezier(0.16, 1, 0.3, 1);
}

.geo-mobile-drawer.is-open .drawer-content {
  transform: translateX(0);
}'''

drawer_css_new = '''.geo-mobile-toggle {
  display: none;
  width: 44px;
  height: 44px;
  min-width: 44px;
  min-height: 44px;
  background: rgba(255, 255, 255, 0.06);
  border: 1px solid rgba(255, 255, 255, 0.18);
  border-radius: var(--radius-sm);
  cursor: pointer;
  padding: 0;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 5px;
  transition: all var(--transition-fast);
  color: var(--text-primary);
  z-index: 102;
  touch-action: manipulation;
  -webkit-tap-highlight-color: transparent;
}

.geo-mobile-toggle:hover {
  background: rgba(0, 229, 255, 0.12);
  border-color: var(--geo-cyan);
}

.hamburger-bar {
  display: block;
  width: 20px;
  height: 2px;
  background-color: #f8fafc;
  border-radius: 2px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  pointer-events: none;
}

.geo-mobile-toggle.is-active .hamburger-bar:nth-child(1) {
  transform: translateY(7px) rotate(45deg);
  background-color: var(--geo-cyan);
}

.geo-mobile-toggle.is-active .hamburger-bar:nth-child(2) {
  opacity: 0;
  transform: translateX(-8px);
}

.geo-mobile-toggle.is-active .hamburger-bar:nth-child(3) {
  transform: translateY(-7px) rotate(-45deg);
  background-color: var(--geo-cyan);
}

.geo-mobile-drawer {
  position: fixed;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  height: 100dvh;
  z-index: 99999;
  visibility: hidden;
  pointer-events: none;
  overflow: hidden;
  transition: visibility 0.25s ease;
}

.geo-mobile-drawer.is-open {
  visibility: visible;
  pointer-events: auto;
}

.drawer-backdrop {
  position: absolute;
  top: 0;
  left: 0;
  right: 0;
  bottom: 0;
  width: 100%;
  height: 100%;
  background: rgba(2, 4, 10, 0.85);
  backdrop-filter: blur(8px);
  -webkit-backdrop-filter: blur(8px);
  opacity: 0;
  transition: opacity 0.25s ease;
  z-index: 1;
}

.geo-mobile-drawer.is-open .drawer-backdrop {
  opacity: 1;
}

.drawer-content {
  position: absolute;
  top: 0;
  right: 0;
  bottom: 0;
  width: 85%;
  max-width: 340px;
  height: 100%;
  height: 100dvh;
  background: #090e1a;
  border-left: 1px solid rgba(0, 229, 255, 0.3);
  box-shadow: -10px 0 40px rgba(0, 0, 0, 0.85);
  display: flex;
  flex-direction: column;
  padding: 22px 18px;
  overflow-y: auto;
  -webkit-overflow-scrolling: touch;
  transform: translateX(100%);
  transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1);
  z-index: 2;
}

.geo-mobile-drawer.is-open .drawer-content {
  transform: translateX(0);
}'''

# Replace toggle and drawer base definition
drawer_block_pattern = re.compile(r'\.geo-mobile-toggle\s*\{.*?\n\.geo-mobile-drawer\.is-open\s*\.drawer-content\s*\{[^}]*\}', re.DOTALL)
if drawer_block_pattern.search(css):
    css = drawer_block_pattern.sub(drawer_css_new, css)
    print('Updated drawer CSS base rules!')
else:
    print('Notice: drawer_block_pattern not found, attempting direct replace...')
    css = css.replace(drawer_css_old, drawer_css_new)

# Now update the responsive section (Breakpoint 3 <= 900px, Breakpoint 4 <= 768px, Breakpoint 5 <= 640px)
responsive_start = css.find('/* ---- BREAKPOINT 1:')
assert responsive_start != -1, 'Could not find responsive breakpoints start'

new_responsive_section = '''/* ---- BREAKPOINT 1: LARGE TABLETS & SMALL LAPTOPS (<= 1200px) ---- */
@media (max-width: 1200px) {
  .container {
    max-width: 100%;
    padding: 0 24px;
  }
  .geo-nav-list {
    gap: 14px;
  }
  .geo-nav-link {
    font-size: 13px;
  }
}

/* ---- BREAKPOINT 2: TABLETS LANDSCAPE & IPAD PRO (<= 1024px) ---- */
@media (max-width: 1024px) {
  .geo-nav-menu {
    display: none !important; /* Switch to sleek mobile/tablet hamburger navigation */
  }
  .geo-mobile-toggle {
    display: flex !important;
  }
  .geo-header-actions {
    gap: 10px;
  }
  .geo-header {
    height: 72px;
  }
  .geo-hero-grid {
    grid-template-columns: 1fr;
    gap: 36px;
  }
  .geo-hero-left {
    max-width: 100%;
  }
  .geo-hero-title {
    font-size: 44px;
  }
  .geo-hero-lead {
    max-width: 100%;
    font-size: 16px;
  }
  .products-cards-grid {
    grid-template-columns: repeat(2, 1fr) !important;
    gap: 20px;
  }
  .machinery-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  .quality-instruments-grid {
    grid-template-columns: repeat(2, 1fr);
    gap: 20px;
  }
  .geo-footer-inner {
    grid-template-columns: 1.2fr 1fr;
    gap: 32px;
  }
  .footer-col-contact,
  .footer-col-materials {
    grid-column: 1 / -1;
  }
}

/* ---- BREAKPOINT 3: MEDIUM TABLETS & COMPACT DESKTOPS (<= 900px) ---- */
@media (max-width: 900px) {
  .scroll-sequence-wrapper {
    grid-template-columns: 1fr;
    gap: 16px;
    margin-bottom: 20px;
  }
  .sequence-sticky-container {
    position: relative;
    top: 0;
    width: 100%;
    max-width: 100%;
    overflow: hidden;
  }
  /* Sequence Pills Bar: horizontal touch scrolling, no overflow */
  .sequence-pills-row,
  .seq-pills-bar {
    display: flex !important;
    flex-wrap: nowrap !important;
    overflow-x: auto !important;
    -webkit-overflow-scrolling: touch;
    gap: 8px;
    padding: 6px 2px 10px;
    margin-top: 10px;
    scrollbar-width: none;
    max-width: 100%;
    box-sizing: border-box;
  }
  .sequence-pills-row::-webkit-scrollbar,
  .seq-pills-bar::-webkit-scrollbar {
    display: none;
  }
  .seq-pill {
    flex-shrink: 0;
    white-space: nowrap;
    padding: 8px 14px;
    font-size: 12px;
  }

  /* Compact sequence track: ELIMINATE 200px+ gaps */
  .sequence-scroll-track {
    display: flex !important;
    flex-direction: column !important;
    gap: 12px !important;
    padding: 12px 0 20px !important;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .scroll-step {
    min-height: auto !important;
    display: block !important;
    margin: 0 !important;
    padding: 0 !important;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .scroll-step:last-child {
    margin-bottom: 0 !important;
  }
  .step-card {
    padding: 16px 18px !important;
    margin: 0 !important;
    width: 100% !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
  }
  .scroll-step.active .step-card {
    transform: none !important; /* Prevent 4px horizontal nudging overflow */
  }
  .step-card h3 {
    font-size: 16px;
    margin-bottom: 6px;
  }
  .step-card p {
    font-size: 13px;
    line-height: 1.55;
  }

  .master-showcase-banner {
    grid-template-columns: 1fr;
  }
  .master-showcase-media {
    border-right: none;
    border-bottom: 1px solid #e2e8f0;
    min-height: 240px;
  }
  .master-showcase-content {
    padding: 24px 20px;
  }
  .products-toolbar-bar {
    flex-direction: column;
    align-items: stretch;
    gap: 14px;
  }
  .product-category-pills {
    display: flex;
    overflow-x: auto;
    flex-wrap: nowrap;
    gap: 8px;
    padding: 4px 2px 8px;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    max-width: 100%;
    box-sizing: border-box;
  }
  .product-category-pills::-webkit-scrollbar {
    display: none;
  }
  .prod-filter-btn {
    flex-shrink: 0;
    white-space: nowrap;
    padding: 9px 15px;
    font-size: 13px;
  }
  .product-search-box {
    width: 100%;
    min-width: 0;
  }
  .materials-explorer-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .materials-tabs-nav {
    display: flex;
    flex-direction: row;
    overflow-x: auto;
    flex-wrap: nowrap;
    gap: 8px;
    padding: 4px 2px 10px;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
    max-width: 100%;
    box-sizing: border-box;
  }
  .materials-tabs-nav::-webkit-scrollbar {
    display: none;
  }
  .material-nav-btn {
    flex-shrink: 0;
    white-space: nowrap;
    padding: 10px 16px;
    display: inline-flex;
    align-items: center;
    gap: 8px;
  }
  .material-nav-btn .mat-badge {
    display: none;
  }
  .material-nav-btn .mat-name {
    font-size: 13px;
  }
  .geo-about-grid {
    grid-template-columns: 1fr;
    gap: 24px;
  }
  .tooling-showcase-grid {
    grid-template-columns: 1fr;
    gap: 28px;
  }
}

/* ---- BREAKPOINT 4: TABLET PORTRAIT & LARGE PHONES (<= 768px) ---- */
@media (max-width: 768px) {
  /* Ticker Bar */
  .geo-ticker-bar {
    padding: 6px 0;
    font-size: 10.5px;
    background: #04060c;
  }
  .geo-ticker-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    width: 100%;
    gap: 10px;
    padding: 0 16px;
  }
  .geo-coord-badge {
    display: none;
  }
  .geo-ticker-status {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-right: 6px;
    font-size: 10px;
  }
  .geo-ticker-contact span:first-child,
  .geo-ticker-contact .divider {
    display: none;
  }
  .geo-tel-link {
    font-weight: 700;
    color: var(--geo-cyan);
    white-space: nowrap;
    font-size: 10.5px;
  }

  /* Form & Contact */
  .rfq-calculator-container,
  .contact-details-card {
    padding: 24px 18px;
  }
  .form-row, .contact-data-grid {
    grid-template-columns: 1fr;
    gap: 14px;
  }
  .form-group input,
  .form-group select,
  .form-group textarea {
    font-size: 16px !important; /* iOS automatic zoom prevention */
    min-height: 48px;
    width: 100%;
    box-sizing: border-box;
  }
  .machinery-grid {
    grid-template-columns: 1fr;
  }
  .quality-instruments-grid {
    grid-template-columns: 1fr;
  }
  .geo-header-actions .btn-geo-ghost {
    display: none; /* Hide brochure in header on tablets/phones */
  }
}

/* ---- BREAKPOINT 5: STANDARD MOBILE DEVICES (<= 640px) ---- */
@media (max-width: 640px) {
  .container {
    padding: 0 16px;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .geo-hero-section {
    padding: 22px 0 34px;
  }
  .geo-hero-title {
    font-size: clamp(26px, 7.5vw, 34px);
    line-height: 1.18;
  }
  .title-sub {
    font-size: 12px;
    letter-spacing: 0.12em;
  }
  .geo-hero-lead {
    font-size: 14px;
    line-height: 1.6;
    margin-bottom: 20px;
  }
  .geo-hero-cta-group {
    flex-direction: column;
    width: 100%;
    gap: 12px;
    margin-bottom: 22px;
  }
  .geo-hero-cta-group .btn-geo-primary,
  .geo-hero-cta-group .btn-geo-secondary {
    width: 100%;
    justify-content: center;
    padding: 14px 20px;
    box-sizing: border-box;
    text-align: center;
  }
  .geo-micro-specs-row {
    flex-direction: column;
    align-items: stretch;
    padding: 14px 16px;
    gap: 10px;
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .micro-spec-divider {
    width: 100%;
    height: 1px;
    margin: 0;
    background: #e2e8f0;
  }
  .micro-spec-box {
    display: flex;
    flex-direction: row;
    align-items: center;
    justify-content: space-between;
    text-align: left;
    width: 100%;
  }
  .micro-spec-box .spec-value {
    font-size: 15px;
    margin: 0;
  }
  .micro-spec-box .spec-sub {
    display: none;
  }

  /* Display card & Machine viewport */
  .geo-display-card {
    padding: 16px;
    box-sizing: border-box;
    width: 100%;
    max-width: 100%;
  }
  .geo-card-header {
    flex-direction: column;
    align-items: flex-start;
    gap: 6px;
  }
  .card-status-pill {
    font-size: 10px;
  }
  .geo-floating-widgets {
    grid-template-columns: 1fr;
    gap: 10px;
  }

  /* Canvas Render Container: proportional height prevention */
  .canvas-render-container {
    aspect-ratio: 900 / 420;
    height: auto;
    min-height: 180px;
    width: 100%;
    max-width: 100%;
    overflow: hidden;
  }

  /* Process Cycle HUD on Mobile */
  .sequence-hud-top {
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 10px 12px;
  }
  .sequence-hud-top .hud-item:first-child {
    grid-column: 1 / -1 !important;
  }
  .hud-value {
    font-size: 11px;
  }
  .hud-label {
    font-size: 9px;
  }

  /* Products Cards: Clean 1 Column on Mobile */
  .products-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 18px;
    width: 100%;
    max-width: 100%;
  }
  .product-card {
    width: 100%;
    max-width: 100%;
    box-sizing: border-box;
  }
  .product-media-wrap {
    height: 220px;
  }
  .product-body {
    padding: 18px 16px;
  }
  .product-title {
    font-size: 16.5px;
  }
  .product-desc {
    font-size: 13px;
    line-height: 1.55;
  }
  .prod-spec-row {
    display: flex;
    justify-content: space-between;
    align-items: baseline;
    gap: 10px;
    font-size: 12px;
  }
  .spec-k {
    flex-shrink: 0;
  }
  .spec-v {
    text-align: right;
    word-break: break-word;
  }

  /* Material Detail Header */
  .detail-header-row {
    flex-direction: column;
    align-items: flex-start;
    gap: 8px;
  }
  .detail-mat-name {
    font-size: 20px;
  }
  .mat-properties-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  .mat-prop-box {
    word-break: break-word;
    overflow-wrap: break-word;
  }

  /* Machinery Specs */
  .specs-data-grid {
    grid-template-columns: 1fr 1fr;
    gap: 10px;
    padding: 12px;
  }

  /* Quality Instruments on Mobile */
  .quality-instruments-grid {
    grid-template-columns: 1fr;
    gap: 16px;
  }
  .instrument-card {
    padding: 18px 16px;
  }

  /* RFQ Actions on Mobile */
  .rfq-actions-row {
    flex-direction: column;
    width: 100%;
    gap: 12px;
  }
  .rfq-actions-row .btn-geo-primary,
  .rfq-actions-row .btn-geo-whatsapp {
    width: 100%;
    justify-content: center;
    box-sizing: border-box;
    text-align: center;
  }

  /* Contact Card on Mobile */
  .contact-card-header {
    flex-direction: row;
    align-items: center;
    gap: 14px;
  }
  .contact-logo {
    height: 50px;
  }
  .contact-company-title {
    font-size: 21px;
  }
  .contact-item {
    gap: 12px;
  }

  /* Footer on Mobile */
  .geo-footer-inner {
    grid-template-columns: 1fr;
    gap: 30px;
    padding-bottom: 30px;
  }
  .footer-col-brand {
    align-items: flex-start;
    text-align: left;
    width: 100%;
  }
  .footer-logo {
    height: 42px;
    max-width: 210px;
    align-self: flex-start;
  }
  .footer-col-nav ul {
    grid-template-columns: 1fr 1fr;
    gap: 10px 16px;
  }
  .footer-bottom-inner {
    flex-direction: column;
    text-align: center;
    gap: 8px;
    padding: 16px 0;
  }
  .clients-marquee-grid {
    grid-template-columns: 1fr;
  }
}

/* ---- BREAKPOINT 6: COMPACT PHONES (<= 520px) ---- */
@media (max-width: 520px) {
  .geo-brand-logo {
    height: 36px;
    max-width: 130px;
  }
  .geo-header-actions .btn-geo-primary {
    padding: 7px 11px;
    font-size: 11.5px;
  }
  .geo-header-actions .btn-geo-primary svg {
    display: none;
  }
  .master-showcase-stats {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .specs-data-grid {
    grid-template-columns: 1fr;
    gap: 8px;
  }
  .geo-section-title {
    font-size: 22px;
  }
  .geo-section-subtitle {
    font-size: 13.5px;
  }
}

/* ---- BREAKPOINT 7: ULTRA-COMPACT SCREENS (<= 380px) ---- */
@media (max-width: 380px) {
  .geo-header-actions .btn-geo-primary {
    display: none; /* In very compact viewports, leave header clean for logo & hamburger button */
  }
  .container {
    padding: 0 12px;
  }
  .geo-hero-title {
    font-size: 24px;
  }
  .product-media-wrap {
    height: 195px;
  }
  .rfq-calculator-container,
  .contact-details-card {
    padding: 16px 12px;
  }
  .drawer-content {
    width: 90%;
  }
  .footer-col-nav ul {
    grid-template-columns: 1fr;
  }
}

/* ==========================================================================
   UTILITY HELPER CLASSES
   ========================================================================== */
.drawer-brand {
  display: flex;
  align-items: center;
  text-decoration: none;
}

.drawer-cta-btn {
  margin-bottom: 4px;
}

.aux-icon {
  font-size: 18px;
  line-height: 1;
  flex-shrink: 0;
}

.contact-item-body {
  display: flex;
  flex-direction: column;
  gap: 2px;
}

.footer-col-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}

.geo-tag-text {
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  letter-spacing: 0.05em;
}
'''

updated_css = css[:responsive_start] + new_responsive_section

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(updated_css)

print('Updated css/styles.css with complete gap-fix and overflow-proof rules!')

