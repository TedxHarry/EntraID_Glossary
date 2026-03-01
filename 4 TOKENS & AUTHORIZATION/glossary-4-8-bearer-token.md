# Bearer Tokens: The Name That Tells You Everything About the Risk

**Part of Entra ID Glossary Series: Glossary#4.8 - Bearer Token**

---

In the early days of rail travel, you could buy a journey ticket that was tied to your name. Lose it, and whoever found it couldn't use it because the conductor would check your ID. Then there were platform tickets, cloakroom tokens, and bus passes: you paid once, and whoever holds the token rides the bus. No questions asked.

The name "bearer token" comes from that second model. Bearer means: whoever holds this gets in. No additional proof of identity required.

That property is both what makes bearer tokens so practical and what makes losing one a security incident.

## 🎫 What Bearer Token Means Technically

When you see `"token_type": "Bearer"` in an Entra ID token response, it tells you exactly how to use the access token. You include it in an HTTP Authorization header like this:

```
Authorization: Bearer eyJ0eXAiOiJKV1Qi...
```

The API receiving that request doesn't call back to Entra ID to check whether this token is legitimate. It validates the signature using Entra ID's published public keys, checks the claims (audience, expiry, issuer), and if everything checks out, grants access. The token itself is the entire credential.

No session lookup. No database check. No phone call home. Just cryptographic verification of a self-contained credential.

## ⚡ Why Bearer Tokens Are Useful

The stateless nature of bearer tokens is one of the things that makes modern cloud APIs scale. Microsoft Graph handles billions of API calls. If every single call required a real-time database lookup to validate a session, the performance cost would be enormous. Instead, Graph validates the token's cryptographic signature (a fast local operation) and reads the claims. Done.

Distributed systems benefit enormously from this model. A token issued by Entra ID in one region can be validated by an API endpoint in another region without any coordination between them. The signature is the proof. The signing keys are published publicly and cached locally.

## 🔒 The Security Implication You Can't Ignore

The flip side of "whoever holds it gets in" is obvious: if someone steals a bearer token, they can use it. The API won't know the difference between the legitimate holder and the thief. The token doesn't know its holder.

This is why secure token handling is non-negotiable:

**In transit** 🔐
Bearer tokens must travel over HTTPS. Always. Transmitting a bearer token over HTTP exposes it to network interception. Any infrastructure between the client and server (proxies, load balancers, CDNs) that processes unencrypted HTTP sees the token in plain text. HTTPS encrypts the Authorization header, protecting the token during transit.

**In storage** 💾
Where tokens are stored matters significantly:
- 🟢 Memory (runtime variables): Safest. Lost when the process ends.
- 🟡 Secure storage APIs (iOS Keychain, Android Keystore, Windows DPAPI): Good. Protected by the OS.
- 🔴 localStorage in browsers: Accessible to any JavaScript on the page. XSS vulnerabilities can steal tokens stored here.
- 🔴 URLs, logs, or anywhere else that persists text: Tokens in log files are credentials in log files.

**Lifetime as risk mitigation** ⏱️
Short token lifetimes limit the damage from theft. A token stolen at minute 59 of its 60-minute lifetime is useful for one minute. A token with a 24-hour lifetime is useful for up to 24 hours after theft. This is one of the reasons access tokens have short lifetimes while refresh tokens have longer ones: refresh tokens are exchanged server-to-server over HTTPS (harder to steal), while access tokens travel more broadly.

## 🔄 Beyond Bearer: Proof of Possession Tokens

Bearer tokens are the standard today, but a more secure model exists: proof-of-possession (PoP) tokens. Instead of "whoever holds this gets in," PoP tokens require the caller to also prove they hold a specific private key.

The token is cryptographically bound to the key pair of the legitimate caller. Stealing the token without also stealing the private key makes it useless.

Continuous Access Evaluation (CAE, covered in Glossary#7.32) introduces some of these properties for longer-lived tokens in supported Microsoft services. It's not full PoP, but it moves beyond pure bearer semantics by adding real-time revocation capability.

For most Entra ID scenarios today, bearer tokens are what you'll work with. Handle them accordingly: treat every token like a key, because that's what it is.

---

💬 **Have you ever found an access token in a log file, a shared document, or a place it definitely shouldn't have been?** It happens more often than people realize, and most of the time it's not malicious, just someone debugging without thinking through where the output goes. What did you do when you found it?
<!-- nav -->

---

[← Refresh Tokens: What "Keep Me Signed In" Is Actually Doing](glossary-4-7-refresh-token.md) | [Home](../README.md) | [Token Lifetime: The Trade-Off Between Security and Not Annoying Your Users →](glossary-4-9-token-lifetime.md)
