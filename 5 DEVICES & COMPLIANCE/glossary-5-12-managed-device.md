# Managed Device
*Enrolled Isn't the Same as Secure*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #5.12 - Managed Device

---

## 🎯 TL;DR

- A managed device is enrolled in Intune and receives policies, apps, and compliance checks from the organization
- Management enables remote wipe, configuration enforcement, and detailed inventory
- Not all managed devices are compliant : a device can be enrolled but fail compliance requirements


A security audit came back with a finding: 23% of corporate devices accessing sensitive applications were "unmanaged." The IT team pushed back. "All our corporate devices are enrolled in Intune. How can they be unmanaged?"

The auditor pulled up the Conditional Access logs and pointed to devices with a join type of "Entra Registered" accessing SharePoint. These were employees' personal phones. Enrolled? No. Managed? No. Accessing sensitive data? Yes.

The IT team had been thinking about managed devices in terms of their corporate Windows fleet. They hadn't accounted for the mobile surface.

## 📋 What "managed" actually means

A managed device is one that is enrolled in a mobile device management solution (typically Intune) and actively receiving policies from it. The organization has a management relationship with the device through which it can:

- Evaluate and report compliance state
- Push configuration settings
- Deploy or remove applications
- Trigger remote wipe if needed

in Entra ID's Conditional Access context, "managed device" refers specifically to devices that are either:

- **Intune-enrolled**: Enrolled in Intune MDM with an active management relationship
- **Hybrid Entra Joined**: Joined to both on-premises Active Directory and Entra ID, with Group Policy providing management from the on-premises side

An Entra Registered personal device is not managed in this sense, even though Entra ID knows it exists.

## 🔒 Managed vs compliant: the critical distinction

Managed means the device is under management. Compliant means the device passes its compliance policy checks. These are related but not identical states.

| State | What It Means |
|-------|--------------|
| Managed and compliant | Enrolled in Intune AND passing all compliance checks |
| Managed but non-compliant | Enrolled in Intune BUT failing one or more compliance checks |
| Not managed | Not enrolled, no management relationship |

A device can be enrolled in Intune (managed) but have Defender disabled, BitLocker off, and a 90-day-old OS patch level. It's managed in the sense that Intune can push policies to it. It's non-compliant in the sense that it's currently failing those policies.

Conditional Access has separate grant controls for each:
- **Require device to be managed**: Satisfied by Intune enrollment or Hybrid join. Doesn't require compliance.
- **Require device to be compliant**: Requires managed AND passing compliance. Stronger requirement.

For sensitive resources, requiring compliant is almost always the right choice. Requiring only "managed" means a device with disabled Defender gets through as long as it's enrolled.

## 🔧 How devices become managed

For corporate Windows devices, management typically happens through:

**Windows Autopilot**: New device ships to employee, auto-enrolls in Intune during first-run setup with no IT hands-on-keyboard required.

**Automatic enrollment via Group Policy**: Existing domain-joined devices get a Group Policy that triggers MDM auto-enrollment. Devices enroll silently in the background.

**Manual enrollment**: User opens Settings and manually enrolls. Less common for corporate devices, used for testing or one-off scenarios.

For mobile devices:

**Apple Device Enrollment Program (ADE)**: Corporate-owned iPhones and iPads auto-enroll when restored or set up for the first time, with no user interaction required.

**Android Enterprise**: Various enrollment methods depending on device ownership model (Fully Managed, Dedicated, Work Profile).

**Company Portal**: User-initiated enrollment for personal devices accepting MDM management.

## ⚠️ The managed device assumption gap

The most common misconception: "our devices are managed" meaning "our Windows fleet is enrolled." What this misses:

- 📱 Personal phones used for work email: not managed unless explicitly enrolled
- 💻 Contractor laptops: personal devices, almost never managed by your organization
- 🏠 Home computers accessing corporate web apps: not managed
- 📟 Shared/kiosk devices: may be enrolled but with different compliance policies

Conditional Access gives you visibility into what's actually hitting your resources. The sign-in logs show device management state for every authentication. Running a report on devices accessing your most sensitive applications often reveals a managed device rate lower than the IT team expects.

## 💡 Require managed as a minimum bar

For organizations that can't yet enforce full compliance on all devices, requiring "managed device" as a minimum for medium-sensitivity resources is a reasonable interim step. It closes the personal device gap while compliance policy rollout is underway.

Then, as compliance policies are tuned and devices pass reliably, the policy requirement upgrades to "compliant" for sensitive resources.

---

💬 **When your organization ran its first Conditional Access report on device management state, what percentage of accesses were coming from unmanaged devices?** The gap between "we think our devices are managed" and "here's what's actually hitting our apps" is often surprising. What did the data show?
✍️ TedxHarry

<!-- nav -->

---

[← Device State](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-11-device-state.md) | [🏠 Contents](/README) | [Compliant Device →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-13-compliant-device.md)
