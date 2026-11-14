<?php
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
