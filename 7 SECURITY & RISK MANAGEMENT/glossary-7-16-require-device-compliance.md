# Require Device Compliance
*The Grant Control That Stops Token Theft*

📚 **Part of Entra ID Glossary Series: Glossary#7.16 - Require Device Compliance**

---

The attacker had everything. Username. Password. They'd even intercepted the MFA session token through an AiTM proxy attack. The user had signed in, clicked approve on the MFA prompt, and never knew anything was wrong.

The attacker used the stolen session token to try accessing Microsoft 365 from their machine. The Conditional Access policy for Require Device Compliance evaluated. The attacker's device wasn't enrolled in Intune. It wasn't compliant. Access denied.

MFA was bypassed. The device compliance check wasn't. That's why these are different controls.

## 💻 What Require Device Compliance Does

Require Device Compliance is a grant control in a Conditional Access policy. When it fires, the device making the access request must:

1. Be enrolled in Microsoft Intune (or a supported third-party MDM)
2. Meet all compliance policy requirements set in Intune (encryption, OS version, antivirus, password policy, etc.)
3. Have a current compliance status checked within the compliance check-in interval

If any of those conditions aren't met, access is denied. No bypass. No step-up option. The device itself is the gating factor.

This is fundamentally different from MFA. MFA verifies the user's identity. Device compliance verifies the device's health and management status. An attacker who steals a valid MFA token still can't access resources from their unmanaged device.

## 🛡️ Why Device Compliance Matters for Modern Attacks

The AiTM attack scenario is common and well-understood by attackers. Tools to execute it are available as phishing kits on criminal forums. The attack flow:

1. User is directed to a phishing page that proxies the real Microsoft sign-in
2. User enters credentials. The proxy passes them to Microsoft.
3. Microsoft requires MFA. The proxy shows the user the MFA prompt.
4. User completes MFA. The proxy passes the response to Microsoft.
5. Microsoft issues a session token. The proxy captures it.
6. Attacker uses the stolen token from their own device.

Every step except the last one involves the legitimate user. MFA is satisfied legitimately. The session token is valid. But when the attacker uses it from an unmanaged device, the device compliance check fails. The token doesn't grant access.

Device compliance breaks this attack class specifically because it evaluates the device making the current request, not the device that completed authentication.

## ⚙️ What Compliance Means

Compliance is assessed by Intune compliance policies. Organizations define what "compliant" means:

**Windows** 🪟: BitLocker encryption enabled, Windows Defender running with current definitions, OS version above minimum, no detected malware, password/PIN required, Secure Boot enabled.

**macOS** 🍎: FileVault encryption, Gatekeeper enabled, OS version requirements, password policy.

**iOS/iPadOS** 📱: OS version minimum, device not jailbroken, passcode required.

**Android** 🤖: OS version minimum, device not rooted, Google Play Protect enabled, passcode required.

Each platform's compliance policy is configured separately in Intune. A device must satisfy all requirements to be marked compliant. If any single requirement fails, the device is non-compliant.

Compliance status is checked on a schedule. The check-in interval (typically every 8 hours for Windows) means compliance is refreshed regularly, not just at enrollment. A device that was compliant yesterday but hasn't updated Windows can become non-compliant today.

## 🔧 Implementation Dependencies

Require Device Compliance as a Conditional Access grant control only works if Intune is deployed. This is the most common blocker for organizations that want this control:

- Devices must be enrolled in Intune
- Compliance policies must be configured and assigned to device groups
- Devices must have completed at least one compliance check-in to have a known status

A device with no compliance data is treated as non-compliant. This creates an enrollment catch-22: a new device that isn't enrolled can't become enrolled if it can't access the resources needed to complete enrollment. Always exclude the Microsoft Intune and MDM enrollment endpoints from device compliance requirements.

## 🔗 Require Compliance vs Require Hybrid Join

Both are device-based grant controls. They're not the same:

**Require Hybrid Azure AD Joined** 🖥️: Device must be domain-joined on-premises AND registered in Entra ID. Validates the device is in the right management structure. Does NOT validate device health or compliance with security policies.

**Require Compliant Device** ✅: Device must be enrolled in MDM AND must meet all compliance policy requirements. Validates both management enrollment AND active security health.

Require Compliant Device is the stronger control. A hybrid joined device that hasn't been patched in six months is joined but not necessarily compliant. Require Compliant Device would block it. Require Hybrid Join wouldn't.

## 💡 AND Combinations for Defense in Depth

Require MFA AND Require Compliant Device is the combination that closes the most attack vectors:

- Password alone: defeated by credential theft
- Password + MFA: defeated by AiTM
- Password + MFA + Compliant Device: the attacker needs valid credentials, MFA access, AND a managed compliant device. All three are rarely achievable by an external attacker.

This is the recommended configuration for access to sensitive resources: both requirements, in AND combination.

---

💬 **When you enforced Require Device Compliance, what was the first non-compliant device category that surprised you?** Often it's a device that's been in the environment for years and hasn't been updated because "it just works." What was the compliance failure that surfaced devices you didn't know were out of date?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Require MFA](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-15-require-mfa.md) | [🏠 Contents](/README) | [Require Authentication Strength →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-17-require-authentication-strength.md)
