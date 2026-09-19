/**
 * NEGIZHI INDUSTRIES - High-Performance Application Logic
 * Interactive Scroll Sequence Animation (200T Moulding Cycle),
 * Product Filter/Search, Polymer Matrix Explorer, and Technical RFQ System.
 */

document.addEventListener('DOMContentLoaded', () => {

  // =========================================================================
  // 1. SCROLL SEQUENCE ANIMATION ENGINE: 200-TON MOULDING CYCLE
  // =========================================================================
  const canvas = document.getElementById('mouldingCanvas');
  const ctx = canvas.getContext('2d');
  const sequenceWrapper = document.getElementById('sequenceWrapper');
  const progressBar = document.getElementById('sequenceProgressBar');
  const hudStageName = document.getElementById('hudStageName');
  const hudClamp = document.getElementById('hudClamp');
  const hudPressure = document.getElementById('hudPressure');
  const hudTemp = document.getElementById('hudTemp');
  const hudCycle = document.getElementById('hudCycle');
  const seqPills = document.querySelectorAll('.seq-pill');
  const scrollSteps = document.querySelectorAll('.scroll-step');

  let currentProgress = 0; // 0.0 to 1.0
  let targetProgress = 0;
  let animFrameId = null;

  // Set logical resolution
  canvas.width = 900;
  canvas.height = 420;

  // Stages definition
  const STAGES = [
    {
      num: 1,
      name: "STAGE 01: POLYMER GRANULE INGESTION & HEATING",
      clamp: "0 TONS",
      pressure: "0 MPa",
      temp: "300°C",
      cycle: "1.2s / 14.8s"
    },
    {
      num: 2,
      name: "STAGE 02: 200-TON HYDRAULIC CLAMP LOCKING",
      clamp: "200 TONS LOCKED",
      pressure: "15 MPa",
      temp: "295°C",
      cycle: "4.5s / 14.8s"
    },
    {
      num: 3,
      name: "STAGE 03: HIGH-PRESSURE CAVITY INJECTION",
      clamp: "200 TONS",
      pressure: "185 MPa PEAK",
      temp: "280°C",
      cycle: "7.8s / 14.8s"
    },
    {
      num: 4,
      name: "STAGE 04: CONFORMAL COOLING & CRYSTALLIZATION",
      clamp: "200 TONS",
      pressure: "40 MPa HOLD",
      temp: "85°C SOLIDIFIED",
      cycle: "11.5s / 14.8s"
    },
    {
      num: 5,
      name: "STAGE 05: DEMOULDING & MITUTOYO QA INSPECTION",
      clamp: "0 TONS OPEN",
      pressure: "0 MPa",
      temp: "50°C AMBIENT",
      cycle: "14.8s COMPLETE"
    }
  ];

  // Render Machine & Cycle on Canvas
  function drawMouldingCycle(p) {
    ctx.clearRect(0, 0, canvas.width, canvas.height);

    const w = canvas.width;
    const h = canvas.height;

    // Technical Coordinate Grid Background
    ctx.strokeStyle = "rgba(0, 229, 255, 0.05)";
    ctx.lineWidth = 1;
    for (let x = 0; x < w; x += 40) {
      ctx.beginPath();
      ctx.moveTo(x, 0);
      ctx.lineTo(x, h);
      ctx.stroke();
    }
    for (let y = 0; y < h; y += 40) {
      ctx.beginPath();
      ctx.moveTo(0, y);
      ctx.lineTo(w, y);
      ctx.stroke();
    }

    // Machine Base Frame
    ctx.fillStyle = "#0c1424";
    ctx.strokeStyle = "#1e293b";
    ctx.lineWidth = 2;
    ctx.fillRect(80, 280, 740, 60);
    ctx.strokeRect(80, 280, 740, 60);

    // Tie Bars (Upper & Lower Hardened Chrome Columns)
    ctx.fillStyle = "#334155";
    ctx.fillRect(100, 110, 480, 16);
    ctx.fillRect(100, 250, 480, 16);
    ctx.fillStyle = "#64748b";
    ctx.fillRect(100, 112, 480, 4);
    ctx.fillRect(100, 252, 480, 4);

    // Fixed Platen (Stationary Die Base on Right)
    const fixedPlatenX = 420;
    ctx.fillStyle = "#162238";
    ctx.strokeStyle = "#00e5ff";
    ctx.lineWidth = 1.5;
    ctx.fillRect(fixedPlatenX, 80, 60, 200);
    ctx.strokeRect(fixedPlatenX, 80, 60, 200);

    // Moving Platen on Left: Moves from 180 to 340 based on Stage 2 progress
    // When p <= 0.25 (Stage 1), open at X = 200
    // When 0.25 < p <= 0.45 (Stage 2), moves from 200 to 340 (closed)
    // When p > 0.8 (Stage 5), opens back to 220
    let platenX = 200;
    if (p > 0.2 && p <= 0.45) {
      const t = (p - 0.2) / 0.25;
      platenX = 200 + (340 - 200) * t;
    } else if (p > 0.45 && p <= 0.8) {
      platenX = 340; // Fully locked
    } else if (p > 0.8) {
      const t = (p - 0.8) / 0.2;
      platenX = 340 - (340 - 220) * t; // Opening
    }

    // Moving Platen Die
    ctx.fillStyle = "#1e2d4a";
    ctx.strokeStyle = "#38bdf8";
    ctx.fillRect(platenX, 80, 60, 200);
    ctx.strokeRect(platenX, 80, 60, 200);

    // Mold Halves (Cavity & Core)
    const coreX = platenX + 60;
    const cavityX = fixedPlatenX - 25;

    // Moving Core Half
    ctx.fillStyle = "#2a3b5c";
    ctx.strokeStyle = "#00e5ff";
    ctx.fillRect(coreX, 110, 25, 140);
    ctx.strokeRect(coreX, 110, 25, 140);

    // Stationary Cavity Half
    ctx.fillStyle = "#2a3b5c";
    ctx.strokeStyle = "#00e5ff";
    ctx.fillRect(cavityX, 110, 25, 140);
    ctx.strokeRect(cavityX, 110, 25, 140);

    // Injection Barrel & Screw Unit (Right Side)
    const barrelX = fixedPlatenX + 60;
    ctx.fillStyle = "#111b2d";
    ctx.strokeStyle = "#475569";
    ctx.fillRect(barrelX, 150, 240, 60);
    ctx.strokeRect(barrelX, 150, 240, 60);

    // Injection Nozzle
    ctx.beginPath();
    ctx.moveTo(barrelX, 170);
    ctx.lineTo(fixedPlatenX + 5, 175);
    ctx.lineTo(fixedPlatenX + 5, 185);
    ctx.lineTo(barrelX, 190);
    ctx.fillStyle = "#38bdf8";
    ctx.fill();

    // Raw Material Hopper (Top of Barrel)
    ctx.beginPath();
    ctx.moveTo(barrelX + 130, 150);
    ctx.lineTo(barrelX + 90, 60);
    ctx.lineTo(barrelX + 190, 60);
    ctx.lineTo(barrelX + 150, 150);
    ctx.closePath();
    ctx.fillStyle = "#1a253c";
    ctx.strokeStyle = "#00e5ff";
    ctx.fill();
    ctx.stroke();

    // Granule Pellets in Hopper
    ctx.fillStyle = "#00e5ff";
    for (let i = 0; i < 24; i++) {
      const px = barrelX + 105 + (i % 6) * 12 + (i % 2) * 5;
      const py = 75 + Math.floor(i / 6) * 14;
      ctx.beginPath();
      ctx.arc(px, py, 3, 0, Math.PI * 2);
      ctx.fill();
    }

    // 50mm Reciprocating Screw inside Barrel
    // Screw advances forward during injection (p: 0.4 to 0.65)
    let screwOffset = 0;
    if (p > 0.4 && p <= 0.65) {
      screwOffset = ((p - 0.4) / 0.25) * 35;
    } else if (p > 0.65 && p <= 0.8) {
      screwOffset = 35;
    } else if (p > 0.8) {
      screwOffset = 35 * (1 - (p - 0.8) / 0.2);
    }

    ctx.fillStyle = "#334155";
    ctx.fillRect(barrelX + 80 - screwOffset, 168, 140, 24);
    // Screw Flight Ribs
    ctx.strokeStyle = "#64748b";
    ctx.lineWidth = 2;
    for (let s = 0; s < 7; s++) {
      const sx = barrelX + 85 - screwOffset + s * 18;
      ctx.beginPath();
      ctx.moveTo(sx, 168);
      ctx.lineTo(sx + 10, 192);
      ctx.stroke();
    }

    // Molten Polymer Injection Melt Glow inside Barrel Nozzle
    if (p > 0.35 && p <= 0.8) {
      ctx.fillStyle = "rgba(0, 229, 255, 0.8)";
      ctx.fillRect(barrelX, 172, 80 - screwOffset, 16);
      ctx.shadowColor = "#00e5ff";
      ctx.shadowBlur = 15;
      ctx.fillRect(fixedPlatenX + 5, 176, 20, 8);
      ctx.shadowBlur = 0;
    }

    // Component Forming inside Mold Cavity (When dies meet at platenX == 340)
    if (platenX >= 335) {
      // Cavity fill progress
      let fillRatio = 0;
      if (p > 0.45 && p <= 0.65) {
        fillRatio = (p - 0.45) / 0.2;
      } else if (p > 0.65) {
        fillRatio = 1;
      }

      if (fillRatio > 0) {
        // High-precision gear profile forming inside cavity
        ctx.save();
        ctx.translate(380, 180);
        ctx.fillStyle = fillRatio >= 0.9 ? "#ffffff" : "#00e5ff";
        ctx.shadowColor = "#00e5ff";
        ctx.shadowBlur = fillRatio < 1 ? 12 : 4;
        
        ctx.beginPath();
        ctx.arc(0, 0, 30 * fillRatio, 0, Math.PI * 2);
        ctx.fill();

        if (fillRatio > 0.7) {
          ctx.strokeStyle = "#0066ff";
          ctx.lineWidth = 3;
          ctx.stroke();
          // Center hole
          ctx.fillStyle = "#0c1424";
          ctx.beginPath();
          ctx.arc(0, 0, 8, 0, Math.PI * 2);
          ctx.fill();
        }
        ctx.restore();
      }
    }

    // Ejected Part & Mitutoyo Metrology Laser Beam during Stage 5 (p > 0.8)
    if (p > 0.8) {
      const ejectT = (p - 0.8) / 0.2;
      const partX = 350 - ejectT * 50;
      const partY = 180 + ejectT * 40;

      // Finished Precision Involute Gear Falling toward Conveyor
      ctx.save();
      ctx.translate(partX, partY);
      ctx.rotate(ejectT * Math.PI * 1.5);
      ctx.fillStyle = "#f8fafc";
      ctx.strokeStyle = "#00e5ff";
      ctx.lineWidth = 2;
      ctx.beginPath();
      ctx.arc(0, 0, 24, 0, Math.PI * 2);
      ctx.fill();
      ctx.stroke();

      // Gear teeth
      for (let g = 0; g < 8; g++) {
        ctx.rotate(Math.PI / 4);
        ctx.fillRect(-3, -28, 6, 6);
      }

      ctx.fillStyle = "#090d16";
      ctx.beginPath();
      ctx.arc(0, 0, 7, 0, Math.PI * 2);
      ctx.fill();
      ctx.restore();

      // Laser Metrology QA Line
      ctx.strokeStyle = "rgba(0, 229, 255, 0.8)";
      ctx.lineWidth = 1.5;
      ctx.beginPath();
      ctx.moveTo(partX, 40);
      ctx.lineTo(partX, 300);
      ctx.stroke();

      ctx.fillStyle = "#00e5ff";
      ctx.font = "11px 'JetBrains Mono', monospace";
      ctx.fillText("MITUTOYO SCAN: Ø 120.00mm [PASS]", partX - 70, 35);
    }

    // Technical Overlay Badges
    ctx.fillStyle = "#94a3b8";
    ctx.font = "10px 'JetBrains Mono', monospace";
    ctx.fillText("AAITIAN 200T AUTOMATIC // DIE BAR 510x510", 90, 315);
    ctx.fillText("PID CONTROLLED NOZZLE // 300°C PRE-HEATER", 510, 315);
  }

  // Smooth Interpolation Loop
  function updateLoop() {
    currentProgress += (targetProgress - currentProgress) * 0.12;
    drawMouldingCycle(currentProgress);

    // Update Telemetry Indicators
    const stageIdx = Math.min(4, Math.floor(currentProgress * 5));
    const stage = STAGES[stageIdx];

    hudStageName.textContent = stage.name;
    hudClamp.textContent = stage.clamp;
    hudPressure.textContent = stage.pressure;
    hudTemp.textContent = stage.temp;
    hudCycle.textContent = stage.cycle;

    progressBar.style.width = `${Math.max(5, currentProgress * 100)}%`;

    // Highlight Active Navigation Pill
    seqPills.forEach((pill, idx) => {
      pill.classList.toggle('active', idx === stageIdx);
    });

    scrollSteps.forEach((step, idx) => {
      step.classList.toggle('active', idx === stageIdx);
    });

    animFrameId = requestAnimationFrame(updateLoop);
  }

  // Scroll Event Listener
  function onScroll() {
    if (!sequenceWrapper) return;
    const rect = sequenceWrapper.getBoundingClientRect();
    const windowH = window.innerHeight;

    // Relative scroll inside wrapper
    const totalDist = rect.height - windowH;
    const scrolled = -rect.top;

    if (totalDist > 0) {
      const progress = Math.max(0, Math.min(1, scrolled / totalDist));
      targetProgress = progress;
    }
  }

  window.addEventListener('scroll', onScroll, { passive: true });
  animFrameId = requestAnimationFrame(updateLoop);

  // Click on stage pills jumps to stage
  seqPills.forEach((pill, idx) => {
    pill.addEventListener('click', () => {
      targetProgress = idx * 0.22 + 0.05;
      const stepEl = scrollSteps[idx];
      if (stepEl) {
        stepEl.scrollIntoView({ behavior: 'smooth', block: 'center' });
      }
    });
  });

  // =========================================================================
  // 2. PRODUCT LIST SECTION: FILTERING & SEARCH
  // =========================================================================
  const productFilterBtns = document.querySelectorAll('.prod-filter-btn');
  const productCards = document.querySelectorAll('.product-card');
  const productSearchInput = document.getElementById('productSearchInput');

  function filterProducts() {
    const activeCatBtn = document.querySelector('.prod-filter-btn.active');
    const cat = activeCatBtn ? activeCatBtn.getAttribute('data-cat') : 'all';
    const query = productSearchInput ? productSearchInput.value.toLowerCase().trim() : '';

    productCards.forEach(card => {
      const cardCat = card.getAttribute('data-cat');
      const textContent = card.textContent.toLowerCase();

      const matchesCat = (cat === 'all' || cardCat === cat);
      const matchesSearch = (!query || textContent.includes(query));

      if (matchesCat && matchesSearch) {
        card.style.display = 'flex';
      } else {
        card.style.display = 'none';
      }
    });
  }

  productFilterBtns.forEach(btn => {
    btn.addEventListener('click', () => {
      productFilterBtns.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');
      filterProducts();
    });
  });

  if (productSearchInput) {
    productSearchInput.addEventListener('input', filterProducts);
  }

  // Pre-select Material & Part from Product Card
  window.preselectMaterial = function(matName, partName) {
    const matSelect = document.getElementById('rfqMaterial');
    const partInput = document.getElementById('rfqPartName');
    
    if (matSelect) {
      for (let i = 0; i < matSelect.options.length; i++) {
        if (matSelect.options[i].value.includes(matName) || matName.includes(matSelect.options[i].value)) {
          matSelect.selectedIndex = i;
          break;
        }
      }
    }

    if (partInput && partName) {
      partInput.value = partName;
    }
  };

  // =========================================================================
  // 3. POLYMER SCIENCE & MATERIALS MATRIX
  // =========================================================================
  const MATERIALS_DATA = {
    delrin: {
      code: "POLYMER ID: POM-01 // HOMOPOLYMER / COPOLYMER",
      name: "Delrin (Polyoxymethylene / Acetal)",
      tag: "ENGINEERING GRADE // PRECISION GEARS",
      desc: "Delrin is renowned for high mechanical strength, dimensional stability, low coefficient of friction, and superb fatigue endurance. Widely utilized as metal replacements in precision gear systems, cams, and bearings.",
      tensile: "70 - 85 MPa",
      temp: "105°C Continuous (120°C Peak)",
      wear: "Extremely Low (Self-Lubricating)",
      water: "< 0.2% (Rigid Dimensional Lock)",
      apps: [
        "Precision Spur & Helical Gears",
        "Self-Lubricating Bushings",
        "Switchgear Actuators",
        "Conveyor Wear Guides",
        "Precision Cams & Rollers"
      ]
    },

    nylon6gf: {
      code: "POLYMER ID: PA6-GF30 // 30% GLASS REINFORCED",
      name: "Nylon 6 GF30% (Polyamide Glass Filled)",
      tag: "STRUCTURAL GRADE // HIGH STIFFNESS",
      desc: "Reinforced with 30% electrical-grade glass fibers, providing exceptional tensile strength, elevated heat distortion temperature, and minimal creep under sustained mechanical load.",
      tensile: "165 - 180 MPa",
      temp: "140°C Continuous (180°C Peak)",
      wear: "High Abrasion Resistance",
      water: "1.2% (Stabilized with Annealing)",
      apps: [
        "High-Torque Gear Housings",
        "Motor End Shields",
        "Industrial Pump Impellers",
        "Heavy-Duty Switchgear Enclosures",
        "Automotive Engine Bracketry"
      ]
    },

    nylon6: {
      code: "POLYMER ID: PA6-UNFILLED // GENERAL POLYAMIDE",
      name: "Nylon 6 (Pure Polyamide)",
      tag: "MECHANICAL GRADE // WEAR & TOUGHNESS",
      desc: "Offers excellent toughness, high dynamic damping capacity, and shock resistance. Ideal for components subject to recurring shock loads and cyclic vibrations.",
      tensile: "75 - 85 MPa",
      temp: "90°C Continuous",
      wear: "Very Low Wear Against Steel",
      water: "2.5% (High Impact Plasticization)",
      apps: [
        "Shock-Absorbing Washers",
        "Sleeve Bearings",
        "Cable Ties & Clamps",
        "Slide Pulleys",
        "Industrial Bushings"
      ]
    },

    pc: {
      code: "POLYMER ID: PC-01 // OPTICAL & THERMAL POLYCARBONATE",
      name: "Polycarbonate (PC)",
      tag: "OPTICAL & IMPACT PROOF",
      desc: "An amorphous thermoplastic featuring virtually unbreakable impact resistance, optical clarity, excellent thermal endurance, and UL94 V-0 flame-retardant capability.",
      tensile: "65 - 75 MPa",
      temp: "125°C Continuous (135°C HDT)",
      wear: "Medium (Requires Polishing)",
      water: "< 0.15% (Strict Water Barrier)",
      apps: [
        "Transparent Dial Meters",
        "Electrical Meter Boxes",
        "High-Impact Lens Covers",
        "High-Voltage Terminal Shields",
        "Shatterproof Enclosures"
      ]
    },

    abs: {
      code: "POLYMER ID: ABS-02 // TERPOLYMER",
      name: "Acrylonitrile Butadiene Styrene (ABS)",
      tag: "DIMENSIONAL STABILITY & DIELECTRIC",
      desc: "Combines the structural rigidity of acrylonitrile, the impact tenacity of butadiene, and the smooth gloss aesthetics of styrene. Superb machinability and dielectric resistance.",
      tensile: "40 - 50 MPa",
      temp: "85°C Continuous",
      wear: "Good Scratch & Mar Resistance",
      water: "< 0.3% (Stable Dielectrics)",
      apps: [
        "Electrical Switch Covers",
        "Control Panel Bezels",
        "Electronics Housings",
        "Appliance Casings",
        "Display Frames"
      ]
    },

    pps: {
      code: "POLYMER ID: PPS-GF40 // POLYPHENYLENE SULFIDE",
      name: "Polyphenylene Sulfide (PPS)",
      tag: "ULTRA HIGH TEMP (220°C+) & CHEMICAL",
      desc: "High-performance semicrystalline engineering polymer designed for extreme environments. Insoluble in all known industrial solvents below 200°C with continuous service above 200°C.",
      tensile: "185 - 200 MPa",
      temp: "220°C Continuous (260°C Short-term)",
      wear: "Extreme Chemical & Wear Resistance",
      water: "< 0.02% (Virtually Impervious)",
      apps: [
        "High-Heat Transformer Bobbins",
        "Chemical Valve Bodies",
        "High-Voltage Arc Chutes",
        "Precision Sensor Housings",
        "Automotive Exhaust Sensors"
      ]
    },

    pu: {
      code: "POLYMER ID: TPU-85A / 95A // THERMOPLASTIC URETHANE",
      name: "Polyurethane (PU / TPU)",
      tag: "ELASTOMERIC LOAD & SHOCK",
      desc: "Bridge between flexible rubber and rigid plastics. Exhibits incredible abrasion resistance, superior tear strength, oil resistance, and low-temperature flexibility.",
      tensile: "45 - 60 MPa",
      temp: "80°C Continuous",
      wear: "Highest Wear Resistance Among Polymers",
      water: "< 0.5%",
      apps: [
        "Vibration Isolator Mounts",
        "Flexible Coupling Spiders",
        "Heavy-Duty Roller Liners",
        "Pneumatic O-Ring Seals",
        "Protective Bumper Caps"
      ]
    },

    pp: {
      code: "POLYMER ID: PP-HOMO // ISOTACTIC POLYPROPYLENE",
      name: "Polypropylene (PP)",
      tag: "FATIGUE PROOF & CHEMICAL BARRIER",
      desc: "Exceptional fatigue resistance for integral living hinges, low density (lightweighting), and virtually 100% resistance to acid, base, and salt solutions.",
      tensile: "30 - 40 MPa",
      temp: "100°C Continuous",
      wear: "Low Friction Surface",
      water: "< 0.01% (Zero Moisture Uptake)",
      apps: [
        "Integral Living Hinge Enclosures",
        "Chemical Tank Caps & Bungs",
        "Electrical Wiring Conduits",
        "Lightweight Mechanical Plugs",
        "Battery Casings"
      ]
    },

    hdpe: {
      code: "POLYMER ID: PE-HD // HIGH DENSITY POLYETHYLENE",
      name: "High Density & Low Density Polyethylene (HDPE/LDPE)",
      tag: "HIGH SLIP & CORROSION BARRIER",
      desc: "High impact strength down to -40°C, zero water absorption, and self-lubricating surface characteristics. Highly economical for wear plates and chemical guides.",
      tensile: "25 - 35 MPa",
      temp: "80°C Continuous (-40°C Low Temp)",
      wear: "Smooth Sliding Surface",
      water: "< 0.01%",
      apps: [
        "Conveyor Guide Rails",
        "Wear Strips & Slide Pads",
        "Chemical Pipe Flanges",
        "Protective End Ferrules",
        "Impact Dampers"
      ]
    }
  };

  const tabButtons = document.querySelectorAll('.material-nav-btn');
  const matDetailCode = document.getElementById('matDetailCode');
  const matDetailName = document.getElementById('matDetailName');
  const matDetailTag = document.getElementById('matDetailTag');
  const matDetailDesc = document.getElementById('matDetailDesc');
  const matPropTensile = document.getElementById('matPropTensile');
  const matPropTemp = document.getElementById('matPropTemp');
  const matPropWear = document.getElementById('matPropWear');
  const matPropWater = document.getElementById('matPropWater');
  const matDetailApps = document.getElementById('matDetailApps');

  tabButtons.forEach(btn => {
    btn.addEventListener('click', () => {
      const matKey = btn.getAttribute('data-mat');
      if (!MATERIALS_DATA[matKey]) return;

      tabButtons.forEach(b => b.classList.remove('active'));
      btn.classList.add('active');

      const data = MATERIALS_DATA[matKey];

      matDetailCode.textContent = data.code;
      matDetailName.textContent = data.name;
      matDetailTag.textContent = data.tag;
      matDetailDesc.textContent = data.desc;
      matPropTensile.textContent = data.tensile;
      matPropTemp.textContent = data.temp;
      matPropWear.textContent = data.wear;
      matPropWater.textContent = data.water;

      matDetailApps.innerHTML = data.apps.map(app => `
        <span class="app-pill">${app}</span>
      `).join('');
    });
  });

  // =========================================================================
  // 4. TECHNICAL RFQ FORM SUBMISSION & WHATSAPP SYNC
  // =========================================================================
  window.submitRFQ = function() {
    const partName = document.getElementById('rfqPartName').value;
    const material = document.getElementById('rfqMaterial').value;
    const qty = document.getElementById('rfqQuantity').value;
    const tooling = document.getElementById('rfqToolingStatus').value;
    const contact = document.getElementById('rfqContactName').value;
    const phone = document.getElementById('rfqPhone').value;
    const notes = document.getElementById('rfqNotes').value || 'None';

    const successMsg = document.getElementById('rfqSuccessMsg');
    successMsg.style.display = 'block';

    const waText = encodeURIComponent(
      `*Technical RFQ Inquiry - Negizhi Industries*\n` +
      `--------------------------------\n` +
      `*Part Name:* ${partName}\n` +
      `*Material:* ${material}\n` +
      `*Batch Quantity:* ${qty}\n` +
      `*Tooling:* ${tooling}\n` +
      `*Client:* ${contact} (${phone})\n` +
      `*Notes:* ${notes}\n` +
      `--------------------------------\n` +
      `Submitted via official website`
    );

    setTimeout(() => {
      window.open(`https://wa.me/918610888097?text=${waText}`, '_blank');
    }, 600);
  };

  // =========================================================================
  // 5. HEADER SCROLL & NAVIGATION OBSERVER
  // =========================================================================
  const header = document.getElementById('headerNav');
  const navLinks = document.querySelectorAll('.geo-nav-link');
  const sections = document.querySelectorAll('section[id]');

  window.addEventListener('scroll', () => {
    if (window.scrollY > 40) {
      header.style.boxShadow = '0 10px 30px rgba(0, 0, 0, 0.8)';
      header.style.borderBottomColor = 'rgba(0, 229, 255, 0.3)';
    } else {
      header.style.boxShadow = 'none';
      header.style.borderBottomColor = 'rgba(255, 255, 255, 0.08)';
    }

    // Update active nav link
    let current = '';
    sections.forEach(sec => {
      const secTop = sec.offsetTop - 120;
      if (window.scrollY >= secTop) {
        current = sec.getAttribute('id');
      }
    });

    navLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${current}`) {
        link.classList.add('active');
      }
    });
  });

});
