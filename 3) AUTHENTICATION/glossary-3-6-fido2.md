# FIDO2: Why a Small USB Stick Can Eliminate Phishing from Your Attack Surface

**Part of Entra ID Glossary Series: Glossary#3.6 - FIDO2**

---

I handed a YubiKey to a sceptical security engineer and told her it would make her admin account essentially immune to phishing. She turned it over in her hand, looked at the USB plug on one end, and said: "This little thing?"

Yes. This little thing.

FIDO2 is the reason why. Understanding what FIDO2 actually is, and specifically why it's phishing-resistant (not just phishing-harder), is what makes it click.

## 📖 What FIDO2 Is

FIDO2 is not a product. It's a set of open standards developed by the FIDO Alliance, a consortium of technology companies including Microsoft, Google, Apple, and hardware manufacturers. The standard covers how devices and browsers perform passwordless, phishing-resistant authentication.

It has two components:

**WebAuthn** is the web standard that defines how browsers communicate with authenticators. It's a W3C standard, meaning it's built into every modern browser natively.

**CTAP2** (Client to Authenticator Protocol 2) defines how a browser or operating system talks to an external authenticator, like a USB security key or a platform authenticator (device built-in).

When someone says "FIDO2 authentication," they mean authentication using this combined standard, where the authenticator generates a cryptographic signature that proves the user's identity without transmitting a secret that can be stolen.

## 🔐 Why FIDO2 Is Actually Phishing-Resistant (Not Just Harder to Phish)

This is the property that matters most and gets explained poorly most often.

When you register a FIDO2 key with a website or service, the key generates a unique public/private key pair *for that specific origin* (the domain name). The public key is stored on the server. The private key never leaves the key.

When you authenticate, the server sends a challenge. The key signs that challenge with the private key. The signature is only valid for the specific origin it was created for.

Here's the critical part: **the origin is cryptographically bound**. The key will refuse to sign a challenge from a different origin.

So if an attacker creates `login.micros0ft.com` to phish your credentials, and somehow tricks you into opening it:

- The browser sees `micros0ft.com` as the origin
- Your FIDO2 key has no credentials registered for `micros0ft.com`
- Authentication simply fails
- There's no password to steal, no code to intercept, no notification to manipulate

The attacker gets nothing. Not "less than they wanted." Nothing. The key won't authenticate to a site it wasn't registered with, period. This is why phishing-resistant is the accurate term, not phishing-resistant.

## 🔌 Hardware Keys vs Platform Authenticators

FIDO2 authenticators come in two forms:

**Hardware security keys** are external devices. Common examples include YubiKey (multiple form factors: USB-A, USB-C, NFC), Feitian keys, and Google's Titan Key. Users carry the key and plug it in or tap it to authenticate.

Advantages: works across multiple devices, survives device replacement, tangible physical object the user understands they must protect.

Disadvantages: can be lost, an additional device to manage, requires a USB port or NFC reader, has a per-unit cost (typically $25-$60 per key).

**Platform authenticators** are built into the device itself. Windows Hello for Business is a platform authenticator. Apple Face ID and Touch ID in Safari are platform authenticators. The TPM chip on the device serves as the hardware-backed key store.

Advantages: nothing extra to carry, frictionless experience, already provisioned with the device.

Disadvantages: credentials are tied to that specific device. If the device is replaced, the user must re-enroll. Not appropriate as a sole authentication method for admin accounts where device availability might vary.

## 🏢 Deploying FIDO2 Keys in Entra ID

Enabling FIDO2 in Entra ID takes two steps:

1. **Enable FIDO2 security keys** in the Authentication Methods Policy under Protection > Authentication Methods
2. **Optionally restrict** to specific makes and models using AAGUIDs (authenticator attestation globally unique identifiers) if your organization wants to enforce a specific approved key list

Users then register their keys at `mysignins.microsoft.com` under Security Info. They plug in the key, create a PIN for the key, and the registration is complete. From that point, signing in involves entering their username, inserting (or tapping) the key, and entering the key's PIN or biometric.

💡 For admin accounts: consider requiring two FIDO2 keys per admin (registered as backup). A single key lost is a locked-out admin with no recovery path if no backup method is registered.

## ✅ Where FIDO2 Fits in Your Authentication Strategy

FIDO2 security keys are the right choice for:

- 👑 Administrator and privileged accounts where phishing-resistant MFA is required
- 🏭 Shared workstation environments where multiple people use the same machine (factory floors, call centres, nursing stations)
- 🚫 Environments where personal phones can't be used (no-phone-in-the-building policies)
- 🔒 High-assurance scenarios requiring the strongest available authentication

---

💬 **Have you deployed FIDO2 security keys in your organization?** Which hardware did you choose, and what was the user experience feedback? The enrollment process is surprisingly straightforward once people have the key in hand.

#EntraID #FIDO2 #Passwordless #CloudSecurity #MicrosoftEntra #PhishingResistant #YubiKey
