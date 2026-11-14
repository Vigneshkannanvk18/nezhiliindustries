import re

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

# 1. Update .footer-col-brand and .footer-logo in the base section (around line 1920)
base_footer_old = '''/* Footer */
.geo-footer {
  background: #03050a;
  border-top: 1px solid var(--geo-border-subtle);
  padding: 60px 0 0;
  position: relative;
  z-index: 2;
  color: var(--text-primary);
}

.geo-footer-inner {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1.2fr;
  gap: 40px;
  padding-bottom: 40px;
}

.footer-logo {
  height: 48px;
  width: auto;
  margin-bottom: 14px;
}'''

base_footer_new = '''/* Footer */
.geo-footer {
  background: #03050a;
  border-top: 1px solid var(--geo-border-subtle);
  padding: 60px 0 0;
  position: relative;
  z-index: 2;
  color: var(--text-primary);
}

.geo-footer-inner {
  display: grid;
  grid-template-columns: 1.4fr 1fr 1.2fr;
  gap: 40px;
  padding-bottom: 40px;
}

.footer-col-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}

.footer-brand-link {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
}

.footer-logo {
  height: 44px;
  width: auto;
  max-width: 240px;
  object-fit: contain;
  align-self: flex-start;
  display: block;
  margin-bottom: 8px;
  filter: drop-shadow(0 2px 10px rgba(0, 229, 255, 0.25));
}'''

if base_footer_old in css:
    css = css.replace(base_footer_old, base_footer_new)
    print('Replaced base footer styles!')
else:
    print('Notice: base footer pattern not exact, updating with regex...')
    css = re.sub(
        r'\.footer-logo\s*\{\s*height:\s*48px;\s*width:\s*auto;\s*margin-bottom:\s*14px;\s*\}',
        '''.footer-col-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}

.footer-brand-link {
  display: inline-flex;
  align-items: center;
  text-decoration: none;
}

.footer-logo {
  height: 44px;
  width: auto;
  max-width: 240px;
  object-fit: contain;
  align-self: flex-start;
  display: block;
  margin-bottom: 8px;
  filter: drop-shadow(0 2px 10px rgba(0, 229, 255, 0.25));
}''',
        css
    )

# 2. Update the duplicate .footer-col-brand at line 3472
dup_footer = '''.footer-col-brand {
  display: flex;
  flex-direction: column;
  gap: 16px;
}'''

dup_footer_new = '''.footer-col-brand {
  display: flex;
  flex-direction: column;
  align-items: flex-start;
  gap: 14px;
}'''

css = css.replace(dup_footer, dup_footer_new)

# 3. Add responsive enhancements to media queries
# Let's inspect breakpoints starting from '/* ---- BREAKPOINT 1:'
responsive_start = css.find('/* ---- BREAKPOINT 1:')
assert responsive_start != -1, 'Could not find responsive breakpoints start'

responsive_section = '''/* ---- BREAKPOINT 1: LARGE TABLETS & SMALL LAPTOPS (<= 1200px) ---- */
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
    display: none; /* Switch to sleek mobile/tablet hamburger navigation */
  }
  .geo-mobile-toggle {
    display: flex;
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
    gap: 24px;
  }
  .sequence-sticky-container {
    position: relative;
    top: 0;
  }
  .seq-pills-bar {
    display: flex;
    overflow-x: auto;
    flex-wrap: nowrap;
    gap: 8px;
    padding: 4px 2px 8px;
    -webkit-overflow-scrolling: touch;
    scrollbar-width: none;
  }
  .seq-pills-bar::-webkit-scrollbar {
    display: none;
  }
  .seq-pill {
    flex-shrink: 0;
    white-space: nowrap;
    padding: 8px 14px;
    font-size: 12px;
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
  /* Ticker Bar: sleek compact mobile format */
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
}

/* ---- BREAKPOINT 5: STANDARD MOBILE DEVICES (<= 640px) ---- */
@media (max-width: 640px) {
  .container {
    padding: 0 16px;
  }
  .geo-hero-section {
    padding: 26px 0 38px;
  }
  .geo-hero-title {
    font-size: clamp(26px, 7.5vw, 34px);
    line-height: 1.18;
  }
  .title-sub {
    font-size: 12.5px;
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
    margin-bottom: 24px;
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
    min-height: 190px;
    width: 100%;
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
  .step-card {
    padding: 18px 16px;
  }
  .step-title {
    font-size: 15px;
  }
  .step-desc {
    font-size: 13px;
  }

  /* Products Cards: Clean 1 Column on Mobile */
  .products-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 20px;
  }
  .product-card {
    width: 100%;
    box-sizing: border-box;
  }
  .product-media-wrap {
    height: 230px;
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
    height: 52px;
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
  .geo-header-actions .btn-geo-ghost {
    display: none; /* Hide brochure CTA from tight mobile header bar */
  }
  .geo-brand-logo {
    height: 40px;
    max-width: 140px;
  }
  .geo-header-actions .btn-geo-primary {
    padding: 8px 12px;
    font-size: 12px;
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
    font-size: 23px;
  }
  .geo-section-subtitle {
    font-size: 13.5px;
  }
}

/* ---- BREAKPOINT 7: ULTRA-COMPACT SCREENS (<= 360px) ---- */
@media (max-width: 360px) {
  .container {
    padding: 0 12px;
  }
  .geo-hero-title {
    font-size: 24px;
  }
  .product-media-wrap {
    height: 200px;
  }
  .rfq-calculator-container,
  .contact-details-card {
    padding: 18px 12px;
  }
  .drawer-content {
    width: 92%;
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

updated_css = css[:responsive_start] + responsive_section

with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(updated_css)

print('Updated css/styles.css successfully!')

