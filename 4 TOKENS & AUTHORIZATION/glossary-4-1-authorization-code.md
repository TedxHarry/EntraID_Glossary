# Authorization Code
*Why Sign-In Takes Two Steps Instead of One*

**Part of Entra ID Glossary Series: Glossary#4.1 - Authorization Code**

---

A developer I mentored once asked me a genuinely good question: "Why does the OAuth flow need this intermediate code? If the user just authenticated, why not give the app the token directly? Why the extra step?"

It's the kind of question that sounds naive until you think about it for thirty seconds and realize it's actually exactly the right thing to ask. The answer explains something fundamental about how secure token delivery works.

## 🔄 What the Authorization Code Is

The authorization code is a short-lived, single-use string that Entra ID sends back to an application after a user successfully authenticates. It's not the token. It's a temporary receipt that proves authentication happened, and it can be exchanged for the actual tokens once the application proves its own identity.

The flow looks like this:

1. 🌐 User's browser navigates to Entra ID's authorization endpoint
2. 👤 User authenticates and consents (if needed)
3. 📨 Entra ID redirects the browser back to the app's redirect URI, with the authorization code in the URL
4. 🔒 App's server takes that code and makes a direct POST request to the token endpoint, including the code plus the app's client secret
5. 🎫 Entra ID validates everything and returns the actual tokens

The code is what makes step 4 possible without skipping step 3's security check.

## 🤔 So Why Not Skip Straight to the Token?

The reason comes down to where sensitive data should and shouldn't travel.

Step 3 puts the authorization code in a URL. URLs are not private. They appear in browser history, server logs, proxy logs, and Referer headers. Anything that ends up in a URL is potentially visible to more parties than intended.

If the token itself were delivered in that redirect URL, it would be sitting in browser history and log files on every proxy between the user and your server. That's not acceptable for a credential that grants API access.

The authorization code in the URL is safe to be seen by logs because it's useless without the client secret, and a code can only be used once. The moment the app exchanges it for tokens, the code is permanently invalidated. Anyone who finds it in a log file after that point has nothing.

The actual tokens travel in the body of the token endpoint response, a direct server-to-server connection over HTTPS. They never touch a browser URL. That's the security guarantee the code exchange step provides.

## 🔑 The Client Secret: Proving the App's Identity

When the app presents the authorization code to the token endpoint, it also presents its client secret (or a client certificate, which is better). This proves that the entity making the exchange request is actually the registered application, not someone who intercepted the code from a log file.

The combination of "valid code" plus "valid client credentials" is what Entra ID requires before issuing tokens. Either alone is insufficient.

## 📱 What About Public Clients? PKCE to the Rescue

This model works cleanly for web applications running on servers that can securely store a client secret. It gets complicated for mobile apps and single-page applications (SPAs), which run on devices or browsers where storing a secret is impossible. Any secret embedded in a mobile app can be extracted by inspecting the app package.

PKCE (Proof Key for Code Exchange, pronounced "pixy") solves this. Instead of a client secret, the app generates a random value called a code verifier before starting the flow. It hashes that value to create a code challenge, sends the challenge to the authorization endpoint, and later sends the original verifier to the token endpoint. Entra ID hashes the verifier and checks it matches the challenge.

The attacker who intercepts the authorization code still can't use it, because they'd need the code verifier that was only ever in the app's memory.

Microsoft recommends PKCE for all authorization code flows now, including confidential clients that have a client secret. Belt and suspenders.

## ⚠️ Authorization Code Security Rules

A few properties worth understanding when debugging or reviewing app implementations:

- ⏱️ Authorization codes expire quickly, typically in a few minutes. An expired code returns an error.
- 🔂 Authorization codes are single-use. Attempting to use a code twice returns an error and, in some implementations, triggers a security alert.
- 📎 The redirect URI in the token request must exactly match the one used in the authorization request. Mismatches are rejected.
- 🛡️ The `state` parameter sent in the authorization request should be validated when the code comes back, to prevent CSRF attacks.

---

💬 **Have you ever had to debug an authorization code flow?** The "invalid_grant" error from a code that expired or was already used is a rite of passage for anyone integrating OAuth applications with Entra ID. What was the culprit in your case?
<!-- nav -->

---

[← Microsoft Authenticator](../3%20AUTHENTICATION/glossary-3-8-microsoft-authenticator.md) | [Home](../README.md) | [Authorization Endpoint →](glossary-4-2-authorization-endpoint.md)
