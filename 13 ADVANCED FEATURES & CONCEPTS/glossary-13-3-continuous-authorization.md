# Continuous Authorization (CAE)
*Shifting From "You Were Trusted" to "You Are Trusted Right Now"*

> **Difficulty:** 🔴 Advanced

📚 **Part of Entra ID Glossary Series: Glossary#13.3 - Continuous Authorization (CAE)**

---

## 🎯 TL;DR

- Continuous Authorization evaluates access decisions continuously throughout a session, not just at sign-in
- CAE is the Microsoft implementation — resource servers receive real-time revocation events from Entra ID
- Without continuous authorization, a signed-in session persists even after account disable or policy change


The traditional authorization model works like a photograph. The authentication happens at sign-in. Access is evaluated at that moment. A token is issued capturing that evaluation. For the next hour, the application trusts that photograph even though the world has moved on.

The user's account might have been disabled. Their role might have changed. A risk event might have been detected. The Conditional Access policy might have been updated. None of it matters to the application holding an hour-old token. The photograph says they were trusted at 9:00 AM. It's 9:45 AM and the photograph is still in effect.

Continuous authorization is the shift from the photograph model to a live video model. Authorization isn't just evaluated at sign-in; it's evaluated continuously for the duration of the session.

## 🔄 The Protocol Behind Continuous Authorization

Continuous Access Evaluation is the implementation of continuous authorization in the Microsoft identity platform. The protocol involves three parties: Entra ID (the authorization server), the CAE-capable resource provider (Microsoft Graph, Exchange, SharePoint, Teams, Azure ARM), and the CAE-capable client application.

The protocol establishes two mechanisms:

**Event-based evaluation** ⚡: Entra ID notifies resource providers when specific events occur for a user or workload: account disabled, password changed, user risk elevated, token revoked, policy changed. The resource provider caches this notification. When the user's client next presents a token to that resource, the provider checks whether a relevant event has occurred since the token was issued. If yes, the token is rejected.

**Claim challenges** 🔑: Instead of silently rejecting a token, the resource provider can issue a claims challenge: a structured response telling the client exactly what changed and what the client needs to do to get a new token. The client processes the challenge, goes back to Entra ID with the challenge included in the new token request, and Entra ID evaluates the current state before issuing a new token.

This is fundamentally different from just letting tokens expire. The resource provider is an active participant in authorization enforcement, not just a passive token validator.

## 📊 What Changes in the Authorization Model

In the static token model, authorization state is captured at token issuance and valid for the token's lifetime. The resource provider trusts the token completely until it expires.

In the continuous authorization model, authorization has two components:

**Token validity** ✅: Standard JWT validation. Signature, expiry, audience, issuer. The token was legitimately issued by Entra ID.

**Current authorization state** 🔄: Has anything changed since this token was issued that should affect access? This is the CAE layer. Token validity alone isn't sufficient; current state must also be valid.

The second component is what "continuous" means. It's not re-authentication at every request (that would be unusable). It's near-real-time enforcement of policy changes and revocation events, checked against a cache of events the resource provider maintains.

## 🔐 Policy Changes and Continuous Authorization

One underappreciated aspect of CAE is that it enforces not just revocation but policy changes.

If a Conditional Access policy is updated during a user's session to require MFA from a new set of users, the old tokens held by those users remain technically valid but the resource provider now has a policy change event. The next time those users' tokens are presented, the provider can issue a claims challenge indicating that the policy now requires a higher authentication strength.

The client receives the challenge, re-authenticates to satisfy the new policy requirement, and gets a new token that includes evidence of the required authentication. Access continues, but it now reflects the current policy state rather than the policy state at the time of the original authentication.

This is what "continuous" means in practice: the authorization decision tracks the current state of the world, not just the state at sign-in.

## ⚙️ Client and Resource Requirements

Continuous authorization requires both ends to support the protocol:

**CAE-capable resources** 🔵: Microsoft Graph, Exchange Online, SharePoint Online, Teams, Azure Resource Manager. These services maintain the event cache and issue claims challenges. Third-party APIs and non-CAE-capable services fall back to standard token expiry.

**CAE-capable clients** 💻: MSAL (all major language versions) supports CAE claim challenges. When a CAE challenge is received, MSAL automatically triggers a new token acquisition that includes the challenge. Applications using current MSAL versions get CAE handling essentially for free.

Older client applications or applications using non-MSAL token handling may not process CAE challenges correctly. These applications fall back to the pre-CAE behavior: token valid until expiry regardless of revocation events.

## ⚠️ Continuous Authorization Is Not Continuous Authentication

The distinction matters for user experience. Continuous authorization doesn't mean users are prompted to authenticate repeatedly. It means the authorization state is continuously evaluated. Most of the time, nothing changes and the user experiences no interruption.

When something does change (account disabled, policy updated, risk elevated), the response is targeted: either silent token refresh with the new state, or a focused authentication step to satisfy the new requirement. Not a full re-login; a specific re-authentication for the specific change that occurred.

---

💬 **Has your organization configured Conditional Access with the expectation that policy changes would take effect immediately for active sessions, and have you verified that CAE is actually enforcing this for the services you care about?** The gap between "we updated the policy" and "active sessions are now subject to it" varies significantly based on which services are involved and whether clients are CAE-capable. What's your process for validating policy change enforcement timing?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Cloud-Based Sync (Advanced)](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-2-cloud-sync-advanced.md) | [🏠 Contents](/README) | [Identity Correlations →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-4-identity-correlations.md)
