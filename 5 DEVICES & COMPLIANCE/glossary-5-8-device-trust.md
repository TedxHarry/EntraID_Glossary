# Device Trust: Not All Devices Are Equally Trustworthy (And Entra ID Knows It)

**Part of Entra ID Glossary Series: Glossary#5.8 - Device Trust**

---

A consultant connected to a client's SharePoint from her personal laptop using her guest account. Same Conditional Access policy applied. Same user risk level. Completely different access experience from a corporate employee on a managed device.

The employee got through without additional prompts. The consultant hit an MFA requirement, then was limited to read-only access in the browser. Not because of who they were, but because of the device they were on.

That's device trust working exactly as designed: the organization makes different decisions based on the confidence level it has in the device making the request.

## 🏗️ The Device Trust Hierarchy

Entra ID recognizes different levels of device trust based on how the device registered and what management state it's in. From lowest to highest trust:

**Unknown device** 📵
No device identity in Entra ID. The request comes from a browser or app on a device Entra ID has never seen. No claims about the device appear in the token. Conditional Access can treat these as untrusted and require MFA, restrict to browser-only access, or block entirely.

**Entra Registered device** 📱
A personal device where the user has registered their work account. Entra ID knows the device exists. Basic device claims appear in tokens. This is the minimum trust level for BYOD scenarios. Most organizations don't give registered devices the same trust as managed corporate devices.

**Entra Joined device** 💻
A corporate device joined directly to Entra ID and typically enrolled in Intune. Strong device identity backed by a device certificate stored in the TPM where available. Compliance state is actively reported. This is the trusted corporate device level for cloud-first organizations.

**Hybrid Entra Joined device** 🏢
A corporate device joined to both on-premises Active Directory and Entra ID. The highest trust level for organizations running hybrid environments. Authentication can satisfy both Kerberos (on-premises) and modern auth (cloud) scenarios.

**Compliant device** ✅
Any of the joined types above, plus passing all active Intune compliance policy checks. This is the highest trust state a device can achieve. Compliant implies managed and meeting security requirements.

## 🔒 How Conditional Access Uses Device Trust

Conditional Access grant controls map directly to trust levels:

- **Require device to be marked as compliant**: Highest bar. Device must be joined and meet all compliance policy requirements.
- **Require Hybrid Entra Joined device**: Corporate devices from hybrid organizations. Joined to on-premises AD and Entra ID.
- **Require Entra Joined or Hybrid Entra Joined**: Corporate devices, either join type.
- No device requirement: User-focused policy only, device trust not evaluated.

Organizations typically use different policies for different resource sensitivity:

🔵 **Low sensitivity** (general productivity apps): Allow access from any device with MFA
🟡 **Medium sensitivity** (HR systems, finance apps): Require registered or managed device
🔴 **High sensitivity** (admin tools, payroll, strategic data): Require compliant managed device

## ⚠️ The Trust Gap: Registration vs Compliance

The most common device trust misconfiguration I've seen: organizations set Conditional Access to require "Entra Joined" devices, thinking this means secure corporate devices. But an Entra Joined device with Defender disabled, BitLocker off, and a 6-month-old OS still satisfies the "joined" requirement.

"Joined" means the device has an identity and a management relationship with the organization. "Compliant" means the device is actively meeting defined security requirements.

For sensitive resources, require compliant, not just joined. The compliance requirement is what gives the trust level its actual security meaning.

## 💡 Session Controls and Device Trust

Even after granting access, Conditional Access session controls let organizations adjust what the user can do based on device trust:

- Unmanaged devices: restrict to browser-only, no downloads, no copy/paste of sensitive content (via Microsoft Defender for Cloud Apps integration)
- Managed but non-compliant devices: allow access but trigger remediation guidance
- Compliant devices: full access within normal user permissions

This creates a gradient of access rather than a binary allow/deny, which is much more practical for real-world environments where not every device is fully managed.

---

💬 **Has your organization built a tiered access model based on device trust levels?** The move from binary "allowed or blocked" to a tiered model based on device state is one of the most meaningful Zero Trust improvements you can make. What did your trust tiers end up looking like?

#EntraID #DeviceTrust #ZeroTrust #ConditionalAccess #DeviceCompliance #MicrosoftEntra #EndpointSecurity
