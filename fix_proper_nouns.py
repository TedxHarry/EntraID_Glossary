#!/usr/bin/env python3
"""
Fix-up script for proper noun preservation in glossary articles.

Handles edge cases where heading sentence-case conversion affected
acronyms and product names that should have been preserved.
"""

import re
from pathlib import Path

# Mapping of incorrect patterns to correct versions
CORRECTIONS = {
    # Acronyms that got lowercased
    r'\b(saml vs oidc)\b': 'SAML vs OIDC',
    r'\boidc vs saml\b': 'OIDC vs SAML',
    r'\b(oauth2|oauth 2\.0) kind\b': 'OAuth 2.0 kind',
    r'the (oauth2) kind': 'the OAuth 2.0 kind',
    r'\b(in entra id)\b': 'in Entra ID',
    r'\b(what (entra id|oidc|saml|oauth) (?:is|does|means))\b': lambda m: _fix_phrase(m),
    r'(microsoft ecosystem)': 'Microsoft ecosystem',
    r'(oidc)([^a-z]|$)': r'OIDC\2',  # oidc when not part of a larger word
}

def _fix_phrase(match):
    """Fix common phrases with proper nouns."""
    text = match.group(0)
    replacements = {
        'what entra id is': 'what Entra ID is',
        'what oidc is': 'what OIDC is',
        'what saml is': 'what SAML is',
        'what oauth is': 'what OAuth is',
        'what microsoft graph': 'what Microsoft Graph',
    }
    return replacements.get(text.lower(), text)

def fix_file(file_path: Path) -> bool:
    """Fix proper nouns in a single file. Returns True if changed."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()

        original = content

        # Apply corrections (in order of specificity)
        # Fix specific heading patterns
        content = re.sub(r'## 🏢 OIDC vs saml', '## 🏢 OIDC vs SAML', content, flags=re.IGNORECASE)
        content = re.sub(r'## 💡 SAML vs oidc', '## 💡 SAML vs OIDC', content, flags=re.IGNORECASE)
        content = re.sub(r'## 📌 Permission delegation \(the oauth2 kind\)',
                        '## 📌 Permission delegation (the OAuth 2.0 kind)', content, flags=re.IGNORECASE)

        # Fix "in entra id" or "in oidc" contexts
        content = re.sub(r'\bin entra id\b', 'in Entra ID', content, flags=re.IGNORECASE)
        content = re.sub(r'\b(microsoft) ecosystem\b', r'Microsoft ecosystem', content)

        # Fix standalone acronyms that got lowercased
        # But be careful not to change them in URLs or code blocks
        lines = content.split('\n')
        in_code = False
        for i, line in enumerate(lines):
            if line.startswith('```'):
                in_code = not in_code
            elif not in_code:
                # Fix common patterns
                line = re.sub(r'\boidc\b(?!\.)', 'OIDC', line)  # oidc but not in URLs
                line = re.sub(r'\bsaml\b(?!\.)', 'SAML', line)
                line = re.sub(r'\boauth\b', 'OAuth', line)
                lines[i] = line

        content = '\n'.join(lines)

        if content != original:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(content)
            return True
        return False

    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return False

def main():
    root_path = Path(__file__).parent
    articles = sorted(root_path.rglob('glossary-*.md'))

    print("=" * 70)
    print("FIX-UP: Proper Noun Preservation")
    print("=" * 70)
    print(f"\nProcessing {len(articles)} articles...\n")

    fixed_count = 0
    for article in articles:
        if fix_file(article):
            print(f"✓ Fixed: {article.relative_to(root_path)}")
            fixed_count += 1

    print(f"\n{fixed_count} files updated")
    print("=" * 70)

if __name__ == '__main__':
    main()
