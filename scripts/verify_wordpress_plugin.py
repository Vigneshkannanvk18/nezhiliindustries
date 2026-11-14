import zipfile, os, re

with open("negizhi-industries-landing/templates/page-negizhi-landing.php", "r", encoding="utf-8") as f:
    php = f.read()

imgs = re.findall(r'<img[^>]+>', php)
sources = re.findall(r'<source[^>]+>', php)

print(f"Total img tags: {len(imgs)}")
for i, img in enumerate(imgs[:6]):
    print(f"  IMG {i+1}: {img[:100]}...")

print(f"\nTotal source tags: {len(sources)}")
for i, src in enumerate(sources[:6]):
    print(f"  SOURCE {i+1}: {src[:100]}...")

# Check for any malformed attributes: src" or srcset" or href"
broken = re.findall(r'(?:src|href|srcset)["\']', php)
print(f"\nBroken attributes check (e.g. src\"): {len(broken)}")
if broken:
    print(f"  FAIL: Found broken attributes: {broken}")
else:
    print("  PASS: Zero broken attributes found!")

# Check that every img tag has src="<?php echo esc_url(NEGIZHI_PLUGIN_URL ...
all_imgs_valid = all('src="<?php echo esc_url(NEGIZHI_PLUGIN_URL' in img or 'src=\'<?php echo esc_url(NEGIZHI_PLUGIN_URL' in img for img in imgs)
print(f"All img tags have dynamic NEGIZHI_PLUGIN_URL: {all_imgs_valid}")

# Check that every source tag has srcset="<?php echo esc_url(NEGIZHI_PLUGIN_URL ...
all_sources_valid = all('srcset="<?php echo esc_url(NEGIZHI_PLUGIN_URL' in src for src in sources)
print(f"All source tags have dynamic NEGIZHI_PLUGIN_URL: {all_sources_valid}")
import zipfile, os, re

with zipfile.ZipFile("negizhi-industries-landing.zip", "r") as z:
    tmpl = z.read("negizhi-industries-landing/templates/page-negizhi-landing.php").decode("utf-8")
    assert 'src="<?php echo esc_url(NEGIZHI_PLUGIN_URL' in tmpl, "Missing valid src in zip!"
    broken_in_zip = re.findall(r'(?:src|href|srcset)["\']', tmpl)
    print(f"ZIP Archive Check: Broken attributes: {len(broken_in_zip)}")
    if broken_in_zip:
        print("  FAIL in ZIP:", broken_in_zip)
    else:
        print("  PASS: ZIP archive contains 100% valid src= and srcset= attributes!")

print("ZIP file size:", os.path.getsize("negizhi-industries-landing.zip") / 1024, "KB")
