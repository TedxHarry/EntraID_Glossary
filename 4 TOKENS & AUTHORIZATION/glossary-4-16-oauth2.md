# OAuth 2.0
*The Protocol That Solved a Problem We Didn't Realize Was a Problem*

**Part of Entra ID Glossary Series: Glossary#4.16 - OAuth 2.0**

---

Before OAuth existed, if you wanted a third-party app to access your photos to print them, the only way to give it access was to hand over your email and password. The app could read your photos. It could also delete them, read your email, change your password, and do anything else your account allowed. You couldn't give it narrow access. It was everything or nothing.

That's the problem OAuth 2.0 solved. Not authentication. Authorization. The ability to say "this application can do this specific thing with my data" without ever handing over your credentials.

## 📜 What OAuth 2.0 Actually Is

OAuth 2.0 is an authorization framework, not an authentication protocol. This distinction matters more than it sounds, and it trips people up regularly.

Authentication is "who are you?" OAuth 2.0 doesn't answer this question. It was never designed to. OAuth answers a different question: "can this application access this resource on behalf of this user?"

The framework defines:
- How an application requests authorization from a user
- How a user grants that authorization
- How the authorization is communicated to APIs (via access tokens)
- How the application refreshes that authorization when tokens expire

What it deliberately does not define: what the user's identity is. That's OpenID Connect's job, the protocol that sits on top of OAuth 2.0. The distinction matters because combining the two is how modern sign-in actually works.

## 🏗️ The Four Roles

OAuth 2.0 defines four roles that map directly to Entra ID concepts:

**Resource Owner**: The user who owns the data. When you sign in and approve an app's permissions on the consent screen, you're the resource owner deciding whether to grant access to your resources.

**Client**: The application requesting access. Your web app, mobile app, background service, or third-party integration that wants to do something with the user's data.

**Authorization Server**: The system that authenticates the user and issues tokens. In the Microsoft ecosystem, this is Entra ID, specifically its token endpoint at `login.microsoftonline.com`.

**Resource Server**: The API holding the data. Microsoft Graph, your own APIs, or any other service the application is trying to access. Resource servers validate the access tokens presented to them.

## 🔄 What Actually Happens

When your application integrates with Entra ID using OAuth 2.0, the sequence looks like this:

1. Application directs user to Entra ID's authorization endpoint
2. User authenticates and approves the requested scopes on the consent screen
3. Entra ID issues an authorization code back to the application's redirect URI
4. Application exchanges the code for an access token (this is a server-to-server call the browser doesn't see)
5. Application presents the access token to the resource server
6. Resource server validates the token and returns data

Step 4 is where the client secret or PKCE code verifier is used to prove the request came from the legitimate application. This is what keeps tokens out of browser history and prevents interception attacks.

## 💡 Why "2.0" - What Changed

OAuth 1.0 existed before OAuth 2.0. It required complex cryptographic signatures on every API request, which was secure but extremely difficult to implement correctly. Library support was inconsistent. Bugs were common.

OAuth 2.0 simplified the protocol significantly by relying on HTTPS for transport security instead of per-request cryptographic signing. The tradeoff: OAuth 2.0 requires HTTPS everywhere without exception, but in exchange it's dramatically easier to implement correctly, and the library ecosystem is strong.

Most OAuth implementations you'll encounter today are OAuth 2.0. OAuth 1.0 still exists in some very old APIs but is effectively obsolete for new development.

## ⚠️ Common Misconceptions

OAuth 2.0 is not:
- ❌ An authentication protocol (it doesn't tell you who the user is)
- ❌ A single defined flow (it's a framework with multiple grant types for different scenarios)
- ❌ Specific to web applications (it works for mobile, CLI tools, and server-to-server)
- ❌ A Microsoft technology (it's an IETF standard, RFC 6749, used by every major platform)

Understanding that OAuth 2.0 is specifically about authorization rather than authentication is the foundation for understanding why OpenID Connect exists alongside it, why access tokens and ID tokens are different things, and why you need both when building a complete sign-in experience.

---

💬 **When did it click for you that OAuth was about authorization, not authentication?** It's one of those distinctions that seems obvious once you understand it but creates real confusion before that. What's the clearest way you've found to explain it to someone new to identity concepts?
<!-- nav -->

---

[← Subject](glossary-4-15-subject.md) | [Home](../README.md) | [OIDC (OpenID Connect) →](glossary-4-17-oidc.md)
