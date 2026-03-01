# Device Compliance: When the Device Has to Earn Its Access

**Part of Entra ID Glossary Series: Glossary#5.1 - Device Compliance**

---

A remote worker called on a Monday morning, unable to access SharePoint. She'd been using it from the same laptop for two years. Nothing had changed on her end.

What had changed: over the weekend, the security team had enabled a new Conditional Access policy requiring compliant devices for SharePoint access. Her laptop's Windows Defender had been disabled (she'd turned it off months ago to troubleshoot a conflict and never re-enabled it), and Intune had been flagging it as non-compliant for weeks. The policy change made that flag consequential.

Her device wasn't compliant. The policy enforced it. The access was blocked. All of that was working exactly as designed.

## 📋 What Device Compliance Actually Is

Device compliance is a state, not a product. It's the result of evaluating a device against a set of rules defined in a compliance policy, usually managed through Microsoft Intune.

A compliance policy is a set of requirements: minimum OS version, disk encryption enabled, password required, Defender real-time protection on, specific firewall state, maximum OS build age. Intune evaluates each enrolled device against these requirements continuously and assigns one of three states:

- ✅ **Compliant**: All requirements met
- ❌ **Non-compliant**: One or more requirements not met
- ⏳ **Not evaluated**: Policy hasn't run yet, or device just enrolled

That compliance state is reported to Entra ID and becomes available as a signal in Conditional Access policies. A policy can say "require compliant device" as a grant control, and Entra ID enforces it at every authentication attempt.

## 🔒 How Compliance Connects to Access

The connection between compliance and access is Conditional Access. Without it, compliance state is just a monitoring metric. With it, compliance state becomes an enforcement gate.

A typical enterprise Conditional Access policy:

- **If**: User is in the "All Employees" group AND app is SharePoint Online
- **And if**: Device is not compliant
- **Then**: Block access (or require additional MFA as a fallback)

This means a device that drifts out of compliance automatically loses access to protected applications at the next authentication attempt. No admin action required. No manual review process. The enforcement is continuous and automatic.

## 🔧 What Goes Into a Compliance Policy

Compliance policies are configured in Intune and typically include:

**Device health checks** 🏥
- Device has passed Windows health attestation
- BitLocker encryption is enabled
- Secure Boot is on
- Code integrity is enabled

**System security** 🔐
- Password is required with minimum complexity
- Maximum minutes of inactivity before password is required
- Password expiration and reuse rules

**Defender status** 🛡️
- Real-time protection is enabled
- Antivirus definitions are up to date
- No detected malware in active state

**OS version requirements** 💻
- Minimum OS version (blocks devices running outdated, unpatched operating systems)
- Maximum OS version (rare, but used in some regulated environments)

Each requirement that fails contributes to a non-compliant status. One failing requirement = non-compliant, regardless of how many others pass.

## ⏱️ Compliance Evaluation Timing

Intune doesn't evaluate compliance in real-time every second. Devices check in on a schedule (typically every 8 hours for Windows, more frequently after a sync is forced). After a compliance policy change, there's a window before all devices have been re-evaluated.

This means: after the remote worker's organization enabled the new Conditional Access policy, devices that were already marked non-compliant immediately lost access. Devices not yet evaluated had a brief grace period until Intune ran its next compliance check.

For urgent situations, admins can force a sync from the Intune portal, triggering immediate re-evaluation on specific devices.

## 💡 Compliant vs Managed: An Important Distinction

Compliant means the device has passed its compliance policy checks. Managed means the device is enrolled in Intune.

These are related but not identical. A device can be enrolled in Intune (managed) but still be non-compliant because it fails a requirement. A device can theoretically have a compliance state reported without being fully managed, in some configurations.

Conditional Access has separate conditions for "managed device" (Intune-enrolled or Hybrid Entra joined) and "compliant device." Requiring compliant is the stronger condition: it implies the device is managed AND passes all compliance checks.

---

💬 **Have you had a situation where a Conditional Access compliance requirement blocked a user who was surprised it was possible?** The moment someone realizes their device's security state directly affects their application access is usually when the conversation about patch management gets a lot more productive. What changed after that?
<!-- nav -->

---

[← Token Security: Treating Every Token Like the Key It Is](../4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-19-token-security.md) | [Home](../README.md) | [Device Identity: When the Device Itself Has to Prove Who It Is →](glossary-5-2-device-identity.md)
