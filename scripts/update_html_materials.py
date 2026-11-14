with open('index.html', 'r', encoding='utf-8') as f:
    html = f.read()

# 1. Update materials tabs nav
old_tabs_start = '<div class="materials-tabs-nav" role="tablist" id="materialsTabList">'
old_tabs_end = '</div>\n\n          <div class="material-detail-card" id="materialDetailViewer">'

p_tabs1 = html.find(old_tabs_start)
p_tabs2 = html.find(old_tabs_end)
assert p_tabs1 != -1 and p_tabs2 != -1, 'Could not find materialsTabList in index.html'

new_tabs = '''<div class="materials-tabs-nav" role="tablist" id="materialsTabList">
            <button class="material-nav-btn active" data-mat="delrin" role="tab">
              <span class="mat-code">01</span>
              <span class="mat-name">Delrin (POM / Acetal)</span>
              <span class="mat-badge">Gears &amp; Bushings</span>
            </button>

            <button class="material-nav-btn" data-mat="nylon6gf" role="tab">
              <span class="mat-code">02</span>
              <span class="mat-name">Nylon 6 GF30% (Glass Filled)</span>
              <span class="mat-badge">High Tensile</span>
            </button>

            <button class="material-nav-btn" data-mat="nylon6" role="tab">
              <span class="mat-code">03</span>
              <span class="mat-name">Nylon 6 (Pure Polyamide)</span>
              <span class="mat-badge">Wear &amp; Toughness</span>
            </button>

            <button class="material-nav-btn" data-mat="nylon66" role="tab">
              <span class="mat-code">04</span>
              <span class="mat-name">Nylon 66 (Unfilled)</span>
              <span class="mat-badge">High Heat Polyamide</span>
            </button>

            <button class="material-nav-btn" data-mat="nylon66gf50" role="tab">
              <span class="mat-code">05</span>
              <span class="mat-name">Nylon 66 GF 50%</span>
              <span class="mat-badge">Metal Replacement</span>
            </button>

            <button class="material-nav-btn" data-mat="noryl" role="tab">
              <span class="mat-code">06</span>
              <span class="mat-name">Noryl (Modified PPE)</span>
              <span class="mat-badge">Hydrolytic &amp; Dielectric</span>
            </button>

            <button class="material-nav-btn" data-mat="pc" role="tab">
              <span class="mat-code">07</span>
              <span class="mat-name">Polycarbonate (PC)</span>
              <span class="mat-badge">Impact &amp; Optical</span>
            </button>

            <button class="material-nav-btn" data-mat="abs" role="tab">
              <span class="mat-code">08</span>
              <span class="mat-name">ABS (Terpolymer)</span>
              <span class="mat-badge">Rigid &amp; Gloss</span>
            </button>

            <button class="material-nav-btn" data-mat="polystyrene" role="tab">
              <span class="mat-code">09</span>
              <span class="mat-name">Polystyrene (HIPS / GPPS)</span>
              <span class="mat-badge">Dimensional &amp; Bezels</span>
            </button>

            <button class="material-nav-btn" data-mat="pps" role="tab">
              <span class="mat-code">10</span>
              <span class="mat-name">Polyphenylene Sulfide (PPS)</span>
              <span class="mat-badge">220°C Thermal</span>
            </button>

            <button class="material-nav-btn" data-mat="pu" role="tab">
              <span class="mat-code">11</span>
              <span class="mat-name">Polyurethane (PU / TPU)</span>
              <span class="mat-badge">Elastomer Shock</span>
            </button>

            <button class="material-nav-btn" data-mat="tpe" role="tab">
              <span class="mat-code">12</span>
              <span class="mat-name">Thermoplastic Elastomer (TPE)</span>
              <span class="mat-badge">Flexible Sealing Grip</span>
            </button>

            <button class="material-nav-btn" data-mat="pp" role="tab">
              <span class="mat-code">13</span>
              <span class="mat-name">Polypropylene (PP)</span>
              <span class="mat-badge">Chemical Barrier</span>
            </button>

            <button class="material-nav-btn" data-mat="hdpe" role="tab">
              <span class="mat-code">14</span>
              <span class="mat-name">HDPE &amp; LDPE</span>
              <span class="mat-badge">High Slip</span>
            </button>'''

html = html[:p_tabs1] + new_tabs + html[p_tabs2:]

# 2. Update rfqMaterial select
old_rfq_start = '<select id="rfqMaterial" required>'
old_rfq_end = '</select>'
p_rfq1 = html.find(old_rfq_start)
p_rfq2 = html.find(old_rfq_end, p_rfq1)
assert p_rfq1 != -1 and p_rfq2 != -1, 'Could not find rfqMaterial in index.html'

new_rfq = '''<select id="rfqMaterial" required>
                  <option value="Delrin (POM)">Delrin (POM / Acetal)</option>
                  <option value="Nylon 6 GF30%">Nylon 6 GF30% (Glass Filled)</option>
                  <option value="Nylon 6">Nylon 6 (Unfilled)</option>
                  <option value="Nylon 66 unfilled">Nylon 66 (Unfilled)</option>
                  <option value="Nylon 66 GF 50%">Nylon 66 GF 50% (High Modulus Structural)</option>
                  <option value="Noryl">Noryl (Modified Polyphenylene Ether / PPE)</option>
                  <option value="Polycarbonate (PC)">Polycarbonate (PC)</option>
                  <option value="ABS">ABS (General Purpose / Flame Retardant)</option>
                  <option value="Polystyrene">Polystyrene (HIPS / GPPS)</option>
                  <option value="PPS">Polyphenylene Sulfide (PPS)</option>
                  <option value="Polyurethane (PU)">Polyurethane (PU)</option>
                  <option value="Thermoplastic Elastomer">Thermoplastic Elastomer (TPE)</option>
                  <option value="PP">Polypropylene (PP)</option>
                  <option value="HDPE / LDPE">HDPE / LDPE</option>
                  <option value="Consulting Needed">Help Me Select the Best Material</option>
                </select>'''

html = html[:p_rfq1] + new_rfq + html[p_rfq2 + len(old_rfq_end):]

# 3. Update Hero micro-specs row
html = html.replace(
    '<span class="spec-label">POLYMER PORTFOLIO</span>\n              <span class="spec-value">10+ GRADES</span>\n              <span class="spec-sub">Delrin, GF-Nylon, PPS, PC</span>',
    '<span class="spec-label">POLYMER PORTFOLIO</span>\n              <span class="spec-value">14+ GRADES</span>\n              <span class="spec-sub">Delrin, PA66 GF50, Noryl, TPE, PPS</span>'
)

# 4. Update Showcase banner stat
html = html.replace(
    '<span class="stat-number">10+</span>\n                <span class="stat-label">Polymer Grades</span>',
    '<span class="stat-number">14+</span>\n                <span class="stat-label">Polymer Grades</span>'
)

# 5. Update meta keywords
html = html.replace(
    'Delrin, Nylon 6 GF30, PPS, PC, ABS',
    'Delrin, Nylon 6 GF30, Nylon 66 unfilled, Nylon 66 GF 50%, Noryl, Polystyrene, Thermoplastic Elastomer TPE, PPS, PC, ABS'
)

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(html)

print('Updated index.html with all 14 materials successfully!')

