# Authentication Strength
*Why Some MFA Is Stronger Than Others*

**Part of Entra ID Glossary Series: Glossary#7.25 - Authentication Strength**

---

Two users both had MFA enabled. Both completed MFA before accessing their accounts.

User A used a TOTP code from an authenticator app. An attacker using an AiTM phishing proxy captured the code as it was submitted. They replayed it from their own session within 30 seconds. MFA was satisfied. The account was compromised.

User B used a FIDO2 security key. An attacker tried the same AiTM approach. The FIDO2 authentication failed. The key's cryptographic response was bound to the specific origin domain. The proxy couldn't replay it because the replayed response was for the wrong domain.

Both users had MFA. Only one of them had MFA that resisted the attack.

## 📊 Authentication Strength as a Classification

Authentication Strength is the framework for classifying how resistant different authentication methods are to specific attack types. It's not a single feature; it's a way of thinking about the security properties of authentication methods and the Conditional Access mechanism that lets you require specific properties.

The classification exists because "MFA enabled" is a category, not a specification. SMS OTP, TOTP codes, push notifications, FIDO2 keys, and Windows Hello are all MFA. They have dramatically different security properties. Authentication Strength makes those differences actionable in policy.

## 🔐 What Makes One Method Stronger Than Another

Authentication methods have different properties along several dimensions:

**Phishability** 🎣: Can the credential be intercepted by a proxy or relayed to the attacker? TOTP codes are valid for 30 seconds and can be relayed within that window. Push notifications can be approved on a legitimate device by a user who doesn't understand the context. FIDO2 keys use origin-bound credentials that cryptographically cannot be replayed on a different domain.

**Social engineerability** 🗣️: Can an attacker convince a user or a third party to give up the credential? SMS codes can be obtained via SIM swapping (convincing the carrier to transfer the number). FIDO2 keys require physical possession. Windows Hello biometrics can't be transferred at all.

**Credential mobility** 🔑: Can the credential be extracted from the device and used elsewhere? TOTP shared secrets can theoretically be extracted from poorly secured apps. FIDO2 credentials are stored in tamper-resistant hardware and cannot be exported. Windows Hello PINs don't leave the device.

**Second factor requirement** 👤: Does the method require two factors? A FIDO2 key that doesn't require a PIN is still one factor (possession). Windows Hello requiring biometric plus device possession is two factors from a single interaction.

## 🎚️ The Strength Spectrum

At the lower end: SMS OTP. One-time code sent via text message. Better than password alone. Defeatable by SIM swapping and, to a lesser extent, by social engineering the user into revealing the code.

In the middle: TOTP authenticator apps, push notifications without additional context. Better than SMS because they don't involve carrier infrastructure. Defeatable by AiTM proxy attacks that relay the TOTP code or MFA push notification within the validity window.

Push notifications with number matching are meaningfully stronger than basic push notifications. The user must enter a specific number shown on the sign-in screen into the app. A push notification without context (from an attacker) doesn't display a matching number, which lets the user recognize it as suspicious.

At the higher end: FIDO2 security keys, Windows Hello for Business, certificate-based authentication. These use public key cryptography with origin binding. The authentication is cryptographically tied to the specific website or application. An AiTM proxy attack fails because the credential is bound to the legitimate domain and the proxy is serving a different domain.

## 📋 The Built-In Strength Classifications

Entra ID codifies the spectrum into three built-in Authentication Strength definitions for use in Conditional Access:

**Multifactor authentication** 🟡: Any method combination that satisfies two or more factors. Includes all MFA methods, including SMS OTP.

**Passwordless MFA** 🟢: Authentication without a password. Windows Hello, FIDO2, Authenticator passwordless. Eliminates password theft as an attack vector.

**Phishing-resistant MFA** 🔴: Methods where the credential is cryptographically bound to the specific origin. FIDO2 keys, Windows Hello for Business, certificate-based authentication. AiTM attacks fail because the credential is origin-bound.

## 🎯 Applying Strength to Policy Decisions

The purpose of the classification is to match authentication strength requirements to the sensitivity of what's being protected:

Standard user access to productivity apps: any MFA is a meaningful improvement. Start here.

Privileged accounts, administrative roles, sensitive data: phishing-resistant MFA closes attack vectors that standard MFA leaves open. The attacker who can run AiTM phishing on standard MFA cannot run the same attack on FIDO2.

The practical question when deciding what strength to require: what's the worst case if this account is compromised, and does that worst case justify the deployment complexity of higher-strength methods?

For a Global Administrator, the worst case is complete tenant compromise. Phishing-resistant MFA is worth the deployment effort.

---

💬 **Has your organization differentiated authentication strength requirements between regular users and privileged accounts?** The conversation about "we have MFA" vs "we have phishing-resistant MFA for our admins" reflects a real security gap. What was the event or recommendation that drove the decision to require stronger methods for specific roles?
<!-- nav -->

---

[← Terms of Use](glossary-7-24-terms-of-use.md) | [Home](../README.md) | [Authentication Methods (Security Focus) →](glossary-7-26-authentication-methods-security.md)
