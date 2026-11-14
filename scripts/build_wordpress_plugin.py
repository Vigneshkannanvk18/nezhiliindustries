import os
import shutil
import re
import zipfile

PLUGIN_SLUG = "negizhi-industries-landing"
PLUGIN_DIR = os.path.join(".", PLUGIN_SLUG)

print(f"Creating WordPress plugin package in: {PLUGIN_DIR}")

# 1. Clean & recreate plugin directory structure
if os.path.exists(PLUGIN_DIR):
    shutil.rmtree(PLUGIN_DIR)

os.makedirs(os.path.join(PLUGIN_DIR, "templates"), exist_ok=True)
os.makedirs(os.path.join(PLUGIN_DIR, "css"), exist_ok=True)
os.makedirs(os.path.join(PLUGIN_DIR, "js"), exist_ok=True)
os.makedirs(os.path.join(PLUGIN_DIR, "assets", "extracted"), exist_ok=True)
os.makedirs(os.path.join(PLUGIN_DIR, "assets", "products"), exist_ok=True)

# 2. Copy production assets
shutil.copy2("assets/logo-horizontal-clean.png", os.path.join(PLUGIN_DIR, "assets", "logo-horizontal-clean.png"))
shutil.copy2("assets/logo.png", os.path.join(PLUGIN_DIR, "assets", "logo.png"))
shutil.copy2("NEGIZHII.pdf", os.path.join(PLUGIN_DIR, "NEGIZHII.pdf"))

for f in os.listdir("assets/extracted"):
    src_f = os.path.join("assets/extracted", f)
    if os.path.isfile(src_f):
        shutil.copy2(src_f, os.path.join(PLUGIN_DIR, "assets", "extracted", f))

for f in os.listdir("assets/products"):
    src_f = os.path.join("assets/products", f)
    if os.path.isfile(src_f):
        shutil.copy2(src_f, os.path.join(PLUGIN_DIR, "assets", "products", f))

# 3. Process & copy CSS
with open("css/styles.css", "r", encoding="utf-8") as f:
    css_content = f.read()

# Append WordPress Admin Bar compatibility & Hello Elementor isolation rules
wp_css_additions = """

/* ==========================================================================
   WORDPRESS & ELEMENTOR COMPATIBILITY ENHANCEMENTS
   ========================================================================== */

/* Clean isolation from Hello Elementor theme defaults */
body.geometric-industrial-theme {
  margin: 0 !important;
  padding: 0 !important;
  background-color: #060a12 !important;
  color: #f8fafc !important;
  overflow-x: clip !important;
  width: 100% !important;
  max-width: 100% !important;
}

/* WordPress Admin Bar Sticky Header Offset */
body.admin-bar .geo-header {
  top: 32px !important;
}

@media screen and (max-width: 782px) {
  body.admin-bar .geo-header {
    top: 46px !important;
  }
  body.admin-bar .geo-mobile-drawer {
    top: 46px !important;
    height: calc(100vh - 46px) !important;
    height: calc(100dvh - 46px) !important;
  }
}

/* Ensure Elementor default wrapper does not constrain our standalone layout */
.negizhi-wp-wrapper {
  width: 100%;
  max-width: 100%;
  margin: 0;
  padding: 0;
}
"""

with open(os.path.join(PLUGIN_DIR, "css", "styles.css"), "w", encoding="utf-8") as f:
    f.write(css_content + wp_css_additions)

# 4. Copy JS
shutil.copy2("js/app.js", os.path.join(PLUGIN_DIR, "js", "app.js"))

# 5. Generate templates/page-negizhi-landing.php from index.html
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Replace asset URLs with PHP dynamic URLs
# assets/logo-horizontal-clean.png -> <?php echo esc_url(NEGIZHI_PLUGIN_URL . 'assets/logo-horizontal-clean.png'); ?>
def replace_asset_path(match):
    prefix = match.group(1) # src= or href= or srcset=
    quote = match.group(2)
    path = match.group(3)
    return f'{prefix}{quote}<?php echo esc_url(NEGIZHI_PLUGIN_URL . \'{path}\'); ?>{quote}'

php_content = re.sub(
    r'(src|href|srcset)=(["\'])(assets/[^"\']+|NEGIZHII\.pdf)(["\'])',
    replace_asset_path,
    html
)

# Extract content starting from ambient elements up to end of </body>
body_match = re.search(r'<body class="geometric-industrial-theme">([\s\S]*?)<script src="js/app\.js"></script>\s*</body>', php_content)
if not body_match:
    raise Exception("Could not match body content in index.html")

body_inner = body_match.group(1)

# Extract JSON-LD script from head
json_ld_match = re.search(r'(<script type="application/ld\+json">[\s\S]*?</script>)', html)
json_ld = json_ld_match.group(1) if json_ld_match else ""

template_php = f"""<?php
/**
 * Template Name: Negizhi Industries Landing Page
 * Description: Standalone High-Performance Geometric Industrial Landing Page for Negizhi Industries.
 * Fully compatible with Hello Elementor, Elementor Canvas, and modern WordPress page builders.
 */

if (!defined('ABSPATH')) {{
    exit; // Prevent direct access
}}
?>
<!DOCTYPE html>
<html <?php language_attributes(); ?> prefix="og: https://ogp.me/ns#">
<head>
    <meta charset="<?php bloginfo('charset'); ?>" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />

    <!-- Geographic Meta Tags for Local SEO in Coimbatore, Tamil Nadu, India -->
    <meta name="geo.region" content="IN-TN" />
    <meta name="geo.placename" content="Coimbatore, Tamil Nadu, India" />
    <meta name="geo.position" content="11.0168;77.1265" />
    <meta name="ICBM" content="11.0168, 77.1265" />

    {json_ld}

    <?php wp_head(); ?>
</head>
<body <?php body_class('geometric-industrial-theme negizhi-standalone-page'); ?>>
<?php wp_body_open(); ?>

<div class="negizhi-wp-wrapper">
{body_inner}
</div>

<?php wp_footer(); ?>
</body>
</html>
"""

with open(os.path.join(PLUGIN_DIR, "templates", "page-negizhi-landing.php"), "w", encoding="utf-8") as f:
    f.write(template_php)

# 6. Generate main plugin file: negizhi-industries-landing.php
main_plugin_php = """<?php
/**
 * Plugin Name: Negizhi Industries Landing Page Template
 * Plugin URI: https://negizhiindustries.com/
 * Description: High-Performance Precision Engineering Plastic Components landing page template for Negizhi Industries. Adds a custom "Negizhi Industries Landing Page" page template selectable in the Page Attributes / Template dropdown on any WordPress page. Fully isolated and zero-conflict with Hello Elementor theme.
 * Version: 1.0.0
 * Author: Negizhi Industries
 * Author URI: https://negizhiindustries.com/
 * Text Domain: negizhi-industries-landing
 * Domain Path: /languages
 */

if (!defined('ABSPATH')) {
    exit; // Exit if accessed directly
}

define('NEGIZHI_VERSION', '1.0.0');
define('NEGIZHI_PLUGIN_DIR', plugin_dir_path(__FILE__));
define('NEGIZHI_PLUGIN_URL', plugin_dir_url(__FILE__));
define('NEGIZHI_TEMPLATE_SLUG', 'negizhi-landing-template.php');

class Negizhi_Industries_Plugin {

    private static $instance = null;

    public static function get_instance() {
        if (null === self::$instance) {
            self::$instance = new self();
        }
        return self::$instance;
    }

    private function __construct() {
        // Register Page Template in WordPress (Classic Editor, Gutenberg & Elementor)
        add_filter('theme_page_templates', array($this, 'register_page_template'), 20, 4);

        // Intercept template rendering when this template is selected
        add_filter('template_include', array($this, 'render_page_template'), 99);

        // Enqueue Assets only on the Negizhi Landing Page (zero conflict on other site pages)
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'), 99);

        // Optional shortcode for embedding or Elementor shortcode widget
        add_shortcode('negizhi_landing_page', array($this, 'render_shortcode'));

        // Elementor Canvas / Hello Elementor clean isolation
        add_action('elementor/page_templates/header', array($this, 'maybe_suppress_elementor_header'));
    }

    /**
     * Check if current page is using the Negizhi template
     */
    public function is_negizhi_page() {
        if (is_page()) {
            $current_template = get_post_meta(get_the_ID(), '_wp_page_template', true);
            return ($current_template === NEGIZHI_TEMPLATE_SLUG);
        }
        return false;
    }

    /**
     * Add our custom template to the Page Attributes / Template dropdown
     */
    public function register_page_template($post_templates, $wp_theme, $post, $post_type) {
        if ('page' === $post_type || empty($post_type)) {
            $post_templates[NEGIZHI_TEMPLATE_SLUG] = __('Negizhi Industries Landing Page', 'negizhi-industries-landing');
        }
        return $post_templates;
    }

    /**
     * Load our custom template when selected
     */
    public function render_page_template($template) {
        if ($this->is_negizhi_page()) {
            $plugin_template = NEGIZHI_PLUGIN_DIR . 'templates/page-negizhi-landing.php';
            if (file_exists($plugin_template)) {
                return $plugin_template;
            }
        }
        return $template;
    }

    /**
     * Enqueue Google Fonts, CSS, and JS only on Negizhi Landing Page
     */
    public function enqueue_assets() {
        if ($this->is_negizhi_page()) {
            // Google Fonts: Outfit, Plus Jakarta Sans, JetBrains Mono
            wp_enqueue_style(
                'negizhi-google-fonts',
                'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap',
                array(),
                null
            );

            // Scoped & High-Performance Stylesheet
            wp_enqueue_style(
                'negizhi-styles',
                NEGIZHI_PLUGIN_URL . 'css/styles.css',
                array(),
                NEGIZHI_VERSION
            );

            // Core Application Logic (Interactive Canvas, Matrix Explorer, Mobile Menu, RFQ)
            wp_enqueue_script(
                'negizhi-app',
                NEGIZHI_PLUGIN_URL . 'js/app.js',
                array(),
                NEGIZHI_VERSION,
                true // Enqueue in footer for non-blocking rendering
            );

            // Dequeue conflicting Hello Elementor theme styles if present
            wp_dequeue_style('hello-elementor-header-footer');
            wp_dequeue_style('hello-elementor-theme-style');
        }
    }

    /**
     * Suppress default Elementor header/footer injection on our standalone template
     */
    public function maybe_suppress_elementor_header() {
        if ($this->is_negizhi_page()) {
            // Standalone page maintains its own self-contained header and footer
            remove_action('wp_body_open', 'elementor_theme_do_location_header');
        }
    }

    /**
     * Shortcode support: [negizhi_landing_page]
     */
    public function render_shortcode($atts) {
        // Enqueue assets for shortcode usage
        wp_enqueue_style('negizhi-google-fonts', 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap', array(), null);
        wp_enqueue_style('negizhi-styles', NEGIZHI_PLUGIN_URL . 'css/styles.css', array(), NEGIZHI_VERSION);
        wp_enqueue_script('negizhi-app', NEGIZHI_PLUGIN_URL . 'js/app.js', array(), NEGIZHI_VERSION, true);

        ob_start();
        $template_path = NEGIZHI_PLUGIN_DIR . 'templates/page-negizhi-landing.php';
        if (file_exists($template_path)) {
            include $template_path;
        }
        return ob_get_clean();
    }
}

// Initialize Plugin
add_action('plugins_loaded', array('Negizhi_Industries_Plugin', 'get_instance'));
"""

with open(os.path.join(PLUGIN_DIR, "negizhi-industries-landing.php"), "w", encoding="utf-8") as f:
    f.write(main_plugin_php)

# 7. Generate readme.txt for WordPress documentation
readme_txt = """=== Negizhi Industries Landing Page Template ===
Contributors: Negizhi Industries
Tags: elementor, page template, manufacturing, engineering plastics, injection moulding
Requires at least: 5.4
Tested up to: 6.7
Requires PHP: 7.4
Stable tag: 1.0.0
License: Proprietary
License URI: https://negizhiindustries.com/

High-Performance Precision Engineering Plastic Components landing page template for Negizhi Industries. Fully compatible with Hello Elementor theme.

== Description ==

This plugin provides a dedicated standalone Page Template titled "Negizhi Industries Landing Page".
When selected under the Page Attributes / Template dropdown on any WordPress page, it renders the complete, dark geometric industrial website for Negizhi Industries.

Key Features:
- 100% Zero Conflict with Hello Elementor theme and Elementor Pro.
- Dedicated Page Template: Simply select "Negizhi Industries Landing Page" on any page and publish.
- Real Component Images: All 10 engineering plastic products with WebP / JPG high-resolution photos.
- Interactive 200-Ton Moulding Cycle Canvas Simulation (Stage 1 to 5).
- Interactive Polymer Matrix Explorer with technical specifications.
- Mobile & Tablet Responsive Navigation Drawer with instant touch response.
- Technical RFQ quote modal & WhatsApp direct integration.
- WordPress Admin Bar aware: Sticky header automatically adjusts when logged in as admin.

== Installation ==

1. In your WordPress Admin Dashboard, navigate to: Plugins -> Add New -> Upload Plugin.
2. Choose the `negizhi-industries-landing.zip` file and click "Install Now".
3. Click "Activate Plugin".
4. Create or edit a page in WordPress (e.g. "Home" or "Engineering Plastics"):
   - If using the Block Editor (Gutenberg): In the right sidebar under "Summary" -> "Template", select **Negizhi Industries Landing Page**.
   - If using the Classic Editor: In the right sidebar under "Page Attributes" -> "Template", select **Negizhi Industries Landing Page**.
   - If editing with Elementor: Click the Settings gear icon (bottom-left) -> Page Layout -> select **Negizhi Industries Landing Page**.
5. Click **Publish** or **Update**.
6. View your page! It will render the complete, high-performance landing page.

== Frequently Asked Questions ==

= Does this conflict with Hello Elementor's header or footer? =
No. The template is an independent standalone canvas that does not call Hello Elementor's theme header/footer. It renders cleanly without theme interference.

= Are assets loaded on other pages of my website? =
No. All CSS and JS are conditionally enqueued ONLY on the page where the Negizhi Industries template is selected, keeping the rest of your WordPress site fast and lean.

== Changelog ==

= 1.0.0 =
* Initial production release.
"""

with open(os.path.join(PLUGIN_DIR, "readme.txt"), "w", encoding="utf-8") as f:
    f.write(readme_txt)

# 8. Create installable ZIP archive: negizhi-industries-landing.zip
zip_filename = f"{PLUGIN_SLUG}.zip"
print(f"Packaging plugin into: {zip_filename}...")

with zipfile.ZipFile(zip_filename, "w", zipfile.ZIP_DEFLATED) as zipf:
    for root, dirs, files in os.walk(PLUGIN_DIR):
        for file in files:
            file_path = os.path.join(root, file)
            # Store relative to parent of plugin dir so ZIP contains folder 'negizhi-industries-landing/...'
            arcname = os.path.relpath(file_path, ".")
            zipf.write(file_path, arcname)

zip_size_kb = os.path.getsize(zip_filename) / 1024
print(f"SUCCESS! Plugin ZIP created: {zip_filename} ({zip_size_kb:.1f} KB)")

