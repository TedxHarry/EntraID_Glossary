# Windows Hello
*It's Not Just a PIN*

**Part of Entra ID Glossary Series: Glossary#3.7 - Windows Hello**

---

"So users just set a 4-digit PIN instead of a password? That sounds less secure."

I hear this every time I introduce Windows Hello for Business to someone. The mental model is: shorter PIN, weaker security. It makes intuitive sense. It's also completely wrong, and explaining *why* it's wrong is one of the most useful conversations I have with IT teams starting their passwordless journey.

## 🧩 The Fundamental Difference: Where the Credential Lives

A password is a secret shared between you and every server you authenticate to. You create `P@ssw0rd123!`, and that secret (in hashed form) gets stored on the Entra ID server. When you log in, your password travels across the network, gets compared to the stored hash, and authentication proceeds.

That shared secret model has one structural weakness: the credential exists in two places. If either end gets compromised, the credential is exposed. Password breaches happen at the server end. Phishing steals it from the user end. Malware can capture keystrokes as it's typed.

A Windows Hello for Business PIN works completely differently.

When a user sets up Windows Hello for Business, the device generates a public/private key pair. The private key is stored inside the device's Trusted Platform Module (TPM), a dedicated security chip on the motherboard. The public key is registered with Entra ID.

The PIN doesn't authenticate to anything. It unlocks the private key inside the TPM, locally, on the device. When authentication happens, the TPM uses the private key to sign a cryptographic challenge from Entra ID. The private key never leaves the chip.

Entra ID verifies the signature using the registered public key. No password was transmitted. No shared secret exists. The server doesn't have your PIN. The credential can't be phished because there's nothing to steal remotely.

## 🔑 PIN vs Password: The Security Properties

| | Password | Windows Hello PIN |
|---|---|---|
| Stored on server | Yes (hashed) | No |
| Transmitted during auth | Yes | No |
| Phishable | Yes | No |
| Usable from another device | Yes | No |
| Brute-forceable remotely | Yes | No |
| Backed by hardware | No | Yes (TPM) |

The PIN being short doesn't weaken it because it's never compared against a remote database. An attacker with the PIN but without physical access to that specific device gets nothing. The TPM limits incorrect PIN attempts and can lock out or wipe after repeated failures.

A 6-digit PIN protecting a hardware-bound key is meaningfully more secure than a 20-character password protecting a remotely stored hash.

## 🏢 Windows Hello vs Windows Hello for Business

This distinction matters and gets confused frequently.

**Windows Hello** is the consumer version. It's the facial recognition or fingerprint login that Windows sets up by default on personal devices. It uses a PIN or biometric to unlock the device. For home users, it's convenient and fine.

**Windows Hello for Business** is the enterprise version, deployed through Intune or Group Policy, backed by certificates or keys registered to Entra ID or an on-premises PKI. It's designed for managed enterprise environments, provides phishing-resistant MFA, and satisfies Conditional Access requirements for authentication strength.

From a user experience perspective they look identical. From a security architecture perspective they're very different. Entra ID's Conditional Access policies that require phishing-resistant MFA specifically check for Windows Hello *for Business* credentials. Consumer Windows Hello doesn't satisfy those requirements.

If your organization is relying on users' personal Windows Hello setup for phishing-resistant authentication, you may not actually have phishing-resistant authentication.

## ⚙️ What Deployment Looks Like

Windows Hello for Business can be deployed in two trust models:

**Cloud Kerberos trust** is the modern, recommended approach for hybrid environments. Entra ID issues a partial Kerberos ticket that the on-premises AD can accept. This simplifies deployment significantly and doesn't require an on-premises PKI.

**Certificate trust** is the older model, requiring a Public Key Infrastructure (PKI) to issue certificates to devices. More complex to operate but necessary in some legacy scenarios.

For cloud-only tenants, deployment is simpler: configure via Intune, users enroll during device setup or are prompted to enroll after a set number of sign-ins.

The enrollment experience from the user's side: they open a sign-in on their managed device, get prompted to set up Windows Hello for Business, go through biometric or PIN setup, and from that point use their face/fingerprint/PIN to sign in. Takes about two minutes.

## ✅ When Windows Hello for Business Is the Right Choice

- 💻 For any managed Windows device fleet where phishing-resistant MFA is a goal
- 👑 For administrator accounts with sensitive access (combined with PIM)
- 🏢 For organizations wanting to improve sign-in speed while strengthening security
- 🚫 For environments where phone-based MFA isn't practical

⚠️ Requires device TPM 2.0. Most Windows 11 devices have this by default. Some older Windows 10 hardware doesn't. Check your device inventory before scoping the rollout.

---

💬 **Has your team made the case for Windows Hello for Business yet?** The "it's just a PIN" objection is the most common pushback I encounter. How do you explain the TPM and key-binding concept to non-technical stakeholders?
<!-- nav -->

---

[← FIDO2](/3%20AUTHENTICATION/glossary-3-6-fido2.md) | [🏠 Contents](/README) | [Microsoft Authenticator →](/3%20AUTHENTICATION/glossary-3-8-microsoft-authenticator.md)
