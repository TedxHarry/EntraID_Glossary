#!/usr/bin/env python3
"""
Add cover images to Section 2 (Core Identity Concepts) articles.
"""

import os
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

    # Extract the filename to determine the image name
    filename = file_path.stem  # e.g., glossary-2-1-identity
    image_filename = f"{filename}.png"  # e.g., glossary-2-1-identity.png

    # Pattern: "Part of Entra ID Glossary Series #X.Y - Term Name" followed by optional blank line(s) and first "---"
    # We want to insert the image after the "Part of..." line
    pattern = r'(📚 Part of Entra ID Glossary Series #\d+\.\d+ - [^\n]+)\n(\n+)(---)'

    # Check if image is already present
    if f'![Cover image](./images/{image_filename}' in content:
        print(f"✓ Already has cover image: {file_path.name}")
        continue

    # Replace pattern to insert the cover image
    replacement = rf'\1\n\n![Cover image](./images/{image_filename})\n\2\3'
    new_content = re.sub(pattern, replacement, content)

    if new_content != content:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(new_content)

        changes.append(file_path.name)
        print(f"✓ Added cover image: {file_path.name}")
    else:
        print(f"✗ Could not find pattern in: {file_path.name}")

print("=" * 60)
print(f"\nTotal files updated: {len(changes)}")
if changes:
    print("\nFiles changed:")
    for f in changes:
        print(f"  - {f}")
