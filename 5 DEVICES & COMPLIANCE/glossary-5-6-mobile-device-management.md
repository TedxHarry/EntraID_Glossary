# Mobile Device Management
*The Trade-Off Between Control and Trust*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #5.6 - Mobile Device Management

---

## 🎯 TL;DR

- MDM (Mobile Device Management) manages entire device: controls settings, deploys apps, enforces compliance
- MAM (Mobile Application Management) manages specific apps without requiring device enrollment
- MDM is for corporate devices; MAM is for BYOD scenarios where full device control isn't appropriate


When an employee uses their personal phone for work email, the organization is immediately in an uncomfortable position. Corporate emails sit on a device the organization doesn't control. If the employee leaves tomorrow, those emails leave with them. If the phone is lost, the data is gone.

The organization has two options: require MDM enrollment (full management, they control the device) or use app protection policies (manage the app, not the device). Neither is obviously correct. The right answer depends on what data is at risk, who owns the device, and how much friction the organization can afford to create for its employees.

Understanding MDM properly is how you make that decision well.

## 📱 What MDM is

Mobile Device Management is the practice of centrally managing mobile devices: enforcing security policies, controlling configuration, deploying apps, and maintaining the ability to remotely wipe or lock devices.

MDM works through a management profile (on iOS/macOS) or an enrollment agent (on Android and Windows) that creates a channel between the device and the MDM server. Through this channel, the MDM solution can:

- 🔒 **Enforce security settings**: Require PIN/biometric, minimum PIN length, disable specific features
- ⚙️ **Push configurations**: Wi-Fi, VPN, email accounts, certificates
- 📦 **Deploy and remove apps**: Install required apps silently, remove apps when device is unenrolled
- 🗑️ **Wipe devices**: Full wipe (factory reset) or selective wipe (corporate data only)
- 📊 **Inventory devices**: OS version, hardware specs, installed apps, compliance state

In the Microsoft ecosystem, Intune is the MDM server. Devices enroll in Intune. Intune pushes policies. Intune reports compliance to Entra ID.

## 🔄 MDM vs mam: the crucial distinction

MDM manages the entire device. MAM (Mobile Application Management) manages specific applications.

**MDM enrollment** gives the organization control over the device's operating system settings, not just the apps. IT can enforce full-disk encryption, disable the camera, require a complex PIN, and wipe the entire device if it's lost. For corporate-owned devices, this is typically the right model.

**MAM without MDM** (often called "MAM-WE" - Mobile Application Management Without Enrollment) targets specific apps. The organization manages Outlook, Teams, and OneDrive. Everything else on the phone is untouched. The user's personal photos, banking apps, and personal email are completely outside Intune's reach. If the user leaves, a selective wipe removes corporate data from managed apps only.

## ⚖️ The BYOD trade-off in practice

I've had this conversation dozens of times with employees who are asked to enroll their personal iPhone:

**Their concern**: IT will be able to see my photos, read my personal messages, and wipe my entire phone.

**The reality with full MDM**: IT can see device inventory (OS version, enrolled apps), enforce security settings, and do a full wipe if needed.

**The reality with MAM-WE**: IT can only manage the specific work apps they enrolled. They can see nothing about the device itself and can only do a selective wipe of corporate app data.

For most organizations, MAM-WE is the right model for personal devices. It protects corporate data in apps without creating the privacy concerns that MDM enrollment on a personal device raises. It also makes the conversation with employees much easier.

For corporate-owned devices, full MDM enrollment is the right model. The organization owns the device and needs full control of its security posture.

## 📋 What MDM cannot do

Even with full MDM enrollment, there are limits:

- MDM cannot access personal apps or personal data within apps
- MDM cannot read personal messages or emails in personal accounts
- MDM cannot track user location (without the user explicitly enabling a locate feature)
- MDM policies apply to the management channel, not the entire OS in some cases

These limits are built into the MDM protocol by Apple, Google, and Microsoft specifically to maintain trust with users.

## 💡 Conditional access and MDM

Conditional Access can require that devices be "managed" as a condition for accessing sensitive resources. A managed device is one that is either Intune-enrolled or Hybrid Entra Joined (domain joined and registered with Entra ID).

For organizations that want to allow BYOD for low-sensitivity apps but require corporate-managed devices for sensitive data, this Conditional Access condition provides the enforcement point. Different apps get different policies based on the sensitivity of what they access.

---

💬 **How has your organization handled the BYOD vs MDM conversation with employees?** The personal device enrollment policy is one of the most contentious in enterprise mobile management. What was the tipping point that determined your approach?
✍️ TedxHarry

<!-- nav -->

---

[← Intune](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-5-intune.md) | [🏠 Contents](/README) | [Endpoint Manager →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-7-endpoint-manager.md)
