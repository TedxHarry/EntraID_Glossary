# Access Tokens: What's Actually Inside That Long String

**Part of Entra ID Glossary Series: Glossary#4.5 - Access Token**

---

An access token looks like a random string of characters about 1,500 characters long. Developers copy-paste them into Postman headers, IT pros see them flash past in Fiddler traces, and most people treat them as opaque blobs that either work or don't.

They're not opaque. They're JWTs (JSON Web Tokens), and they're fully readable. Paste one into jwt.ms (Microsoft's own token decoder) and you'll see exactly what Entra ID packed into it. What you find is worth understanding, because the claims inside the token drive authorization decisions across every API that accepts it.

## 🔍 Anatomy of an Entra ID Access Token

A JWT has three parts separated by dots: header, payload, and signature. The header and payload are Base64-encoded JSON, not encrypted. Anyone with the token can read the first two parts. Only the signature requires Entra ID's private key to create, and any resource server can verify it using Entra ID's public keys.

Here are the claims you'll consistently find in an Entra ID access token:

**aud** 🎯 (Audience)
Who the token is for. The resource server validates that this matches its own identifier. A token issued for Microsoft Graph won't work against SharePoint's API because the audience is wrong. This prevents token replay across different APIs.

**iss** 🏛️ (Issuer)
Which Entra ID tenant issued the token. Format: `https://sts.windows.net/{tenant-id}/` for v1 tokens, `https://login.microsoftonline.com/{tenant-id}/v2.0` for v2. The resource server uses this to find the right public key for signature verification.

**iat, nbf, exp** ⏱️ (Issued At, Not Before, Expiry)
Unix timestamps. `iat` is when the token was created. `nbf` is the earliest the token is valid (usually the same as `iat`). `exp` is when it expires. The resource server rejects any token where the current time is past `exp`. Default expiry is 3600 seconds (60 minutes) from issuance.

**oid** 🆔 (Object ID)
The unique identifier of the user or service principal in Entra ID. Stable across applications and across token refresh. If you're storing user data in a database, use `oid` as the key, not email or username (those can change).

**tid** 🏢 (Tenant ID)
The GUID of the Entra ID tenant that issued the token. Useful for multi-tenant apps that need to know which organization's user is signing in.

**scp** 🔐 (Scope, for delegated tokens)
The delegated permissions the application was granted for this token. Space-separated. Example: `"User.Read email profile openid"`. The resource server checks this to determine what actions the caller is authorized to perform on behalf of the user.

**roles** 👑 (for application permissions or app role assignments)
When an app has application permissions granted, they appear here. Also where app role assignments appear when a user is assigned an app role. Different from `scp` in that these are not delegated from the user.

**upn** or **preferred_username** 📧
The user's sign-in name. Not guaranteed to be stable (users can rename their UPN), which is why `oid` is the right key for persistence. Useful for display purposes.

**name** 👤
Display name of the user. For showing "Welcome, Alex" in your app UI.

**ver** 📋
Token version: `"1.0"` or `"2.0"`. v2 tokens have some structural differences and are the recommended endpoint for new applications.

## ⚠️ What Access Tokens Are Not For

Access tokens are not ID tokens. This distinction matters and gets confused regularly.

An access token is a credential the application presents to a resource server to prove authorization. The resource server (Microsoft Graph, your custom API) reads and validates it. Your application shouldn't read an access token intended for another API and try to extract claims from it. The format can change, the signature isn't validated by your app, and the claims might not be what you expect.

If your application needs to know who signed in, use the ID token. That's what it's for.

If your API needs to know who is calling it, validate the access token and read its claims in the API layer. The downstream API is the intended audience, not the calling client application.

## 🔒 Access Token Security

Access tokens are bearer tokens (covered in Glossary#4.8). Whoever holds a valid token can use it. This makes protection in transit and at rest important:

- ✅ Always transmit access tokens over HTTPS
- ✅ Store tokens in memory where possible (not localStorage in browsers, which is accessible to JavaScript)
- ✅ Don't log token values (those log files become credential stores)
- ✅ Validate tokens in your API: check signature, audience, issuer, and expiry

A resource server that doesn't properly validate access tokens is accepting unsigned checks. The signature validation step, using Entra ID's published public keys, is non-negotiable.

---

💬 **Have you ever decoded an access token to debug a permissions issue?** The moment when you paste a token into jwt.ms and see a `scp` claim that doesn't include what you expected is one of those instant "ah, that's why" moments. What did decoding a token reveal for you?
<!-- nav -->

---

[← The Authorization Server: What Entra ID Is Actually Doing Behind the Scenes](glossary-4-4-authorization-server.md) | [Home](../README.md) | [The ID Token: Proof of Who Signed In (Not a Key to the API) →](glossary-4-6-id-token.md)
