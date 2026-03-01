# Conditional Access: The Policy Engine That Makes "Never Trust, Always Verify" Real

**Part of Entra ID Glossary Series: Glossary#7.8 - Conditional Access**

---

A company had MFA deployed. They thought they were protected.

Then they got hit by an AiTM (adversary-in-the-middle) phishing attack. The attacker set up a proxy that sat between the user and the Microsoft sign-in page. The user authenticated, completed MFA, and never realized anything was wrong. The attacker captured the session token and used it from their own device. MFA had been satisfied. The session token was valid. Traditional defenses saw a clean authentication.

Conditional Access with a device compliance requirement would have blocked it. When the attacker tried to use the session token from their unmanaged device, the device compliance check would have failed. No compliant device = no access, regardless of how clean the authentication looked.

MFA alone wasn't enough. Conditional Access is what made the difference.

## 🚦 What Conditional Access Is

Conditional Access is Entra ID's policy engine. It evaluates every access request against a set of conditions and decides whether to grant access, grant access with additional requirements, or block access entirely.

The logic is: **IF these conditions are met, THEN enforce these controls.**

Before Conditional Access, access decisions were binary: authenticated or not. If you had valid credentials and satisfied authentication, you got access. Conditional Access adds a second evaluation layer. Authentication confirms who you are. Conditional Access decides whether the circumstances of this authentication warrant access to this resource.

It's the technical implementation of Zero Trust: don't assume that an authenticated user in the right network location has the right to access everything. Evaluate each request against the conditions of that specific request.

## 🏗️ The Structure of Conditional Access

Every Conditional Access policy has the same structure:

**Assignments** 👥: Who does this policy apply to? Which apps does it apply to? These define the scope. A policy with no assignments does nothing.

**Conditions** 📋: Additional signals evaluated beyond the fact of authentication. Sign-in risk level, user risk level, device platform, device compliance status, location, client application type, authentication strength.

**Grant controls** 🔑: What happens when the assignments match and the conditions are met. Block access. Require MFA. Require compliant device. Require domain-joined device. Combinations of the above.

**Session controls** 🔒: For granted sessions, what constraints apply. Limit session duration. Require continuous access evaluation. Restrict what users can do within the application. Control downloads.

A policy fires when the assignments match (this user, this app) and the conditions are evaluated. The grant control determines the outcome.

## 📋 Why Conditions Matter

The power of Conditional Access comes from conditions. They let policies respond to the context of a request, not just the identity.

A user signing in from a corporate-managed device at the office gets one policy outcome. The same user signing in from a personal phone at a coffee shop from an unfamiliar country gets a different outcome. Same user. Same application. Different context. Different access decision.

This is what distinguishes modern identity-based access control from network perimeter security. The perimeter model assumed that anything inside the network was safe. Conditional Access assumes nothing and evaluates every request on its own merits.

## 🔒 What Conditional Access Protects Against

The AiTM scenario from the opening is illustrative. Conditional Access with device compliance breaks the attack because it evaluates something the attacker can't easily fake: whether the device making the request is managed, enrolled, and compliant with organizational policy.

Other scenarios where Conditional Access provides protection that MFA alone doesn't:

**Stolen credentials**: Conditional Access requiring a compliant device means even if an attacker has username, password, and MFA factor, they can't access resources from their unmanaged device.

**Token theft**: Continuous Access Evaluation (CAE), a session control, enforces revocation in near-real-time when conditions change mid-session. A token stolen and replayed from a different location or after a policy change gets revoked.

**Insider risk**: Risk-based Conditional Access policies respond to behavioral signals. A legitimate user whose account shows high user risk gets stepped up to a password reset requirement, even if their authentication looked clean.

**Geographic access**: Named Locations with country blocking prevents access from jurisdictions where your organization has no presence, reducing the attack surface for credential stuffing.

## ⚙️ What Conditional Access Requires to Work

Conditional Access is not a standalone feature. It evaluates signals that other components generate:

- **Device compliance** requires Intune enrollment and compliance policy
- **Sign-in risk and user risk** require Entra ID P2 licensing and ID Protection
- **Authentication strength** requires configured authentication methods
- **Named Locations** require pre-configured location definitions

A Conditional Access policy that requires compliant device on a tenant where no devices are enrolled in Intune will block everyone. The access control is only as good as the signals feeding into it.

## ⚠️ The "Report-Only" Mode

New Conditional Access policies should be deployed in report-only mode before enforcement. In report-only mode, the policy evaluates every matching sign-in and logs what it would have done, without actually blocking or requiring anything.

This lets administrators see the effect of a policy before it goes live. Unintended scope, unexpected conditions, and misconfigured assignments show up in the report-only logs before they affect production access.

Skipping report-only mode is how organizations accidentally lock themselves out of their own tenant.

---

💬 **What's the most impactful Conditional Access policy your organization has implemented?** Requiring compliant devices is often the one that generates the most initial resistance and the most security value. What was the conversation like when you pushed the policy from report-only to enforcement?

#EntraID #ConditionalAccess #ZeroTrust #MicrosoftEntra #IdentitySecurity #MFA #DeviceCompliance
<!-- nav -->

---

[← Threat Intelligence: Why Entra ID Knows an IP Is Bad Before You Do](glossary-7-7-threat-intelligence.md) | [Home](../README.md) | [CA Policy: Building the If-Then Logic of Access Control →](glossary-7-9-ca-policy.md)
