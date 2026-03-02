#!/usr/bin/env python3
"""
Convert SVG cover images from HTML to PNG using Playwright (cross-platform).
"""

import os
import re
from pathlib import Path
import asyncio

async def convert_html_to_png():
    """Convert HTML files to PNG using Playwright."""
    try:
        from playwright.async_api import async_playwright
    except ImportError:
        print("Playwright not installed. Installing...")
        import subprocess
        subprocess.check_call(['pip', 'install', 'playwright', '-q'])
        from playwright.async_api import async_playwright

    base_path = Path(__file__).parent
    section_path = base_path / "1 FOUNDATIONAL CONCEPTS"
    images_path = section_path / "images"
    images_path.mkdir(exist_ok=True)

    print("=" * 70)
    print("CONVERT COVER IMAGES: HTML → PNG")
    print("=" * 70)

    html_files = sorted(section_path.glob("glossary-1-*.html"))

    if not html_files:
        print("No HTML cover image files found!")
        return []

    print(f"\nFound {len(html_files)} HTML cover images\n")

    conversions = []

    async with async_playwright() as p:
        browser = await p.chromium.launch()

        for html_file in html_files:
            print(f"Converting: {html_file.name}")

            # Create full file path
            html_path = f"file:///{html_file.absolute()}".replace('\\', '/')

            # PNG filename
            png_name = html_file.stem + '-cover.png'
            png_path = images_path / png_name

            try:
                page = await browser.new_page(viewport={"width": 1200, "height": 675})
                await page.goto(html_path, wait_until="networkidle")
                await page.screenshot(path=str(png_path), full_page=False)
                await page.close()

                print(f"  ✓ Saved: {png_name}")
                conversions.append({
                    'html_file': html_file.name,
                    'md_file': html_file.name.replace('.html', '.md'),
                    'png_file': png_name,
                })
            except Exception as e:
                print(f"  ✗ Error converting {html_file.name}: {e}")

        await browser.close()

    return conversions, images_path

def integrate_images_into_markdown(conversions, section_path):
    """Integrate images into markdown files."""
    if not conversions:
        return

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
        image_markdown = f"\n![Cover image](./images/{conv['png_file']})\n"

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

        print(f"✓ {conv['md_file']}: Image added")

def main():
    """Main function."""
    base_path = Path(__file__).parent
    section_path = base_path / "1 FOUNDATIONAL CONCEPTS"

    # Run async conversion
    conversions, images_path = asyncio.run(convert_html_to_png())

    if conversions:
        integrate_images_into_markdown(conversions, section_path)

    print("\n" + "=" * 70)
    print("COMPLETE!")
    print("=" * 70)
    if conversions:
        print(f"\n✓ {len(conversions)} images converted and integrated")
        print(f"Images saved to: {images_path}")
    else:
        print("\nNo images were converted.")

if __name__ == '__main__':
    main()
