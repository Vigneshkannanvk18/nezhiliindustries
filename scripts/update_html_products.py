import os

with open('index.html', 'r', encoding='utf-8') as f:
    text = f.read()

start_marker = '        <!-- Product Filter Pills & Instant Component Search -->'
end_marker = '        </div>\n\n      </div>\n    </section>\n\n    <!-- ===================================================================\n         ABOUT US & VALUE ENGINEERING'

p1 = text.find(start_marker)
p2 = text.find(end_marker)
assert p1 != -1 and p2 != -1, f'Markers not found! p1={p1}, p2={p2}'

new_products_block = '''        <!-- Master Production Line Showcase Banner -->
        <div class="master-showcase-banner">
          <div class="master-showcase-media">
            <picture>
              <source srcset="assets/products/master-component-showcase.webp" type="image/webp" />
              <img src="assets/products/master-component-showcase.jpg" alt="Negizhi Industries Complete Engineering Plastic Components Master Portfolio" class="master-showcase-img" loading="lazy" />
            </picture>
            <div class="master-showcase-badge">
              <span class="status-indicator-dot"></span>
              <span>COIMBATORE FACILITY // LIVE COMPONENT ARRAY</span>
            </div>
          </div>
          <div class="master-showcase-content">
            <div class="geo-kicker">[ PRODUCTION LINE SHOWCASE ]</div>
            <h3 class="master-showcase-title">100% In-House Manufactured Precision Components</h3>
            <p class="master-showcase-desc">
              From high-torque Delrin helical gears with splined metallic hubs to 5-frame motor fan cowls, shielded bearing rollers, Shore 92A/98A elastomeric spider couplings, and dual-brass insert brackets—manufactured to ±0.01 mm tolerance for Coimbatore's premier machine builders and electrical OEMs.
            </p>
            <div class="master-showcase-stats">
              <div class="showcase-stat-item">
                <span class="stat-number">200T</span>
                <span class="stat-label">Clamping Force</span>
              </div>
              <div class="showcase-stat-item">
                <span class="stat-number">±0.01 mm</span>
                <span class="stat-label">Mitutoyo Calibration</span>
              </div>
              <div class="showcase-stat-item">
                <span class="stat-number">10+</span>
                <span class="stat-label">Polymer Grades</span>
              </div>
            </div>
          </div>
        </div>

        <!-- Product Filter Pills & Instant Component Search -->
        <div class="products-toolbar-bar">
          <div class="product-category-pills" id="productFilterPills">
            <button class="prod-filter-btn active" data-cat="all" type="button">All Components (10)</button>
            <button class="prod-filter-btn" data-cat="mechanical" type="button">Mechanical &amp; Gears (4)</button>
            <button class="prod-filter-btn" data-cat="electrical" type="button">Electrical &amp; Switchgear (2)</button>
            <button class="prod-filter-btn" data-cat="bushings" type="button">Bushings &amp; Bearings (1)</button>
            <button class="prod-filter-btn" data-cat="specialty" type="button">High-Heat &amp; Specialty (3)</button>
          </div>

          <div class="product-search-box">
            <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="11" cy="11" r="8"/><line x1="21" y1="21" x2="16.65" y2="16.65"/></svg>
            <input type="text" id="productSearchInput" placeholder="Search by component, polymer, or application..." />
          </div>
        </div>

        <!-- Product Cards Grid (All with Enhanced Real Industrial Photos) -->
        <div class="products-cards-grid" id="productGridContainer">
          
          <!-- Product 1: Precision Delrin Gears -->
          <article class="product-card" data-cat="mechanical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/gear-delrin-helical.webp" type="image/webp" />
                <img src="assets/products/gear-delrin-helical.jpg" alt="Precision Delrin Involute Spur and Helical Gear with Splined Hub" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">MECHANICAL TRANSMISSION</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Precision Delrin (POM) Spur &amp; Helical Gears</h3>
              <p class="product-desc">High-torque, low-wear replacement for metallic gears featuring integrated internal splined hubs. Low dynamic friction and zero lubrication requirement in demanding industrial drives.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Delrin 100P / Polyoxymethylene</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Moulding Unit:</span>
                  <span class="spec-v">Haitian 200T / 90T Automatic</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Tolerance:</span>
                  <span class="spec-v">±0.01 mm (Mitutoyo Calibrated)</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Shanthi Gears, Sieger Spintech</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Delrin (POM)', 'Precision Delrin Helical Gear')">Request Gear Quote</a>
            </div>
          </article>

          <!-- Product 2: Industrial Motor Cooling Fan Cowls & Impellers -->
          <article class="product-card" data-cat="mechanical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/motor-cooling-fan-family.webp" type="image/webp" />
                <img src="assets/products/motor-cooling-fan-family.jpg" alt="Industrial Motor Cooling Fan Cowls and High-Flow Impellers Set" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">THERMAL AERODYNAMICS</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Motor Cooling Fan Cowls &amp; Radial Impellers</h3>
              <p class="product-desc">Complete graduated range of 5 frame sizes of slotted motor cooling cowls paired with multi-blade aerodynamic radial impellers for uniform electric motor airflow.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Nylon 6 GF30% / Impact Copolymer</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Range Sizes:</span>
                  <span class="spec-v">5 Standard Frame Series (63 to 132)</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Airflow Dynamic:</span>
                  <span class="spec-v">High-CFM Slotted Low-Vibration</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Electric Motors, Industrial Pumps</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Nylon 6 GF30%', 'Motor Cooling Fan Cowl & Impeller')">Request Fan Quote</a>
            </div>
          </article>

          <!-- Product 3: PU Flexible Spider Couplings -->
          <article class="product-card" data-cat="mechanical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/pu-spider-couplings-family.webp" type="image/webp" />
                <img src="assets/products/pu-spider-couplings-family.jpg" alt="Polyurethane Elastomer Flexible Spider Couplings" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">SHOCK &amp; VIBRATION DAMPING</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Polyurethane (PU) Flexible Spider Couplings</h3>
              <p class="product-desc">Four graduated frame sizes of Rotex-type elastomer spider inserts. Effectively absorbs angular shaft misalignments, damping high-frequency shocks and motor torsional flutter.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Thermoplastic Polyurethane (TPU)</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Durometer:</span>
                  <span class="spec-v">Shore 92A / 98A Calibrated</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Thermal Service:</span>
                  <span class="spec-v">-40°C to +90°C Continuous</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Motor-Gearbox Couplings, Star Drives</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Polyurethane (PU)', 'PU Flexible Spider Coupling')">Request Coupling Quote</a>
            </div>
          </article>

          <!-- Product 4: Threaded Brass Insert Overmoulded Structural Bracket -->
          <article class="product-card" data-cat="mechanical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/brass-insert-bracket.webp" type="image/webp" />
                <img src="assets/products/brass-insert-bracket.jpg" alt="Threaded Brass Insert Overmoulded Structural Bracket" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">INSERT OVERMOULDING</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Threaded Brass Insert Overmoulded Brackets</h3>
              <p class="product-desc">Precision vertical insert moulding integrating dual diamond-knurled brass threaded bushings directly into high-tensile structural polymers with extreme pullout strength.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Technology:</span>
                  <span class="spec-v">15T Vertical Screw Injection Unit</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Pullout Force:</span>
                  <span class="spec-v">&gt; 8.5 kN Torque &amp; Axial Lock</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Thread Sizes:</span>
                  <span class="spec-v">Dual Knurled M4 / M5 / M6 / M8</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Gishnu Gears, Bas-j Industries</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Nylon 6', 'Threaded Brass Overmould Bracket')">Request Insert Quote</a>
            </div>
          </article>

          <!-- Product 5: Precision Overmoulded Bearing Rollers -->
          <article class="product-card" data-cat="bushings">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/bearing-rollers-overmoulded.webp" type="image/webp" />
                <img src="assets/products/bearing-rollers-overmoulded.jpg" alt="Precision Overmoulded Bearing Roller Wheels and Sleeve Bushings" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">HEAVY DYNAMIC LOAD</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Overmoulded Bearing Rollers &amp; Sleeve Bushings</h3>
              <p class="product-desc">Precision overmoulded roller wheels with integrated shielded steel ball bearings. Provides smooth rolling motion, ultra-low rolling friction, and zero galling under sustained loads.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Delrin POM / Cast Polyamide</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Bearing Core:</span>
                  <span class="spec-v">Shielded Steel Ball Bearing Race</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Bore Fit:</span>
                  <span class="spec-v">H7 / g6 Standard Press-Fit</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Vignesh Gears, Covai Gears</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Delrin (POM)', 'Overmoulded Bearing Roller')">Request Roller Quote</a>
            </div>
          </article>

          <!-- Product 6: Switchgear Housing & Terminal Box -->
          <article class="product-card" data-cat="electrical">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/switchgear-terminal-enclosure.webp" type="image/webp" />
                <img src="assets/products/switchgear-terminal-enclosure.jpg" alt="Glass-Filled Nylon Switchgear Terminal Housing" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">ELECTRICAL INSULATION</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Nylon 6 GF30% Switchgear Enclosures</h3>
              <p class="product-desc">Heavy-duty 30% glass-reinforced electrical terminal housings with circular conduit knockouts, mounting lugs, high dielectric breakdown resistance, and flame retardancy.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Polyamide 6 GF30% Reinforced</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Moulding Unit:</span>
                  <span class="spec-v">200-Ton High-Clamping Platen</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Flame Rating:</span>
                  <span class="spec-v">UL94 V-0 Self-Extinguishing</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Safvolt Switch Gears, Rydon</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Nylon 6 GF30%', 'Switchgear Terminal Enclosure')">Request Housing Quote</a>
            </div>
          </article>

          <!-- Product 7: Optical PC Meter Cover -->
          <article class="product-card" data-cat="electrical">
            <div class="product-media-wrap">
              <img src="assets/products/optical-meter-cover.svg?v=2" alt="Optical Grade Polycarbonate Meter Cover" class="product-img" loading="lazy" />
              <span class="product-tag-badge">OPTICAL &amp; IMPACT PROOF</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Optical Polycarbonate (PC) Meter Covers</h3>
              <p class="product-desc">High-clarity, vandal-proof inspection window covers engineered for outdoor electricity meters, dial gauges, and industrial digital readouts.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Optical Virgin Polycarbonate (PC)</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Light Transmit:</span>
                  <span class="spec-v">92% Optical Clarity</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Impact Rating:</span>
                  <span class="spec-v">IK10 Shock &amp; UV Stabilized</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Power Distribution &amp; Digital Meters</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Polycarbonate (PC)', 'Optical Meter Cover')">Request Cover Quote</a>
            </div>
          </article>

          <!-- Product 8: Precision Fluidics & Sealing Plugs -->
          <article class="product-card" data-cat="specialty">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/fluidic-connectors-plugs.webp" type="image/webp" />
                <img src="assets/products/fluidic-connectors-plugs.jpg" alt="Precision Fluidic Barbed Connectors and Threaded Sealing Plugs" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">FLUIDIC SEALING</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Fluidic Barbed Connectors &amp; Sealing Plugs</h3>
              <p class="product-desc">Precision barbed hose adapters and threaded blanking plugs featuring elastomeric O-ring seals. Engineered for zero fluid leakage in industrial pneumatic and coolant lines.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Engineering Polypropylene (PP) / POM</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Thread Standards:</span>
                  <span class="spec-v">BSP / NPT Precision Molded Threads</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Sealing System:</span>
                  <span class="spec-v">Nitrile O-Ring &amp; Barb Lock</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Coolant Manifolds, Pneumatic Lines</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Polypropylene (PP)', 'Fluidic Connectors & Plugs')">Request Fluidics Quote</a>
            </div>
          </article>

          <!-- Product 9: Threaded Pipe & Flange Caps -->
          <article class="product-card" data-cat="specialty">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/threaded-pipe-caps.webp" type="image/webp" />
                <img src="assets/products/threaded-pipe-caps.jpg" alt="HDPE Heavy Duty Threaded Protective Pipe and Flange Caps" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">CORROSION &amp; THREAD SHIELD</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Threaded Protective Pipe Caps &amp; Flanges</h3>
              <p class="product-desc">Heavy-duty internal threaded end caps and chemical flanges manufactured from high-density polymers. Guarantees 100% moisture barrier and impact protection during transit.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">High Density Polyethylene (HDPE) / PP</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Pressure Class:</span>
                  <span class="spec-v">PN10 / PN16 Standard Thread Fit</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Water Uptake:</span>
                  <span class="spec-v">&lt; 0.01% (Completely Inert)</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Chemical Piping, Hydraulic Transits</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('HDPE / LDPE', 'Threaded Protective Pipe Cap')">Request Cap Quote</a>
            </div>
          </article>

          <!-- Product 10: Color-Coded Alignment Bullet Pins -->
          <article class="product-card" data-cat="specialty">
            <div class="product-media-wrap">
              <picture>
                <source srcset="assets/products/alignment-bullet-pins.webp" type="image/webp" />
                <img src="assets/products/alignment-bullet-pins.jpg" alt="Color Coded Precision Alignment Bullet Pins and Masking Plugs" class="product-img" loading="lazy" />
              </picture>
              <span class="product-tag-badge">PRECISION TOOLING LOCATORS</span>
            </div>
            <div class="product-body">
              <h3 class="product-title">Color-Coded Alignment Bullet Pins &amp; Plugs</h3>
              <p class="product-desc">Precision tapered dowel locator pins and high-temperature masking stoppers in 4 distinct color-coded diameters for foolproof assembly line positioning and painting mask protection.</p>
              
              <div class="product-spec-matrix">
                <div class="prod-spec-row">
                  <span class="spec-k">Polymer Grade:</span>
                  <span class="spec-v">Impact Nylon 6 / Polyurethane TPU</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Color Coding:</span>
                  <span class="spec-v">Red, Natural, Blue, Orange</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Base Flange:</span>
                  <span class="spec-v">Integrated Ergonomic Rim Lock</span>
                </div>
                <div class="prod-spec-row">
                  <span class="spec-k">Application:</span>
                  <span class="spec-v">Assembly Fixtures, Paint Masking</span>
                </div>
              </div>

              <a href="#rfq" class="btn-geo-primary btn-full" onclick="preselectMaterial('Nylon 6', 'Alignment Bullet Pins')">Request Pin Quote</a>
            </div>
          </article>'''

updated = text[:p1] + new_products_block + text[p2:]
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(updated)
print('Updated index.html successfully!')

