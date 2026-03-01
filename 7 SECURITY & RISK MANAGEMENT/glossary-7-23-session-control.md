# Session Control: Governing What Happens After Access Is Granted

**Part of Entra ID Glossary Series: Glossary#7.23 - Session Control**

---

A healthcare organization needed to allow access to patient records from personal devices. Their nurses worked across multiple facilities and sometimes needed to access records on their own phones during shifts.

They couldn't block personal devices: the legitimate use case was real. They couldn't allow unrestricted access: patient records on personal phones with no management controls was a data risk.

Session controls gave them a middle path. Personal devices got access to the records application, but the session was constrained: no download, no print, read-only. The nurse could view what they needed. The records couldn't leave the controlled environment.

## 🔒 What Session Controls Are

Session controls are Conditional Access settings that apply constraints to a session after access has been granted. Where grant controls determine whether access is allowed and under what initial requirements, session controls govern what happens within the granted session.

The distinction matters: a user can satisfy all grant requirements (MFA, compliant device) and still be subject to session constraints. Session controls operate after the grant decision.

They answer the question: "We've decided to allow this user in. What limits should apply to what they can do?"

## ⏱️ Sign-In Frequency

Sign-in frequency controls how long a user's session remains valid before they're required to re-authenticate.

By default, Entra ID issues refresh tokens with relatively long lifetimes. A user who signs in once can remain signed in for days without re-authenticating. For most scenarios, this is the right balance between security and user experience.

Sign-in frequency overrides this default for specific scenarios:

**Sensitive resources** 🔴: Require re-authentication every 1 or 4 hours for access to high-value applications. If a session token is stolen, it has a shorter validity window.

**Risk-based re-auth** ⚠️: For unmanaged devices or external users, requiring re-authentication every 8 hours balances access with periodic verification.

**Persistent browser sessions** 🖥️: Session controls can also configure whether users see the "Stay signed in?" prompt and whether that option actually creates a long-lived session. For sensitive environments, disable persistent sessions on browser clients.

## 🔏 App-Enforced Restrictions

For applications that support it, session controls can instruct the application to apply restrictions based on the device state. Microsoft 365 applications including Exchange Online, SharePoint Online, and Teams support app-enforced restrictions.

The configuration passes device compliance and management information to the application, which then applies restrictions based on that context:

**Managed and compliant device** ✅: Full access. Download, print, edit, share.

**Managed but non-compliant device** ⚠️: Reduced access. View only, no download, no external sharing.

**Unmanaged device** ❌: Minimal access. Browser-only view, no download, no print, session may be further constrained.

This lets organizations support BYOD access to Microsoft 365 without giving unmanaged devices the same access level as managed ones. The user gets in, but what they can do is proportionate to the device's management state.

## 🛡️ Microsoft Defender for Cloud Apps Session Policies

For organizations with Microsoft Defender for Cloud Apps (MDCA), session controls can route the session through MDCA's cloud app security proxy. This enables real-time session monitoring and control:

**Activity monitoring** 👀: Log all user activity within the application during the session. Downloads, uploads, file access, sharing events.

**Conditional actions** ⚡: Block specific actions in real time. Allow viewing but block downloading files above a certain size. Allow access but block uploading files with certain content types. Warn before sharing externally.

**Label-based protection** 🏷️: Apply sensitivity labels or protect content on download. Files downloaded from SharePoint on unmanaged devices get encrypted automatically.

MDCA session proxy is a more sophisticated and expensive approach than app-enforced restrictions, but it works for third-party SaaS applications that don't natively support Conditional Access session controls.

## 📋 Continuous Access Evaluation as a Session Control

Continuous Access Evaluation (CAE) is a session control that enables near-real-time revocation of access during an active session when critical events occur.

Without CAE, access tokens issued with a one-hour lifetime continue working for that hour even if the user is blocked, the password is changed, or compliance status changes. The token was valid when issued. It remains valid until it expires.

With CAE, participating applications can receive revocation signals from Entra ID and enforce them immediately:

- User account disabled → session revoked in seconds
- Password changed → session revoked in seconds
- Conditional Access policy changed in a way that would now block the user → session revoked

CAE shifts the security model from "tokens expire eventually" to "tokens are revoked when conditions change." For high-value resources, this is significant.

## 🎯 Matching Session Controls to Scenarios

**Personal device access to M365** 📱: App-enforced restrictions. Allow viewing, disable download and print. User can work, data can't leave the managed environment.

**External user access to SharePoint** 🌍: Sign-in frequency set to 1-4 hours, app-enforced restrictions to read-only. External users get access with tighter constraints than internal users.

**Admin portal access** 👑: Short sign-in frequency (1 hour or less), no persistent sessions. Privileged sessions should require regular re-authentication.

**High-risk unmanaged device** 🚨: MDCA session proxy for monitoring, or app-enforced restrictions for read-only. If risk is high enough, grant control blocks access instead.

---

💬 **Have you used app-enforced restrictions or sign-in frequency controls to enable a use case that would otherwise have been "block it"?** The BYOD scenario where personal devices get read-only access is the classic example. What was the access scenario that session controls made possible without compromising data security?
<!-- nav -->

---

[← Legacy Authentication: The Open Door That MFA Can't Close](glossary-7-22-legacy-authentication.md) | [Home](../README.md) | [Terms of Use: Making Consent Part of the Access Flow →](glossary-7-24-terms-of-use.md)
