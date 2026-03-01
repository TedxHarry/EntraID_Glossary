# Token Endpoint
*The Server-Side Half Nobody Talks About*

📚 **Part of Entra ID Glossary Series: Glossary#4.3 - Token Endpoint**

---

When I'm teaching OAuth to people who are new to it, I split the whiteboard in half. Left side: the authorization endpoint, browser-facing, user-visible, the part people experience. Right side: the token endpoint, server-to-server, invisible to the user, the part where tokens actually get issued.

Most explanations of OAuth spend most of their time on the left side. The right side is where the actual security happens, and it's worth understanding properly.

## 🔒 What the Token Endpoint Is

The token endpoint is the URL where an application sends a POST request to exchange credentials, codes, or tokens for access tokens. For Entra ID:

```
https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/token
```

Unlike the authorization endpoint, nothing navigates a browser to this URL. No user sees a page. The application's back-end server constructs an HTTP POST request and sends it directly to Entra ID. Entra ID validates the request and responds with tokens in the response body.

This server-to-server channel is why tokens can be safely delivered here in a way they couldn't be at the authorization endpoint. The response body of an HTTPS POST doesn't appear in browser history, proxy logs, or Referer headers.

## 📤 What Gets Sent to the Token Endpoint

The token endpoint accepts several different grant types, each with its own required parameters:

**Authorization Code Exchange** 🔄
Used after the authorization endpoint returns a code:
- `grant_type=authorization_code`
- `code` (the authorization code received)
- `redirect_uri` (must match what was used in the authorization request)
- `client_id` and `client_secret` (the app proving its own identity)

**Refresh Token Grant** ♻️
Used to get new tokens without requiring the user to sign in again:
- `grant_type=refresh_token`
- `refresh_token` (the previously issued refresh token)
- `client_id` and `client_secret`
- `scope` (can request the same or a subset of the original scopes)

**Client Credentials Grant** 🤖
Used by apps with no signed-in user (daemons, background services):
- `grant_type=client_credentials`
- `client_id` and `client_secret` (or certificate assertion)
- `scope` (must use `/.default` to request all pre-consented permissions)

Each grant type is suited to a different scenario. Authorization code exchange is for user-signed-in apps. Refresh token is for maintaining sessions. Client credentials is for machine-to-machine scenarios where no user is involved.

## 📥 What Comes Back

A successful token response is a JSON object containing:

```json
{
  "token_type": "Bearer",
  "scope": "User.Read email profile openid",
  "expires_in": 3600,
  "access_token": "eyJ0eXAiOiJKV1Qi...",
  "id_token": "eyJ0eXAiOiJKV1Qi...",
  "refresh_token": "0.AXoA..."
}
```

- `token_type` is always `Bearer` for Entra ID tokens, indicating how to use the token in API calls
- `expires_in` is seconds until the access token expires (typically 3600, which is 60 minutes)
- `access_token` is the JWT used to call APIs
- `id_token` is present only when `openid` scope was requested
- `refresh_token` is present only when `offline_access` scope was requested

## ⚠️ Common Token Endpoint Errors

Understanding error responses from the token endpoint saves a lot of debugging time:

- 🔴 `invalid_grant`: The code or refresh token is invalid, expired, or already used. For codes, this usually means the code expired (they last only a few minutes) or was used twice. For refresh tokens, it means the token was revoked, the user changed their password, or the token simply expired.

- 🔴 `unauthorized_client`: The client is not permitted to use this grant type. Check the app registration and whether the requested grant is allowed.

- 🔴 `invalid_client`: Client authentication failed. Wrong client secret, expired secret, or a certificate that doesn't match what's registered.

- 🔴 `AADSTS70011`: The scope requested is invalid. A permission that isn't configured on the app registration or hasn't received admin consent.

## 🔧 A Practical Debugging Tip

When a token exchange is failing, the most useful tool is capturing the raw HTTP request and response. Tools like Fiddler, the browser's network tab (for SPA flows), or Microsoft's sign-in logs all give you visibility into what was sent and what Entra ID returned.

The error response from the token endpoint always includes an `error` field and an `error_description`. The description is usually specific enough to point directly at the problem. "AADSTS70011: The provided request must include a 'scope' input parameter" is infinitely more actionable than "something went wrong."

💡 The Entra ID sign-in logs record token endpoint interactions under "Non-interactive sign-ins." If a background service is failing its token requests, that's where you'll find the error details alongside the client IP, the requested scopes, and whether Conditional Access had any impact.

---

💬 **What's the most cryptic token endpoint error you've had to debug?** The `invalid_grant` on a refresh token that worked fine yesterday is a classic that sends people down long rabbit holes before they find the revocation event in the logs.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Authorization Endpoint](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-2-authorization-endpoint.md) | [🏠 Contents](/README) | [Authorization Server →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-4-authorization-server.md)
