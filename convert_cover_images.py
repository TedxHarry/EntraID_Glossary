#!/usr/bin/env python3
"""
Convert SVG cover images from HTML to PNG and integrate them into markdown articles.
"""

import os
import re
from pathlib import Path
import subprocess
import sys

def extract_svg_from_html(html_content):
    """Extract SVG content from HTML file."""
    # Find the SVG element
    svg_match = re.search(r'<svg[^>]*>.*?</svg>', html_content, re.DOTALL)
    if svg_match:
        return svg_match.group(0)
    return None

def save_svg_to_file(svg_content, filepath):
    """Save SVG content to a temporary file."""
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n')
        f.write(svg_content)

def convert_svg_to_png(svg_path, png_path):
    """Convert SVG to PNG using ImageMagick or cairosvg."""
    try:
        # Try using cairosvg first (better quality)
        import cairosvg
        cairosvg.svg2png(url=svg_path, write_to=png_path, dpi=300)
        return True
    except ImportError:
        print("cairosvg not installed, trying ImageMagick...")
        try:
            # Try ImageMagick (convert command)
            result = subprocess.run(
                ['magick', 'convert', svg_path, '-density', '300', png_path],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                return True
            # Try alternative command
            result = subprocess.run(
                ['convert', svg_path, '-density', '300', png_path],
                capture_output=True,
                text=True
            )
            return result.returncode == 0
        except FileNotFoundError:
            print("ImageMagick not installed, trying Inkscape...")
            try:
                result = subprocess.run(
                    ['inkscape', svg_path, '--export-type=png', f'--export-filename={png_path}'],
                    capture_output=True,
                    text=True
                )
                return result.returncode == 0
            except FileNotFoundError:
                print("ERROR: No image conversion tool found.")
                print("Please install one of: cairosvg (pip install cairosvg), ImageMagick, or Inkscape")
                return False

def main():
    """Main function to convert all cover images and integrate them."""
    base_path = Path(__file__).parent
    section_path = base_path / "1 FOUNDATIONAL CONCEPTS"
    images_path = section_path / "images"

    # Create images directory
    images_path.mkdir(exist_ok=True)

    print("=" * 70)
    print("CONVERT COVER IMAGES: SVG → PNG")
    print("=" * 70)

    # Find all HTML cover image files
    html_files = sorted(section_path.glob("glossary-1-*.html"))

    if not html_files:
        print("No HTML cover image files found!")
        return

    print(f"\nFound {len(html_files)} HTML cover images\n")

    conversions = []

    for html_file in html_files:
        print(f"Processing: {html_file.name}")

        # Read HTML
        with open(html_file, 'r', encoding='utf-8') as f:
            html_content = f.read()

        # Extract SVG
        svg_content = extract_svg_from_html(html_content)
        if not svg_content:
            print(f"  ✗ Could not extract SVG from {html_file.name}")
            continue

        # Create PNG filename matching the markdown file
        md_name = html_file.name.replace('.html', '.md')
        png_name = html_file.stem + '-cover.png'
        png_path = images_path / png_name

        # Save SVG temporarily
        temp_svg = images_path / f"{html_file.stem}-temp.svg"
        save_svg_to_file(svg_content, temp_svg)

        # Convert to PNG
        print(f"  Converting to PNG...")
        if convert_svg_to_png(str(temp_svg), str(png_path)):
            print(f"  ✓ Saved: {png_name}")
            conversions.append({
                'html_file': html_file.name,
                'md_file': md_name,
                'png_file': png_name,
                'png_path': png_path
            })
        else:
            print(f"  ✗ Failed to convert: {html_file.name}")

        # Clean up temp SVG
        if temp_svg.exists():
            temp_svg.unlink()

    print(f"\n{len(conversions)} images converted successfully")

    # Now integrate images into markdown files
    if conversions:
        print("\n" + "=" * 70)
        print("INTEGRATING IMAGES INTO MARKDOWN FILES")
        print("=" * 70 + "\n")

        for conv in conversions:
            md_path = section_path / conv['md_file']
            if not md_path.exists():
                print(f"✗ Markdown file not found: {conv['md_file']}")
                continue

            # Read markdown
            with open(md_path, 'r', encoding='utf-8') as f:
                md_content = f.read()

            # Prepare image markdown
            image_markdown = f"\n![{conv['md_file'].replace('glossary-1-', '').replace('.md', ' cover image')}](./images/{conv['png_file']})\n"

            # Find insertion point: after "📚 Part of Entra ID Glossary Series" line
            lines = md_content.split('\n')
            insert_index = None

            for i, line in enumerate(lines):
                if line.startswith('📚 Part of Entra ID Glossary Series'):
                    insert_index = i + 1
                    break

            if insert_index is None:
                print(f"✗ Could not find insertion point in: {conv['md_file']}")
                continue

            # Insert image
            lines.insert(insert_index, image_markdown)
            updated_content = '\n'.join(lines)

            # Write back
            with open(md_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)

            print(f"✓ {conv['md_file']}: Image added after series line")

    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    print(f"\nImages saved to: {images_path}")
    print("Images integrated into all 6 markdown articles")

if __name__ == '__main__':
    main()
