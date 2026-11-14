import zipfile, os, re

zip_path = "negizhi-industries-landing.zip"
print(f"Inspecting {zip_path}...")

with zipfile.ZipFile(zip_path, 'r') as z:
    file_list = z.namelist()
    print(f"Total entries in ZIP: {len(file_list)}")
    
    # Check that all files start with 'negizhi-industries-landing/'
    non_conforming = [f for f in file_list if not f.startswith("negizhi-industries-landing/")]
    if non_conforming:
        print("ERROR: Entries not in root folder:", non_conforming)
    else:
        print("PASS: 100% of files are in 'negizhi-industries-landing/' root folder.")

    # Check key files exist
    required_files = [
        "negizhi-industries-landing/negizhi-industries-landing.php",
        "negizhi-industries-landing/templates/page-negizhi-landing.php",
        "negizhi-industries-landing/css/styles.css",
        "negizhi-industries-landing/js/app.js",
        "negizhi-industries-landing/NEGIZHII.pdf",
        "negizhi-industries-landing/readme.txt",
        "negizhi-industries-landing/assets/logo-horizontal-clean.png",
        "negizhi-industries-landing/assets/extracted/highshine_machine_clean.jpg",
        "negizhi-industries-landing/assets/products/master-component-showcase.webp",
    ]
    for rf in required_files:
        if rf in file_list:
            print(f"  [FOUND] {rf}")
        else:
            print(f"  [MISSING!] {rf}")

# Check PHP syntax patterns in negizhi-industries-landing.php
with open("negizhi-industries-landing/negizhi-industries-landing.php", "r", encoding="utf-8") as f:
    main_php = f.read()

print("\nValidating negizhi-industries-landing.php:")
checks = [
    ("Plugin Name header", "Plugin Name: Negizhi Industries Landing Page Template" in main_php),
    ("theme_page_templates filter", "add_filter('theme_page_templates'" in main_php or 'add_filter("theme_page_templates"' in main_php),
    ("template_include filter", "add_filter('template_include'" in main_php or 'add_filter("template_include"' in main_php),
    ("wp_enqueue_scripts action", "add_action('wp_enqueue_scripts'" in main_php or 'add_action("wp_enqueue_scripts"' in main_php),
    ("Shortcode registration", "add_shortcode('negizhi_landing_page'" in main_php),
    ("Hello Elementor dequeue", "wp_dequeue_style('hello-elementor-header-footer')" in main_php),
]
for name, passed in checks:
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

# Check templates/page-negizhi-landing.php
with open("negizhi-industries-landing/templates/page-negizhi-landing.php", "r", encoding="utf-8") as f:
    tmpl_php = f.read()

print("\nValidating templates/page-negizhi-landing.php:")
tmpl_checks = [
    ("Template Name header", "Template Name: Negizhi Industries Landing Page" in tmpl_php),
    ("wp_head() call", "wp_head();" in tmpl_php),
    ("wp_footer() call", "wp_footer();" in tmpl_php),
    ("wp_body_open() call", "wp_body_open();" in tmpl_php),
    ("body_class() call", "body_class(" in tmpl_php),
    ("Dynamic NEGIZHI_PLUGIN_URL logo", "NEGIZHI_PLUGIN_URL . 'assets/logo-horizontal-clean.png'" in tmpl_php),
    ("Dynamic NEGIZHI_PLUGIN_URL brochure", "NEGIZHI_PLUGIN_URL . 'NEGIZHII.pdf'" in tmpl_php),
    ("Zero hardcoded src=\"assets/", 'src="assets/' not in tmpl_php and "src='assets/" not in tmpl_php),
    ("Zero hardcoded srcset=\"assets/", 'srcset="assets/' not in tmpl_php and "srcset='assets/" not in tmpl_php),
]
for name, passed in tmpl_checks:
    print(f"  [{'PASS' if passed else 'FAIL'}] {name}")

