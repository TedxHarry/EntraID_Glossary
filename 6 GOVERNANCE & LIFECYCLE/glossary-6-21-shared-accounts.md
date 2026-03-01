# Shared Accounts
*Why "We All Use the Same Login" Is a Security Problem*

**Part of Entra ID Glossary Series: Glossary#6.21 - Shared Accounts**

---

A manufacturing company had a shared admin account for their SCADA system. Username: `scada_admin`. Password: known to 14 people in three shifts. When a configuration change caused a production line to stop, the investigation needed to answer: who made the change?

The audit log showed `scada_admin` made the change. That narrowed it to 14 people. It did not narrow it further.

The investigation took three weeks to resolve through indirect evidence. It would have taken 15 minutes with individual accounts.

## ⚠️ What's Wrong with Shared Accounts

Shared accounts are accounts where the same credentials are used by multiple different people. One username. One password. Multiple users.

The problems are structural, not just policy violations:

**No accountability** 📋: Audit logs record the account identifier, not the person. Every action logged under `shared_account@contoso.com` is attributed to the account, not to any individual. Investigations become exercises in indirect evidence. Compliance auditors reject audit trails that can't attribute actions to individuals.

**No individual revocation** 🔑: When one person's access should be removed (employee leaves, role changes), the only option with a shared account is changing the password and redistributing it to everyone who should still have access. This is operationally disruptive and frequently doesn't happen promptly.

**MFA is impractical** 📱: MFA requires something the individual has. A shared account can't have individual MFA. The workarounds (a shared phone, a shared TOTP app on a shelf) reduce MFA to theater. Or MFA gets disabled on the shared account entirely.

**Password hygiene fails** 🔒: When 14 people know a password, it's no longer a secret. It gets written down, shared via chat, included in scripts, emailed. The password's confidentiality is exactly as strong as the least careful person who knows it.

**Conditional Access can't protect it properly** 🚫: Policies based on user attributes, device compliance, or risk level can't apply meaningfully when the same account is used from 14 different devices and locations.

## 🔄 Why People Think They Need Shared Accounts

The reasons organizations create shared accounts are usually legitimate operational needs that have better solutions:

**"The application only supports one admin account"** → Most modern applications support multiple admin users. If the application truly doesn't, that's a vendor conversation about a security requirement. Service accounts (individual accounts for the application's automated access) are not the same as shared human accounts.

**"Multiple people need to use the same inbox"** → Shared mailboxes in Microsoft 365 allow multiple users to access a single mailbox with their own individual accounts. Each person authenticates with their own identity and the mailbox access is delegated. Full audit trail preserved.

**"We need a generic account for kiosk/shared workstation use"** → Entra ID supports kiosk mode configurations where a shared device has a specific, purpose-limited account. The device is locked down to specific applications. The account isn't used by different people for different things; it runs a specific, constrained workflow.

**"We share an account for the vendor portal"** → This is the hardest case. Vendor portals with no individual account capability are common. The best options: push the vendor to support individual accounts, use a privileged access management tool to control who checks out the credential and when, or accept the audit limitation while documenting the business constraint.

## 🔧 The Service Account Alternative

When an application needs to authenticate to another system without a user being present, that's a workload identity scenario, not a shared human account scenario.

Service accounts (individual accounts created for a specific application or process) or managed identities (Azure-managed credentials with no password to steal) are the right model. They have individual identity in audit logs, can be given the minimum permissions they need, and can be revoked without affecting other users.

## 💡 Migrating Away from Shared Accounts

For existing shared accounts that can't be immediately eliminated:

- Audit who knows the current credential and who actually needs access
- Implement a privileged access management (PAM) tool to control credential checkout with individual accountability at the checkout level
- Document the business case for the shared account in your exception register
- Set a review date to reassess when the technical constraint can be addressed

The goal isn't perfection overnight. It's moving toward individual accountability for every action in every system that matters.

---

💬 **Does your organization still have shared accounts in use anywhere?** The vendor portal shared login is almost universal. The critical infrastructure shared admin account is more concerning. What's your approach to managing the ones that can't be eliminated immediately?
<!-- nav -->

---

[← Emergency Access](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-20-emergency-access.md) | [🏠 Contents](/README) | [Account Lockout →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-22-account-lockout.md)
