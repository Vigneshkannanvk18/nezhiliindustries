with open('js/app.js', 'r', encoding='utf-8') as f:
    code = f.read()

target_start = '  const MATERIALS_DATA = {'
target_end = '  const tabButtons = document.querySelectorAll(\'.material-nav-btn\');'

p1 = code.find(target_start)
p2 = code.find(target_end)

assert p1 != -1 and p2 != -1, 'Could not find MATERIALS_DATA markers in js/app.js'

new_materials_data = '''  const MATERIALS_DATA = {
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

    nylon66: {
      code: "POLYMER ID: PA66-UNFILLED // HIGH-HEAT POLYAMIDE",
      name: "Nylon 66 Unfilled (Pure Polyamide 66)",
      tag: "HIGH THERMAL & ABRASION RESISTANCE",
      desc: "Nylon 66 features elevated crystallinity, a high 260°C crystalline melting point, superior creep resistance, and higher mechanical stiffness compared to standard Nylon 6. Exceptional for sliding friction parts and heat-exposed mechanical assemblies.",
      tensile: "80 - 95 MPa",
      temp: "115°C Continuous (200°C Short-term)",
      wear: "Extremely Low Friction Coefficient",
      water: "1.5% - 2.0% (Lower Moisture than PA6)",
      apps: [
        "High-Speed Cams & Pulleys",
        "Thermal Insulating Spacers",
        "Appliance Gears & Ratchets",
        "Textile Machinery Guides",
        "Precision Snap-Fit Connectors"
      ]
    },

    nylon66gf50: {
      code: "POLYMER ID: PA66-GF50 // 50% GLASS REINFORCED",
      name: "Nylon 66 GF 50% (50% Glass-Filled Polyamide)",
      tag: "ULTRA-HIGH RIGIDITY // METAL REPLACEMENT",
      desc: "Heavily reinforced with 50% high-modulus glass fibers, delivering extraordinary tensile modulus, zero creep under massive structural loads, and high heat deflection. Directly replaces aluminum and zinc die-cast parts with 50% weight reduction.",
      tensile: "210 - 245 MPa (Extreme Structural Load)",
      temp: "160°C Continuous (235°C HDT)",
      wear: "Extreme Surface Hardness & Fatigue Endurance",
      water: "0.8% (Extreme Dimensional Stability)",
      apps: [
        "Heavy Structural Machine Braces",
        "Die-Cast Aluminum Replacement Flanges",
        "High-Pressure Pump Manifolds",
        "Automotive Engine Compartment Brackets",
        "Heavy Industrial Toggle Levers"
      ]
    },

    noryl: {
      code: "POLYMER ID: PPE-NORYL // MODIFIED POLYPHENYLENE ETHER",
      name: "Noryl (Modified Polyphenylene Ether / PPE+PS)",
      tag: "HYDROLYTIC STABILITY & ULTRA-LOW WATER ABSORPTION",
      desc: "Noryl blends polyphenylene ether with polystyrene to provide exceptional hydrolytic stability (zero degradation in hot water or steam), continuous dielectric insulation, and virtually zero moisture absorption. Ideal for precision water pumps, switchgear, and terminal blocks.",
      tensile: "55 - 75 MPa",
      temp: "110°C Continuous (130°C HDT)",
      wear: "Smooth Dimensional Wear Resistance",
      water: "< 0.06% (Immune to Moisture Expansion)",
      apps: [
        "Submersible Pump Impellers & Diffusers",
        "Electrical Switchgear Breaker Housings",
        "Water Meter Bodies & Fluidic Sensors",
        "Telecommunication Terminal Blocks",
        "Solar Junction & Inverter Enclosures"
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

    polystyrene: {
      code: "POLYMER ID: PS-HIPS // HIGH IMPACT POLYSTYRENE",
      name: "Polystyrene (HIPS / GPPS Engineering Grades)",
      tag: "DIMENSIONAL ACCURACY & DIELECTRICS",
      desc: "High Impact Polystyrene (HIPS) incorporates polybutadiene rubber for elevated impact toughness, rigid wall stability, and excellent electrical dielectric strength. High dimensional accuracy with fast cycle times and superb mold detail replication.",
      tensile: "35 - 45 MPa",
      temp: "75°C Continuous (85°C HDT)",
      wear: "Moderate Wear (Rigid Surface)",
      water: "< 0.10% (Excellent Moisture Seal)",
      apps: [
        "Instrument Display Bezels & Dial Panels",
        "Electronic Sub-Enclosures & Cassettes",
        "Refrigeration & Appliance Components",
        "Disposable Technical Spools & Bobbins",
        "Lightweight Protective Packaging Shrouds"
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

    tpe: {
      code: "POLYMER ID: TPE-FLEX // THERMOPLASTIC ELASTOMER",
      name: "Thermoplastic Elastomer (TPE)",
      tag: "FLEXIBLE SEALING & DUAL-SHOT OVERMOULDING",
      desc: "Combines the elastic flexibility and sealing resilience of vulcanized rubber with the high-precision processing speed of thermoplastics. Delivers exceptional tactile soft-touch feel, weatherability, chemical resistance, and strong chemical bonding in 2K multi-material overmoulding.",
      tensile: "12 - 25 MPa (High Elongation > 500%)",
      temp: "80°C Continuous (Shore 40A to 90A)",
      wear: "High Tear Strength & Surface Grip",
      water: "< 0.20% (Weatherproof Barrier)",
      apps: [
        "Conformal Fluidic Gaskets & O-Ring Seals",
        "Ergonomic Tool Handles & Grips",
        "Flexible Cable Strain Relief Boots",
        "Dust Caps & Vibration Bumper Dampers",
        "Dual-Material Soft-Touch Enclosures"
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

  '''

updated_code = code[:p1] + new_materials_data + code[p2:]
with open('js/app.js', 'w', encoding='utf-8') as f:
    f.write(updated_code)

print('Updated js/app.js with 14 materials successfully!')

