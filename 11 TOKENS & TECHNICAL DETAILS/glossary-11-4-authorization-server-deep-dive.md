# Authorization Server: What Entra ID Is Actually Doing When It Issues a Token

**Part of Entra ID Glossary Series: Glossary#11.4 - Authorization Server (Deep Dive)**

---

From the developer's perspective, Entra ID is a black box. You send a request with credentials and scopes. You get back a token. What happens in between feels irrelevant until something breaks and you need to understand why Entra ID issued (or refused to issue) a specific token with specific claims.

Entra ID as an authorization server isn't magic. It's a well-specified OAuth 2.0 and OIDC authorization server with a discoverable configuration, a well-understood processing pipeline, and a specific set of responsibilities in the protocol.

## 🏗️ What an Authorization Server Does

An OAuth 2.0 authorization server has three core responsibilities:

**Authenticate the identity** 👤: Verify that the user (or application) is who they claim to be. For users, this means validating credentials against the directory: password check, MFA verification, identity protection risk assessment. For applications, validating the client secret, certificate assertion, or federated credential.

**Authorize the request** 🔐: Determine whether the authenticated identity is allowed to get what it's asking for. Are the requested scopes consented to? Has the user's account been disabled? Does a Conditional Access policy block this authentication? Does the application have permission to access the requested API?

**Issue tokens** 🎫: After authentication and authorization pass, construct and sign tokens that downstream services can validate and trust. Choose the right claims, apply the right expiry, sign with the appropriate key.

## 🔍 The Discovery Document

Every Entra ID tenant exposes an OIDC discovery document (also called the well-known configuration) at:

```
https://login.microsoftonline.com/{tenant}/v2.0/.well-known/openid-configuration
```

This JSON document describes everything about how the authorization server is configured: the authorization endpoint URL, the token endpoint URL, the JWKS URI (where to get the signing keys), supported grant types, supported response types, supported signing algorithms, and more.

Applications and resource servers use this document for auto-configuration. Instead of hardcoding endpoint URLs, a well-built OAuth client fetches the discovery document and derives everything from it. This makes the application resilient to endpoint changes.

The JWKS URI in the discovery document points to the JSON Web Key Set, which contains the public keys used to verify token signatures.

## 🔑 Token Signing and Key Rotation

Entra ID signs tokens using RS256 (RSA Signature with SHA-256) by default, and also supports ES256 (ECDSA). The private signing keys are managed by Microsoft and rotated periodically.

When a resource server receives a token, it needs to validate the signature. It fetches the JWKS from the JWKS URI, finds the key that matches the `kid` (key ID) claim in the token header, and uses that public key to verify the signature.

Key rotation is automatic and transparent to properly implemented applications. The `kid` claim in the token header identifies which key was used for signing. The JWKS URI always contains the current valid keys. Applications that cache the JWKS must handle key rotation by re-fetching the JWKS when they encounter a `kid` they don't recognize.

This is a common implementation mistake: an application or library caches the signing keys and then fails to validate tokens after a key rotation because the cached keys are stale. The fix is always to refresh the JWKS when signature validation fails before returning an error.

## 🧩 How Claims Are Assembled

When Entra ID builds a token, it pulls claims from multiple sources:

**Directory data** 📋: The user's object in Entra ID. Name, email, department, job title, manager. Whatever attributes are populated in the directory and configured for inclusion in tokens.

**Application configuration** ⚙️: The app registration's token configuration. Optional claims added to the manifest. Groups claims (security groups, directory roles). Application roles defined in the app manifest.

**Authentication context** 🔐: Claims about how the authentication occurred. Authentication methods used (`amr` claim), authentication time (`auth_time`), MFA completion, authentication strength.

**Issued-for application** 🎯: Claims about the application receiving the token. The `azp` (authorized party) claim identifies the client application that requested the token. The `aud` claim identifies the resource the token is for.

**Conditional Access and session** 📊: CA satisfaction claims, CAE capability indicators, session ID for sign-out coordination.

## 🌐 Multi-Tenant Authorization Server Behavior

When an authorization server handles multi-tenant authentication (using the `common` or `organizations` endpoint), the token issuer claim (`iss`) changes. Instead of `https://login.microsoftonline.com/{your-tenant-id}/v2.0`, the issuer reflects the tenant that actually authenticated the user.

Resource servers that accept multi-tenant tokens must validate that the issuer is a valid Entra ID tenant, not a specific known issuer value. This is a common security misconfiguration: a resource server configured with a hardcoded issuer value that only accepts tokens from one tenant, when it should accept tokens from any valid Entra ID tenant.

The MSAL libraries and common middleware like `passport-azure-ad` handle multi-tenant issuer validation when configured correctly. The configuration decision belongs to the application developer.

---

💬 **Has your team ever had to debug a token signature validation failure after a key rotation?** The JWKS caching problem shows up in non-standard token validation implementations, custom middleware, and some older libraries that don't handle key rotation correctly. What was the most unexpected thing you found when you looked at the raw token structure or the discovery document for the first time?
<!-- nav -->

---

[← Token Endpoint: Where Codes and Credentials Become Tokens](glossary-11-3-token-endpoint-deep-dive.md) | [Home](../README.md) | [Authorization Grant: Matching the Right OAuth Flow to the Right Scenario →](glossary-11-5-authorization-grant-deep-dive.md)
