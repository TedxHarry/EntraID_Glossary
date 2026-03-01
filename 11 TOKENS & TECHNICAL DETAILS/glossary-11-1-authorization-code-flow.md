# Authorization Code Flow: The OAuth Dance That Powers Most Modern Web App Sign-Ins

**Part of Entra ID Glossary Series: Glossary#11.1 - Authorization Code Flow**

---

A developer was told to implement "Sign in with Microsoft" for a web application. They found an example online that used the implicit flow, returning tokens directly in the URL fragment. It was simple, it worked, and it was wrong.

Tokens in URL fragments get logged by servers, stored in browser history, and captured by referrer headers. The implicit flow was deprecated for exactly this reason. The correct flow is the authorization code flow, where the authorization server never puts a token in the URL. What goes in the URL is a short-lived, single-use code, and that code is exchanged for tokens in a back-channel call that doesn't touch the browser.

Understanding why the authorization code flow is structured the way it is makes the security model clear.

## 🔄 The Flow Step by Step

**Step 1: Authorization request** 🔗: The application redirects the user's browser to Entra ID's authorization endpoint. The request includes the application's client ID, the requested scopes, a redirect URI (where Entra ID should send the user after authentication), a randomly generated state value, and for PKCE, a code challenge.

**Step 2: User authenticates** 👤: Entra ID shows the sign-in page. The user authenticates (username, password, MFA if required). If the user hasn't consented to the requested scopes before, Entra ID shows a consent screen listing what the application is requesting.

**Step 3: Authorization code returned** 📋: After successful authentication, Entra ID redirects the user's browser back to the application's redirect URI with an authorization code in the query string. This code is short-lived (typically valid for a few minutes), single-use, and meaningless on its own.

**Step 4: Code exchange** 🔑: The application's server (not the browser) makes a POST request to Entra ID's token endpoint. It sends the authorization code, the client ID, the client secret (for confidential clients), and the PKCE code verifier. This is a server-to-server call; the user's browser isn't involved.

**Step 5: Tokens returned** ✅: Entra ID validates the code and client authentication, then returns an access token, an ID token, and optionally a refresh token. These tokens are returned in the HTTP response body to the server, not in any URL.

## 🔒 Why the Code Exists

The core insight of the authorization code flow is the two-phase design. Phase one happens in the browser: authentication and consent. Phase two happens server-side: token acquisition. The browser never sees a token.

The authorization code that moves through the browser has no value on its own. It can only be exchanged for tokens by a client that can also prove it's the legitimate application (via client secret or PKCE code verifier). If a server log captures the authorization code in a URL, the attacker still can't use it without the client secret.

This is the fundamental security improvement over implicit flow, where the browser received tokens directly.

## 🛡️ PKCE: The Public Client Extension

For applications that can't keep a client secret (single-page applications, mobile apps, desktop apps), PKCE (Proof Key for Code Exchange) provides equivalent protection without a shared secret.

Before starting the flow, the application generates a random `code_verifier` and derives a `code_challenge` from it (a SHA-256 hash). The `code_challenge` goes into the authorization request. When exchanging the code, the application sends the original `code_verifier`. Entra ID hashes it and verifies it matches the `code_challenge`.

An attacker who intercepts the authorization code can't exchange it because they don't have the `code_verifier`, which was generated locally and never sent to the authorization server until exchange time.

PKCE is now recommended for all clients, including confidential web applications. It provides defense in depth alongside the client secret.

## ⚙️ What MSAL Does With This

`msal-browser` (for SPAs), `msal-node` (for Node servers), and MSAL equivalents in other languages implement the authorization code flow so developers don't have to build it manually. The library handles:

Generating the state and nonce values. Storing them to validate the response. Initiating the redirect. Processing the redirect back. Extracting and validating the code. Exchanging the code for tokens. Caching the tokens and handling refresh.

Most developers implementing "Sign in with Microsoft" write a few lines of MSAL configuration, not a raw OAuth flow. Understanding what's happening underneath is what matters when something goes wrong.

---

💬 **Has your team ever debugged an authorization code flow failure in production, and what was the root cause?** The most common failures are redirect URI mismatches, state parameter validation errors, and PKCE verifier mismatches. Which part of the flow has caused the most debugging time for your team?

#EntraID #AuthorizationCodeFlow #OAuth2 #PKCE #MSAL #MicrosoftEntra #AppDevelopment
