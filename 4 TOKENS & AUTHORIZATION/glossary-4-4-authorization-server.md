# The Authorization Server: What Entra ID Is Actually Doing Behind the Scenes

**Part of Entra ID Glossary Series: Glossary#4.4 - Authorization Server**

---

Most people interact with Entra ID through three things: the admin portal, the sign-in page, and whatever PowerShell commands they've memorized. That's fine for day-to-day administration. But it creates a mental model of Entra ID as a user management system with some policy features bolted on.

When you look at Entra ID through the lens of OAuth 2.0, you see something different. You see an authorization server, and understanding what that means explains why Entra ID behaves the way it does across dozens of scenarios that otherwise seem unrelated.

## 🏛️ What an Authorization Server Is

In the OAuth 2.0 specification, the authorization server is the system responsible for authenticating resource owners (users), authorizing client applications (your apps), and issuing tokens. It's the trusted intermediary that sits between applications and the resources they want to access.

Three other roles exist in the OAuth model:

- 👤 **Resource owner:** The user who owns the data and can grant access to it
- 🖥️ **Client:** The application requesting access on the user's behalf
- 🗄️ **Resource server:** The API or service that holds the protected resources (Microsoft Graph, your custom API, SharePoint)

The authorization server is none of these. It's the trusted third party that all of them rely on. Applications don't trust each other directly. They both trust the authorization server, and use tokens it issues as the proof of authorization.

## 🔑 Entra ID's Authorization Server Responsibilities

When Entra ID acts as the authorization server for a sign-in or token request, it's doing a lot of work that happens invisibly:

**Authenticating the user** 🪪
Entra ID verifies the user's credentials against what's stored in the directory, or delegates authentication to a federated identity provider. This includes evaluating MFA requirements and authentication method strength.

**Evaluating Conditional Access** 🛡️
Before issuing any token, Entra ID runs every applicable Conditional Access policy against the current sign-in context. Location, device compliance, risk level, authentication method, and user group membership all get evaluated. A token is only issued if the policies are satisfied or passed.

**Checking consent and permissions** ✅
Entra ID verifies that the requested scopes have been granted. For delegated permissions, it checks user or admin consent. For application permissions, it checks admin consent. Scopes that haven't been consented to are stripped from the token or the request is rejected.

**Issuing and signing tokens** 🎫
Entra ID creates the token, embeds the relevant claims (user identity, permissions, tenant, expiry times), and cryptographically signs the token using its private key. The signature allows any resource server to verify the token was genuinely issued by Entra ID without calling Entra ID to check.

**Publishing public keys** 🔓
Entra ID publishes its public keys at a well-known endpoint (the JWKS URI from the OpenID Connect discovery document). Resource servers fetch these keys and use them to validate token signatures offline, without making a network call to Entra ID for every API request.

## 🌐 The Discovery Document: How Clients Find the Endpoints

Entra ID follows the OpenID Connect standard for publishing its configuration. The discovery document is available at:

```
https://login.microsoftonline.com/{tenant}/.well-known/openid-configuration
```

This JSON document lists the authorization endpoint URL, the token endpoint URL, the JWKS URI for public keys, the supported grant types, the supported scopes, and much more. Well-behaved OAuth clients fetch this document and configure themselves from it automatically, rather than having hardcoded endpoint URLs.

If you ever need to find the exact token endpoint or check what Entra ID supports for a given tenant, this is where to look.

## 🤝 Multi-Tenant: The Authorization Server at Scale

One of the things that makes Entra ID's authorization server model interesting is multi-tenancy. A single application registration in one tenant can serve users from thousands of different tenants, because every Entra ID tenant runs the same authorization server infrastructure.

When a user from `contoso.com` signs in to a multi-tenant app registered in `fabrikam.com`, the authorization server for `contoso.com` authenticates the user and issues tokens. The app registered in `fabrikam.com` receives a token from the `contoso.com` authorization server and validates it against `contoso.com`'s published public keys.

This works because all Entra ID tenants follow the same protocol, publish their keys in the same format, and produce tokens with the same structure. The application doesn't need to know about `contoso.com` in advance. It just needs to know how to validate a standard Entra ID token.

## 💡 Why This Mental Model Matters

Once you see Entra ID as an authorization server rather than just a user directory, a lot of things make more sense:

- Why tokens have expiry times (authorization decisions should be re-evaluated periodically)
- Why Conditional Access can block a token even if the user's credentials are correct (the authorization server decides what conditions must be met, not just whether the password matches)
- Why apps need to be registered (the authorization server needs to know which clients are legitimate)
- Why admin consent exists (the resource owner can't always consent to their own data being accessed by high-privilege apps)

The authorization server is the trust anchor. Everything else is built on top of it.

---

💬 **How has thinking about Entra ID as an authorization server (rather than just a user directory) changed how you approach identity architecture?** Or are you still mostly thinking in terms of "user accounts and permissions"? Both are valid starting points. The OAuth lens tends to become useful when you start integrating custom applications.
<!-- nav -->

---

[← The Token Endpoint: The Server-Side Half Nobody Talks About](glossary-4-3-token-endpoint.md) | [Home](../README.md) | [Access Tokens: What's Actually Inside That Long String →](glossary-4-5-access-token.md)
