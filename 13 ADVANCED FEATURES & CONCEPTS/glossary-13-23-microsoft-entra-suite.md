# Microsoft Entra Suite
*The Consolidated Identity and Network Access Platform*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #13.23 - Microsoft Entra Suite

---


A security architect was mapping the tools her organization used for identity and access: Entra ID P2 for Conditional Access and Identity Protection, Entra ID Governance for access reviews and entitlement management, Global Secure Access for network-level Zero Trust, Entra Permissions Management for cloud permissions visibility, and Entra Verified ID for identity verification workflows.

Five separate licensing conversations. Five separate admin surfaces. Capabilities that should work together requiring manual integration work to actually do so.

Microsoft Entra Suite is the licensing and product bundle that assembles these capabilities into a unified platform, and understanding what's in it matters for organizations making investment decisions about where their identity security program goes next.

## 📦 What the microsoft entra suite contains

The Entra Suite is a licensing bundle introduced in 2024 that packages the following products together:

**Microsoft Entra ID P2** 🔐: The foundation. Conditional Access, Identity Protection (risk-based policies, risky user/sign-in detection), Privileged Identity Management, and access reviews. Everything covered in the earlier phases of this glossary series lives here.

**Microsoft Entra ID Governance** 📋: Entitlement management, access reviews (expanded beyond what P2 includes), lifecycle workflows, and identity governance capabilities. The difference from P2: Governance adds the automated lifecycle workflow engine, more complex access package configurations, and governance over guest identities.

**Microsoft Entra Private Access** 🔒: The private application side of Global Secure Access. Replaces traditional VPN for accessing on-premises and private cloud applications. Users connect through the Global Secure Access client; the connection is brokered through Microsoft's network without exposing the application directly to the internet.

**Microsoft Entra Internet Access** 🌐: The internet-facing side of Global Secure Access. Secure web gateway capabilities for filtering and monitoring internet traffic from managed devices, with Conditional Access policies applied to internet destinations rather than just Microsoft applications.

**Microsoft Entra ID Protection (expanded)** ⚠️: The Suite includes expanded Identity Protection capabilities including workload identity risk detection.

## 🔗 How the suite changes the integration story

Before the Suite, Global Secure Access was licensed separately from Governance, which was licensed separately from Permissions Management. Each product worked independently, and connecting them required manual configuration work. Conditional Access policies from Entra ID P2 applied to Microsoft applications but not necessarily to internet destinations routed through Internet Access.

The Suite is designed so these products share a unified policy engine. Conditional Access policies in Entra ID P2 apply to Private Access connections. The Compliant Network condition in Conditional Access works with both Private and Internet Access components. Risk signals from Identity Protection feed into decisions about Private Access connections, not just Microsoft 365 application sign-ins.

The practical result: an administrator defines a policy once and it enforces consistently across Microsoft 365 applications, private on-premises applications, and internet destinations, using the same Conditional Access framework.

## 🎯 Microsoft entra permissions management

Permissions Management is the cloud infrastructure entitlement management (CIEM) component of the Entra product family. It provides visibility into permissions across Azure, AWS, and Google Cloud, identifying:

**Overprivileged identities** 📊: Which users, service principals, and workload identities have permissions far exceeding what they actually use. The permissions gap between granted and used is the attack surface reduction opportunity.

**Unused permissions** 🔍: Permissions granted but never exercised in the past 90 days. Candidates for removal under least privilege principles.

**Cross-cloud visibility** ☁️: A unified view across all three major cloud providers, which matters for organizations using multi-cloud architectures where permission sprawl exists across different IAM systems.

Permissions Management is available as a standalone product and as part of some Entra Suite configurations. It addresses the workload identity governance problem at the cloud permission layer rather than at the Entra ID service principal layer.

## 📱 Microsoft entra verified ID

Verified ID is the decentralized identity component of the Entra family. It issues and verifies digital credentials based on open standards (W3C Verifiable Credentials, DIF standards).

Organizations use Verified ID for:

**Employee credential issuance** 🪪: Issuing a verifiable credential representing current employment status. The credential lives in the user's Microsoft Authenticator app. Third-party services (partner organizations, external services) can verify the credential without querying the issuing organization's directory directly.

**Identity verification for account recovery** 🔐: Using third-party identity verification services (document verification, biometric verification) to issue a Verified ID credential that gates access to account recovery workflows. Reduces the risk of social engineering attacks against the helpdesk.

**B2B access provisioning** 👥: Using Verified ID to verify a partner organization's employee status before provisioning access, rather than relying solely on the partner's invitation through B2B collaboration.

## 🗺️ Where the entra product family is heading

The Entra brand encompasses an expanding set of identity and access management capabilities. Understanding the full scope helps with roadmap conversations: what capabilities exist today, what's in preview, and what requires additional licensing beyond Entra ID P1/P2.

For organizations planning identity investments, the Entra Suite represents Microsoft's view of what a complete modern identity platform looks like: identity governance, Zero Trust network access, cloud permissions visibility, and decentralized identity, all built on the same Conditional Access and identity platform foundation.

---

💬 **Is your organization evaluating the Microsoft Entra Suite as a consolidated licensing option, and which component represents the biggest gap in your current identity security stack?** The Entra product family has expanded significantly beyond the core Entra ID directory service. What identity capabilities are you most actively looking at to extend your current Entra ID deployment?
✍️ TedxHarry

<!-- nav -->

---

[← Microsoft Authenticator Advanced](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-22-microsoft-authenticator-advanced.md) | [🏠 Contents](/README) | [Advanced Scenarios →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-24-advanced-scenarios.md)
