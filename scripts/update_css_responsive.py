import os

with open('css/styles.css', 'r', encoding='utf-8') as f:
    css = f.read()

target = '/* Responsive Breakpoints */'
idx = css.find(target)
assert idx != -1, 'Could not find /* Responsive Breakpoints */'

new_responsive_css = '''/* ==========================================================================
   PRODUCT SHOWCASE & COMPONENT CARD ENHANCEMENTS
   ========================================================================== */
.product-media-wrap picture {
  width: 100%;
  height: 100%;
  display: flex;
  align-items: center;
  justify-content: center;
}

.product-img {
  width: 100%;
  height: 100%;
  object-fit: contain;
  object-position: center;
  transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  padding: 14px;
}

.product-card:hover .product-img {
  transform: scale(1.05);
}

/* Master Production Line Showcase Banner */
.master-showcase-banner {
  background: #ffffff;
  border: 1px solid #e2e8f0;
  border-radius: var(--radius-lg);
  overflow: hidden;
  margin-bottom: 36px;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.05);
  display: grid;
  grid-template-columns: 1.2fr 1fr;
  align-items: stretch;
}

.master-showcase-media {
  position: relative;
  background: #f8fafc;
  display: flex;
  align-items: center;
  justify-content: center;
  border-right: 1px solid #e2e8f0;
  overflow: hidden;
  min-height: 290px;
}

.master-showcase-media picture,
.master-showcase-img {
  width: 100%;
  height: 100%;
  object-fit: cover;
  object-position: center;
  display: block;
}

.master-showcase-badge {
  position: absolute;
  top: 14px;
  left: 14px;
  background: rgba(7, 11, 22, 0.88);
  backdrop-filter: blur(8px);
  color: var(--geo-cyan);
  font-family: var(--font-mono);
  font-size: 11px;
  font-weight: 700;
  padding: 6px 14px;
  border-radius: var(--radius-pill);
  border: 1px solid rgba(0, 229, 255, 0.35);
  display: flex;
  align-items: center;
  gap: 8px;
  z-index: 2;
  box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
}

.master-showcase-content {
  padding: 32px 36px;
  display: flex;
  flex-direction: column;
  justify-content: center;
  background: #ffffff;
}

.master-showcase-title {
  font-family: var(--font-heading);
  font-size: 22px;
  font-weight: 800;
  color: #0f172a;
  margin: 8px 0 12px;
  line-height: 1.3;
}

.master-showcase-desc {
  font-size: 14.5px;
  color: #475569;
  line-height: 1.6;
  margin-bottom: 20px;
}

.master-showcase-stats {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 16px;
  border-top: 1px solid #e2e8f0;
  padding-top: 18px;
}

.showcase-stat-item {
  display: flex;
  flex-direction: column;
}

.showcase-stat-item .stat-number {
  font-family: var(--font-mono);
  font-size: 20px;
  font-weight: 800;
  color: #0066ff;
}

.showcase-stat-item .stat-label {
  font-size: 12px;
  color: #64748b;
  margin-top: 2px;
}

/* ==========================================================================
   MOBILE & TABLET NAVIGATION DRAWER
   ========================================================================== */
.geo-mobile-toggle {
  display: none;
  width: 44px;
  height: 44px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.15);
  border-radius: var(--radius-sm);
  cursor: pointer;
  padding: 0;
  align-items: center;
  justify-content: center;
  flex-direction: column;
  gap: 5px;
  transition: all var(--transition-fast);
  color: var(--text-primary);
  z-index: 101;
}

.geo-mobile-toggle:hover {
  background: rgba(0, 229, 255, 0.1);
  border-color: var(--geo-cyan);
}

.hamburger-bar {
  display: block;
  width: 20px;
  height: 2px;
  background-color: #f8fafc;
  border-radius: 2px;
  transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
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
}

.drawer-header {
  display: flex;
  align-items: center;
  justify-content: space-between;
  padding-bottom: 16px;
  border-bottom: 1px solid rgba(255, 255, 255, 0.08);
}

.drawer-logo {
  height: 36px;
  width: auto;
  max-width: 150px;
  object-fit: contain;
}

.drawer-close-btn {
  width: 40px;
  height: 40px;
  background: rgba(255, 255, 255, 0.05);
  border: 1px solid rgba(255, 255, 255, 0.1);
  border-radius: var(--radius-sm);
  color: #cbd5e1;
  display: flex;
  align-items: center;
  justify-content: center;
  cursor: pointer;
  transition: all var(--transition-fast);
}

.drawer-close-btn:hover {
  color: var(--geo-cyan);
  border-color: var(--geo-cyan);
}

.drawer-meta-badge {
  display: flex;
  align-items: center;
  gap: 8px;
  font-family: var(--font-mono);
  font-size: 10px;
  color: var(--geo-cyan);
  padding: 10px 0;
  border-bottom: 1px solid rgba(255, 255, 255, 0.06);
}

.drawer-nav {
  margin: 16px 0;
  flex: 1;
}

.drawer-nav-list {
  list-style: none;
  display: flex;
  flex-direction: column;
  gap: 4px;
}

.drawer-nav-link {
  display: flex;
  align-items: center;
  gap: 12px;
  padding: 12px 14px;
  border-radius: var(--radius-sm);
  color: #cbd5e1;
  text-decoration: none;
  font-family: var(--font-heading);
  font-size: 15px;
  font-weight: 600;
  letter-spacing: 0.02em;
  transition: all var(--transition-fast);
}

.drawer-nav-idx {
  font-family: var(--font-mono);
  font-size: 11px;
  color: var(--geo-cyan);
  opacity: 0.8;
}

.drawer-nav-link:hover,
.drawer-nav-link.active {
  background: rgba(0, 229, 255, 0.1);
  color: #fff;
  border-left: 3px solid var(--geo-cyan);
}

.drawer-actions {
  display: flex;
  flex-direction: column;
  gap: 10px;
  padding-top: 16px;
  border-top: 1px solid rgba(255, 255, 255, 0.08);
}

.drawer-tel-link {
  display: flex;
  align-items: center;
  justify-content: center;
  gap: 8px;
  padding: 12px;
  font-family: var(--font-mono);
  font-size: 13px;
  color: var(--geo-cyan);
  text-decoration: none;
  border: 1px dashed rgba(0, 229, 255, 0.35);
  border-radius: var(--radius-sm);
  background: rgba(0, 229, 255, 0.04);
  transition: all var(--transition-fast);
}

.drawer-tel-link:hover {
  background: rgba(0, 229, 255, 0.1);
  border-color: var(--geo-cyan);
}

body.menu-locked {
  overflow: hidden !important;
}

/* ==========================================================================
   COMPLETE RESPONSIVE LAYOUT SYSTEM (TABLET & MOBILE FIXES)
   ========================================================================== */

/* Universal Responsive Canvas & Images */
canvas#mouldingCanvas {
  width: 100% !important;
  height: auto !important;
  max-width: 100% !important;
  aspect-ratio: 900 / 420;
  display: block;
}

img, svg, video {
  max-width: 100%;
}

/* ---- BREAKPOINT 1: LARGE TABLETS & SMALL LAPTOPS (<= 1200px) ---- */
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
  }
  .quality-instruments-grid {
    grid-template-columns: repeat(2, 1fr);
  }
  .geo-footer-inner {
    grid-template-columns: 1.2fr 1fr;
    gap: 32px;
  }
  .footer-col-contact {
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
    padding-bottom: 8px;
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
    padding-bottom: 6px;
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
    flex-direction: row;
    overflow-x: auto;
    flex-wrap: nowrap;
    gap: 8px;
    padding-bottom: 8px;
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
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 6px 14px;
    font-size: 10.5px;
    background: #04060c;
  }
  .geo-coord-badge {
    display: none;
  }
  .geo-ticker-status {
    flex: 1;
    overflow: hidden;
    text-overflow: ellipsis;
    white-space: nowrap;
    margin-right: 10px;
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
  }
  .machinery-grid {
    grid-template-columns: 1fr;
  }
}

/* ---- BREAKPOINT 5: STANDARD MOBILE DEVICES (<= 640px) ---- */
@media (max-width: 640px) {
  .container {
    padding: 0 16px;
  }
  .geo-hero-section {
    padding: 30px 0 44px;
  }
  .geo-hero-title {
    font-size: clamp(28px, 7.5vw, 36px);
    line-height: 1.18;
  }
  .title-sub {
    font-size: 13px;
    letter-spacing: 0.14em;
  }
  .geo-hero-lead {
    font-size: 14.5px;
    line-height: 1.6;
    margin-bottom: 22px;
  }
  .geo-hero-cta-group {
    flex-direction: column;
    width: 100%;
    gap: 12px;
    margin-bottom: 26px;
  }
  .geo-hero-cta-group .btn-geo-primary,
  .geo-hero-cta-group .btn-geo-secondary {
    width: 100%;
    justify-content: center;
    padding: 14px 20px;
  }
  .geo-micro-specs-row {
    flex-direction: column;
    align-items: stretch;
    padding: 16px;
    gap: 12px;
    max-width: 100%;
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
  }
  .micro-spec-box .spec-value {
    font-size: 16px;
    margin: 0;
  }
  .micro-spec-box .spec-sub {
    display: none;
  }
  .geo-floating-widgets {
    grid-template-columns: 1fr;
  }

  /* Products Cards: Clean 1 Column on Mobile */
  .products-cards-grid {
    grid-template-columns: 1fr !important;
    gap: 20px;
  }
  .product-media-wrap {
    height: 240px;
  }
  .product-body {
    padding: 20px 18px;
  }
  .product-title {
    font-size: 17px;
  }
  .product-desc {
    font-size: 13.5px;
  }

  /* Process Cycle HUD on Mobile */
  .sequence-hud-top {
    grid-template-columns: 1fr 1fr;
    gap: 8px;
    padding: 10px 12px;
  }
  .hud-box.hud-stage {
    grid-column: 1 / -1;
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

  /* Quality Instruments on Mobile */
  .quality-instruments-grid {
    grid-template-columns: 1fr;
  }
  .instrument-card {
    padding: 20px 18px;
  }

  /* Footer on Mobile */
  .geo-footer-inner {
    grid-template-columns: 1fr;
    gap: 28px;
  }
  .footer-bottom {
    flex-direction: column;
    text-align: center;
    gap: 12px;
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
    height: 38px;
    max-width: 135px;
  }
  .geo-header-actions .btn-geo-primary {
    padding: 8px 12px;
    font-size: 12.5px;
  }
  .geo-header-actions .btn-geo-primary svg {
    display: none;
  }
  .master-showcase-stats {
    grid-template-columns: 1fr;
    gap: 12px;
  }
  .mat-properties-grid {
    grid-template-columns: 1fr;
    gap: 10px;
  }
  .specs-data-grid {
    grid-template-columns: 1fr;
  }
  .geo-section-title {
    font-size: 24px;
  }
  .geo-section-subtitle {
    font-size: 14px;
  }
}

/* ---- BREAKPOINT 7: ULTRA-COMPACT SCREENS (<= 360px) ---- */
@media (max-width: 360px) {
  .container {
    padding: 0 12px;
  }
  .geo-hero-title {
    font-size: 26px;
  }
  .product-media-wrap {
    height: 210px;
  }
  .rfq-calculator-container,
  .contact-details-card {
    padding: 20px 12px;
  }
  .drawer-content {
    width: 90%;
  }
}
'''

updated_css = css[:idx] + new_responsive_css
with open('css/styles.css', 'w', encoding='utf-8') as f:
    f.write(updated_css)

print('Updated css/styles.css with complete responsive system!')

