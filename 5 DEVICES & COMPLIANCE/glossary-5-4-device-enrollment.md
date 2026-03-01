# Device Enrollment
*The Difference Between Knowing a Device Exists and Managing It*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#5.4 - Device Enrollment**

---

## 🎯 TL;DR

- Device enrollment is the Intune MDM step that enables remote management, compliance checking, and policy push
- Enrolled devices receive compliance policies, configuration profiles, and app deployments from Intune
- Enrollment ≠ registration: registration is identity; enrollment is management


After a security incident where a former employee's personal phone still had corporate email accessible three weeks after offboarding, the security team wanted a clear answer: "How do we make sure this never happens again?"

The answer involved understanding two things that people often blur together: registration (Entra ID knows the device exists) and enrollment (the organization can actually manage and control the device). They're sequential steps, not synonyms. And in that incident, the device was registered but not enrolled, which meant IT had no way to remotely remove corporate data when the employee left.

## 📲 What Enrollment Actually Means

Device enrollment is the process of bringing a device under management control, typically through Microsoft Intune. When a device is enrolled:

- ✅ Intune can push compliance policies to the device and evaluate them
- ✅ Intune can push configuration profiles (Wi-Fi settings, VPN, certificates)
- ✅ Intune can deploy applications to the device
- ✅ Intune can trigger a remote wipe or selective wipe when needed
- ✅ Compliance state is actively reported to Entra ID for Conditional Access

Without enrollment, a device has an identity in Entra ID but the organization has no visibility into its security posture and no ability to act on it.

## 🔧 How Enrollment Happens

Different enrollment paths exist for different device types and ownership models:

**Windows Autopilot** is the modern corporate Windows enrollment approach. Devices ship directly to employees. The employee powers on, authenticates with their work account, and Autopilot automatically joins the device to Entra ID and enrolls it in Intune. No IT hands-on-keyboard required for setup.

**Windows automatic enrollment** applies to devices that are Entra Joined or Hybrid Entra Joined. When group policy or a configuration setting triggers MDM auto-enrollment, the device enrolls in Intune automatically during or after the join process.

**Company Portal** is the manual enrollment path used on personal devices (BYOD) and mobile devices. The user installs the Intune Company Portal app, signs in with their work account, and follows the enrollment wizard. This gives the user visibility into what enrollment means before they agree to it.

**Apple Device Enrollment Program (DEP) and Android Enterprise** handle enrollment for corporate-owned mobile devices, typically pre-configured before distribution so devices arrive already enrolled.

## 📋 MDM vs MAM: Two Enrollment Philosophies

Full MDM enrollment gives the organization control over the entire device. IT can see device inventory, push any configuration, wipe the device, and enforce compliance. For corporate-owned devices, this is the right model.

For personal devices (BYOD), full MDM enrollment is often a non-starter. Employees don't want their employer controlling their personal phone: limiting what apps they can install, potentially seeing their personal photos, and having the ability to wipe the device entirely.

MAM (Mobile Application Management) enrollment, used with App Protection Policies, is the alternative. Instead of enrolling the device, the organization enrolls specific apps. Intune manages Outlook or Teams without touching anything else on the phone. Corporate data stays contained within managed apps. The device itself is never under management.

This is why the two options exist:
- 🏢 Corporate device: Full MDM enrollment
- 📱 Personal device: MAM without MDM enrollment (or require corporate-owned device for access)

## ⚠️ What Enrollment Doesn't Cover

Enrollment gives the organization management capability. It doesn't guarantee compliance. A device can be enrolled but still fail compliance checks if the user has disabled a required security setting.

Enrollment also doesn't give IT access to personal content. On a personally-enrolled device, Intune can only manage what it enrolled. Personal photos, personal emails, and personal apps are off-limits. When a user's device is enrolled and they leave the company, a selective wipe removes only the corporate apps and data, not personal content.

That distinction matters when explaining enrollment to employees who are concerned about privacy. "We manage the work apps, not your device" is often the framing that makes enrollment acceptable for personal devices.

## 💡 Fixing the Offboarding Gap

In the incident that opened this article, the fix was implementing App Protection Policy on mobile devices (for employees who refused full MDM enrollment) and requiring Intune enrollment with a device enrollment block that prevented corporate app access on unenrolled devices. Offboarding automation was also updated to trigger selective wipes via Intune's API on departure day.

---

💬 **Has your organization struggled with the BYOD enrollment conversation? Getting employees to enroll personal devices in any form of management is a genuine challenge.** What framing or policy change made the difference in getting adoption?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Device Registration](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-3-device-registration.md) | [🏠 Contents](/README) | [Intune →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-5-intune.md)
