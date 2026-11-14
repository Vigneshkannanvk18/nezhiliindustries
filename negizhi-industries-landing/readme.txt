=== Negizhi Industries Landing Page & RFQ Lead System ===
Contributors: Negizhi Industries
Tags: elementor, page template, smtp, hostinger, rfq, manufacturing, leads table
Requires at least: 5.4
Tested up to: 6.7
Requires PHP: 7.4
Stable tag: 1.2.0
License: Proprietary
License URI: https://negizhiindustries.com/

High-Performance Precision Plastic Engineering Landing Page template for Negizhi Industries with Hostinger SMTP and RFQ Leads Manager.

== Description ==

This plugin provides:
1. **Dedicated Page Template**: "Negizhi Industries Landing Page" selectable on any page under Page Attributes / Template.
2. **Hostinger SMTP Email Integration**: Directly uses `contact@negizhiindustries.com` via `smtp.hostinger.com:465 (SSL)` with your Hostinger App Password to dispatch immediate inquiry alerts to `vigneshkannan52@gmail.com`.
3. **Interactive WordPress Leads Table**: View all inquiries under WordPress Admin -> **Negizhi Inquiries**. Includes search, status filtering (New, Contacted, Quoted, Archived), view details modal, and instant **Export to CSV**.
4. **Client Confirmation Email**: Automatically sends a professional acknowledgment to the client's business email.
5. **Zero Conflict**: Full isolation from Hello Elementor theme defaults and admin-bar awareness.

== Hostinger SMTP Setup ==

1. In your WordPress admin dashboard, navigate to: **Negizhi Inquiries** -> **SMTP Settings**.
2. Notice the pre-configured parameters:
   - SMTP Host: `smtp.hostinger.com`
   - Port: `465` (SSL)
   - Sender: `contact@negizhiindustries.com`
   - Receiver: `vigneshkannan52@gmail.com`
3. Paste your **Hostinger App Password** in the "Hostinger App Password" field.
4. Click **Save SMTP Settings**.
5. Click **Send Test Email** to verify the connection. You will see a green success alert!

== Changelog ==

= 1.2.0 =
* Fixed leads database table auto-creation across all MySQL/MariaDB database versions.
* Added self-healing table verification on WordPress admin load and form dispatch.
* Cleaned form submission success alert (removed personal proprietor name and email address).
* Added fallback reference ID retrieval so lead IDs are never empty.

= 1.1.0 =
* Added Hostinger SMTP configuration (`smtp.hostinger.com:465 SSL`).
* Added automatic email notifications to `vigneshkannan52@gmail.com`.
* Added WordPress Admin Leads Table with search, filtering, and CSV export.
* Added Business Email & Company Name fields to RFQ form.
* Added courtesy client confirmation email.

= 1.0.0 =
* Initial release with Hello Elementor compatibility.
