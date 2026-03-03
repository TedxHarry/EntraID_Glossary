# Token Revocation
*Why "I Disabled Their Account" Isn't Always Enough*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #4.10 - Token Revocation

---


An IT manager called me forty minutes after she'd disabled an employee's account. The employee had been let go that morning under difficult circumstances, and the manager wanted to confirm their access was completely cut off. She'd disabled the account in Entra ID and revoked all sign-in sessions.

"They're blocked from signing in, right?"

"Yes," I said. "Signing in new sessions is blocked immediately."

"And Teams? SharePoint? Their email?"

There was a pause where I had to explain something that feels wrong on first hearing: for applications without CAE support, a user with a valid access token can continue accessing those resources until the token expires, even after account disablement. Depending on when they last authenticated, that could be up to 60 minutes.

That conversation is why understanding token revocation properly matters.

## 🔑 The two things you can revoke

**Refresh tokens** can be revoked immediately and completely. When you revoke sign-in sessions, you're invalidating all refresh tokens for that user. The result: the user cannot get new access tokens silently. At the next refresh attempt, the request fails with `invalid_grant`. If the app handles this correctly, it redirects to a sign-in page. The user can't sign in because the account is disabled.

**Access tokens cannot be revoked directly.** They're self-contained, cryptographically signed credentials with an expiry time. Resource servers validate them offline using Entra ID's public keys. There's no real-time revocation check in the baseline token model. A valid access token stays valid until `exp` is reached, regardless of what happens to the user account after issuance.

The gap between "revoke sessions" and "all access gone" is the access token lifetime: up to 60 minutes by default.

## 🚀 How to revoke sessions

Two ways to immediately revoke all refresh tokens for a user:

**Entra admin center:** Navigate to the user's profile, select Revoke sessions. All refresh tokens are invalidated within seconds.

**PowerShell / Graph API:**
```powershell
Revoke-MgUserSignInSession -UserId "user@contoso.com"
```
Or via the Graph API:
```
POST https://graph.microsoft.com/v1.0/users/{userId}/revokeSignInSessions
```

Do this in addition to disabling the account. Disabling alone prevents new authentications. Revoking sessions invalidates existing refresh tokens so the user can't silently refresh access tokens.

For high-risk terminations, also reset the password as a belt-and-suspenders measure, in case the user has stored their credentials somewhere that could be used before the disable takes effect globally.

## ⚡ CAE: near-real-time access token revocation

Continuous Access Evaluation closes the access token gap for supported services.

With CAE enabled (and it's on by default for Microsoft's own services), Entra ID can push critical events to capable resource servers in near-real-time. When you disable a user account or revoke sessions, Entra ID sends a notification to CAE-capable services: Exchange Online, SharePoint Online, Microsoft Teams, and Microsoft Graph.

Those services respond by rejecting existing access tokens for that user immediately, without waiting for natural expiry. The user's active Teams session gets disconnected. Their Exchange access stops. Their SharePoint access stops. All within seconds of the revocation action.

The key qualifier: **CAE-capable services only.** Third-party applications, older Microsoft services, and custom applications that haven't implemented CAE support don't receive these push notifications. For those, the 60-minute window remains.

## 🏃 The urgent offboarding checklist

For a high-priority account termination where immediate access removal matters:

- ✅ Disable the account in Entra ID (blocks new sign-ins immediately)
- ✅ Revoke sign-in sessions (invalidates all refresh tokens)
- ✅ Reset the password (removes any stored credentials)
- ✅ Remove role and group assignments (reduces what any lingering token can access)
- ✅ Revoke any app-specific sessions (some apps like SharePoint have their own session management)
- ✅ Check for active PIM role activations and deactivate them
- ✅ Review recently accessed resources in audit logs

For CAE-capable services, access stops in seconds after steps 1 and 2. For non-CAE applications, the exposure window is the remaining access token lifetime, reduced by removing group memberships and app role assignments which limits what the token can do even if it's technically still valid.

## 💡 Reducing the window before it matters

The best time to think about revocation is before an incident, not during one.

Short Conditional Access sign-in frequency policies reduce the exposure window for sensitive applications. A policy requiring re-authentication every 4 hours means a revoked user's access token is at most 60 minutes old, and their last authentication was at most 4 hours ago. For your most sensitive apps, that boundary matters.

CAE implementation in custom applications eliminates the window entirely for those apps. It requires development work, but for applications processing sensitive data or high-privilege actions, it's the right investment.

---

💬 **Have you had a situation where you needed to cut off access immediately and discovered the 60-minute gap?** It's the kind of thing that's easy to overlook until urgency makes it very real. How did your organization handle it, and did it change how you configured token lifetimes or Conditional Access afterward?
✍️ TedxHarry

<!-- nav -->

---

[← Token Lifetime](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-9-token-lifetime.md) | [🏠 Contents](/README) | [Scope →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-11-scope.md)
