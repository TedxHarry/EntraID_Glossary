# App Protection Policy
*Managing the Data, Not the Device*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #5.10 - App Protection Policy

---

## 🎯 TL;DR

- App Protection Policies (APP/MAM) protect data within apps without requiring device enrollment
- They can require PIN, block copy-paste to unmanaged apps, and wipe corporate data from the app
- Ideal for BYOD: protect company data in Outlook mobile without managing the personal device


An executive pushed back hard on Intune enrollment for his personal iPhone. "I'm not letting IT have any control over my personal device. Period."

It was a fair position. He'd heard stories (some accurate, some exaggerated) about MDM enrollment giving IT visibility into personal data and the ability to wipe the entire phone. He wasn't wrong to be cautious.

The answer wasn't to give him an exception. It was App Protection Policies. The organization could protect corporate data in Outlook, Teams, and OneDrive without ever touching his phone. He controls his device. The organization controls the work data within work apps.

## 🛡️ What app protection policy does

An App Protection Policy (APP) is an Intune policy that applies to specific managed applications, not to the device itself. It defines rules for how organizational data can be used within those apps:

**Data containment** 📦: Corporate data within managed apps stays within managed apps. Copy/paste from Outlook to a personal notes app: blocked. Opening an email attachment in a personal PDF reader: blocked. Saving a OneDrive file to the personal camera roll: blocked.

**Access requirements** 🔐: Users must meet requirements to open managed apps. PIN required to open Outlook. Biometric authentication required. Session timeout after inactivity.

**Device conditions** 📱: If the device is jailbroken or rooted, block access to managed apps entirely. Minimum OS version requirements. Device threat level integration with Defender.

**Selective wipe capability** 🗑️: When an employee leaves, IT can trigger a selective wipe that removes corporate data from managed apps only. The user's personal photos, personal email, and all personal apps remain completely untouched.

## 🔄 MAM without MDM

The traditional MDM model (enroll the device, manage everything) is right for corporate-owned devices. But for personal devices, App Protection Policies enable a different model: MAM without MDM enrollment.

In this model:
- The device is never enrolled in Intune (no management profile installed)
- The user downloads managed apps (Outlook, Teams, OneDrive) from the public app store
- The user signs in with their work account
- Intune detects the sign-in and applies the App Protection Policy to those specific apps
- Corporate data is now protected within those apps, nowhere else on the device

The user's personal apps, personal files, and personal accounts are completely outside Intune's reach. The management boundary is the app, not the device.

## 📋 What policies actually configure

For iOS and Android, App Protection Policies configure:

**Data protection settings**:
- Restrict cut/copy/paste between managed and unmanaged apps
- Restrict saving data to personal storage locations
- Require encryption of organizational data
- Restrict screen capture (Android)
- Block backup to personal cloud services (iCloud, Google Drive)

**Access requirements**:
- PIN type and length, number of attempts before wipe
- Biometric authentication allowed/required
- Recheck access requirements after timeout period
- Block access on jailbroken/rooted devices

**Conditional launch**:
- Minimum app version (force users to update before accessing)
- Minimum OS version
- Maximum device threat level (integrates with Defender for Endpoint)

## ⚠️ What app protection policy doesn't cover

App Protection Policies only work with apps that have the Intune SDK integrated or that are wrapped using the Intune App Wrapping Tool. Microsoft's own apps (Outlook, Teams, OneDrive, Edge) have the SDK built in.

Third-party apps vary. Salesforce mobile, ServiceNow, SAP Fiori: support varies by vendor. Before planning MAM-only as your mobile strategy, check which apps your users need and whether those apps support App Protection Policies.

For apps that don't support the Intune SDK, the fallback is typically requiring MDM enrollment to access those apps, or blocking mobile access and requiring desktop.

## 💡 Combining APP with conditional access

App Protection Policies work alongside Conditional Access, not instead of it. A Conditional Access policy can require an approved client app (one of Microsoft's managed apps) as a condition for accessing Exchange Online or SharePoint.

This creates enforcement at two layers: Conditional Access blocks access from unmanaged apps at the protocol level, and App Protection Policies control what users can do within managed apps once they're in.

---

💬 **Have you had the "I won't enroll my personal device" conversation and used App Protection Policies as the solution?** It's often the path that satisfies both security requirements and employee privacy concerns. What was the reaction when you explained the MAM-without-MDM model?
✍️ TedxHarry

<!-- nav -->

---

[← Hybrid Device](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-9-hybrid-device.md) | [🏠 Contents](/README) | [Device State →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-11-device-state.md)
