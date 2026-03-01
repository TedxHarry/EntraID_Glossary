# Endpoint Manager: One Console, All Your Devices

**Part of Entra ID Glossary Series: Glossary#5.7 - Endpoint Manager**

---

The naming history of Microsoft's device management products is genuinely confusing, and I've watched it trip people up in job interviews, vendor conversations, and Microsoft documentation for years.

Systems Center Configuration Manager. SCCM. MEM. MECM. Microsoft Endpoint Manager. Intune. Microsoft Intune admin center. These are not all different products. They're the same underlying capabilities renamed, rebranded, and consolidated over time.

Understanding what Endpoint Manager actually is, and how it relates to Intune and Configuration Manager, clears up most of the confusion.

## 🗂️ What Microsoft Endpoint Manager Was

Microsoft Endpoint Manager (MEM) was the brand name Microsoft used from 2019 to 2023 to describe a unified management experience combining:

- **Microsoft Intune**: Cloud-native MDM and MAM for all device types
- **Microsoft Endpoint Configuration Manager (MECM, formerly SCCM)**: On-premises Windows management with decades of enterprise history
- **Co-management**: The bridge allowing both tools to manage the same Windows devices simultaneously, with workloads shifted between them gradually

The MEM brand presented these as a single platform accessible through a unified admin center at `endpoint.microsoft.com`.

In 2023, Microsoft simplified the naming. The brand became **Microsoft Intune** again, and the admin center became the **Microsoft Intune admin center**. Configuration Manager (MECM) remains a separate product under the Microsoft Intune family of products but keeps its own identity.

## ⚙️ What the Admin Center Manages

The Intune admin center is the management console for:

**Devices**: View all enrolled devices, their compliance state, last check-in time, assigned user, and hardware details. Force sync compliance checks. Retire or wipe specific devices.

**Policies**: Compliance policies (what makes a device compliant), configuration profiles (device settings), security baselines (Microsoft-recommended settings hardened for security), and app protection policies.

**Apps**: Deploy apps to devices and users, manage app lifecycle, configure App Protection Policies for managed apps.

**Endpoint security**: Antivirus policy, disk encryption policy, attack surface reduction rules, Microsoft Defender for Endpoint integration.

**Tenant administration**: Connector setup for Apple DEP/ABM, Google Enterprise enrollment, on-premises exchange connectors, and Configuration Manager co-management configuration.

## 🔗 Co-management: When You Need Both

Many large enterprises can't switch overnight from Configuration Manager to cloud-only Intune management. They have years of investment in Configuration Manager policies, software deployments, and workflows.

Co-management lets both systems manage the same Windows device simultaneously, with specific management workloads assigned to one system or the other:

- 📋 **Compliance policies**: Move to Intune (required for Conditional Access integration)
- ⚙️ **Device configuration**: Can remain in Configuration Manager initially
- 📦 **Apps**: Can remain in Configuration Manager while cloud delivery is being set up
- 🛡️ **Endpoint Protection**: Move to Intune for cloud-delivered Defender management

Each workload is a slider: Configuration Manager or Intune. You can move workloads one at a time, testing before committing.

The compliance workload is almost always the first to move to Intune, because Conditional Access device compliance requires Intune. You can't have Conditional Access enforce device compliance if Configuration Manager is reporting compliance instead of Intune.

## 📊 Endpoint Manager and Entra ID Together

The combination of Intune (endpoint management) and Entra ID (identity management) is the foundation of Microsoft's Zero Trust device approach:

1. **Entra ID** provides device identity and authentication
2. **Intune** evaluates device security posture and reports compliance
3. **Conditional Access** reads both (identity + compliance) to make access decisions
4. **Defender for Endpoint** provides threat intelligence that feeds back into device risk state

Each piece is meaningful alone. Together, they form a continuous loop: device authenticates, compliance is checked, access is granted or blocked, threats are detected, device risk is updated, access is re-evaluated.

## 💡 Finding Your Way Around

If you're new to Intune admin center, the navigation can feel overwhelming. Start with three sections:

- 🔵 **Devices**: Where you find enrolled devices and compliance state
- 🔵 **Endpoint security**: Where you configure compliance policies and security baselines
- 🔵 **Apps**: Where you manage App Protection Policies for mobile devices

Those three cover the daily operational tasks for most organizations.

---

💬 **Is your organization using Intune alone, Configuration Manager with co-management, or still fully on-premises management?** The migration from on-premises SCCM to cloud Intune management has been a multi-year journey for most large enterprises. What has been the biggest obstacle in your environment?

#EntraID #EndpointManager #Intune #ConfigurationManager #CoManagement #MicrosoftEntra #DeviceManagement
<!-- nav -->

---

[← Mobile Device Management: The Trade-Off Between Control and Trust](glossary-5-6-mobile-device-management.md) | [Home](../README.md) | [Device Trust: Not All Devices Are Equally Trustworthy (And Entra ID Knows It) →](glossary-5-8-device-trust.md)
