# Compliant Device: The Security Baseline That Has to Be Earned Continuously

**Part of Entra ID Glossary Series: Glossary#5.13 - Compliant Device**

---

A manager escalated a help desk ticket to me personally. One of her team members had been locked out of the company's finance application for two days. The user's account was active. MFA was working. The Conditional Access policy was correct.

The problem was device compliance. The user's laptop had BitLocker suspended after a firmware update three days earlier. Suspended BitLocker is treated the same as disabled BitLocker by the compliance policy. The device failed. The policy blocked access. The user had no idea her encryption state had changed.

That's the thing about compliant device status: it's not a setting you enable once. It's a state the device either achieves or fails to achieve, continuously, based on its current security posture.

## ✅ What Compliant Actually Requires

A compliant device is one that has passed every check defined in its assigned Intune compliance policy. Not most checks. All of them. A single failing requirement marks the device non-compliant regardless of how many others pass.

Typical compliance requirements for a Windows corporate device:

**Encryption** 🔐
- BitLocker must be enabled and active (suspended doesn't count)

**Antivirus and Defender** 🛡️
- Microsoft Defender real-time protection must be on
- Antivirus definitions must be current (often within 7 days)
- No active threats detected above a specified severity

**System security** 🔒
- Password or PIN required to unlock
- Minimum password complexity
- Maximum device inactivity before lock

**Operating system** 💻
- Minimum OS version (ensures devices run a supported, patched build)
- Maximum OS version (rare, but sometimes used)
- Device passed Windows health attestation service checks

**Firewall and code integrity** 🧱
- Windows Firewall enabled for all network profiles
- Secure Boot enabled
- Code integrity enabled (ensures only trusted software runs at boot)

## 🔄 The Compliance Evaluation Cycle

Intune evaluates device compliance on a schedule. For Windows, the default check-in is every 8 hours. For mobile devices, it varies by platform and enrollment type.

During each evaluation, Intune:
1. Collects the current device security settings (via the management agent)
2. Compares each setting to the policy requirements
3. Marks the device compliant or non-compliant
4. Reports the result to Entra ID

That result is what Conditional Access reads. If the last check-in was 4 hours ago and the device was compliant then, Conditional Access still sees it as compliant, even if something changed in the past 4 hours. The state is only as current as the last check-in.

## ⏱️ The Grace Period

Most compliance policies include a grace period: a window between when non-compliance is detected and when Conditional Access starts blocking access. The default is typically 0 or 1 day, but organizations often set 3 to 7 days for Windows.

The grace period serves a practical purpose. Without it, a device that misses a definition update on a Friday blocks the user on Saturday, with no IT support available to fix it until Monday. A grace period gives users time to self-remediate before they lose access.

During the grace period, the device shows as "In Grace Period" in Intune. Conditional Access treats it as compliant. At grace period expiry, it becomes non-compliant and Conditional Access starts blocking.

## 🔧 How Users Remediate Compliance

When a device falls out of compliance, users typically need to:

- Run Windows Update to install the pending patch
- Re-enable Defender or update definitions
- Re-enable BitLocker (after confirming the update that suspended it is complete)
- Set a device PIN that meets complexity requirements

The Intune Company Portal app shows users exactly which compliance checks are failing and provides guidance on how to fix them. Without Company Portal, users often don't know what's wrong, which drives help desk volume.

After fixing the issue, the user can trigger a manual sync in Company Portal to force Intune to re-evaluate immediately, rather than waiting for the next scheduled check-in.

## 💡 Testing Compliance Policies Before Enforcement

New compliance policies should run in "report-only" mode first. Intune shows which devices would fail the new requirements without actually marking them non-compliant. This surfaces the scale of impact before enforcement begins.

Enabling a new compliance requirement for 2,000 devices without testing first, then discovering 40% of them immediately fall out of compliance, creates a significant incident. The report-only approach prevents that.

---

💬 **Has your organization had an unexpected mass compliance failure when a new policy was rolled out?** Discovering that a policy you assumed was reasonable would block hundreds of users tends to drive more careful impact analysis on the next rollout. What was the trigger?

#EntraID #DeviceCompliance #Intune #ConditionalAccess #ZeroTrust #MicrosoftEntra #EndpointSecurity
