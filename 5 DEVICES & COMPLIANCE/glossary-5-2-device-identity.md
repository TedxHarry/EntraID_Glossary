# Device Identity: When the Device Itself Has to Prove Who It Is

**Part of Entra ID Glossary Series: Glossary#5.2 - Device Identity**

---

A user's laptop was stolen from a coffee shop. IT disabled the user's Entra ID account within the hour. What they didn't do was disable the device itself.

The laptop had a local Windows account. The attacker used cached credentials. Company files that had synced locally were right there, accessible without touching Entra ID at all. The user's account was locked. The device was never revoked.

That conversation is why device identity matters as something separate from user identity, and why Entra ID maintains an identity object for each device, not just each person.

## 🖥️ What a Device Identity Is

When a device is registered or joined to Entra ID, a device object is created in the directory. This object represents the device as a security principal, just as a user object represents a person.

The device object stores:

- **Device ID**: A unique GUID identifying this device in Entra ID
- **Display name**: Usually the computer hostname
- **Operating system**: Windows, iOS, Android, macOS
- **Join type**: Entra Registered, Entra Joined, or Hybrid Entra Joined
- **Compliance state**: Reported from Intune
- **Enabled state**: Whether the device is active or disabled
- **Last sign-in activity**: When the device last authenticated

That enabled state is critical. Just as you can disable a user account, you can disable a device object. When a device is disabled, it can no longer obtain device-level authentication tokens. The laptop in the theft scenario should have had its device object disabled immediately.

## 🔑 How Device Identity Enables Policies

Device identity transforms devices from anonymous network endpoints into known, authenticated principals. Once a device has an identity in Entra ID, the platform can make access decisions based on that identity.

Conditional Access policies can require:
- ✅ Device is registered with Entra ID (basic identity exists)
- ✅ Device is Entra Joined or Hybrid Joined (corporate management)
- ✅ Device is compliant (passes Intune compliance checks)
- ✅ Device is marked as trusted

Without device identity, Conditional Access can only see user attributes, sign-in risk, and location. With device identity, it sees the full security posture of the hardware making the request.

## 🔐 How Devices Authenticate

A device with an Entra ID identity authenticates using a device certificate issued during the join process. On Windows, this certificate is stored in the device's Trusted Platform Module (TPM), making it hardware-bound.

When a user signs in on an Entra Joined Windows device, the device presents its certificate to Entra ID during authentication. The sign-in token includes device claims. Resource servers and Conditional Access policies can see not just who signed in, but what device they're using and what its current security state is.

This device certificate is what makes Hybrid Entra Join and device compliance enforcement possible. The device has a cryptographic identity that it proves at authentication time, not just a registration record in a database.

## ⚠️ Device Identity vs Device Management

Having a device identity in Entra ID doesn't mean the device is managed. Registration creates an identity. Enrollment in Intune (or another MDM) adds management capability.

An Entra Registered personal device has an identity Entra ID recognizes. But if it's not Intune-enrolled, there's no compliance policy being evaluated, no configuration profiles being applied, no software deployment happening. The device exists to Entra ID, but Entra ID doesn't know anything about its security state beyond what the device itself reports.

Requiring device compliance in Conditional Access is stronger than requiring device identity alone, because compliance verification requires active management reporting.

## 💡 What to Do When a Device Is Lost or Stolen

The immediate steps for a lost or compromised device:

1. **Disable the device object** in Entra ID (blocks device-level authentication immediately)
2. **Revoke the user's sessions** (invalidates access tokens tied to this device)
3. **Initiate a remote wipe** via Intune if the device is enrolled
4. **Review recent sign-in activity** for the device to understand what was accessed

Disabling the device object prevents the device from getting new device-level tokens. Combined with user session revocation, it closes both the device and user authentication paths.

---

💬 **Has a lost or stolen device ever exposed a gap in your offboarding or incident response process?** The device object in Entra ID is often the last thing people think to disable, focusing entirely on the user account. What's in your current device incident response checklist?

#EntraID #DeviceIdentity #ZeroTrust #DeviceManagement #MicrosoftEntra #ConditionalAccess #EndpointSecurity
<!-- nav -->

---

[← Device Compliance: When the Device Has to Earn Its Access](glossary-5-1-device-compliance.md) | [Home](../README.md) | [Device Registration: Three Ways to Join a Device to Entra ID (They're Not the Same) →](glossary-5-3-device-registration.md)
