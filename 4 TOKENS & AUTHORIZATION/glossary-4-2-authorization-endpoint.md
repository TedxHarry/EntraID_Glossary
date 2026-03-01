# Authorization Endpoint
*Reading What That Long URL Is Actually Saying*

**Part of Entra ID Glossary Series: Glossary#4.2 - Authorization Endpoint**

---

The first time I looked at a raw OAuth authorization request URL, it was in a browser's developer tools while debugging why a sign-in wasn't working. The URL was about 400 characters long, full of encoded characters and parameter names I half-recognised. I copy-pasted it into a text editor, broke it into parameters, and read it properly.

It was one of those moments where something clicked. Every parameter was deliberate. Each one was telling Entra ID something specific about the request. Once you know how to read these URLs, you can diagnose sign-in problems from the first HTTP request.

## 🌐 What the Authorization Endpoint Is

The authorization endpoint is the URL where the OAuth sign-in flow begins. For Entra ID, it looks like this:

```
https://login.microsoftonline.com/{tenant-id}/oauth2/v2.0/authorize
```

The `{tenant-id}` can be the tenant's GUID, the primary domain name, or the word `common` (for multi-tenant apps that accept users from any tenant) or `organizations` (for work and school accounts only).

This is the browser-facing endpoint. The user's browser navigates here, the user authenticates, and Entra ID sends the result back to the application via a redirect. No tokens come back from this endpoint directly, only the authorization code (or, in some flows, an error).

## 📋 Breaking Down the Request Parameters

When an app initiates a sign-in, it constructs a URL with query parameters and sends the browser there. Here's what each parameter does:

**client_id** 🏷️
The Application (Client) ID of the registered app. This tells Entra ID which application is requesting sign-in. Entra ID uses this to look up the app's configuration, permitted redirect URIs, and what permissions it's allowed to request.

**response_type** 📤
What the app wants back. For the authorization code flow, this is `code`. For flows that return a token directly (less secure, generally discouraged), it can be `token` or `id_token`.

**redirect_uri** 🔀
Where Entra ID should send the user after authentication. Must exactly match one of the redirect URIs registered on the app. If it doesn't match, Entra ID rejects the request entirely, protecting against attackers redirecting the code to their own server.

**scope** 🎯
What permissions the app is requesting. Expressed as space-separated values. Example: `openid profile email User.Read`. The `openid` scope is required to get an ID token. `offline_access` is required to get a refresh token. Everything else is API-specific.

**state** 🔒
A random value the app generates and includes in the request. Entra ID echoes it back unchanged in the redirect response. The app verifies it matches what was sent. This prevents CSRF attacks where an attacker tricks a browser into completing an authorization flow the user didn't start.

**nonce** 🔁
A random value included in the request that gets embedded in the returned ID token. The app validates it matches. Prevents token replay attacks where an attacker captures a valid ID token and reuses it.

**response_mode** 📬
How Entra ID delivers the response. Options are `query` (code in the URL query string), `fragment` (code in the URL fragment after #), or `form_post` (code sent as an HTTP POST body). For security reasons, `form_post` is preferred for authorization codes because query parameters get logged by servers.

**prompt** 💬
Controls the user experience. `none` means Entra ID should not show any UI at all (fails if interaction is needed). `login` forces the user to enter credentials even if they have a valid session. `select_account` shows an account picker. `consent` forces a consent screen.

**login_hint** 👤
Pre-fills the username field on the sign-in page. Useful when the app already knows who's signing in (from a previous session, for example). Saves the user one step.

## 🔍 A Real Example

Here's what a minimal authorization request URL looks like broken apart:

```
https://login.microsoftonline.com/contoso.com/oauth2/v2.0/authorize
  ?client_id=12345678-abcd-1234-abcd-123456789abc
  &response_type=code
  &redirect_uri=https%3A%2F%2Fmyapp.contoso.com%2Fauth%2Fcallback
  &scope=openid+profile+email+User.Read+offline_access
  &state=abc123randomvalue
  &nonce=xyz789randomnonce
  &response_mode=form_post
```

When you see a sign-in failing at this stage, the Entra ID error page usually includes an error code and description. The most common causes: a `redirect_uri` mismatch (the URI in the request doesn't match what's registered), an invalid `client_id`, or a scope that hasn't been added to the app's permissions.

## ⚠️ Common Mistakes at the Authorization Endpoint

- 🚫 Using a redirect URI in the request that isn't registered on the app (returns AADSTS50011)
- 📝 Requesting scopes the app hasn't been granted (user gets an unexpected consent prompt or error)
- 🔁 Forgetting `offline_access` in the scope when the app needs a refresh token
- 🌐 Using `common` as the tenant when the app should only accept users from a specific tenant

---

💬 **Have you ever read the raw authorize request URL during a debugging session?** Once you know what each parameter means, a broken sign-in URL tells you almost everything you need to know about where the problem is. What's the most useful thing you've learned from reading OAuth request parameters directly?
<!-- nav -->

---

[← Authorization Code](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-1-authorization-code.md) | [🏠 Contents](/README) | [Token Endpoint →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-3-token-endpoint.md)
