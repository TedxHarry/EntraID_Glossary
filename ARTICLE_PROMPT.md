# Glossary Article Writing Prompt

Use this prompt when asking an AI to write new articles for this glossary series.

---

## Prompt

Write a glossary article for a technical documentation site about **[TOPIC]**.

This article is part of the **[SERIES NAME] Glossary Series** — a comprehensive, experience-driven reference written by a practitioner named **TedxHarry**. The series is published as a Docsify site on GitHub Pages with a dark theme.

---

### Voice & Style

- Write in **first-person practitioner voice** — as someone who has done this work in the real world, not a textbook author
- Use **short paragraphs** — 2–4 sentences max. No walls of text
- Start the article with a **concrete real-world story or scenario** (a mistake you made, a customer problem, a common confusion you see) — no generic definitions at the top
- **Bold** key terms and concepts where they first appear. Use bold sparingly — only for things worth highlighting
- Use *italics* for emphasis within a sentence, not for whole sentences
- No fluff. No "In conclusion". No restating what was just said
- Write for **two audiences simultaneously** — a beginner who needs the concept explained simply, and a practitioner who needs the nuance and edge cases
- Avoid em dashes (—). Use a comma, period, or restructure the sentence instead

---

### Article Format

Use **exactly** this structure:

```markdown
# [Term Name]
*[Descriptive subtitle — what makes this term interesting or important, phrased as a statement or question, max 10 words]*

> **Difficulty:** [🟢 Beginner | 🟡 Intermediate | 🔴 Advanced]

📚 **Part of [Series Name] Glossary Series: Glossary#[Section].[Number] - [Term Name]**

---

## 🎯 TL;DR

- [Key point 1 — the single most important thing to know]
- [Key point 2 — the practical implication or common mistake]
- [Key point 3 — the distinguishing fact or gotcha]


[Opening story or scenario — 1–3 paragraphs. No heading. Drop the reader into a real situation.]

## [Emoji] [Section heading — what the term actually is]

[Core definition and explanation]

## [Emoji] [Section heading — why it works this way / the mechanics]

[How it works, what it does, the structure]

## [Emoji] [Section heading — practical relevance / real-world application]

[What this means in practice, how you use it, when it matters]

## [Emoji] [Section heading — common mistakes / gotchas / what to watch out for]

[Edge cases, common confusions, things that go wrong]

[Optional additional sections as needed — 4–6 H2 sections total is the ideal range]

---

💬 **[One genuine, specific question about the reader's experience with this topic]**
> ✍️ *Written by **TedxHarry***

[LICENSING BLOCK if applicable — see below]

[POWERSHELL BLOCK if applicable — see below]

[RELATED TERMS BLOCK if applicable — see below]

<!-- nav -->

---

[← Previous Term](/[url-encoded-path]/previous-file.md) | [🏠 Contents](/README) | [Next Term →](/[url-encoded-path]/next-file.md)
```

---

### Section Headings

Each H2 (`##`) heading must start with a relevant emoji. Use this keyword-to-emoji mapping:

| Keywords in heading | Emoji to use |
|---|---|
| What is, Definition, Overview, So What | 📌 |
| Why, Purpose, Matters, Problem | 💡 |
| How, Works, Mechanics, Process, Flow, Structure | 🏗️ or 🔄 |
| Types, Kinds, Variants | 📋 |
| Protect, Security, Risk, Attack, Threat | 🔒 or 🛡️ |
| Warning, Mistake, Gotcha, Watch out, Common error | ⚠️ |
| Example, Story, Scenario | 📖 |
| Configure, Setup, Requirements, Prerequisites | ⚙️ |
| Compare, vs, Difference, Not to confuse | ⚖️ |
| TL;DR, Summary, Key Takeaways | 🎯 |
| Quick Reference, PowerShell, Code | 🔧 |
| Real world, Practice, Production | 🏢 |

---

### Difficulty Levels

Choose one based on the topic's complexity:

- **🟢 Beginner** — Core concept, no prerequisites, fundamental to understanding the series
- **🟡 Intermediate** — Assumes familiarity with the basics of the domain; involves configuration or nuanced behavior
- **🔴 Advanced** — Protocol-level, architectural, or requires understanding of multiple prior concepts

---

### TL;DR Rules

- Exactly **3 bullets**
- Each bullet is **one sentence**, max 20 words
- Must be **genuinely useful** — not just "X is a thing that does Y"
- At least one bullet should be a **common mistake, gotcha, or non-obvious fact**
- Use **bold** on the single most important word or phrase in each bullet

---

### Licensing Block (include only if the feature requires paid licensing)

Place this immediately after the `> ✍️ *Written by **TedxHarry***` signature line:

```markdown
> 🔑 **Licensing:** [Plain English statement of what license tier is required and what's available for free. Include specific SKU names: Entra ID Free, P1, P2, Entra ID Governance, Workload Identity Premium, Intune Plan 1, etc.]
```

**Common licensing facts to get right:**
- Conditional Access (beyond Security Defaults) = **P1**
- Risk-based CA (sign-in/user risk conditions) = **P2**
- Identity Protection (risk detections, risky users) = **P2**
- PIM (Privileged Identity Management) = **P2**
- Access Reviews = **P2**
- Entitlement Management / Access Packages = **P2**
- Lifecycle Workflows = **P2** or Entra ID Governance
- Automated app provisioning (gallery apps) = **P1**
- HR-driven inbound provisioning = **P2**
- Administrative Units = **P1**
- Custom roles = **P1** (management via PIM = **P2**)
- Conditional Access for workload identities = **Workload Identity Premium**
- Intune MDM/MAM = **Intune Plan 1** (not included in Entra ID P1/P2 alone)

---

### PowerShell / Graph API Block (include if there's a natural quick reference)

Place after the licensing block (or after the signature if no licensing block):

```markdown
### 🔧 Quick Reference: PowerShell

```powershell
# [Comment explaining what this does]
[Actual working PowerShell command using Microsoft.Graph module]

# [Second command — a complementary or related operation]
[Actual working PowerShell command]
```
```

**Rules:**
- Use the **Microsoft Graph PowerShell SDK** (`Get-Mg*`, `New-Mg*`, `Update-Mg*`) — not the deprecated AzureAD module
- Commands must be **real and runnable** — no made-up cmdlet names
- Include comments (`#`) explaining what each command does
- 2–4 commands per block; keep it focused on the most useful operations for this specific topic
- If Graph REST API is more natural (e.g., for log queries), show the `curl` or `Invoke-MgGraphRequest` form

---

### Related Terms Block (include if the term connects to 2–4 other articles in the series)

```markdown
🔗 **Related Terms:**
- [Glossary#[N.M] - [Term Name]](/[url-encoded-folder]/glossary-[n]-[m]-[slug].md) ([one-clause explanation of the relationship])
- [Glossary#[N.M] - [Term Name]](/[url-encoded-folder]/glossary-[n]-[m]-[slug].md) ([one-clause explanation])
```

**Rules:**
- 2–4 related terms maximum
- Each link must include a parenthetical explaining *why* it's related — not just what the term is
- Use the correct Docsify absolute URL path (starts with `/`, uses `%20` for spaces and `%26` for `&`)

---

### Navigation Links

The nav line at the bottom must use this exact format:

```markdown
[← Previous Term Name](/[url-encoded-folder]/glossary-[n]-[m]-[slug].md) | [🏠 Contents](/README) | [Next Term Name →](/[url-encoded-folder]/glossary-[n]-[m]-[slug].md)
```

**URL encoding rules for folder names:**
- Spaces → `%20`
- `&` → `%26`
- `,` → `%2C`

Examples:
- `1 FOUNDATIONAL CONCEPTS` → `1%20FOUNDATIONAL%20CONCEPTS`
- `4 TOKENS & AUTHORIZATION` → `4%20TOKENS%20%26%20AUTHORIZATION`
- `12 MONITORING, AUDIT & COMPLIANCE` → `12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE`

If the article is the first in the series: `← *Start of series*`
If the article is the last: `*End of series* →`

---

### Content Quality Checklist

Before finalizing any article, verify:

- [ ] Opens with a story or real scenario — not a definition
- [ ] No em dashes anywhere in the article
- [ ] All H2 headings have an emoji from the approved list
- [ ] TL;DR has exactly 3 bullets, each genuinely useful
- [ ] Difficulty badge matches the actual complexity
- [ ] Licensing block is present if the feature requires paid licensing
- [ ] PowerShell block uses real `Get-Mg*` cmdlets (not AzureAD module)
- [ ] Related terms links use correct absolute Docsify paths
- [ ] Nav links at the bottom are correct
- [ ] Signature line `> ✍️ *Written by **TedxHarry***` is present
- [ ] No LinkedIn-style call-to-action in the engagement question (no "follow for more", "like and share", "drop a comment below")
- [ ] Article is self-contained — a reader who arrives directly should understand the topic

---

### Example: What a Finished Article Looks Like

See [`7 SECURITY & RISK MANAGEMENT/glossary-7-8-conditional-access.md`](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-8-conditional-access.md) as the reference example. It demonstrates:
- Opening with an AiTM attack story (not a definition)
- Difficulty badge and TL;DR at the top
- H2 sections each with emoji + clear purpose
- Licensing callout after the signature
- PowerShell quick reference block
- Correct nav link format

---

### Series Context (for Entra ID Glossary)

**Glossary numbering:** `Glossary#[Section].[Number]` — e.g., `Glossary#7.8`

**Sections:**
| # | Section Name | Emoji | Focus |
|---|---|---|---|
| 1 | FOUNDATIONAL CONCEPTS | 🏗️ | What Entra ID is, tenants, cloud vs on-prem |
| 2 | CORE IDENTITY CONCEPTS | 🪪 | Users, groups, service principals, roles |
| 3 | AUTHENTICATION | 🔑 | Sign-in, MFA, passwordless, FIDO2 |
| 4 | TOKENS & AUTHORIZATION | 🎫 | OAuth 2.0, OIDC, SAML, token types (read 4.16 first) |
| 5 | DEVICES & COMPLIANCE | 💻 | Intune, device identity, compliance policies |
| 6 | GOVERNANCE & LIFECYCLE | ♻️ | Provisioning, access reviews, PIM, entitlements |
| 7 | SECURITY & RISK MANAGEMENT | 🛡️ | Conditional Access, Identity Protection, Zero Trust |
| 8 | HYBRID & ON-PREMISES | 🔄 | AD Connect, cloud sync, hybrid auth |
| 9 | INTEGRATION & EXTERNAL IDENTITIES | 🔗 | App integration, B2B, B2C, SCIM |
| 10 | WORKLOAD IDENTITIES & MANAGED IDENTITIES | ⚙️ | Managed identity, workload federation |
| 11 | TOKENS & TECHNICAL DETAILS | 🔬 | Deep-dives into Section 4 topics (read Section 4 first) |
| 12 | MONITORING, AUDIT & COMPLIANCE | 📊 | Audit logs, sign-in logs, security alerts |
| 13 | ADVANCED FEATURES & CONCEPTS | 🚀 | ABAC, admin units, Graph API, cross-tenant |
