# OIDC (OpenID Connect)
*The Layer OAuth Was Missing*

**Part of Entra ID Glossary Series: Glossary#4.17 - OIDC (OpenID Connect)**

---

I was explaining OAuth 2.0 to a developer and they stopped me halfway through.

"But how does the app know who the user is? You've described how it gets permission to access things, but where does the identity come from?"

That's exactly the right question. And the answer is OpenID Connect.

OAuth 2.0 handles authorization cleanly but was never designed to tell an application who signed in. OpenID Connect is the protocol layer built on top of OAuth 2.0 that answers that specific question.

## 🔍 What OpenID Connect Adds

OpenID Connect (OIDC) is an identity layer on top of OAuth 2.0. It adds three things:

**The `openid` scope**: Including `openid` in an OAuth authorization request signals that the application wants an identity token alongside authorization. This single scope activates OIDC behavior at the authorization server.

**The ID token**: A JWT returned from the token endpoint. It contains identity claims about the authenticated user: who they are, when they authenticated, what method they used, what tenant they're from. This is the answer to "who signed in?" The ID token is for your application to read. It's not for calling APIs (covered in Glossary#4.6).

**The UserInfo endpoint**: A standardized API endpoint that returns additional identity claims. Some implementations include all needed claims directly in the ID token; others require a call to UserInfo for supplemental attributes like address or phone number.

These three additions transform OAuth's authorization-focused flow into a complete authentication and authorization system. You get both in a single protocol round-trip.

## 📋 The Standard Scopes

OIDC defines standard scope values that correspond to standard categories of identity information:

- `openid` - Required. Triggers ID token issuance. Without this, you're using OAuth without OIDC.
- `profile` - Includes name, family_name, given_name, preferred_username, picture
- `email` - Includes email address and email_verified flag
- `address` - Physical address (rarely used in enterprise scenarios)
- `phone` - Phone number information

When you build an Entra ID application and request `openid profile email`, you're using OIDC. The resulting ID token contains name and email claims alongside the core identity claims. The access token is still issued separately for calling APIs.

## 🔄 OIDC and OAuth Together in Practice

For most applications using Entra ID, you're using both simultaneously without consciously separating them. A single authorization request might look like:

```
scope=openid profile email Mail.Read
```

- `openid profile email` - OIDC scopes: produce an ID token with identity claims
- `Mail.Read` - OAuth scope: produces an access token for Graph mail access

You get an ID token (tells your app who signed in) and an access token (lets your app call Graph). Both from a single authentication flow. Both from the same authorization code exchange at the token endpoint.

## 🏢 OIDC vs SAML: The Modern Default

When integrating an application with Entra ID, you choose a protocol: OIDC or SAML. For new applications, OIDC is the right choice in almost every scenario:

- ✅ Uses JSON and REST (simpler than SAML's XML assertions)
- ✅ Works natively for SPAs, mobile apps, and APIs
- ✅ Supported by MSAL and every current authentication library
- ✅ New features land in OIDC first
- ✅ Much simpler certificate management than SAML

SAML retains its place for legacy applications that don't support OIDC. If you're connecting a 15-year-old enterprise system where the vendor offers only SAML and has no plans to add OIDC, you use SAML. But when you have a choice, OIDC.

## 💡 The Discovery Document

One of OIDC's practical contributions is the discovery document. Every OIDC provider publishes a well-known configuration endpoint:

```
https://login.microsoftonline.com/{tenant}/.well-known/openid-configuration
```

This JSON document contains everything a client needs to configure itself: the authorization endpoint URL, token endpoint URL, JWKS URI (where Entra ID's signing keys are published), supported scopes, supported grant types, and more.

Libraries that support OIDC discovery configure themselves automatically. You provide the issuer URL; the library fetches the rest. No hardcoded endpoint URLs. No manual tracking of signing key locations. When Entra ID updates endpoints or rotates keys, the discovery document reflects the change automatically.

---

💬 **When you first understood that OAuth 2.0 and OpenID Connect were different things built on top of each other, did it change how you thought about the authentication flows you'd already built?** The distinction is fundamental but easy to miss when the library handles both transparently. What triggered the "oh, these are separate" moment?
<!-- nav -->

---

[← OAuth 2.0](glossary-4-16-oauth2.md) | [Home](../README.md) | [SAML →](glossary-4-18-saml.md)
