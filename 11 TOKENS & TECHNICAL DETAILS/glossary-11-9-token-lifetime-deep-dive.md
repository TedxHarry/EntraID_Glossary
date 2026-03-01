# Token Lifetime (Deep Dive)
*The Configuration Behind How Long Your Tokens Last*

> **Difficulty:** 🔴 Advanced

📚 **Part of Entra ID Glossary Series: Glossary#11.9 - Token Lifetime (Deep Dive)**

---

## 🎯 TL;DR

- Access token lifetime: configurable 5 min – 1 day via Token Lifetime Policy (default 60-75 min)
- Refresh token: 90-day sliding window (resets on each use); inactive for 90 days = expired
- CAE-enabled access tokens: 24-hour lifetime but can be revoked in near-real-time by resource servers


A help desk team was seeing an unusual number of complaints: users getting signed out of a critical application every hour during long working sessions. The application was a custom-built web app integrated with Entra ID. The developer had configured it correctly by the book. Access tokens expire in one hour, the app requested a new one using the refresh token, and it worked.

Except the app wasn't requesting a new token silently. It was redirecting the user to the sign-in page on every expiry. A behavior bug in their token refresh code meant the refresh token was never actually used.

The fix was in the application code, not the token lifetime configuration. But the investigation revealed how little the team understood about the default token lifetimes, which lifetimes were configurable, and which weren't.

## 🎫 ⏰ Default Token Lifetimes

Entra ID issues three types of tokens with distinct default lifetimes:

**Access tokens** 🔑: Default one hour. Non-configurable via Token Lifetime Policy since Microsoft locked this down to prevent organizations from issuing extremely long-lived access tokens for security reasons. The one-hour window is the base; CAE can extend effective validity through long-lived tokens.

**ID tokens** 👤: Default one hour. Same as access tokens. Used for authentication assertions, typically discarded after use in most application flows.

**Refresh tokens** 🔄: Default 90 days, sliding window. Each successful use of a refresh token resets the 90-day clock. If the user is active, the refresh token effectively never expires. If the user is inactive for 90 days without using the application, the refresh token expires and they must sign in again.

**Refresh tokens for FOCI apps** 🔵: Family of Client IDs applications (Microsoft's own apps like Teams, Outlook, Office) share refresh tokens. These have different lifetime characteristics and can provide SSO across the Microsoft app family.

## 🔧 Token Lifetime Policy

While access token lifetime is now locked, other token lifetimes are configurable through Token Lifetime Policy objects. These are Entra ID objects that can be applied to:

**Service principals** 🤖: A Token Lifetime Policy applied to a service principal changes token lifetimes for that specific application's tokens. Useful for high-security applications where shorter refresh token lifetimes are appropriate.

**Organizations (tenant-wide)** 🏢: A policy applied at the organization level sets defaults for all applications that don't have their own policy. Overrides the Entra ID defaults for the entire tenant.

A Token Lifetime Policy object defines configurable parameters including the refresh token max age, the max inactive time (how long a refresh token remains valid when not used), and the multi-factor refresh token max age (the maximum validity for tokens issued after MFA, regardless of activity).

These policies are managed via the Microsoft Graph API or PowerShell. There's no portal UI for token lifetime policies as of now.

## 🔄 The Lifetime UX Tradeoff

Token lifetime is a UX vs security tradeoff that plays out differently for different application types:

**High-security applications** 🔐: Financial systems, HR platforms, privileged admin tools. Shorter refresh token inactive times (30 days or less). Possibly requiring fresh MFA on each access session. Users accept more frequent authentication as part of the security model.

**Everyday productivity applications** 💼: Email, collaboration tools, document management. Longer refresh token lifetimes (90 days). Users expect to stay signed in across sessions without repeated authentication. Frequent sign-out prompts create friction and shadow IT risk.

**Customer-facing applications (external tenants/B2C)** 🛍️: Consumer applications often have even longer session lifetimes. "Remember me" behavior. Sessions measured in months, not days. The security model relies on device security and consumer MFA rather than frequent re-authentication.

## 🌐 Conditional Access and Lifetime Interaction

Conditional Access session controls interact with token lifetimes and can create effective shorter sessions:

**Sign-in frequency** 📋: A Conditional Access session control that requires re-authentication after a specified period, regardless of refresh token validity. If the sign-in frequency is set to 8 hours, users must re-authenticate every 8 hours even if their refresh token is still valid. This is separate from token lifetime policy.

**Persistent browser session** 🔄: Controls whether the "stay signed in" experience is offered. Disabling persistent sessions means the browser session state is cleared when the browser is closed, effectively requiring re-authentication per session even with a valid refresh token.

Sign-in frequency through Conditional Access is often the right lever for security-sensitive scenarios, because it can be scoped to specific applications and user groups without affecting all tokens in the tenant.

## ⚠️ What Can't Be Configured

Access token lifetime cannot be extended beyond one hour through policy (with the exception of CAE-enabled long-lived tokens). Microsoft made this non-configurable to prevent a common mistake where administrators would set very long access token lifetimes for convenience, creating large windows for stolen token abuse.

If an application needs longer than one-hour sessions, the correct implementation is silent refresh token usage, not longer access tokens.

---

💬 **Have you had to configure Token Lifetime Policies for a specific application in your tenant, and what drove the requirement?** The most common drivers are compliance requirements for high-security applications (shorter inactive times) and user experience requirements for productivity applications (avoiding excessive sign-out prompts). What lifetime configuration would most improve your users' experience while meeting your security requirements?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Bearer Token (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-8-bearer-token-deep-dive.md) | [🏠 Contents](/README) | [Token Revocation (Deep Dive) →](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-10-token-revocation-deep-dive.md)
