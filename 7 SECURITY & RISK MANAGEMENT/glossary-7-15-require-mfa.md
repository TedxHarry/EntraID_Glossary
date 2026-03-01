# Require MFA: The Grant Control That Changed Identity Security

**Part of Entra ID Glossary Series: Glossary#7.15 - Require MFA**

---

A company ran a phishing simulation. They sent a convincing fake email to 400 employees. 67 clicked the link. 23 entered their username and password on the fake login page.

With passwords alone as protection, those 23 accounts would have been compromised. Every one of them.

With MFA required by Conditional Access, none of them were. The attacker had usernames and passwords. They couldn't get past the MFA prompt. The accounts were safe.

That's what "Require MFA" as a Conditional Access grant control actually does in production.

## 🔐 What "Require MFA" Means in Conditional Access

Require MFA is a grant control in a Conditional Access policy. When it fires, the user must successfully complete an MFA challenge in addition to their primary authentication before access is granted.

It's not the same as having MFA "enabled." Many tenants have MFA enabled through legacy per-user MFA settings or security defaults. Those mechanisms are coarser instruments. Conditional Access with Require MFA gives you policy-driven, conditional MFA that responds to context.

The difference matters:

**Legacy per-user MFA**: Every sign-in requires MFA, regardless of context. Simple to set up, no exceptions by device or location.

**Conditional Access Require MFA**: MFA is required when specific conditions are met. The same user on a compliant device from the office might not be required. The same user on an unmanaged device from a hotel definitely is. The policy is contextual.

## 📱 What Satisfies the MFA Requirement

When a Conditional Access policy requires MFA, the user must complete an additional verification factor. The accepted methods depend on what's configured in the tenant's authentication methods:

**Microsoft Authenticator** 🔔: Push notification (approve/deny), number matching (user enters a number shown on screen into the app), or passwordless phone sign-in. The most common MFA method in Microsoft 365 environments.

**TOTP authenticator app** 🔢: Time-based one-time password from any TOTP-compatible authenticator app. 6-digit code that changes every 30 seconds.

**SMS** 📲: One-time code sent to a registered phone number. Weakest MFA option. Vulnerable to SIM swapping. Still far better than no MFA.

**Voice call** 📞: Phone call to a registered number, press a key to approve.

**FIDO2 security key** 🔑: Hardware key that provides phishing-resistant MFA. The strongest option.

**Windows Hello for Business** 🪟: Biometric or PIN-based authentication on Windows devices. Phishing-resistant because the credential never leaves the device.

## 🎯 When to Apply Require MFA

Require MFA shouldn't be a blanket policy applied to everything without thought. The right pattern is matching the MFA requirement to the risk level of the access:

**All users, all apps** 🌐: The baseline. MFA for everything. This is the minimum security posture for any organization that cares about identity security. Reasonable to exempt compliant devices from the office if user experience is a concern.

**Specific high-value apps** 🔐: If you can't enforce MFA everywhere, enforce it for the applications that matter most. Admin portals. Financial systems. HR data. Email.

**Outside trusted locations** 📍: MFA when signing in from outside the corporate network or trusted IP ranges. Users at the office on managed devices skip MFA. Anyone else doesn't.

**Risk-responsive MFA** 🔴: Require MFA when sign-in risk is Medium. Block when it's High. This lets legitimate users who trigger false positives (unusual travel, unfamiliar device) confirm their identity and proceed.

## ⚙️ MFA Registration: The Prerequisite

Require MFA only works if users have MFA methods registered. A policy that requires MFA for a user with no registered methods generates an error: the user is blocked because they can't complete MFA and they can't skip it.

The common failure pattern: Require MFA policy enabled before users have completed MFA registration. Result: users locked out, helpdesk overwhelmed.

The correct sequence:
1. Enable combined MFA and SSPR registration (combined registration)
2. Run a registration campaign to prompt users to register their methods
3. Confirm registration coverage (Entra admin center shows registration status)
4. Enable the Require MFA Conditional Access policy in report-only mode
5. Review who would be affected
6. Switch to enforcement when coverage is sufficient

## ⚠️ The Gaps Require MFA Doesn't Close

Require MFA is powerful but not complete protection:

**AiTM phishing** 🎣: Adversary-in-the-middle attacks proxy the sign-in page. The user completes MFA against the proxy. The proxy passes it to the real sign-in. The session token is captured. MFA was satisfied but the session is stolen. Closing this requires phishing-resistant MFA (FIDO2, Windows Hello) or device compliance requirements.

**MFA fatigue** 📱: Attackers who have the password spam MFA push notifications hoping the user approves one to make it stop. Number matching in Microsoft Authenticator addresses this by requiring the user to enter a specific number shown on screen.

**SIM swapping** 📲: If SMS is the only MFA method, SIM swapping defeats it. Using app-based methods rather than SMS eliminates this vector.

Require MFA raises the bar significantly. It doesn't make an account unbreakable. Layer it with other controls for defense in depth.

---

💬 **When you enabled MFA as a Conditional Access requirement, what was the biggest challenge during rollout?** The MFA registration coverage gap is the most common blocker. Did you encounter users who genuinely couldn't register because of device or connectivity constraints, and how did you handle the exceptions?

#EntraID #MFA #ConditionalAccess #RequireMFA #MicrosoftEntra #IdentitySecurity #Phishing
<!-- nav -->

---

[← Block Access: The Hardest Grant Control to Get Right](glossary-7-14-block-access.md) | [Home](../README.md) | [Require Device Compliance: The Grant Control That Stops Token Theft →](glossary-7-16-require-device-compliance.md)
