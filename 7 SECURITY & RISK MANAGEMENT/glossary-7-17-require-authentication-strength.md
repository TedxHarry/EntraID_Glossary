# Require Authentication Strength
*Not All MFA Is Equal*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #7.17 - Require Authentication Strength

---


A Global Administrator had MFA enabled. They used SMS as their MFA method. An attacker who had their password called their mobile carrier, posed as the administrator, and convinced them to transfer the number to a new SIM. The attacker received the SMS code. They signed in.

The organization had MFA. They did not have the right MFA. SMS is an MFA method. It's also a method that can be defeated by social engineering a mobile carrier. For a standard user's email access, SMS MFA is a meaningful improvement. For a Global Administrator account, it's insufficient.

This is the problem Require Authentication Strength is designed to solve.

## 🔐 What authentication strength is

Authentication Strength is a Conditional Access grant control that lets you specify not just that MFA is required, but which specific MFA methods are acceptable for a given resource or scenario.

Instead of "require any MFA," you can require "MFA from this approved set of methods." The distinction matters because authentication methods have significantly different security properties:

**Phishable methods** 🎣: SMS OTP, voice call, TOTP codes from authenticator apps. These generate a code or response that can be intercepted by a proxy or social engineered from the user. An AiTM attack can capture these.

**Phishing-resistant methods** 🛡️: FIDO2 security keys, Windows Hello for Business, certificate-based authentication. These use cryptographic binding between the credential and the specific website. A phishing proxy can't replay the credential because the credential is only valid for the exact domain it was issued for.

## 📋 The built-in strength levels

Entra ID provides three built-in authentication strength definitions:

**Multifactor authentication** 🟡: Any combination that satisfies MFA. Password + SMS OTP qualifies. Password + Authenticator push qualifies. Passwordless phone sign-in qualifies. This is the broadest MFA requirement.

**Passwordless MFA** 🟢: Authentication without a password factor. Windows Hello for Business, FIDO2 security keys, or Microsoft Authenticator passwordless phone sign-in. No password means no password to steal. Still includes some methods that could theoretically be phished.

**Phishing-resistant MFA** 🔴: The strongest built-in strength. Requires FIDO2 security keys, Windows Hello for Business, or certificate-based authentication. These methods are cryptographically bound to the specific relying party. An AiTM proxy attack cannot succeed because the credential is tied to the legitimate domain's origin.

## 🎯 When to use each strength

The right strength depends on what's being protected:

**Standard users, standard apps** 🟡: Multifactor authentication strength. Any MFA method is acceptable. Dramatically better than password only. SMS OTP is fine for accessing email and productivity apps.

**High-value apps and sensitive data** 🟢: Passwordless MFA strength. Removes the password from the equation. Users authenticate with something they have (device) plus something they are (biometric) or something they know (PIN, which is device-local and not network-transmittable).

**Privileged access and administrative roles** 🔴: Phishing-resistant MFA strength. Global Administrators, Privileged Role Administrators, Exchange Administrators, and similar high-value roles should only authenticate with methods that cannot be phished. A compromised Global Admin account is catastrophic. The authentication method for these accounts should reflect that.

## 🛠️ Custom authentication strengths

Beyond the three built-in strengths, organizations can define custom authentication strength policies. A custom strength specifies an exact list of allowed authentication method combinations.

Use cases for custom strengths:

**FIDO2 only** 🔑: Some high-security environments want to mandate hardware keys and nothing else. A custom strength that permits only FIDO2 security keys enforces this.

**Specific Authenticator configurations** 📱: Require Microsoft Authenticator with number matching enabled, but not TOTP codes from other apps.

**Certificate-based authentication** 📜: Smart card or certificate-based auth for specific compliance scenarios.

Custom strengths are configured in Entra admin center under Security > Authentication Methods > Authentication Strengths.

## 🔗 Authentication strength vs require MFA

These two grant controls are related but distinct:

**Require MFA**: Requires the user to complete a second factor. Accepts any authentication method that satisfies MFA. Doesn't distinguish between SMS and FIDO2.

**Require Authentication Strength**: Specifies which methods are acceptable. Can be set to require phishing-resistant methods specifically.

When a policy uses "Require authentication strength" with the "Phishing-resistant MFA" built-in, it requires MFA and constrains the acceptable methods. It's a more specific control.

For most organizations, the progression is:
1. Start with Require MFA (any method, broad coverage)
2. Move privileged accounts to Require Authentication Strength: Phishing-resistant
3. Consider higher strengths for sensitive applications as passwordless rollout matures

## ⚠️ The registration dependency

Authentication strength policies only work if users have the required methods registered. Requiring phishing-resistant MFA for all administrators before any administrators have FIDO2 keys or Windows Hello configured will lock out all administrators.

Deployment sequence matters: register the required methods first, verify coverage, then enforce the strength requirement. Run the policy in report-only mode to see who would fail before switching to enforcement.

---

💬 **Have you differentiated authentication strength requirements between regular users and privileged accounts?** The realization that "MFA enabled" isn't good enough for admin accounts, because SMS OTP is technically MFA, is often the catalyst for deploying FIDO2 keys or enforcing Windows Hello. What drove your organization to require stronger methods for privileged access?
✍️ TedxHarry


> 🔑 **Licensing:** Authentication strength as a CA grant control requires **Entra ID P1**. Phishing-resistant strength enforcement is included in P1.

<!-- nav -->

---

[← Require Device Compliance](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-16-require-device-compliance.md) | [🏠 Contents](/README) | [Report-Only Mode →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-18-report-only-mode.md)
