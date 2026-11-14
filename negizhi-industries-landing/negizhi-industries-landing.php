<?php
/**
 * Plugin Name: Negizhi Industries Landing Page & RFQ Lead System
 * Plugin URI: https://negizhiindustries.com/
 * Description: High-Performance Precision Plastic Engineering Landing Page template for Negizhi Industries. Includes Hostinger SMTP integration (contact@negizhiindustries.com), automated email alerts to vigneshkannan52@gmail.com, and an interactive WordPress Admin Leads Table with CSV Export.
 * Version: 1.2.0
 * Author: Negizhi Industries
 * Author URI: https://negizhiindustries.com/
 * Text Domain: negizhi-industries-landing
 */

if (!defined('ABSPATH')) {
    exit;
}

define('NEGIZHI_VERSION', '1.2.0');
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
        // Database table setup - activation hook and admin_init auto-check
        register_activation_hook(__FILE__, array($this, 'ensure_table_exists'));
        add_action('admin_init', array($this, 'ensure_table_exists'));

        // Register Page Template
        add_filter('theme_page_templates', array($this, 'register_page_template'), 20, 4);
        add_filter('template_include', array($this, 'render_page_template'), 99);

        // Enqueue Assets
        add_action('wp_enqueue_scripts', array($this, 'enqueue_assets'), 99);

        // Hostinger SMTP Integration via PHPMailer
        add_action('phpmailer_init', array($this, 'configure_hostinger_smtp'));

        // AJAX Form Submission Handlers
        add_action('wp_ajax_negizhi_submit_rfq', array($this, 'handle_rfq_submission'));
        add_action('wp_ajax_nopriv_negizhi_submit_rfq', array($this, 'handle_rfq_submission'));

        // Admin Menus & Settings
        add_action('admin_menu', array($this, 'register_admin_menus'));
        add_action('admin_init', array($this, 'handle_admin_actions'));
        add_action('admin_post_negizhi_export_leads_csv', array($this, 'export_leads_csv'));

        // Shortcode support
        add_shortcode('negizhi_landing_page', array($this, 'render_shortcode'));

        // Hello Elementor theme isolation
        add_action('elementor/page_templates/header', array($this, 'maybe_suppress_elementor_header'));
    }

    /**
     * Ensure the RFQ leads database table exists (self-healing, zero dbDelta dependency)
     */
    public function ensure_table_exists() {
        global $wpdb;
        $table_name = $wpdb->prefix . 'negizhi_rfq_leads';
        $charset_collate = $wpdb->get_charset_collate();

        $sql = "CREATE TABLE IF NOT EXISTS `$table_name` (
            `id` bigint(20) unsigned NOT NULL AUTO_INCREMENT,
            `created_at` datetime NOT NULL,
            `client_name` varchar(255) NOT NULL DEFAULT '',
            `company_name` varchar(255) NOT NULL DEFAULT '',
            `email` varchar(255) NOT NULL DEFAULT '',
            `phone` varchar(50) NOT NULL DEFAULT '',
            `part_name` varchar(255) NOT NULL DEFAULT '',
            `material` varchar(255) NOT NULL DEFAULT '',
            `quantity` varchar(100) NOT NULL DEFAULT '',
            `tooling_status` varchar(255) NOT NULL DEFAULT '',
            `notes` text,
            `ip_address` varchar(100) NOT NULL DEFAULT '',
            `status` varchar(50) NOT NULL DEFAULT 'New',
            PRIMARY KEY (`id`),
            KEY `created_at` (`created_at`),
            KEY `email` (`email`)
        ) $charset_collate;";

        $wpdb->query($sql);
        update_option('negizhi_db_version', NEGIZHI_VERSION);

        // Seed default options if not set
        if (false === get_option('negizhi_smtp_host')) update_option('negizhi_smtp_host', 'smtp.hostinger.com');
        if (false === get_option('negizhi_smtp_port')) update_option('negizhi_smtp_port', '465');
        if (false === get_option('negizhi_smtp_secure')) update_option('negizhi_smtp_secure', 'ssl');
        if (false === get_option('negizhi_smtp_user')) update_option('negizhi_smtp_user', 'contact@negizhiindustries.com');
        if (false === get_option('negizhi_smtp_from_name')) update_option('negizhi_smtp_from_name', 'Negizhi Industries Website');
        if (false === get_option('negizhi_notification_email')) update_option('negizhi_notification_email', 'vigneshkannan52@gmail.com');
        if (false === get_option('negizhi_smtp_enabled')) update_option('negizhi_smtp_enabled', '1');
    }

    /**
     * Check if current page uses the Negizhi template
     */
    public function is_negizhi_page() {
        if (is_page()) {
            $current_template = get_post_meta(get_the_ID(), '_wp_page_template', true);
            return ($current_template === NEGIZHI_TEMPLATE_SLUG);
        }
        return false;
    }

    /**
     * Register template in WordPress template dropdown
     */
    public function register_page_template($post_templates, $wp_theme, $post, $post_type) {
        if ('page' === $post_type || empty($post_type)) {
            $post_templates[NEGIZHI_TEMPLATE_SLUG] = __('Negizhi Industries Landing Page', 'negizhi-industries-landing');
        }
        return $post_templates;
    }

    /**
     * Render the custom page template
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
     * Enqueue Google Fonts, CSS, and JS with AJAX localization
     */
    public function enqueue_assets() {
        if ($this->is_negizhi_page()) {
            wp_enqueue_style(
                'negizhi-google-fonts',
                'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap',
                array(),
                null
            );

            wp_enqueue_style(
                'negizhi-styles',
                NEGIZHI_PLUGIN_URL . 'css/styles.css',
                array(),
                NEGIZHI_VERSION
            );

            wp_enqueue_script(
                'negizhi-app',
                NEGIZHI_PLUGIN_URL . 'js/app.js',
                array(),
                NEGIZHI_VERSION,
                true
            );

            // Localize AJAX URL and security nonce for the form
            wp_localize_script('negizhi-app', 'negizhi_ajax', array(
                'ajax_url' => admin_url('admin-ajax.php'),
                'nonce'    => wp_create_nonce('negizhi_rfq_nonce'),
            ));

            wp_dequeue_style('hello-elementor-header-footer');
            wp_dequeue_style('hello-elementor-theme-style');
        }
    }

    public function maybe_suppress_elementor_header() {
        if ($this->is_negizhi_page()) {
            remove_action('wp_body_open', 'elementor_theme_do_location_header');
        }
    }

    /**
     * Hostinger SMTP configuration hook for PHPMailer
     */
    public function configure_hostinger_smtp($phpmailer) {
        $smtp_enabled = get_option('negizhi_smtp_enabled', '1');
        $smtp_pass = get_option('negizhi_smtp_pass', '');

        if ('1' === $smtp_enabled && !empty($smtp_pass)) {
            $phpmailer->isSMTP();
            $phpmailer->Host       = get_option('negizhi_smtp_host', 'smtp.hostinger.com');
            $phpmailer->SMTPAuth   = true;
            $phpmailer->Port       = intval(get_option('negizhi_smtp_port', '465'));
            $phpmailer->Username   = get_option('negizhi_smtp_user', 'contact@negizhiindustries.com');
            $phpmailer->Password   = $smtp_pass;
            $phpmailer->SMTPSecure = get_option('negizhi_smtp_secure', 'ssl');
            $phpmailer->From       = get_option('negizhi_smtp_user', 'contact@negizhiindustries.com');
            $phpmailer->FromName   = get_option('negizhi_smtp_from_name', 'Negizhi Industries Website');
        }
    }

    /**
     * AJAX Handler: Process incoming RFQ submissions
     */
    public function handle_rfq_submission() {
        check_ajax_referer('negizhi_rfq_nonce', 'security');

        $this->ensure_table_exists();

        global $wpdb;
        $table_name = $wpdb->prefix . 'negizhi_rfq_leads';

        $part_name      = isset($_POST['part_name']) ? sanitize_text_field($_POST['part_name']) : '';
        $material       = isset($_POST['material']) ? sanitize_text_field($_POST['material']) : '';
        $quantity       = isset($_POST['quantity']) ? sanitize_text_field($_POST['quantity']) : '';
        $tooling_status = isset($_POST['tooling_status']) ? sanitize_text_field($_POST['tooling_status']) : '';
        $contact_name   = isset($_POST['contact_name']) ? sanitize_text_field($_POST['contact_name']) : '';
        $company_name   = isset($_POST['company_name']) ? sanitize_text_field($_POST['company_name']) : '';
        $email          = isset($_POST['email']) ? sanitize_email($_POST['email']) : '';
        $phone          = isset($_POST['phone']) ? sanitize_text_field($_POST['phone']) : '';
        $notes          = isset($_POST['notes']) ? sanitize_textarea_field($_POST['notes']) : '';
        $ip_address     = isset($_SERVER['REMOTE_ADDR']) ? sanitize_text_field($_SERVER['REMOTE_ADDR']) : '';

        if (empty($contact_name) || empty($phone) || empty($part_name)) {
            wp_send_json_error(array('message' => 'Please provide your name, phone number, and component name.'));
        }

        // 1. Insert into Database Table
        $now = current_time('mysql');
        $inserted = $wpdb->insert(
            $table_name,
            array(
                'created_at'     => $now,
                'client_name'    => $contact_name,
                'company_name'   => $company_name,
                'email'          => $email,
                'phone'          => $phone,
                'part_name'      => $part_name,
                'material'       => $material,
                'quantity'       => $quantity,
                'tooling_status' => $tooling_status,
                'notes'          => $notes,
                'ip_address'     => $ip_address,
                'status'         => 'New',
            ),
            array('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')
        );

        $lead_id = $wpdb->insert_id;

        // Fallback: If insert_id is empty or 0, query latest ID
        if (empty($lead_id)) {
            $latest = $wpdb->get_var("SELECT MAX(id) FROM `$table_name`");
            $lead_id = !empty($latest) ? intval($latest) : intval(date('ymd') . rand(100, 999));
        }

        // 2. Dispatch Email via Hostinger SMTP to vigneshkannan52@gmail.com
        $to = get_option('negizhi_notification_email', 'vigneshkannan52@gmail.com');
        $subject = sprintf('[New RFQ Lead #%d] %s - %s (%s)', $lead_id, $part_name, $company_name ? $company_name : 'Direct Inquiry', $contact_name);

        $email_body = $this->build_rfq_email_html(array(
            'lead_id'        => $lead_id,
            'client_name'    => $contact_name,
            'company_name'   => $company_name,
            'email'          => $email,
            'phone'          => $phone,
            'part_name'      => $part_name,
            'material'       => $material,
            'quantity'       => $quantity,
            'tooling_status' => $tooling_status,
            'notes'          => $notes,
            'ip_address'     => $ip_address,
            'date_time'      => current_time('F j, Y, g:i a'),
        ));

        $from_email = get_option('negizhi_smtp_user', 'contact@negizhiindustries.com');
        $from_name  = get_option('negizhi_smtp_from_name', 'Negizhi Industries Website');

        $headers = array(
            'Content-Type: text/html; charset=UTF-8',
            'From: ' . $from_name . ' <' . $from_email . '>',
        );

        if (!empty($email)) {
            $headers[] = 'Reply-To: ' . $contact_name . ' <' . $email . '>';
        }

        $mail_sent = wp_mail($to, $subject, $email_body, $headers);

        // 3. Optional Courtesy Confirmation Email to Client
        if (!empty($email)) {
            $client_subject = 'Technical RFQ Inquiry Received - Negizhi Industries';
            $client_body = $this->build_client_acknowledgment_html($contact_name, $part_name, $material, $lead_id);
            wp_mail($email, $client_subject, $client_body, array(
                'Content-Type: text/html; charset=UTF-8',
                'From: Negizhi Industries <' . $from_email . '>',
            ));
        }

        wp_send_json_success(array(
            'lead_id'   => $lead_id,
            'mail_sent' => $mail_sent,
            'message'   => 'Your technical RFQ has been logged and dispatched to our engineering desk! Our engineering team will review your tolerances and connect with you shortly.'
        ));
    }

    /**
     * Build high-contrast industrial email template for admin notification
     */
    private function build_rfq_email_html($data) {
        $wa_clean_phone = preg_replace('/[^0-9]/', '', $data['phone']);
        $admin_url = admin_url('admin.php?page=negizhi-rfq-leads');

        return '
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background-color: #060a12; color: #f8fafc; margin: 0; padding: 24px; }
            .email-wrap { max-width: 640px; margin: 0 auto; background: #0b1120; border: 1px solid #1e293b; border-radius: 12px; overflow: hidden; box-shadow: 0 10px 30px rgba(0,0,0,0.5); }
            .email-head { background: #060a12; padding: 24px 28px; border-bottom: 2px solid #00e5ff; }
            .email-logo-title { font-size: 20px; font-weight: 800; color: #00e5ff; letter-spacing: 0.05em; text-transform: uppercase; }
            .email-badge { display: inline-block; background: rgba(0, 229, 255, 0.15); color: #00e5ff; padding: 4px 10px; border-radius: 4px; font-size: 11px; font-weight: 700; margin-top: 6px; letter-spacing: 0.08em; }
            .email-body { padding: 28px; }
            .spec-table { width: 100%; border-collapse: collapse; margin-top: 16px; margin-bottom: 24px; }
            .spec-table td { padding: 12px 14px; border-bottom: 1px solid #1e293b; font-size: 14px; vertical-align: top; }
            .spec-k { width: 35%; color: #94a3b8; font-weight: 600; text-transform: uppercase; font-size: 11px; letter-spacing: 0.05em; }
            .spec-v { color: #f1f5f9; font-weight: 600; }
            .spec-v a { color: #00e5ff; text-decoration: none; }
            .notes-box { background: #050811; border-left: 3px solid #00e5ff; padding: 14px 18px; border-radius: 4px; color: #cbd5e1; font-size: 13.5px; line-height: 1.6; margin-top: 16px; }
            .btn-row { display: flex; gap: 12px; margin-top: 24px; }
            .btn-action { display: inline-block; padding: 10px 18px; border-radius: 6px; text-decoration: none; font-size: 13px; font-weight: 700; text-align: center; }
            .btn-wa { background: #25d366; color: #ffffff !important; }
            .btn-dash { background: #0066ff; color: #ffffff !important; }
            .email-foot { background: #060a12; padding: 18px 28px; text-align: center; font-size: 12px; color: #64748b; border-top: 1px solid #1e293b; }
          </style>
        </head>
        <body>
          <div class="email-wrap">
            <div class="email-head">
              <div class="email-logo-title">NEGIZHI INDUSTRIES</div>
              <div class="email-badge">NEW TECHNICAL RFQ LEAD #' . esc_html($data['lead_id']) . '</div>
            </div>
            <div class="email-body">
              <p style="font-size: 15px; color: #e2e8f0; margin-top: 0;">A new technical inquiry was submitted via the website landing page on <strong>' . esc_html($data['date_time']) . '</strong>.</p>
              
              <table class="spec-table">
                <tr>
                  <td class="spec-k">Component Name</td>
                  <td class="spec-v" style="color: #00e5ff; font-size: 16px;">' . esc_html($data['part_name']) . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Target Polymer</td>
                  <td class="spec-v">' . esc_html($data['material']) . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Batch Quantity</td>
                  <td class="spec-v">' . esc_html($data['quantity']) . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Mould Tooling</td>
                  <td class="spec-v">' . esc_html($data['tooling_status']) . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Client Name</td>
                  <td class="spec-v">' . esc_html($data['client_name']) . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Company</td>
                  <td class="spec-v">' . esc_html($data['company_name'] ? $data['company_name'] : 'Not Specified') . '</td>
                </tr>
                <tr>
                  <td class="spec-k">Business Email</td>
                  <td class="spec-v"><a href="mailto:' . esc_attr($data['email']) . '">' . esc_html($data['email']) . '</a></td>
                </tr>
                <tr>
                  <td class="spec-k">Phone Number</td>
                  <td class="spec-v"><a href="tel:' . esc_attr($data['phone']) . '">' . esc_html($data['phone']) . '</a></td>
                </tr>
                <tr>
                  <td class="spec-k">Client IP</td>
                  <td class="spec-v" style="font-family: monospace; font-size: 12px; color: #64748b;">' . esc_html($data['ip_address']) . '</td>
                </tr>
              </table>

              <div style="font-size: 12px; font-weight: 700; color: #94a3b8; text-transform: uppercase; letter-spacing: 0.05em;">Technical Notes &amp; Specifications:</div>
              <div class="notes-box">' . nl2br(esc_html($data['notes'] ? $data['notes'] : 'No extra notes provided.')) . '</div>

              <div style="margin-top: 26px;">
                <a href="https://wa.me/' . esc_attr($wa_clean_phone) . '" class="btn-action btn-wa" style="margin-right: 10px;">Chat on WhatsApp (' . esc_html($data['phone']) . ')</a>
                <a href="' . esc_url($admin_url) . '" class="btn-action btn-dash">Open WordPress Leads Table</a>
              </div>
            </div>
            <div class="email-foot">
              Negizhi Industries &bull; 5/160A, 79/2, Arasur Post, Sulur TK, Coimbatore, Tamil Nadu, India &bull; Direct: +91 86108 88097
            </div>
          </div>
        </body>
        </html>';
    }

    /**
     * Courtesy confirmation email to the client
     */
    private function build_client_acknowledgment_html($name, $part, $material, $id) {
        return '
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
          <style>
            body { font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Arial, sans-serif; background-color: #060a12; color: #f8fafc; margin: 0; padding: 24px; }
            .wrap { max-width: 580px; margin: 0 auto; background: #0b1120; border: 1px solid #1e293b; border-radius: 12px; overflow: hidden; }
            .head { background: #060a12; padding: 24px 28px; border-bottom: 2px solid #00e5ff; }
            .body { padding: 28px; line-height: 1.6; font-size: 14.5px; color: #cbd5e1; }
            .card { background: #050811; border: 1px solid #1e293b; border-radius: 8px; padding: 16px 20px; margin: 18px 0; }
            .foot { background: #060a12; padding: 16px 28px; font-size: 12px; color: #64748b; text-align: center; }
          </style>
        </head>
        <body>
          <div class="wrap">
            <div class="head">
              <div style="font-size: 18px; font-weight: 800; color: #00e5ff; text-transform: uppercase;">NEGIZHI INDUSTRIES</div>
              <div style="font-size: 12px; color: #94a3b8; margin-top: 4px;">Precision Engineering Plastic Components // Coimbatore</div>
            </div>
            <div class="body">
              <p>Dear <strong>' . esc_html($name) . '</strong>,</p>
              <p>Thank you for submitting your Request for Quotation (RFQ) to Negizhi Industries.</p>
              <div class="card">
                <div style="color: #94a3b8; font-size: 11px; font-weight: 700; text-transform: uppercase;">Inquiry Reference #' . esc_html($id) . '</div>
                <div style="color: #00e5ff; font-size: 16px; font-weight: 700; margin-top: 4px;">' . esc_html($part) . '</div>
                <div style="color: #e2e8f0; font-size: 13px; margin-top: 2px;">Polymer: ' . esc_html($material) . '</div>
              </div>
              <p>Our engineering desk and technical tool room team have received your specifications and are reviewing drawing tolerances and moulding feasibility.</p>
              <p>We will connect with you shortly with pricing and delivery timelines. If you have immediate 2D/3D CAD drawings or urgent requirements, feel free to reply directly to this email or reach us on WhatsApp at <strong>+91 86108 88097</strong>.</p>
            </div>
            <div class="foot">
              Negizhi Industries &bull; Coimbatore, Tamil Nadu, India &bull; contact@negizhiindustries.com
            </div>
          </div>
        </body>
        </html>';
    }

    /**
     * Register Admin Menus
     */
    public function register_admin_menus() {
        add_menu_page(
            __('Negizhi RFQ Leads', 'negizhi-industries-landing'),
            __('Negizhi Inquiries', 'negizhi-industries-landing'),
            'manage_options',
            'negizhi-rfq-leads',
            array($this, 'render_admin_leads_page'),
            'dashicons-clipboard',
            25
        );

        add_submenu_page(
            'negizhi-rfq-leads',
            __('All RFQ Inquiries', 'negizhi-industries-landing'),
            __('All Inquiries', 'negizhi-industries-landing'),
            'manage_options',
            'negizhi-rfq-leads',
            array($this, 'render_admin_leads_page')
        );

        add_submenu_page(
            'negizhi-rfq-leads',
            __('Hostinger SMTP Settings', 'negizhi-industries-landing'),
            __('SMTP Settings', 'negizhi-industries-landing'),
            'manage_options',
            'negizhi-smtp-settings',
            array($this, 'render_admin_smtp_page')
        );
    }

    /**
     * Handle Admin Actions (Save SMTP, Delete Lead, Update Status, Test Email)
     */
    public function handle_admin_actions() {
        if (!current_user_can('manage_options')) return;
        $this->ensure_table_exists();

        // Save SMTP Settings
        if (isset($_POST['negizhi_save_smtp']) && check_admin_referer('negizhi_smtp_save_nonce', 'negizhi_smtp_nonce')) {
            update_option('negizhi_smtp_host', sanitize_text_field($_POST['negizhi_smtp_host']));
            update_option('negizhi_smtp_port', sanitize_text_field($_POST['negizhi_smtp_port']));
            update_option('negizhi_smtp_secure', sanitize_text_field($_POST['negizhi_smtp_secure']));
            update_option('negizhi_smtp_user', sanitize_email($_POST['negizhi_smtp_user']));
            update_option('negizhi_smtp_from_name', sanitize_text_field($_POST['negizhi_smtp_from_name']));
            update_option('negizhi_notification_email', sanitize_email($_POST['negizhi_notification_email']));
            update_option('negizhi_smtp_enabled', isset($_POST['negizhi_smtp_enabled']) ? '1' : '0');

            if (!empty($_POST['negizhi_smtp_pass'])) {
                update_option('negizhi_smtp_pass', sanitize_text_field($_POST['negizhi_smtp_pass']));
            }

            wp_redirect(admin_url('admin.php?page=negizhi-smtp-settings&updated=1'));
            exit;
        }

        // Send Test Email
        if (isset($_POST['negizhi_send_test_email']) && check_admin_referer('negizhi_test_email_nonce', 'negizhi_test_nonce')) {
            $to = get_option('negizhi_notification_email', 'vigneshkannan52@gmail.com');
            $subject = 'Hostinger SMTP Test Email - Negizhi Industries';
            $body = '<p><strong>Success!</strong> Your Hostinger SMTP configuration on Negizhi Industries website is working properly.</p><p>Sender: contact@negizhiindustries.com via smtp.hostinger.com<br>Recipient: ' . esc_html($to) . '<br>Timestamp: ' . current_time('mysql') . '</p>';
            $headers = array('Content-Type: text/html; charset=UTF-8');

            $sent = wp_mail($to, $subject, $body, $headers);
            $status = $sent ? 'test_sent' : 'test_failed';
            wp_redirect(admin_url('admin.php?page=negizhi-smtp-settings&test_status=' . $status));
            exit;
        }

        // Delete Single Lead
        if (isset($_GET['action']) && 'delete_lead' === $_GET['action'] && isset($_GET['lead_id'])) {
            $lead_id = intval($_GET['lead_id']);
            check_admin_referer('delete_lead_' . $lead_id);
            global $wpdb;
            $wpdb->delete($wpdb->prefix . 'negizhi_rfq_leads', array('id' => $lead_id), array('%d'));
            wp_redirect(admin_url('admin.php?page=negizhi-rfq-leads&deleted=1'));
            exit;
        }

        // Update Lead Status
        if (isset($_POST['negizhi_update_status']) && isset($_POST['lead_id']) && isset($_POST['lead_status'])) {
            check_admin_referer('update_lead_status');
            global $wpdb;
            $wpdb->update(
                $wpdb->prefix . 'negizhi_rfq_leads',
                array('status' => sanitize_text_field($_POST['lead_status'])),
                array('id' => intval($_POST['lead_id'])),
                array('%s'),
                array('%d')
            );
            wp_redirect(admin_url('admin.php?page=negizhi-rfq-leads&status_updated=1'));
            exit;
        }
    }

    /**
     * Export all leads to CSV
     */
    public function export_leads_csv() {
        if (!current_user_can('manage_options')) wp_die('Unauthorized');
        check_admin_referer('negizhi_export_leads');

        $this->ensure_table_exists();

        global $wpdb;
        $table_name = $wpdb->prefix . 'negizhi_rfq_leads';
        $leads = $wpdb->get_results("SELECT * FROM $table_name ORDER BY id DESC", ARRAY_A);

        header('Content-Type: text/csv; charset=utf-8');
        header('Content-Disposition: attachment; filename=negizhi-rfq-leads-' . date('Y-m-d') . '.csv');

        $output = fopen('php://output', 'w');
        fputcsv($output, array('Lead ID', 'Date & Time', 'Status', 'Client Name', 'Company Name', 'Email', 'Phone', 'Component Name', 'Polymer Material', 'Batch Quantity', 'Tooling Status', 'Technical Notes', 'IP Address'));

        if (!empty($leads)) {
            foreach ($leads as $l) {
                fputcsv($output, array(
                    $l['id'],
                    $l['created_at'],
                    $l['status'],
                    $l['client_name'],
                    $l['company_name'],
                    $l['email'],
                    $l['phone'],
                    $l['part_name'],
                    $l['material'],
                    $l['quantity'],
                    $l['tooling_status'],
                    $l['notes'],
                    $l['ip_address'],
                ));
            }
        }
        fclose($output);
        exit;
    }

    /**
     * Render the All Inquiries Data Table Page
     */
    public function render_admin_leads_page() {
        $this->ensure_table_exists();

        global $wpdb;
        $table_name = $wpdb->prefix . 'negizhi_rfq_leads';

        $search = isset($_GET['s']) ? sanitize_text_field($_GET['s']) : '';
        $filter_status = isset($_GET['status_filter']) ? sanitize_text_field($_GET['status_filter']) : '';

        $where = "WHERE 1=1";
        if (!empty($search)) {
            $like = '%' . $wpdb->esc_like($search) . '%';
            $where .= $wpdb->prepare(" AND (client_name LIKE %s OR company_name LIKE %s OR email LIKE %s OR phone LIKE %s OR part_name LIKE %s)", $like, $like, $like, $like, $like);
        }
        if (!empty($filter_status) && 'all' !== $filter_status) {
            $where .= $wpdb->prepare(" AND status = %s", $filter_status);
        }

        $total_leads = $wpdb->get_var("SELECT COUNT(*) FROM $table_name");
        $new_leads   = $wpdb->get_var("SELECT COUNT(*) FROM $table_name WHERE status = 'New'");
        $leads       = $wpdb->get_results("SELECT * FROM $table_name $where ORDER BY id DESC LIMIT 100");

        ?>
        <div class="wrap" style="max-width: 1280px; margin-top: 20px;">
            <h1 style="display: flex; align-items: center; justify-content: space-between; font-weight: 700; margin-bottom: 20px;">
                <span>Negizhi Industries &mdash; Technical RFQ Inquiries (<?php echo intval($total_leads); ?> Total / <?php echo intval($new_leads); ?> New)</span>
                <div>
                    <a href="<?php echo wp_nonce_url(admin_url('admin-post.php?action=negizhi_export_leads_csv'), 'negizhi_export_leads'); ?>" class="button button-primary" style="margin-left: 10px;">
                        <span class="dashicons dashicons-download" style="vertical-align: middle; margin-top: -2px;"></span> Export to CSV
                    </a>
                    <a href="<?php echo admin_url('admin.php?page=negizhi-smtp-settings'); ?>" class="button button-secondary" style="margin-left: 6px;">
                        <span class="dashicons dashicons-email" style="vertical-align: middle; margin-top: -2px;"></span> Hostinger SMTP Settings
                    </a>
                </div>
            </h1>

            <?php if (isset($_GET['deleted'])): ?>
                <div class="notice notice-success is-dismissible"><p>Lead deleted successfully.</p></div>
            <?php endif; ?>
            <?php if (isset($_GET['status_updated'])): ?>
                <div class="notice notice-success is-dismissible"><p>Lead status updated.</p></div>
            <?php endif; ?>

            <!-- Search & Filters -->
            <div style="background: #ffffff; padding: 14px 18px; border-radius: 6px; box-shadow: 0 1px 3px rgba(0,0,0,0.06); margin-bottom: 16px; display: flex; justify-content: space-between; align-items: center;">
                <form method="get" action="" style="display: flex; gap: 8px; align-items: center;">
                    <input type="hidden" name="page" value="negizhi-rfq-leads" />
                    <input type="text" name="s" value="<?php echo esc_attr($search); ?>" placeholder="Search name, company, email, part..." style="width: 280px;" />
                    <select name="status_filter">
                        <option value="all" <?php selected($filter_status, 'all'); ?>>All Statuses</option>
                        <option value="New" <?php selected($filter_status, 'New'); ?>>New</option>
                        <option value="Contacted" <?php selected($filter_status, 'Contacted'); ?>>Contacted</option>
                        <option value="Quoted" <?php selected($filter_status, 'Quoted'); ?>>Quoted</option>
                        <option value="Archived" <?php selected($filter_status, 'Archived'); ?>>Archived</option>
                    </select>
                    <button type="submit" class="button">Filter</button>
                    <?php if (!empty($search) || !empty($filter_status)): ?>
                        <a href="<?php echo admin_url('admin.php?page=negizhi-rfq-leads'); ?>" class="button button-link">Reset</a>
                    <?php endif; ?>
                </form>
                <div style="font-size: 13px; color: #64748b;">
                    Receiver Email: <strong><?php echo esc_html(get_option('negizhi_notification_email', 'vigneshkannan52@gmail.com')); ?></strong>
                </div>
            </div>

            <!-- Leads Data Table -->
            <table class="wp-list-table widefat fixed striped table-view-list" style="border-radius: 6px; overflow: hidden; box-shadow: 0 1px 4px rgba(0,0,0,0.08);">
                <thead>
                    <tr>
                        <th style="width: 50px;">ID</th>
                        <th style="width: 130px;">Date &amp; Time</th>
                        <th style="width: 170px;">Client &amp; Company</th>
                        <th style="width: 180px;">Contact Info</th>
                        <th style="width: 180px;">Component &amp; Polymer</th>
                        <th style="width: 140px;">Quantity / Tooling</th>
                        <th style="width: 100px;">Status</th>
                        <th style="width: 130px; text-align: right;">Actions</th>
                    </tr>
                </thead>
                <tbody>
                    <?php if (empty($leads)): ?>
                        <tr>
                            <td colspan="8" style="text-align: center; padding: 40px; color: #64748b;">
                                <span class="dashicons dashicons-inbox" style="font-size: 36px; width: 36px; height: 36px; display: block; margin: 0 auto 8px; opacity: 0.5;"></span>
                                No RFQ inquiries found yet. Submissions from your landing page will appear here instantly.
                            </td>
                        </tr>
                    <?php else: ?>
                        <?php foreach ($leads as $l): 
                            $clean_phone = preg_replace('/[^0-9]/', '', $l->phone);
                        ?>
                            <tr>
                                <td><strong>#<?php echo esc_html($l->id); ?></strong></td>
                                <td style="font-size: 12px; color: #64748b;">
                                    <?php echo esc_html(date('M j, Y', strtotime($l->created_at))); ?><br>
                                    <?php echo esc_html(date('g:i a', strtotime($l->created_at))); ?>
                                </td>
                                <td>
                                    <strong><?php echo esc_html($l->client_name); ?></strong><br>
                                    <span style="font-size: 12px; color: #64748b;"><?php echo esc_html($l->company_name ? $l->company_name : 'No Company'); ?></span>
                                </td>
                                <td>
                                    <?php if (!empty($l->email)): ?>
                                        <a href="mailto:<?php echo esc_attr($l->email); ?>" style="text-decoration: none; font-size: 12px;">
                                            <span class="dashicons dashicons-email" style="font-size: 14px; width: 14px; height: 14px; vertical-align: middle;"></span> <?php echo esc_html($l->email); ?>
                                        </a><br>
                                    <?php endif; ?>
                                    <a href="tel:<?php echo esc_attr($l->phone); ?>" style="text-decoration: none; font-size: 12px; font-weight: 600;">
                                        <span class="dashicons dashicons-phone" style="font-size: 14px; width: 14px; height: 14px; vertical-align: middle;"></span> <?php echo esc_html($l->phone); ?>
                                    </a>
                                    <?php if (!empty($clean_phone)): ?>
                                        <a href="https://wa.me/<?php echo esc_attr($clean_phone); ?>" target="_blank" style="margin-left: 4px; display: inline-block; background: #25d366; color: #fff; padding: 1px 6px; border-radius: 3px; font-size: 10px; font-weight: 700; text-decoration: none;" title="Open WhatsApp Chat">WA</a>
                                    <?php endif; ?>
                                </td>
                                <td>
                                    <strong style="color: #0284c7;"><?php echo esc_html($l->part_name); ?></strong><br>
                                    <span style="font-size: 12px; color: #475569;"><?php echo esc_html($l->material); ?></span>
                                </td>
                                <td style="font-size: 12px;">
                                    <strong><?php echo esc_html($l->quantity); ?></strong><br>
                                    <span style="color: #64748b;"><?php echo esc_html($l->tooling_status); ?></span>
                                </td>
                                <td>
                                    <?php 
                                    $bg = '#e0f2fe'; $color = '#0369a1';
                                    if ('Contacted' === $l->status) { $bg = '#fef9c3'; $color = '#a16207'; }
                                    elseif ('Quoted' === $l->status) { $bg = '#dcfce7'; $color = '#15803d'; }
                                    elseif ('Archived' === $l->status) { $bg = '#f1f5f9'; $color = '#475569'; }
                                    ?>
                                    <span style="display: inline-block; padding: 3px 8px; border-radius: 12px; font-size: 11px; font-weight: 700; background: <?php echo $bg; ?>; color: <?php echo $color; ?>;">
                                        <?php echo esc_html($l->status); ?>
                                    </span>
                                </td>
                                <td style="text-align: right;">
                                    <button type="button" class="button button-small" onclick="negizhiViewLead(<?php echo esc_js($l->id); ?>)">View</button>
                                    <a href="<?php echo wp_nonce_url(admin_url('admin.php?page=negizhi-rfq-leads&action=delete_lead&lead_id=' . $l->id), 'delete_lead_' . $l->id); ?>" onclick="return confirm('Are you sure you want to permanently delete Lead #<?php echo $l->id; ?>?');" class="button button-small button-link-delete" style="color: #dc2626; margin-left: 4px;">Delete</a>

                                    <!-- Hidden detail JSON for modal -->
                                    <div id="lead-data-<?php echo esc_attr($l->id); ?>" style="display: none;" 
                                         data-id="<?php echo esc_attr($l->id); ?>"
                                         data-date="<?php echo esc_attr($l->created_at); ?>"
                                         data-client="<?php echo esc_attr($l->client_name); ?>"
                                         data-company="<?php echo esc_attr($l->company_name); ?>"
                                         data-email="<?php echo esc_attr($l->email); ?>"
                                         data-phone="<?php echo esc_attr($l->phone); ?>"
                                         data-part="<?php echo esc_attr($l->part_name); ?>"
                                         data-material="<?php echo esc_attr($l->material); ?>"
                                         data-quantity="<?php echo esc_attr($l->quantity); ?>"
                                         data-tooling="<?php echo esc_attr($l->tooling_status); ?>"
                                         data-notes="<?php echo esc_attr($l->notes); ?>"
                                         data-ip="<?php echo esc_attr($l->ip_address); ?>"
                                         data-status="<?php echo esc_attr($l->status); ?>"></div>
                                </td>
                            </tr>
                        <?php endforeach; ?>
                    <?php endif; ?>
                </tbody>
            </table>
        </div>

        <!-- Details & Status Modal -->
        <div id="negizhiLeadModal" style="display: none; position: fixed; inset: 0; background: rgba(0,0,0,0.65); z-index: 99999; align-items: center; justify-content: center;">
            <div style="background: #ffffff; width: 620px; max-width: 90%; border-radius: 8px; overflow: hidden; box-shadow: 0 20px 40px rgba(0,0,0,0.3); max-height: 90vh; display: flex; flex-direction: column;">
                <div style="padding: 18px 24px; background: #0f172a; color: #ffffff; display: flex; justify-content: space-between; align-items: center;">
                    <h3 style="margin: 0; color: #00e5ff; font-size: 16px;" id="modalLeadTitle">Lead Details</h3>
                    <button type="button" onclick="negizhiCloseModal()" style="background: transparent; border: none; color: #94a3b8; font-size: 20px; cursor: pointer;">&times;</button>
                </div>
                <div style="padding: 24px; overflow-y: auto;" id="modalLeadBody">
                    <!-- Populated dynamically via JS -->
                </div>
                <div style="padding: 14px 24px; background: #f8fafc; border-top: 1px solid #e2e8f0; display: flex; justify-content: space-between; align-items: center;">
                    <form method="post" action="" style="display: flex; gap: 8px; align-items: center;">
                        <?php wp_nonce_field('update_lead_status'); ?>
                        <input type="hidden" name="negizhi_update_status" value="1" />
                        <input type="hidden" name="lead_id" id="modalStatusLeadId" value="" />
                        <label for="modalLeadStatus" style="font-size: 13px; font-weight: 600;">Status:</label>
                        <select name="lead_status" id="modalLeadStatus">
                            <option value="New">New</option>
                            <option value="Contacted">Contacted</option>
                            <option value="Quoted">Quoted</option>
                            <option value="Archived">Archived</option>
                        </select>
                        <button type="submit" class="button button-primary">Update Status</button>
                    </form>
                    <button type="button" class="button" onclick="negizhiCloseModal()">Close</button>
                </div>
            </div>
        </div>

        <script>
        function negizhiViewLead(id) {
            var dataEl = document.getElementById('lead-data-' + id);
            if (!dataEl) return;
            var d = dataEl.dataset;
            document.getElementById('modalLeadTitle').innerText = 'RFQ Lead #' + d.id + ' — ' + d.part;
            document.getElementById('modalStatusLeadId').value = d.id;
            document.getElementById('modalLeadStatus').value = d.status;

            var html = '<table class="widefat striped" style="margin-bottom: 16px;">' +
                '<tr><th style="width: 35%;">Client Name:</th><td><strong>' + escapeHtml(d.client) + '</strong></td></tr>' +
                '<tr><th>Company:</th><td>' + escapeHtml(d.company || 'Not provided') + '</td></tr>' +
                '<tr><th>Email:</th><td><a href="mailto:' + escapeHtml(d.email) + '">' + escapeHtml(d.email) + '</a></td></tr>' +
                '<tr><th>Phone:</th><td><a href="tel:' + escapeHtml(d.phone) + '">' + escapeHtml(d.phone) + '</a></td></tr>' +
                '<tr><th>Component Part:</th><td><strong style="color: #0284c7;">' + escapeHtml(d.part) + '</strong></td></tr>' +
                '<tr><th>Target Polymer:</th><td>' + escapeHtml(d.material) + '</td></tr>' +
                '<tr><th>Batch Volume:</th><td>' + escapeHtml(d.quantity) + '</td></tr>' +
                '<tr><th>Mould Tooling:</th><td>' + escapeHtml(d.tooling) + '</td></tr>' +
                '<tr><th>Submission Time:</th><td>' + escapeHtml(d.date) + '</td></tr>' +
                '<tr><th>IP Address:</th><td><code>' + escapeHtml(d.ip) + '</code></td></tr>' +
                '</table>' +
                '<h4 style="margin: 12px 0 6px;">Technical Notes / Specs:</h4>' +
                '<div style="background: #f1f5f9; padding: 12px 14px; border-radius: 4px; font-size: 13px; line-height: 1.6; white-space: pre-wrap;">' + escapeHtml(d.notes || 'No notes provided.') + '</div>';

            document.getElementById('modalLeadBody').innerHTML = html;
            document.getElementById('negizhiLeadModal').style.display = 'flex';
        }
        function negizhiCloseModal() {
            document.getElementById('negizhiLeadModal').style.display = 'none';
        }
        function escapeHtml(str) {
            if (!str) return '';
            return str.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;').replace(/"/g, '&quot;');
        }
        </script>
        <?php
    }

    /**
     * Render the Hostinger SMTP Settings Page
     */
    public function render_admin_smtp_page() {
        $host       = get_option('negizhi_smtp_host', 'smtp.hostinger.com');
        $port       = get_option('negizhi_smtp_port', '465');
        $secure     = get_option('negizhi_smtp_secure', 'ssl');
        $user       = get_option('negizhi_smtp_user', 'contact@negizhiindustries.com');
        $pass       = get_option('negizhi_smtp_pass', '');
        $from_name  = get_option('negizhi_smtp_from_name', 'Negizhi Industries Website');
        $recipient  = get_option('negizhi_notification_email', 'vigneshkannan52@gmail.com');
        $enabled    = get_option('negizhi_smtp_enabled', '1');

        $has_password = !empty($pass);
        ?>
        <div class="wrap" style="max-width: 900px; margin-top: 20px;">
            <h1>Hostinger SMTP &amp; Lead Notification Settings</h1>
            
            <?php if (isset($_GET['updated'])): ?>
                <div class="notice notice-success is-dismissible"><p>Hostinger SMTP settings saved successfully!</p></div>
            <?php endif; ?>

            <?php if (isset($_GET['test_status'])): ?>
                <?php if ('test_sent' === $_GET['test_status']): ?>
                    <div class="notice notice-success is-dismissible">
                        <p><strong>✓ Success!</strong> Test email dispatched via <code>smtp.hostinger.com</code> to <strong><?php echo esc_html($recipient); ?></strong>. Please check your inbox or spam folder.</p>
                    </div>
                <?php else: ?>
                    <div class="notice notice-error is-dismissible">
                        <p><strong>✕ Delivery Failed!</strong> Please verify that your Hostinger App Password is correct and that Hostinger allows SMTP connections on port <?php echo esc_html($port); ?>.</p>
                    </div>
                <?php endif; ?>
            <?php endif; ?>

            <!-- Status Banner -->
            <div style="background: <?php echo $has_password ? '#f0fdf4' : '#fffbeb'; ?>; border-left: 4px solid <?php echo $has_password ? '#22c55e' : '#f59e0b'; ?>; padding: 14px 18px; margin: 18px 0; border-radius: 4px; display: flex; align-items: center; justify-content: space-between;">
                <div>
                    <strong style="color: <?php echo $has_password ? '#15803d' : '#b45309'; ?>;">
                        <?php echo $has_password ? '✓ Hostinger SMTP Configured (smtp.hostinger.com:465 SSL)' : '⚠ App Password Required'; ?>
                    </strong>
                    <div style="font-size: 13px; color: #475569; margin-top: 2px;">
                        <?php echo $has_password ? 'All RFQ leads are automatically emailed to ' . esc_html($recipient) . ' from ' . esc_html($user) . '.' : 'Please paste your Hostinger Mail App Password below to enable direct SMTP delivery.'; ?>
                    </div>
                </div>
                <span class="dashicons <?php echo $has_password ? 'dashicons-yes-alt' : 'dashicons-warning'; ?>" style="font-size: 28px; width: 28px; height: 28px; color: <?php echo $has_password ? '#22c55e' : '#f59e0b'; ?>;"></span>
            </div>

            <!-- Settings Form -->
            <div style="background: #ffffff; padding: 24px 30px; border-radius: 8px; box-shadow: 0 1px 3px rgba(0,0,0,0.08);">
                <form method="post" action="">
                    <?php wp_nonce_field('negizhi_smtp_save_nonce', 'negizhi_smtp_nonce'); ?>
                    <input type="hidden" name="negizhi_save_smtp" value="1" />

                    <h2 style="font-size: 16px; margin-top: 0; padding-bottom: 12px; border-bottom: 1px solid #e2e8f0;">1. Hostinger Mail Account (contact@negizhiindustries.com)</h2>
                    
                    <table class="form-table">
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_enabled">Enable SMTP</label></th>
                            <td>
                                <label>
                                    <input type="checkbox" name="negizhi_smtp_enabled" id="negizhi_smtp_enabled" value="1" <?php checked($enabled, '1'); ?> />
                                    Send all landing page inquiries via Hostinger SMTP
                                </label>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_user">Hostinger Mail Address</label></th>
                            <td>
                                <input type="email" name="negizhi_smtp_user" id="negizhi_smtp_user" value="<?php echo esc_attr($user); ?>" class="regular-text" required />
                                <p class="description">Your primary sender mailbox (default: <code>contact@negizhiindustries.com</code>).</p>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_pass">Hostinger App Password</label></th>
                            <td>
                                <div style="display: flex; gap: 8px; align-items: center;">
                                    <input type="password" name="negizhi_smtp_pass" id="negizhi_smtp_pass" value="<?php echo esc_attr($pass); ?>" class="regular-text" placeholder="Enter Hostinger App Password..." />
                                    <button type="button" class="button" onclick="togglePassVisibility()">Show / Hide</button>
                                </div>
                                <p class="description">Enter the application password generated in your Hostinger Webmail panel for <code>contact@negizhiindustries.com</code>.</p>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_from_name">Sender Name</label></th>
                            <td>
                                <input type="text" name="negizhi_smtp_from_name" id="negizhi_smtp_from_name" value="<?php echo esc_attr($from_name); ?>" class="regular-text" />
                                <p class="description">Appears as the sender display name in incoming emails.</p>
                            </td>
                        </tr>
                    </table>

                    <h2 style="font-size: 16px; margin-top: 24px; padding-bottom: 12px; border-bottom: 1px solid #e2e8f0;">2. Inquiry Lead Receiver (vigneshkannan52@gmail.com)</h2>

                    <table class="form-table">
                        <tr>
                            <th scope="row"><label for="negizhi_notification_email">Receiver Email Address</label></th>
                            <td>
                                <input type="email" name="negizhi_notification_email" id="negizhi_notification_email" value="<?php echo esc_attr($recipient); ?>" class="regular-text" required />
                                <p class="description">Every technical RFQ submitted on the website will be instantly delivered to this address.</p>
                            </td>
                        </tr>
                    </table>

                    <h2 style="font-size: 16px; margin-top: 24px; padding-bottom: 12px; border-bottom: 1px solid #e2e8f0;">3. Hostinger Server Connection Parameters</h2>

                    <table class="form-table">
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_host">SMTP Host</label></th>
                            <td>
                                <input type="text" name="negizhi_smtp_host" id="negizhi_smtp_host" value="<?php echo esc_attr($host); ?>" class="regular-text" />
                                <p class="description">Hostinger SMTP Server: <code>smtp.hostinger.com</code></p>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_port">SMTP Port</label></th>
                            <td>
                                <input type="number" name="negizhi_smtp_port" id="negizhi_smtp_port" value="<?php echo esc_attr($port); ?>" style="width: 120px;" />
                                <p class="description">Port <strong>465</strong> for SSL (Recommended by Hostinger) or <strong>587</strong> for TLS.</p>
                            </td>
                        </tr>
                        <tr>
                            <th scope="row"><label for="negizhi_smtp_secure">Encryption Protocol</label></th>
                            <td>
                                <select name="negizhi_smtp_secure" id="negizhi_smtp_secure">
                                    <option value="ssl" <?php selected($secure, 'ssl'); ?>>SSL (Port 465 - Recommended)</option>
                                    <option value="tls" <?php selected($secure, 'tls'); ?>>TLS (Port 587)</option>
                                </select>
                            </td>
                        </tr>
                    </table>

                    <div style="margin-top: 24px;">
                        <button type="submit" class="button button-primary button-large">Save SMTP Settings</button>
                    </div>
                </form>

                <!-- Send Test Email Tool -->
                <?php if ($has_password): ?>
                    <div style="margin-top: 36px; padding-top: 24px; border-top: 2px dashed #e2e8f0;">
                        <h3 style="margin-top: 0;">Test Hostinger SMTP Connection</h3>
                        <p style="color: #64748b; font-size: 13px;">Send a live test verification email to confirm that your Hostinger credentials authenticate successfully.</p>
                        <form method="post" action="">
                            <?php wp_nonce_field('negizhi_test_email_nonce', 'negizhi_test_nonce'); ?>
                            <input type="hidden" name="negizhi_send_test_email" value="1" />
                            <button type="submit" class="button button-secondary">
                                <span class="dashicons dashicons-email-alt" style="vertical-align: middle; margin-top: -2px;"></span> Send Test Email to <?php echo esc_html($recipient); ?>
                            </button>
                        </form>
                    </div>
                <?php endif; ?>
            </div>
        </div>

        <script>
        function togglePassVisibility() {
            var input = document.getElementById('negizhi_smtp_pass');
            if (input.type === 'password') {
                input.type = 'text';
            } else {
                input.type = 'password';
            }
        }
        </script>
        <?php
    }

    /**
     * Shortcode support: [negizhi_landing_page]
     */
    public function render_shortcode($atts) {
        wp_enqueue_style('negizhi-google-fonts', 'https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;500;600;700&family=Outfit:wght@500;600;700;800;900&family=Plus+Jakarta+Sans:wght@400;500;600;700;800&display=swap', array(), null);
        wp_enqueue_style('negizhi-styles', NEGIZHI_PLUGIN_URL . 'css/styles.css', array(), NEGIZHI_VERSION);
        wp_enqueue_script('negizhi-app', NEGIZHI_PLUGIN_URL . 'js/app.js', array(), NEGIZHI_VERSION, true);

        wp_localize_script('negizhi-app', 'negizhi_ajax', array(
            'ajax_url' => admin_url('admin-ajax.php'),
            'nonce'    => wp_create_nonce('negizhi_rfq_nonce'),
        ));

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
