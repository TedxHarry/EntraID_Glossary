# Token Endpoint: Where Codes and Credentials Become Tokens

**Part of Entra ID Glossary Series: Glossary#11.3 - Token Endpoint (Deep Dive)**

---

The authorization endpoint is where users interact. The token endpoint is where applications interact. No browser, no UI, no redirects. Just an HTTP POST from application code to Entra ID, and a JSON response with tokens.

Most developers working with MSAL never call the token endpoint directly. The SDK handles it. But when token acquisition fails and the error is coming from the token endpoint, knowing exactly what that endpoint expects and what it returns is what turns a 20-minute debug session into a 2-minute one.

## 🌐 The Endpoint

```
https://login.microsoftonline.com/{tenant}/oauth2/v2.0/token
```

Same tenant variants as the authorization endpoint: specific tenant ID, `common`, `organizations`, or `consumers`. The token endpoint is always a POST. Parameters go in the request body as `application/x-www-form-urlencoded`, not JSON, not query string.

## 📋 The Grant Types

The `grant_type` parameter tells the token endpoint what kind of token request this is. Different grant types mean different required parameters.

**`authorization_code`** 🔄: Exchanging an authorization code for tokens. Required parameters: `code` (the code from the authorization endpoint), `redirect_uri` (must match the original request), `client_id`, client authentication (client_secret or client_assertion), and `code_verifier` if PKCE was used. Returns: access token, ID token, and optionally refresh token.

**`client_credentials`** 🤖: Service-to-service authentication where no user is involved. The application authenticates with its own identity. Required: `client_id`, client authentication, `scope` (must include `/.default`). Returns: access token only. No refresh token (client_credentials tokens are short-lived and re-acquired directly).

**`refresh_token`** 🔁: Silently acquiring a new access token using an existing refresh token. Required: `refresh_token`, `client_id`, client authentication (for confidential clients), `scope`. Returns: new access token, new ID token if `openid` in scope, and potentially a new refresh token (sliding window).

**`urn:ietf:params:oauth:grant-type:device_code`** 📱: Exchanging a device code for tokens after user completes authentication on another device. Used for devices without browsers.

**`urn:ietf:params:oauth:grant-type:jwt-bearer`** 🔗: The On-Behalf-Of flow. A middle-tier service presents a user's access token and requests a new token for a downstream API on behalf of that user. Requires `assertion` (the incoming token) and `requested_token_use=on_behalf_of`.

## 🔑 Client Authentication

For confidential clients (web applications and APIs that can keep a secret), the token endpoint requires the application to prove it's the legitimate app, not just anyone who knows the client ID. Two methods:

**Client secret** 🗝️: The `client_secret` parameter. A password-style credential registered in the app registration. Simple but has a rotation requirement and a secret management problem. If the secret expires or is leaked, authentication breaks.

**Client assertion (certificate)** 🔐: The `client_assertion` parameter containing a JWT signed with the application's private key. Entra ID validates the signature against the public certificate registered in the app registration. More secure than shared secrets: the private key never leaves the application, and certificates have a managed lifecycle with clear expiry.

**Federated identity credential** 🔗: For workload federation scenarios, the `client_assertion` is an external OIDC token (GitHub, Kubernetes, etc.). The token endpoint validates it against the configured federated identity credential. No Azure secret stored anywhere.

For public clients (SPAs, mobile apps, desktop apps), client authentication isn't required or expected at the token endpoint. PKCE serves as the binding mechanism instead.

## 📦 What the Token Response Contains

A successful token response is a JSON object with:

**`access_token`**: The JWT to use for API calls. Decode it (it's base64-encoded JSON) to see the claims: `aud` (intended audience), `iss` (issuer), `sub` (subject), `exp` (expiry), `scp` or `roles` (permissions), `oid` (object ID of the user or service principal), and whatever other claims were configured in the token configuration.

**`id_token`**: Present when `openid` was in the scope. Contains identity claims about the user: `name`, `email`, `preferred_username`. Used to display user information after sign-in, not for authorization.

**`refresh_token`**: Present when `offline_access` was in the scope. Used to get new access tokens without user interaction.

**`expires_in`**: Seconds until the access token expires. The SDK uses this for cache management.

**`token_type`**: Always `Bearer` for Entra ID tokens.

## ⚠️ Common Token Endpoint Errors

`invalid_grant`: The authorization code is invalid, expired, or already used. Or the refresh token has been revoked. This is the error you get when re-using a code or when a user's session has been invalidated.

`invalid_client`: Client authentication failed. Wrong client secret, expired certificate, or mismatched client ID.

`unauthorized_client`: The application isn't allowed to use this grant type. Check the app registration's manifest and platform configuration.

`AADSTS70011`: Scope is invalid. The requested scope doesn't match any configured API permissions or the scope format is wrong.

---

💬 **What's the most useful thing you've found by decoding an access token from the token endpoint during a debugging session?** JWT decoders like jwt.ms make it easy to see the actual claims Entra ID is issuing. Have you ever found a missing claim, wrong audience, or unexpected permission scope that explained a permission failure?
<!-- nav -->

---

[← Authorization Endpoint: What's Actually in That Sign-In URL](glossary-11-2-authorization-endpoint-deep-dive.md) | [Home](../README.md) | [Authorization Server: What Entra ID Is Actually Doing When It Issues a Token →](glossary-11-4-authorization-server-deep-dive.md)
