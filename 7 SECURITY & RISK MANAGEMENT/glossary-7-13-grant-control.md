# Grant Control
*The Access Decision in Conditional Access*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #7.13 - Grant Control

---

## 🎯 TL;DR

- Grant controls are the actions enforced when a CA policy matches: Block, Require MFA, Require compliant device
- Multiple grant controls can combine with AND (all required) or OR (any one sufficient)
- Require compliant device is stronger than Require MFA : it's harder for attackers to satisfy


A security architect described their Conditional Access design philosophy in one sentence: "The assignment tells us who. The condition tells us when. The grant control tells us what we're going to do about it."

That's the right mental model. You can have the most sophisticated assignment targeting and the most nuanced condition logic in your tenant, and none of it matters if the grant control is misconfigured. The grant control is the actual access decision. Everything else is setup.

## 🔑 What grant controls do

When a Conditional Access policy fires (assignment matches, conditions evaluate), the grant control determines one of two outcomes:

**Block access** 🚫: The request is denied entirely. The user cannot proceed regardless of what they do.

**Grant access** ✅: Access is allowed, either unconditionally or with specific requirements the user must satisfy to receive the grant.

If the grant is conditional, the user is presented with a requirement. Satisfy it and access is granted. Fail to satisfy it and access is denied.

## 🛡️ The grant access requirements

When granting access with requirements, these are the options Entra ID supports:

**Require multifactor authentication** 📱: The user must complete an MFA step. The specific MFA method allowed is determined by the authentication methods configured in the tenant, or more specifically by an Authentication Strength policy if one is specified.

**Require authentication strength** 🔐: A more granular version of MFA requirement. Instead of just "any MFA," specify a strength level: MFA (any), Passwordless MFA, or Phishing-resistant MFA. Phishing-resistant MFA includes FIDO2 security keys, Windows Hello for Business, and certificate-based authentication. These methods can't be intercepted by adversary-in-the-middle attacks the way that TOTP codes can.

**Require device to be marked as compliant** 💻: The device must be enrolled in Intune and must meet all compliance policy requirements (encryption, OS version, antivirus, etc.). This requires Intune deployment. It's the control that breaks AiTM token theft attacks because the attacker's device isn't enrolled or compliant.

**Require hybrid Azure AD joined device** 🖥️: The device must be joined to both on-premises Active Directory and Entra ID. Different from compliant device. A hybrid joined device is in the right structure but isn't necessarily compliant. Compliant is generally the stronger requirement because it validates device health, not just device structure.

**Require approved client app** 📲: Access must come through an application on Microsoft's approved app list. This forces mobile access through managed apps like Outlook mobile rather than any browser, enabling app protection policies to apply.

**Require app protection policy** 🛡️: The client application must have an Intune App Protection Policy applied. This is the MAM-without-enrollment control for BYOD scenarios. The device isn't managed, but the app is.

**Require password change** 🔄: The user must set a new password before access is granted. Used in user risk policies when credentials may be compromised. MFA confirmation isn't enough; the credential itself needs to change.

**Require compliant network** 🌐: Access must come through a network that's been verified as compliant (using Global Secure Access network verification). A newer control for organizations using Microsoft's Security Service Edge.

## 🔗 Combining requirements

When multiple requirements are specified, the combination mode determines the logic:

**Require all selected controls** (AND): Every specified requirement must be satisfied. "Require MFA AND require compliant device" means the user must complete MFA and must be on a compliant device. Failure on either blocks access. This is the strictest combination.

**Require one of the selected controls** (OR): Satisfying any one requirement is sufficient. "Require compliant device OR require MFA" means a user on a compliant device can skip MFA. A user without a compliant device must complete MFA. This gives flexibility, particularly useful during device compliance rollouts.

The AND vs OR choice significantly affects user experience and security. AND is more secure and more disruptive. OR provides a step-up path.

## 🎯 Matching grant controls to scenarios

**High-sensitivity resources** 🔴: Require MFA + Require compliant device (AND). Both requirements must be met. Forces both identity verification and device health validation.

**Risk-based step-up** 🟠: Sign-in risk medium + Require MFA. The MFA step confirms the legitimate user is present during a suspicious sign-in. Low friction for legitimate users. Blocks automated attacks.

**Privileged access** 👑: Require phishing-resistant MFA + Require compliant device. Administrators accessing sensitive systems need stronger authentication than TOTP codes allow.

**BYOD mobile access** 📱: Require app protection policy. The device isn't managed, but the app containing corporate data is.

**User risk remediation** 🔑: User risk high + Require password change. The compromised credential must be replaced, not just confirmed.

**Unknown/unmanaged devices** 🚫: Device filter for non-compliant + Block access (for sensitive apps). Or apply session controls (read-only, no downloads) for lower-sensitivity apps.

## ⚠️ The grant vs session control distinction

Grant controls determine whether access is granted. Session controls apply after access is granted to constrain what happens within the session.

A session control that limits sign-in frequency to 1 hour doesn't block the initial access. It requires re-authentication after the session expires. Session controls are the right mechanism for enforcing ongoing verification within a session. Grant controls are the right mechanism for the initial access decision.

Using grant controls when session controls are the right tool (and vice versa) is a common misconfiguration.

---

💬 **What combination of grant controls do you use for your most sensitive resources?** The "require MFA AND require compliant device" combination is a significant maturity step. Organizations that have it in place for admin portals and high-value data often note that the device compliance requirement was harder to implement than the MFA requirement. What was your experience?
✍️ TedxHarry

<!-- nav -->

---

[← Condition](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-12-condition.md) | [🏠 Contents](/README) | [Block Access →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-14-block-access.md)
