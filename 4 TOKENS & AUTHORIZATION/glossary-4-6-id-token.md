# The ID Token: Proof of Who Signed In (Not a Key to the API)

**Part of Entra ID Glossary Series: Glossary#4.6 - ID Token**

---

I reviewed a developer's application code once and noticed they were calling Microsoft Graph like this: passing the ID token in the Authorization header where the access token should go. The API was returning 401 Unauthorized. The developer was confused because the user had clearly signed in successfully and the token was right there.

The token was wrong. Not invalid, wrong. An ID token is for your application to know who signed in. It's not a credential you present to an API. Those are two different jobs, handled by two different tokens.

## 🪪 What the ID Token Is

The ID token is a JWT issued by Entra ID specifically to tell your application who just authenticated. It's defined by the OpenID Connect protocol (the authentication layer built on top of OAuth 2.0), and it answers one question: who is this user?

Your application receives an ID token after a successful sign-in when the `openid` scope was included in the request. Your application reads it. That's the end of the ID token's journey. It doesn't leave your application to be presented to anyone else.

## 📋 What's Inside an ID Token

ID tokens carry identity claims about the authenticated user:

**sub** 🔑 (Subject)
A unique identifier for the user within this application. Important: the `sub` claim is unique per user per application. The same user signing into two different applications gets a different `sub` in each. Don't use `sub` as a universal user identifier across services.

**oid** 🆔 (Object ID)
The user's Object ID in Entra ID. This one is consistent across all applications in the tenant. If you need to correlate a user across multiple applications, or store user data that persists across sign-ins, use `oid`.

**iss** 🏛️ (Issuer)
Which Entra ID tenant issued the token. Your application should verify this matches the expected issuer before trusting the token.

**aud** 🎯 (Audience)
Your application's client ID. Your application should verify the audience matches its own client ID. An ID token with a different audience wasn't issued for you and shouldn't be trusted.

**exp and iat** ⏱️
Expiry and issued-at timestamps. Your application should validate that the token hasn't expired.

**nonce** 🔁
The value you sent in the authorization request. Your application should verify it matches. This prevents an attacker from taking an ID token from one session and replaying it in another.

**email** 📧
The user's email address. May not always be present depending on scopes and Entra ID configuration.

**name** 👤
Display name. Good for "Hello, Alex" in your UI.

**preferred_username** 📝
The user's UPN or email used for sign-in. Can change if the user's UPN changes, so not suitable as a database key.

## 🔄 ID Token vs Access Token: The Essential Distinction

This comparison clears up most of the confusion:

| | ID Token | Access Token |
|---|---|---|
| Purpose | Authentication (who signed in) | Authorization (what the app can do) |
| Audience | Your application | The target API |
| Who reads it | Your application | The resource server (API) |
| Claims focus | User identity | Permissions and scopes |
| Pass to APIs | ❌ Never | ✅ Always |
| Protocol | OpenID Connect | OAuth 2.0 |

The ID token is your application's proof that authentication happened and confirmation of who the user is. Your app reads it once, validates it, extracts the identity information it needs (usually `oid`, `name`, `email`), and then discards or stores it locally.

The access token is the credential your application presents to APIs. It's issued for a specific resource (Microsoft Graph, your own API, etc.) and proves the application has been granted permission to perform specific actions.

Sending an ID token to an API is like showing a venue your concert ticket stub after the show to get backstage. The stub proves you attended; it doesn't grant further access. The backstage pass (access token) does that job.

## 🔒 Validating ID Tokens Properly

Your application must validate the ID token before trusting its contents:

- ✅ Verify the signature using Entra ID's published public keys (from the JWKS URI)
- ✅ Check that `iss` matches the expected issuer for your tenant
- ✅ Check that `aud` matches your application's client ID
- ✅ Check that the current time is before `exp`
- ✅ Verify the `nonce` matches what you sent (prevents replay attacks)

In practice, use a well-maintained OAuth/OIDC library for your platform rather than implementing validation manually. Microsoft provides MSAL (Microsoft Authentication Library) for most major platforms, and it handles token validation correctly. Rolling your own validation logic is a reliable way to introduce subtle security bugs.

💡 If you're using ASP.NET Core, the `Microsoft.Identity.Web` package handles all ID token validation automatically when you call `AddMicrosoftIdentityWebApp`. You configure it with your tenant and client ID, and the library does the rest.

---

💬 **Have you come across code that confused ID tokens with access tokens?** It's one of the most common OAuth implementation mistakes and usually surfaces as mysterious 401 errors from APIs that worked fine during development. What was the context when you spotted it?

#EntraID #IDToken #OpenIDConnect #OAuth2 #AppDevelopment #MicrosoftEntra #CloudSecurity
<!-- nav -->

---

[← Access Tokens: What's Actually Inside That Long String](glossary-4-5-access-token.md) | [Home](../README.md) | [Refresh Tokens: What "Keep Me Signed In" Is Actually Doing →](glossary-4-7-refresh-token.md)
