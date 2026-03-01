# Intune
*What the Device Management Piece of Microsoft's Puzzle Actually Does*

📚 **Part of Entra ID Glossary Series: Glossary#5.5 - Intune**

---

An IT manager asked me if Intune was "basically just a thing you need to make Conditional Access device compliance work."

That's not wrong as a starting point, but it undersells what Intune does by about 80%. The compliance reporting piece is the part that makes Entra ID and Intune visible to each other, but the management work Intune does on devices every day is what keeps that compliance state meaningful.

## 📦 What Intune Actually Is

Microsoft Intune is a cloud-based endpoint management service. It's the platform that lets organizations manage devices (Windows, macOS, iOS, Android) and applications at scale, without requiring on-premises infrastructure like Configuration Manager's management point servers.

Everything Intune does falls into four categories:

**Device compliance** 📋: Define what a healthy device looks like (encryption on, Defender running, OS patched, PIN required). Intune evaluates enrolled devices against these policies and reports their compliance state to Entra ID. This is the piece that Conditional Access reads.

**Device configuration** ⚙️: Push settings to devices without requiring users to configure them manually. Wi-Fi certificates deployed automatically. VPN clients configured and ready. Disk encryption enforced. Email accounts pre-configured. Security baselines applied to all corporate Windows devices from a central policy.

**Application management** 📱: Deploy applications to devices automatically, manage app lifecycle (updates, removal), and protect organizational data within apps using App Protection Policies. Corporate apps can be deployed silently to Windows or required on mobile.

**Device lifecycle** 🔄: Enroll new devices, retire devices when no longer needed, wipe lost or stolen devices remotely, and reassign devices to new users. Autopilot integration means new Windows devices can set themselves up.

## 🔗 How Intune Connects to Entra ID

Intune and Entra ID are deeply integrated. Intune uses Entra ID for:

- **Authentication**: Users sign in to Company Portal and Intune-managed apps using their Entra ID identity
- **Device identity**: Intune enrollment registers device objects in Entra ID (or uses existing device objects from Entra Join)
- **Group targeting**: Intune policies are targeted to Entra ID groups
- **Compliance reporting**: Device compliance state flows from Intune to Entra ID where Conditional Access reads it

The compliance state is the critical handshake. Entra ID doesn't evaluate device security directly; Intune does. Intune reports the result to Entra ID. Conditional Access enforces access based on what Intune reported.

If Intune hasn't checked in recently, the device's compliance state in Entra ID may be stale. This is why forcing a device sync before enforcing a new compliance requirement matters.

## 🏢 Intune vs Configuration Manager

Microsoft has two device management tools: Intune (cloud) and Configuration Manager / MECM (on-premises). Many large enterprises run both.

**Configuration Manager** (formerly SCCM) is the mature, feature-rich on-premises solution with 20+ years of enterprise history. It excels at managing large numbers of Windows PCs, software distribution, OS deployment, and patch management in complex environments.

**Intune** is cloud-native, requires no on-premises infrastructure, and is the foundation for modern management approaches like Autopilot. It manages Windows, macOS, iOS, and Android from a single cloud console.

**Co-management** (running both simultaneously) is common during transition. Specific workloads are moved from Configuration Manager to Intune incrementally: compliance policies first, then configuration policies, then app deployment. Organizations gradually shift control to the cloud without a cutover event.

## 💡 What Changes When You Enable Intune

The practical impact when an organization turns on Intune enrollment with compliance policies:

- Devices that never had security baselines enforced suddenly fail compliance checks
- Users with disabled Defender get blocked from SharePoint until they fix it
- IT can actually see how many devices are running a vulnerable OS version
- Remote wiping a lost device becomes a 2-minute operation instead of a physical recovery mission

The visibility alone is often the most valuable initial outcome. Before Intune, organizations often had no reliable inventory of device OS versions, encryption states, or antivirus status at scale.

---

💬 **What was the first Intune compliance or configuration policy your organization enabled, and what did it reveal about the current state of your device fleet?** The first compliance policy rollout often surfaces surprises about device health that nobody knew were there. What did you find?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Device Enrollment](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-4-device-enrollment.md) | [🏠 Contents](/README) | [Mobile Device Management →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-6-mobile-device-management.md)
