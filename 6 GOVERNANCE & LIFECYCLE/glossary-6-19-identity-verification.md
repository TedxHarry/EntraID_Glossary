# Identity Verification
*Confirming the Person Behind the Account*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.19 - Identity Verification

---


A new employee called the help desk on their first day. They needed a Temporary Access Pass to set up their phone for MFA. Standard request. The help desk asked them to confirm their employee ID and start date to verify they were who they claimed to be.

The employee provided both correctly. The TAP was issued.

Later, a review found that the same employee ID had been used in a phishing attempt the week before. Someone had obtained the employee ID from a LinkedIn post the new hire made announcing their start date. The "verification" was two pieces of information that were publicly available.

That's the gap identity verification tries to close: the difference between checking that someone knows the right answers and confirming they are actually who they claim to be.

## 🪪 What identity verification means

Identity verification is the process of confirming that a digital identity corresponds to a real, specific person in the way claimed. Authentication verifies credentials. Identity verification goes further: it validates that the person presenting those credentials is actually the person the account represents.

This distinction matters most at specific high-stakes moments:

**Account creation**: Before creating an account for someone, verify they're a legitimate member of the organization who should have an account.

**Privilege elevation**: Before granting someone elevated access (a new admin role, access to sensitive data), verify they're the right person with the right authorization.

**Account recovery**: Before resetting credentials for someone who claims to be locked out, verify they're the legitimate account owner and not an attacker attempting to take over the account.

**Guest invitation**: Before granting a partner or vendor access to organizational resources, verify their identity matches their claimed affiliation.

## 🔐 Microsoft entra verified ID

Microsoft Entra Verified ID is a decentralized identity solution that enables organizations to issue and verify cryptographically signed digital credentials.

The model works like this:

1. A trusted issuer (a university, employer, government agency, or identity verification service) issues a digital credential to a person, cryptographically signed and stored in their Microsoft Authenticator wallet
2. When verification is needed, the person presents their credential
3. The verifier checks the cryptographic signature, confirming the credential was issued by the trusted issuer and hasn't been tampered with

A university credential proves the holder has a degree from that institution. An employer credential proves employment status. A government-backed ID credential proves identity at a high assurance level.

The credential stays with the person. It's not stored centrally by the verifier. The privacy model is person-held: the individual controls when and to whom they present their credentials.

## 📋 Identity verification use cases in Entra ID

**High-assurance access provisioning** 🔒: Before an employee is granted access to systems handling financial data, sensitive IP, or regulated information, require them to complete an identity verification step confirming they are who the HR record says they are.

**Account recovery with high assurance** 🔑: Rather than verifying identity via knowledge questions (employee ID, start date) that can be researched, require presentation of a verified credential for account recovery. Significantly harder for an attacker to impersonate.

**Guest user verification** 👤: Before a partner organization's employee is granted access, require them to present a credential issued by their employer. Proves they actually work where they claim, not just that they have an email address at the domain.

**Helpdesk verification** 📞: When a user calls for support requiring sensitive account changes, the helpdesk can request a verified credential presentation via Authenticator before proceeding, rather than relying on knowledge-based verification.

## ⚠️ The weak verification problem

Most organizations use weak identity verification by default because it's convenient:

- Knowledge questions (employee ID, date of birth, manager's name): Discoverable via OSINT, phishing, or social engineering
- Video calls: Sufficient for common cases but vulnerable to deepfakes as the technology improves
- Email-based verification: Only proves access to the email, not identity

The risk tolerance for weak verification depends on what's being verified. For a general password reset, knowledge-based verification may be acceptable. For granting permanent Global Administrator access, it should not be.

## 💡 Matching verification strength to access sensitivity

Verification requirements should scale with what the verified identity will access:

- Standard employee access: HR confirmation + first-day in-person presence
- Sensitive data access: Verified credential or in-person identity verification with documentation
- Privileged admin access: Verified ID credential + separate approval chain
- Account recovery (standard): Knowledge verification + manager confirmation
- Account recovery (privileged account): In-person verification with documentation, separate approver sign-off

---

💬 **What does your organization use to verify someone's identity before granting access or recovering an account?** The gap between "we ask them their employee ID" and "we require cryptographic proof of identity" is wide, and most organizations are closer to the former. What's the highest-assurance verification step you currently use?
✍️ TedxHarry

<!-- nav -->

---

[← Source of Authority](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-18-source-of-authority.md) | [🏠 Contents](/README) | [Emergency Access →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-20-emergency-access.md)
