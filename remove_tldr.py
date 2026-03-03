#!/usr/bin/env python3
"""
Remove TL;DR sections from all glossary articles.
"""

import os
import re
from pathlib import Path

# Directory containing glossary articles
base_dir = Path(r"C:\Users\punna\Videos\Github Learning\Entra ID")

# Find all glossary markdown files
glossary_files = list(base_dir.glob("*/glossary-*.md"))
glossary_files.sort()

print(f"Found {len(glossary_files)} glossary files")
print("=" * 60)

changes = []

for file_path in glossary_files:
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    original_content = content

    # Pattern to match TL;DR section:
    # ## 🎯 TL;DR
    # followed by any number of bullet lines (- text)
    # until we hit a blank line or next section
    pattern = r'## 🎯 TL;DR\s*\n(?:- [^\n]*\n)+\n'

    if re.search(pattern, content):
        # Remove the TL;DR section
        content = re.sub(pattern, '', content)

        # Write back to file
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)

        # Log the change
        rel_path = file_path.relative_to(base_dir)
        changes.append(str(rel_path))
        print(f"✓ Removed TL;DR from: {rel_path}")

print("=" * 60)
print(f"\nTotal files modified: {len(changes)}")
print("\nFiles changed:")
for f in changes:
    print(f"  - {f}")
