#!/usr/bin/env python3
"""
Fix image references in Section 2 articles to point to images folder.
"""

import re
from pathlib import Path

# Directory containing Section 2 articles
section2_dir = Path(r"C:\Users\punna\Videos\Github Learning\Entra ID\2 CORE IDENTITY CONCEPTS")

# Find all glossary-2-*.md files
glossary_files = sorted(section2_dir.glob("glossary-2-*.md"))

print(f"Found {len(glossary_files)} articles in Section 2")
print("=" * 60)

changes = []

for file_path in glossary_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Find the filename to get the image name
    filename = file_path.stem  # e.g., glossary-2-1-identity
    image_filename = f"{filename}.png"

    # Pattern 1: ![Cover image](glossary-2-X-{slug}.png) - incorrect reference
    pattern1 = rf'!\[Cover image\]\({image_filename}\)'
    replacement1 = rf'![Cover image](./images/{image_filename})'

    # Pattern 2: ![Cover image](./images/{image_filename}) - already correct
    # Pattern 3: Any other variation

    content = re.sub(pattern1, replacement1, content)

    if content != original_content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        changes.append(file_path.name)
        print(f"✓ Fixed image reference: {file_path.name}")
    else:
        print(f"✓ Already correct or no change needed: {file_path.name}")

print("=" * 60)
print(f"\nTotal files processed: {len(glossary_files)}")
print(f"Files with changes: {len(changes)}")
