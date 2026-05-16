"""
extract_base64_images.py
========================
Extracts Base64-encoded images from HTML files and replaces them with
references to saved image files.

Usage
-----
1. Put this script in the ROOT of your Netlify project folder
   (the same folder that contains index.html, la-post.html, etc.)
2. Run:   python extract_base64_images.py
3. The script will:
   - Create an  images/  sub-folder (if it doesn't exist)
   - Save every embedded image as  images/<html-filename>-img-<N>.<ext>
   - Rewrite each HTML file so  src="data:image/..."  becomes  src="images/..."
   - Print a summary of what it did

Requirements: Python 3.6+  (no third-party packages needed)
"""

import base64
import os
import re

# ── Configuration ─────────────────────────────────────────────────────────────

# HTML files to process (relative to this script's location).
# Add more filenames here if you have additional pages.
HTML_FILES = [
    "index.html",
    "la-post.html",
]

# Folder where extracted images will be saved.
OUTPUT_DIR = "images"

# ── Helpers ───────────────────────────────────────────────────────────────────

# Maps MIME type → file extension
MIME_TO_EXT = {
    "image/jpeg": "jpg",
    "image/jpg":  "jpg",
    "image/png":  "png",
    "image/gif":  "gif",
    "image/webp": "webp",
    "image/svg+xml": "svg",
    "image/avif": "avif",
    "image/bmp":  "bmp",
    "image/tiff": "tiff",
}

# Regex: matches   src="data:<mime>;base64,<data>"
#        also handles single-quoted and unquoted variants
DATA_URI_RE = re.compile(
    r"""(src\s*=\s*)(["'])(data:(image/[^;]+);base64,([A-Za-z0-9+/=\s]+?))\2""",
    re.IGNORECASE | re.DOTALL,
)

# Also catch CSS background-image: url("data:...") patterns
CSS_BG_RE = re.compile(
    r"""(url\s*\()(["']?)(data:(image/[^;]+);base64,([A-Za-z0-9+/=\s]+?))\2(\))""",
    re.IGNORECASE | re.DOTALL,
)


def extract_images_from_html(html_path: str, output_dir: str) -> tuple[str, int, int]:
    """
    Parse *html_path*, extract Base64 images, save them to *output_dir*,
    and return the rewritten HTML plus counts of images found / saved.
    """
    with open(html_path, "r", encoding="utf-8", errors="replace") as fh:
        html = fh.read()

    base_name = os.path.splitext(os.path.basename(html_path))[0]
    images_saved = 0
    images_skipped = 0
    counter = [0]  # mutable so inner function can update it

    def replace_src(match):
        prefix    = match.group(1)   # 'src='
        quote     = match.group(2)   # " or '
        mime_type = match.group(4).lower().strip()
        b64_data  = match.group(5).replace("\n", "").replace("\r", "").replace(" ", "")

        ext = MIME_TO_EXT.get(mime_type, "bin")
        counter[0] += 1
        filename = f"{base_name}-img-{counter[0]:03d}.{ext}"
        filepath = os.path.join(output_dir, filename)

        # Decode and save
        try:
            raw = base64.b64decode(b64_data)
            with open(filepath, "wb") as img_file:
                img_file.write(raw)
            kb = len(raw) / 1024
            print(f"  ✓  Saved {filename}  ({kb:,.1f} KB)")
            nonlocal images_saved
            images_saved += 1
            return f"{prefix}{quote}{OUTPUT_DIR}/{filename}{quote}"
        except Exception as exc:
            print(f"  ✗  Could not decode image #{counter[0]}: {exc}")
            nonlocal images_skipped
            images_skipped += 1
            return match.group(0)  # leave unchanged

    def replace_css_bg(match):
        url_open  = match.group(1)   # 'url('
        inner_q   = match.group(2)   # optional quote
        mime_type = match.group(4).lower().strip()
        b64_data  = match.group(5).replace("\n", "").replace("\r", "").replace(" ", "")
        url_close = match.group(6)   # ')'

        ext = MIME_TO_EXT.get(mime_type, "bin")
        counter[0] += 1
        filename = f"{base_name}-img-{counter[0]:03d}.{ext}"
        filepath = os.path.join(output_dir, filename)

        try:
            raw = base64.b64decode(b64_data)
            with open(filepath, "wb") as img_file:
                img_file.write(raw)
            kb = len(raw) / 1024
            print(f"  ✓  Saved {filename}  ({kb:,.1f} KB)")
            nonlocal images_saved
            images_saved += 1
            return f"{url_open}{inner_q}{OUTPUT_DIR}/{filename}{inner_q}{url_close}"
        except Exception as exc:
            print(f"  ✗  Could not decode CSS image #{counter[0]}: {exc}")
            nonlocal images_skipped
            images_skipped += 1
            return match.group(0)

    html = DATA_URI_RE.sub(replace_src, html)
    html = CSS_BG_RE.sub(replace_css_bg, html)

    return html, images_saved, images_skipped


# ── Main ──────────────────────────────────────────────────────────────────────

def main():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    output_dir = os.path.join(script_dir, OUTPUT_DIR)
    os.makedirs(output_dir, exist_ok=True)

    total_saved   = 0
    total_skipped = 0

    for filename in HTML_FILES:
        html_path = os.path.join(script_dir, filename)

        if not os.path.exists(html_path):
            print(f"\n⚠️  File not found, skipping: {filename}")
            continue

        original_size = os.path.getsize(html_path)
        print(f"\n{'─'*60}")
        print(f"Processing: {filename}  ({original_size/1024/1024:.1f} MB)")
        print(f"{'─'*60}")

        new_html, saved, skipped = extract_images_from_html(html_path, output_dir)
        total_saved   += saved
        total_skipped += skipped

        # Write rewritten HTML back to the same file
        with open(html_path, "w", encoding="utf-8") as fh:
            fh.write(new_html)

        new_size = os.path.getsize(html_path)
        reduction = (1 - new_size / original_size) * 100 if original_size else 0
        print(f"\n  Before : {original_size/1024/1024:.2f} MB")
        print(f"  After  : {new_size/1024/1024:.2f} MB")
        print(f"  Reduced: {reduction:.1f}%")
        print(f"  Images extracted: {saved}  |  Skipped: {skipped}")

    print(f"\n{'='*60}")
    print(f"Done!  Total images extracted: {total_saved}")
    if total_skipped:
        print(f"       Images skipped (decode errors): {total_skipped}")
    print(f"       Images saved to: {OUTPUT_DIR}/")
    print(f"{'='*60}")
    print("\nNext steps:")
    print("  1. Review the images/ folder to confirm everything looks right.")
    print("  2. Commit & push all changes (HTML files + images/ folder) to your repo.")
    print("  3. Netlify will redeploy automatically.\n")


if __name__ == "__main__":
    main()
