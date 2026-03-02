#!/usr/bin/env python3
"""
Entra ID Glossary Formatting Overhaul Script

Automates mechanical formatting changes across all 189 glossary articles:
1. Convert H2/H3 headings from title case to sentence case
2. Preserve proper nouns, acronyms, product names
3. Simplify author signature format
4. Update "Part of Series" line format
5. Remove meta-commentary about comments from engagement questions
6. Convert em-dashes to appropriate alternatives
7. Log all changes for verification
"""

import os
import re
from pathlib import Path
from typing import List, Tuple

# Proper nouns and acronyms to preserve in uppercase
PROPER_NOUNS = {
    'Microsoft Entra ID',
    'Microsoft Entra',
    'Entra ID',
    'Azure',
    'Active Directory',
    'PowerShell',
    'OAuth',
    'OpenID Connect',
    'OIDC',
    'SAML',
    'SCIM',
    'JWT',
    'JSON',
    'XML',
    'REST',
    'API',
    'Graph API',
    'Microsoft Graph',
    'MFA',
    'SSO',
    'JIT',
    'RBAC',
    'ABAC',
    'IMDS',
    'ARM',
    'CAE',
    'CIAM',
    'B2B',
    'B2C',
    'GDPR',
    'CCPA',
    'UPN',
    'SPN',
    'OID',
    'FIDO2',
    'POP',
    'IMAP',
    'SMTP',
    'MIM',
}

class GlossaryFormatter:
    def __init__(self, root_path: str):
        self.root_path = Path(root_path)
        self.changes_log = []

    def find_all_articles(self) -> List[Path]:
        """Find all glossary articles in the repository."""
        articles = []
        for md_file in self.root_path.rglob('glossary-*.md'):
            articles.append(md_file)
        return sorted(articles)

    def convert_heading_case(self, heading: str) -> str:
        """
        Convert H2/H3 heading from Title Case to Sentence Case.
        Preserves proper nouns, acronyms, and product names.
        """
        # Extract the leading emoji and text
        match = re.match(r'^(#{2,3})\s+(.*?)?\s+(.+)$', heading)
        if not match:
            return heading

        level = match.group(1)  # ## or ###
        emoji = match.group(2) if match.group(2) and match.group(2).strip() else ''
        text = match.group(3) if match.group(3) else ''

        if not text:
            return heading

        # Split text into words
        words = text.split()
        if not words:
            return heading

        # Capitalize first word
        converted_words = [words[0]]

        # For remaining words, check if they're proper nouns/acronyms
        for word in words[1:]:
            word_lower = word.lower()

            # Check if word is a proper noun
            is_proper = False
            for proper_noun in PROPER_NOUNS:
                if word.lower() == proper_noun.lower():
                    converted_words.append(proper_noun)
                    is_proper = True
                    break

            if not is_proper:
                # Check for acronyms (all caps, 2+ letters)
                if re.match(r'^[A-Z]{2,}$', word):
                    converted_words.append(word)  # Keep acronyms as-is
                else:
                    # Convert to lowercase
                    converted_words.append(word_lower)

        converted_text = ' '.join(converted_words)

        # Reconstruct heading
        if emoji:
            return f"{level} {emoji} {converted_text}"
        else:
            return f"{level} {converted_text}"

    def process_file(self, file_path: Path) -> Tuple[bool, str]:
        """
        Process a single article file with all formatting transformations.
        Returns: (success, message)
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()

            original_content = content
            file_name = file_path.relative_to(self.root_path)

            # 1. Convert H2/H3 headings to sentence case
            def replace_heading(match):
                heading = match.group(0)
                converted = self.convert_heading_case(heading)
                if heading != converted:
                    self.changes_log.append(f"  [HEADING] {file_name}: '{heading}' → '{converted}'")
                return converted

            content = re.sub(r'^#{2,3}\s+.+$', replace_heading, content, flags=re.MULTILINE)

            # 2. Update "Part of Entra ID Glossary Series" line
            # FROM: 📚 **Part of Entra ID Glossary Series: Glossary#N.M - Term**
            # TO:   📚 Part of Entra ID Glossary Series #N.M - Term
            def replace_part_line(match):
                line = match.group(0)
                # Extract the series number and term name
                series_match = re.search(r'Glossary#([\d.]+)\s*-\s*(.+)', line)
                if series_match:
                    series_num = series_match.group(1)
                    term_name = series_match.group(2).strip('*')
                    new_line = f"📚 Part of Entra ID Glossary Series #{series_num} - {term_name}"
                    self.changes_log.append(f"  [SERIES LINE] {file_name}: Updated format")
                    return new_line
                return line

            content = re.sub(
                r'📚\s+\*\*Part of Entra ID Glossary Series:.+?\*\*',
                replace_part_line,
                content,
                flags=re.MULTILINE
            )

            # 3. Simplify author signature
            # FROM: > ✍️ *Written by **TedxHarry***
            # TO:   ✍️ TedxHarry
            def replace_signature(match):
                self.changes_log.append(f"  [SIGNATURE] {file_name}: Simplified format")
                return "✍️ TedxHarry"

            content = re.sub(
                r'>\s+✍️\s+\*Written by \*\*TedxHarry\*\*\*',
                replace_signature,
                content
            )

            # 4. Remove meta-commentary about comments from engagement questions
            # Remove patterns like:
            # - "Drop your story in the comments, I read every one."
            # - "Leave a comment"
            # - "Drop your comment"
            # But keep the conversational question itself

            def replace_engagement_question(match):
                full_match = match.group(0)
                # Extract just the question part, remove comment meta-commentary

                # Remove "Drop your story in the comments, I read every one."
                cleaned = re.sub(
                    r'\s*Drop your story in the comments, I read every one\.',
                    '',
                    full_match,
                    flags=re.IGNORECASE
                )

                # Remove other comment meta-commentary patterns
                cleaned = re.sub(
                    r'\s*Leave a comment.*?(?=\n|$)',
                    '',
                    cleaned,
                    flags=re.IGNORECASE | re.DOTALL
                )
                cleaned = re.sub(
                    r'\s*Drop your comment.*?(?=\n|$)',
                    '',
                    cleaned,
                    flags=re.IGNORECASE | re.DOTALL
                )
                cleaned = re.sub(
                    r'\s*Share your.*?(?=\n|$)',
                    '',
                    cleaned,
                    flags=re.IGNORECASE | re.DOTALL
                )

                # Clean up trailing whitespace
                cleaned = cleaned.rstrip()

                if cleaned != full_match:
                    self.changes_log.append(f"  [ENGAGEMENT] {file_name}: Removed meta-commentary")

                return cleaned

            # Match engagement question blocks
            content = re.sub(
                r'💬\s+\*\*[^*]+\*\*.*?(?=\n✍️|$)',
                replace_engagement_question,
                content,
                flags=re.DOTALL
            )

            # 5. Convert em-dashes to appropriate alternatives
            def replace_emdash(match):
                text = match.group(0)
                # In most cases, convert — to :
                converted = text.replace('—', ':')
                if text != converted:
                    self.changes_log.append(f"  [EMDASH] {file_name}: Replaced em-dash with colon")
                return converted

            # Find and replace em-dashes in body text (not in code blocks)
            lines = content.split('\n')
            in_code_block = False
            for i, line in enumerate(lines):
                if line.startswith('```'):
                    in_code_block = not in_code_block
                elif not in_code_block and '—' in line:
                    lines[i] = line.replace('—', ':')
                    self.changes_log.append(f"  [EMDASH] {file_name} (line {i+1}): Replaced em-dash")

            content = '\n'.join(lines)

            # Write back to file if changes were made
            if content != original_content:
                with open(file_path, 'w', encoding='utf-8') as f:
                    f.write(content)
                return True, f"✓ {file_name}"
            else:
                return True, f"- {file_name} (no changes)"

        except Exception as e:
            return False, f"✗ {file_name}: {str(e)}"

    def run(self):
        """Process all glossary articles."""
        print("=" * 70)
        print("ENTRA ID GLOSSARY FORMATTING OVERHAUL")
        print("=" * 70)

        articles = self.find_all_articles()
        print(f"\nFound {len(articles)} glossary articles\n")

        if not articles:
            print("No glossary articles found!")
            return

        success_count = 0
        error_count = 0

        print("Processing articles...\n")

        for article in articles:
            success, message = self.process_file(article)
            print(message)
            if success:
                success_count += 1
            else:
                error_count += 1

        print("\n" + "=" * 70)
        print(f"SUMMARY: {success_count} processed, {error_count} errors")
        print("=" * 70)

        if self.changes_log:
            print("\nCHANGES MADE:\n")
            for change in self.changes_log[:50]:  # Show first 50 changes
                print(change)

            if len(self.changes_log) > 50:
                print(f"\n... and {len(self.changes_log) - 50} more changes")

        # Save detailed log to file
        log_file = self.root_path / "formatting_changes.log"
        with open(log_file, 'w', encoding='utf-8') as f:
            f.write("ENTRA ID GLOSSARY FORMATTING CHANGES\n")
            f.write("=" * 70 + "\n\n")
            for change in self.changes_log:
                f.write(change + "\n")

        print(f"\nDetailed log saved to: {log_file}")


def main():
    root_path = Path(__file__).parent
    formatter = GlossaryFormatter(root_path)
    formatter.run()


if __name__ == '__main__':
    main()
