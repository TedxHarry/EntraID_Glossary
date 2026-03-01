# Refresh Token
*What "Keep Me Signed In" Is Actually Doing*

**Part of Entra ID Glossary Series: Glossary#4.7 - Refresh Token**

---

A user complained to me that she kept getting signed out of Microsoft 365 while working from home, even though she'd ticked "Keep me signed in" every time. Meanwhile her colleague, sitting next to her in the office on the same network, never got signed out. Same application. Same browser. Different experience.

The answer wasn't a bug. It was token lifetime policies and Conditional Access sign-in frequency settings combining in a way that made remote access behave differently from on-premises. Understanding how refresh tokens work was the key to diagnosing it and explaining to her what was happening.

## 🔄 What a Refresh Token Is

When a user signs in and the `offline_access` scope is included in the request, Entra ID issues a refresh token alongside the access token. The refresh token is a long-lived, opaque credential (not a JWT, not readable by anyone) stored by the application.

Its job is simple: when the access token expires, the application presents the refresh token to Entra ID's token endpoint and receives a fresh access token, without requiring the user to sign in again. From the user's perspective, their session continues uninterrupted.

This is the mechanism behind "keep me signed in." It's not that the access token stays valid forever. It's that the application keeps quietly trading in the refresh token for new access tokens as each one expires.

## ⏱️ How Long Refresh Tokens Last

Refresh token lifetime in Entra ID isn't a single fixed value. It's a sliding window with a maximum:

- 🕐 **Inactivity period:** 90 days by default. If the refresh token isn't used within 90 days, it expires. Each successful use resets the 90-day clock.
- 📅 **Maximum lifetime:** By default, no hard maximum for most configurations (though configurable). Some policies set a hard cap.
- 🔧 **Configurable:** Token lifetime policies can adjust these values per application or per the entire tenant.

The practical effect: a user who signs in Monday and uses their laptop daily will typically stay signed in indefinitely (or until something explicitly invalidates the token). A user who goes on a three-month sabbatical will need to sign in again when they return.

Conditional Access sign-in frequency settings can also override the refresh token behavior, requiring users to re-authenticate after a set interval regardless of refresh token status. This is what was causing the remote user's experience: a Conditional Access policy required re-authentication every 8 hours for sign-ins from outside the office network.

## ♻️ Refresh Token Rotation

Some Entra ID flows and configurations use rolling refresh tokens. Each time the application uses a refresh token to get a new access token, Entra ID:

1. Issues a new refresh token
2. Invalidates the old one

This means if a refresh token is stolen and used by an attacker, when the legitimate application tries to use its (now invalidated) refresh token, the request fails. Entra ID detects that a refresh token has been used twice and can revoke the entire session chain as a security response.

The SPAs and mobile apps using the authorization code flow with PKCE get refresh token rotation automatically. This is a meaningful improvement in security posture for long-lived sessions.

## 🚫 When Refresh Tokens Get Invalidated

Refresh tokens don't just expire from age. Several events immediately invalidate them:

- 🔐 **User changes their password:** All refresh tokens for that user are invalidated
- ❌ **Admin revokes all sessions:** `Revoke-MgUserSignInSession` in PowerShell or via the Entra admin center
- 🚫 **Account disabled:** Refresh token exchanges start failing
- 🔒 **Conditional Access policy change:** Policies that now block the user's access
- ⚡ **Suspicious activity detected:** Identity Protection can revoke refresh tokens for risky users

When a refresh token is invalidated, the application's next silent token request fails with `invalid_grant`. If the app is well-written, it handles this gracefully by redirecting the user to sign in interactively. If it's not well-written, the user sees a confusing error.

## 💡 Refresh Tokens and Conditional Access

Here's something that catches people out: Conditional Access policies are re-evaluated when a refresh token is used. It's not enough that the policies were satisfied at initial sign-in.

If a user's device becomes non-compliant after sign-in, the next refresh token exchange will fail the device compliance check. The user gets kicked out, which is the correct security behaviour. It feels surprising from the user's perspective ("but I was just working in this app"), but it's exactly how Zero Trust is supposed to work: every access request is evaluated in context, not just at the door.

---

💬 **Have you had to troubleshoot a "keeps signing me out" complaint?** Nine times out of ten it traces back to either a sign-in frequency Conditional Access policy or a refresh token being invalidated by a policy change, password reset, or admin action. What was the root cause in your experience?
<!-- nav -->

---

[← ID Token](glossary-4-6-id-token.md) | [Home](../README.md) | [Bearer Token →](glossary-4-8-bearer-token.md)
