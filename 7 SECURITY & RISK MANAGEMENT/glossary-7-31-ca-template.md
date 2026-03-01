# CA Template: Microsoft's Starting Points for Conditional Access

**Part of Entra ID Glossary Series: Glossary#7.31 - CA Template**

---

An organization wanted to implement Conditional Access but didn't know where to start. Their tenant was empty of policies. Every time they sat down to design policies, the conversation turned into a two-hour debate about scope, exclusions, and whether to require compliant device for the warehouse team.

They discovered CA Templates: pre-built policy configurations covering the most common security scenarios. They deployed five templates in report-only mode in under an hour, reviewed the results for two weeks, and had a working baseline by the end of the month.

The debate didn't disappear. But the starting point was no longer a blank screen.

## 📋 What CA Templates Are

Conditional Access Templates are pre-built policy configurations provided by Microsoft in the Entra admin center. They're not deployed automatically. They're a library of recommended configurations for common security scenarios that you can review, modify, and deploy.

Templates are found in the Entra admin center under Security > Conditional Access > Policies > New policy from template (or the Template gallery button).

Each template represents a specific security scenario: blocking legacy authentication, requiring MFA for administrators, requiring compliant devices for specific resource types. They're based on Microsoft's security recommendations and the patterns observed across the Microsoft 365 customer base.

## 🏗️ The Template Categories

**Securing administrator accounts** 👑:

- Require MFA for administrators: All users holding directory roles (Global Admin, Exchange Admin, etc.) must complete MFA for every sign-in. No exceptions by location or device.
- Require phishing-resistant MFA for administrators: Stronger version requiring FIDO2 or Windows Hello instead of any MFA method.
- Require password change for high-risk admins: When a user in an admin role has high user risk, require password reset before access.

**Securing all users** 👥:

- Require MFA for all users: The baseline. Every user, every app, every sign-in requires MFA. This is the starting point for any organization that doesn't have MFA deployed.
- Block legacy authentication: Block all sign-ins using protocols that don't support modern auth (SMTP, POP, IMAP, basic auth). The most impactful single policy for reducing credential stuffing risk.
- Require MFA for Azure management: Require MFA specifically for Azure portal, Azure CLI, and Azure PowerShell access. Azure management has significant blast radius if compromised.
- Sign-in risk policy: If sign-in risk is high, require MFA or block. If medium, require MFA.
- User risk policy: If user risk is high, require password change.

**Securing device access** 💻:

- Require compliant device or MFA for all users: Either a compliant device or completed MFA satisfies the policy. Transitions users toward device compliance without immediately blocking those without managed devices.
- Require compliant device for administrators: Administrators must sign in from compliant managed devices. Higher bar than MFA alone.

**Protecting sensitive resources** 🔒:

- Require MFA for Azure management (variation with device compliance).
- Block access from specific countries.
- Require terms of use acceptance.

## 🔧 How to Use Templates Effectively

Templates are starting points, not finished configurations. The right workflow:

**Step 1: Review before deploying** 📖: Each template has a description, the assignments, conditions, and grant controls pre-configured. Read through it. Understand what it does and who it affects.

**Step 2: Deploy in report-only** 📊: Never deploy a template directly to enforcement without testing. Unexpected scope is common: service accounts caught by "all users" policies, devices that don't meet compliance requirements you didn't know about, legacy auth applications you forgot existed.

**Step 3: Customize to your environment** 🔧: Templates use "All users" as the default assignment. In your environment, you likely need to exclude emergency access accounts, specific service accounts, or specific groups. Add those exclusions.

**Step 4: Review results** 🔍: Two to four weeks in report-only reveals the real impact. Review the sign-in logs for what would have been blocked or stepped up.

**Step 5: Enforce** ✅: Switch to enforcement when the report-only results are understood and exclusions are configured.

## ⚠️ Template Limitations

Templates are generic. Your environment is specific. Common gaps:

**Service account coverage**: Templates target "All users" but service accounts often need separate handling. A template may catch service accounts in ways that break automated processes.

**Emergency access exclusion**: Templates don't automatically exclude your break-glass accounts. Always add those exclusions manually.

**Licensing requirements**: Some templates (risk-based policies) require Entra ID P2. Deploying a P2 template in a P1-only environment doesn't generate an error immediately, but the risk conditions won't evaluate correctly.

**Hybrid environment considerations**: Templates designed for cloud-only or modern auth environments may interact unexpectedly with on-premises systems, pass-through authentication, or legacy hybrid configurations.

Templates reduce the activation energy for getting started. They don't replace understanding what your policies do.

---

💬 **Did your organization use CA Templates as a starting point for your Conditional Access deployment, or did you build from scratch?** The template approach accelerates getting to a functional baseline, but the organizations that built from scratch often have cleaner, more intentional policy sets. What approach did you take and what would you do differently?

#EntraID #ConditionalAccess #CATemplates #MicrosoftEntra #ZeroTrust #SecurityBaseline #IdentitySecurity
