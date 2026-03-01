# Non-Compliant Device: What Happens When the Device Fails Its Security Check

**Part of Entra ID Glossary Series: Glossary#5.14 - Non-Compliant Device**

---

Monday morning, 8:47am. Three tickets arrive within 20 minutes of each other: users can't access SharePoint. By 9:15am there are 14 tickets. By 10am, 31.

The weekend's automatic Windows Update had triggered a reboot that suspended BitLocker on a batch of devices. Suspended BitLocker = non-compliant. Non-compliant = blocked from SharePoint by the Conditional Access policy. The policy had been working correctly for months. The compliance failure was new.

Non-compliant device incidents are some of the most time-sensitive support situations in Entra ID environments, because they affect users immediately, often en masse, and the fix usually requires both IT action and user action.

## ❌ What Non-Compliant Means

A non-compliant device is one that has failed at least one check in its assigned Intune compliance policy. The check-in happened, Intune evaluated the device, something didn't pass, and the device is marked non-compliant.

Non-compliant devices in a Conditional Access environment face consequences depending on how the policy is configured:

**Block access**: The user cannot access the protected resource from this device at all until compliance is restored. This is the enforcement setting for sensitive applications.

**Require MFA**: Some organizations use non-compliant as a trigger to step up to MFA rather than blocking outright. The user proves their identity more strongly to compensate for the device trust gap.

**Limited access**: Session controls can restrict what non-compliant device users can do: browser-only access, no downloads, read-only mode.

**No consequence**: If Conditional Access doesn't include a compliant device requirement for that specific app, non-compliance has no access impact. The user continues normally. This is a monitoring state only.

## 🔄 The Non-Compliant State Lifecycle

Non-compliance follows a predictable path once detected:

**Detection**: Intune's scheduled check-in runs. One or more compliance requirements fail. Device state changes to "Not Compliant" in Intune.

**Grace period**: If the compliance policy includes a grace period (1, 3, or 7 days are common), the device is marked "In Grace Period" rather than immediately non-compliant to Conditional Access. The user can still access resources while they remediate.

**Enforcement**: At grace period expiry (or immediately if no grace period), Conditional Access starts reading the non-compliant state. Access to resources requiring compliant devices is blocked.

**Remediation**: User or IT fixes the underlying issue (runs Windows Update, re-enables Defender, fixes BitLocker, sets a PIN).

**Re-evaluation**: User triggers a sync in Intune Company Portal, or waits for the next scheduled check-in. Intune re-evaluates. If everything passes, device returns to compliant.

**Access restored**: Conditional Access reads the new compliant state. Access is granted again at the next authentication attempt.

## 🔧 Common Non-Compliance Causes

The reasons devices fall out of compliance follow patterns:

🔴 **Windows updates**: Update installation can temporarily suspend BitLocker. Automatic restarts can change system state. Updates can fall behind the minimum version requirement.

🔴 **Defender definitions**: Definition updates that fail silently leave the device non-compliant for the "up-to-date definitions" requirement. Users often don't notice Defender update failures.

🔴 **BitLocker suspended**: Firmware updates, hardware changes, and some maintenance operations suspend BitLocker. The device looks encrypted in some views but fails the Intune compliance check.

🔴 **OS version**: A device that misses OS updates drifts below the minimum required version over time.

🔴 **PIN/password removed**: A user removes their device PIN for convenience. The device fails the password requirement.

## 💡 Reducing Help Desk Impact

Three things that reduce the support burden from non-compliance incidents:

**Generous grace periods**: A 3 to 7 day grace period for the most volatile compliance checks (like Defender definitions) gives users time to self-remediate before blocking occurs.

**Clear Company Portal notifications**: Intune can send push notifications to users when their device becomes non-compliant, with the specific failing check listed. Users who know what's wrong can often fix it themselves.

**Staged compliance rollout**: Enable new compliance requirements in report-only mode first, identify which devices will fail, communicate to affected users, then enable enforcement with a grace period.

The BitLocker-and-Windows-Update incident from the opening was resolved by temporarily adjusting the BitLocker compliance requirement to allow "suspended" for 48 hours, giving time for the affected devices to complete their update cycle and for IT to push a BitLocker resume script via Intune.

---

💬 **Has your organization had a mass compliance incident where a routine update or change caused widespread access blocks?** The scenario where something routine breaks compliance at scale is a good forcing function for reviewing grace period settings and remediation guidance. How did your team respond?
<!-- nav -->

---

[← Compliant Device: The Security Baseline That Has to Be Earned Continuously](glossary-5-13-compliant-device.md) | [Home](../README.md) | [User Provisioning: Accounts That Create Themselves (When It's Done Right) →](../6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-1-user-provisioning.md)
