# Bearer Token (Deep Dive)
*Why "Whoever Has It Can Use It" Is Both the Point and the Risk*

**Part of Entra ID Glossary Series: Glossary#11.8 - Bearer Token (Deep Dive)**

---

A developer found an access token in an application's debug log. The token had been printed during testing and the log file had been committed to the repository along with the rest of the debugging output. The repository was private, but eleven developers had access.

The question: was that token a security incident?

The answer depended on what it was: a bearer token, and when it was issued. If the token was still within its validity window, yes. Any of those eleven developers could have taken that token and used it against the API it was issued for, without any additional authentication.

That's what "bearer" means. Whoever holds it, uses it. The token is the credential.

## 🎫 What Bearer Means

A bearer token is a security token where possession is sufficient for use. There's no binding between the token and the identity of the party presenting it. No client certificate check. No proof of possession required. You hold the token, you present it, you get access.

This is the `Authorization: Bearer <token>` header that appears in virtually every API call to Entra ID-protected resources. The format is defined in RFC 6750 and is universal across OAuth 2.0 implementations.

The "bearer" designation contrasts with bound tokens or proof-of-possession tokens, where the server validates that the party presenting the token can prove they possess the corresponding private key. Bearer tokens make no such check. Simpler to implement, simpler to use, simpler to steal.

## 🔐 The HTTP Implementation

Every authenticated API call to an Entra ID-protected resource uses the bearer token in the Authorization header:

```
GET /v1.0/me
Host: graph.microsoft.com
Authorization: Bearer eyJ0eXAiOiJKV1QiLCJub...
```

The resource API extracts the token from the header, validates the signature, checks the expiry, validates the audience and issuer, and checks the scopes or roles in the token. If all validations pass, the request is honored.

The token itself is a JWT: three base64-encoded sections separated by dots. Header (algorithm and token type). Payload (claims). Signature. The payload is readable without any key; it's just base64-encoded JSON. The signature is what proves the token came from Entra ID and hasn't been tampered with.

This means anyone who intercepts a bearer token can read its claims. The token isn't encrypted by default. It's signed. Signing provides integrity (proves the token was issued by Entra ID and hasn't been modified). It doesn't provide confidentiality (anyone can read the claims).

## ⚠️ The Security Implications

**Never log tokens** 📋: The debug log scenario from the opening is the most common bearer token exposure in practice. Frameworks, ORMs, HTTP clients, and custom logging code all have opportunities to capture tokens. Logging middleware that captures the Authorization header logs the token. Application code that logs full request/response pairs logs the token. Audit this carefully.

**HTTPS is not optional** 🔒: Bearer tokens in transit must be protected by TLS. An HTTP request with a bearer token is trivially intercepted. The OAuth 2.0 spec requires TLS for bearer token transmission; sending bearer tokens over HTTP is a misconfiguration.

**Token lifetime limits exposure** ⏰: A bearer token that expires in one hour and is then captured in a log is a one-hour security incident. A bearer token from a session with a 24-hour token (with CAE) is a more serious one. Short token lifetimes limit the blast radius of token capture.

**Secure in-memory handling** 💻: MSAL caches tokens in memory and handles their storage. Applications that persist tokens to disk, include them in application state that gets serialized, or pass them through systems that log payloads need to treat those tokens with the same care as passwords.

## 🔗 Sender-Constrained Tokens: The Alternative

The OAuth working group has developed mechanisms to bind tokens to the client presenting them, making stolen tokens unusable by other parties.

**mTLS Sender-Constrained Tokens**: The client authenticates to the token endpoint using a mutual TLS certificate. The certificate's thumbprint is embedded in the token. When the client presents the token to the resource, the resource validates that the client's current certificate matches the thumbprint in the token. A stolen token without the certificate is useless.

**DPoP (Demonstration of Proof-of-Possession)**: The client generates an asymmetric key pair and creates a DPoP proof JWT signed with the private key for each API request. The token endpoint binds the token to the public key. The resource validates the DPoP proof on each request. Stolen token alone is unusable.

Neither mechanism is universally supported across Azure services today. Bearer tokens remain the standard. The mitigations (short lifetime, HTTPS, no logging, secure caching) are the practical security layer.

## 📊 What Proper Bearer Token Handling Looks Like

An application that handles bearer tokens correctly:
- Acquires tokens via MSAL and never stores them outside MSAL's cache
- Uses HTTPS exclusively for API calls
- Never logs Authorization headers or token values
- Doesn't include tokens in error messages or diagnostic output
- Validates tokens on the API side before trusting their claims

---

💬 **Has your team ever found an access token in a log file, a Slack message, a git commit, or any other unintended location?** The bearer token exposure in development tooling is more common than most teams track formally. What controls does your organization have for preventing token capture in logs and debugging output?
<!-- nav -->

---

[← Subject (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-7-subject-deep-dive.md) | [🏠 Contents](/README) | [Token Lifetime (Deep Dive) →](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-9-token-lifetime-deep-dive.md)
