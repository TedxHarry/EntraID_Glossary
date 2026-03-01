# Token Revocation: Why "Revoke All Tokens" Doesn't Mean Instant Lockout

**Part of Entra ID Glossary Series: Glossary#11.10 - Token Revocation (Deep Dive)**

---

A user's account was compromised. The security team confirmed it at 2:15 PM and immediately went to Entra ID to revoke all sessions. "Revoke all refresh tokens" button. Clicked. Done.

At 2:48 PM, the security team noticed the attacker was still successfully calling Microsoft Graph with the compromised account. They asked: "We revoked the tokens. Why is access still working?"

The access token hadn't expired yet. Revoking refresh tokens in Entra ID prevents new access tokens from being issued. It doesn't invalidate access tokens that are already in circulation.

Understanding the difference between refresh token revocation and access token revocation, and how CAE changes this picture, is essential for incident response.

## 🔄 Two Different Revocation Problems

Access tokens and refresh tokens have fundamentally different revocation architectures, and the reason is in their design.

**Refresh tokens** are stateful. Entra ID stores information about issued refresh tokens and can check against that store when a refresh token is presented. When you revoke a refresh token, Entra ID marks it in a revocation list. The next time that token is presented at the token endpoint, Entra ID checks the list, finds the revocation, and rejects the request. Effective immediately.

**Access tokens** are stateless JWTs. Entra ID doesn't maintain a database of issued access tokens. When a resource API receives an access token, it validates the signature and the claims locally, without calling back to Entra ID. There's nothing to revoke in a central store because there's no central store.

This is the fundamental tension in JWT-based access token design: stateless tokens are efficient and scalable, but they can't be revoked before they expire without some additional mechanism.

## ⏰ The Standard Revocation Gap

Without CAE, the revocation gap for access tokens is the remaining token lifetime. If an attacker has an access token that expires at 3:00 PM and you revoke the user's refresh tokens at 2:15 PM, the attacker retains access until 3:00 PM. That's up to one hour.

This is a known, documented characteristic of OAuth 2.0 bearer tokens, not a bug. The tradeoff was made deliberately: stateless tokens at scale vs instant revocability. Short token lifetimes (one hour) limit the maximum exposure window.

For most security scenarios, a maximum one-hour gap is acceptable. For high-security scenarios where faster revocation matters, CAE changes the picture.

## ⚡ CAE and Near-Real-Time Revocation

With CAE, the gap between refresh token revocation and effective access loss is measured in seconds to minutes, not hours. When Entra ID revokes a user's refresh tokens (or disables their account, or elevates their risk), it signals to CAE-capable resource providers (Microsoft Graph, SharePoint, Exchange, Teams, Azure ARM) that this user's tokens should be rejected.

The next time the attacker's application presents the access token to a CAE-capable resource, the resource rejects it with a CAE-specific response code. The application sees this response, attempts to get a new access token, discovers the refresh token is revoked, and the authentication chain fails.

For organizations using Microsoft 365 and Azure services (all CAE-capable), "revoke all tokens" in Entra ID effectively stops access within minutes, not hours, for those services.

Non-CAE-capable services still experience the full token lifetime gap.

## 🔑 What "Revoke All Tokens" Actually Does

When an administrator clicks "Revoke all refresh tokens" or "Revoke sessions" in the Entra ID portal (or calls `revokeSignInSessions` via Graph API), Entra ID:

1. Increments the user's `refreshTokensValidFromDateTime` property in the directory
2. Any refresh token issued before this timestamp is now considered revoked
3. CAE-capable resources are notified to reject tokens for this user
4. New token requests using old refresh tokens fail immediately

The access tokens already issued remain technically valid until their `exp` claim, but CAE-capable services reject them in near-real-time.

## 📋 Sign-Out Flows

Sign-out is a different but related problem. When a user signs out of an application, the application clears its local token cache. But the refresh token may still be valid in Entra ID's view, and other applications that share the user's session may still have valid tokens.

**Front-channel logout**: The application initiates sign-out and Entra ID notifies other applications the user has sessions with (by redirecting to their logout URIs). Effective when all applications implement and register their logout URIs.

**Back-channel logout**: Entra ID sends a logout token (a JWT) directly to registered logout endpoints of other applications, without going through the browser. More reliable than front-channel because it doesn't depend on browser redirects completing.

For organizations with multiple integrated applications, implementing proper back-channel logout ensures sign-out from one application propagates to others.

## ⚠️ Incident Response Implications

For a compromised account incident:

1. Disable the user account (immediate: blocks new authentications and CAE-capable services)
2. Revoke all refresh tokens (stops new access token acquisition)
3. For non-CAE services: wait for existing access tokens to expire (up to 1 hour)
4. Review audit and sign-in logs for what the attacker accessed during the gap

Disabling the account is faster than revoking tokens for stopping access to CAE-capable services, because account disabled state is also a CAE revocation event.

---

💬 **Has your organization's incident response playbook accounted for the access token revocation gap?** The gap between "we revoked the tokens" and "access actually stopped" surprises most teams the first time they encounter it in a real incident. Does your playbook distinguish between CAE-capable and non-CAE-capable services in the revocation workflow?

#EntraID #TokenRevocation #CAE #IncidentResponse #OAuth2 #MicrosoftEntra #IdentitySecurity
<!-- nav -->

---

[← Token Lifetime: The Configuration Behind How Long Your Tokens Last](glossary-11-9-token-lifetime-deep-dive.md) | [Home](../README.md) | [Audience: The Token Claim That Prevents One API's Token From Working on Another →](glossary-11-11-audience-deep-dive.md)
