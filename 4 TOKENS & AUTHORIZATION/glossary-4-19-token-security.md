# Token Security
*Treating Every Token Like the Key It Is*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #4.19 - Token Security

---


A developer shared a debug log with me over Teams. They were troubleshooting API call failures. The log was pasted directly into the chat message: a full OAuth flow trace, access tokens included.

Those tokens were valid for another 47 minutes. I told them to revoke the user session immediately and get fresh tokens. They asked why - the chat was private, after all.

The answer is that "private" doesn't mean "secure." Log files, screenshots, chat messages, bug reports, shared documents: tokens end up in all of these. A token in a Teams chat is a credential in a Teams chat. It's valid until it expires, regardless of where it's sitting.

## 🔑 The fundamental principle

An access token is a credential. Treat it exactly like you'd treat a password, with one important difference: a password requires the attacker to know your username and figure out where to authenticate. A bearer token can be used by anyone who has it, to any endpoint it's valid for, without knowing anything else about the user.

"Treat it like a password" means:
- Don't put it in logs
- Don't share it in communication channels
- Don't store it where others can read it
- Don't transmit it over unencrypted connections

These aren't guidelines for mature security programs. They're the minimum baseline.

## 🔐 Transport: HTTPS without exception

Bearer tokens must travel over HTTPS. This is not negotiable.

HTTP connections expose the entire request, including the Authorization header, to anyone who can observe the network: proxies, load balancers, ISPs, network monitoring tools, other devices on the same network segment. An access token in an HTTP Authorization header is an access token in plaintext on the wire.

Modern browsers and frameworks enforce HTTPS in most contexts, but API clients, scripts, CLI tools, and legacy code don't always. Check that:

- ✅ All API endpoints your application calls use HTTPS
- ✅ Your application rejects HTTP or upgrades it to HTTPS
- ✅ Infrastructure components (reverse proxies, load balancers) don't accept both HTTP and HTTPS for the same endpoint

## 💾 Storage: where tokens live matters significantly

How tokens are stored between uses determines the attack surface at rest:

🟢 **Memory only**: Safest option. The token exists while the process runs and is gone when it stops. No persistence means nothing to steal between sessions. MSAL stores tokens in memory by default; this is intentional.

🟡 **Secure platform storage**: Good choice for persistence. iOS Keychain, Android Keystore, and Windows Data Protection API (DPAPI) encrypt credentials at rest using keys tied to the device or user account. MSAL uses these when persistence is explicitly needed.

🔴 **Browser localStorage**: Accessible to any JavaScript running on the page. An XSS vulnerability in your application, or in any third-party script your application loads, can read and exfiltrate tokens stored here. Use the MSAL browser library, which handles token storage correctly and keeps tokens out of localStorage.

🔴 **Database columns (plaintext)**: Tokens stored as readable text in a database are credentials at rest in a queryable system. If the database is compromised, the tokens are compromised. If persistence is genuinely required, store an encrypted form with keys managed separately.

🔴 **Log files**: Never log token values. Log files are shared with support teams, aggregated in SIEM systems, sent to vendors, and retained for years. An access token that appears in a log file at 2pm is a live credential sitting in a log file at 2pm.

## 📌 ⏱️ expiry: a safety net, not a strategy

Short token lifetimes limit damage. A token stolen with 3 minutes remaining is useful for 3 minutes. A token stolen at issuance is useful for up to 60 minutes. This is why access tokens have short lifetimes by default, and why CAE-capable services can safely extend them to 24 hours while retaining real-time revocation capability.

But don't treat expiry as your primary security control. A well-stored, well-transmitted token expiring in 60 minutes is far safer than a poorly stored token with a 10-minute lifetime. The goal is to avoid losing tokens in the first place.

## 💡 If you find a token that shouldn't be there

Revoke first, investigate second. If you find a live access token somewhere it has no business being, the immediate action is revoking the user's sessions via the Entra admin center or `Revoke-MgUserSignInSession` in PowerShell. Then investigate how it got there and close the path that allowed it.

Depending on the token's permissions and how long it was accessible, a breach notification process may also be warranted.

---

💬 **Have you found an access token somewhere it had no business being - a log file, a public repository, a chat message?** It happens more often than organizations realize, and it's usually not malicious, just someone debugging without thinking through where the output lands. What was the cleanup process?
✍️ TedxHarry

<!-- nav -->

---

[← SAML](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-18-saml.md) | [🏠 Contents](/README) | [Device Compliance →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-1-device-compliance.md)
