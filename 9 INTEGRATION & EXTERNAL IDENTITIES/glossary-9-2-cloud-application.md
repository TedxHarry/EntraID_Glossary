# Cloud Application
*SaaS in Your Tenant's Security Perimeter*

📚 **Part of Entra ID Glossary Series: Glossary#9.2 - Cloud Application**

---

A security audit found that employees were using 340 cloud applications. The IT team was aware of 23 of them. The other 317 were shadow IT: applications people had signed up for individually, using their work email, with no IT visibility or governance.

Of the 23 known applications, 18 were integrated with Entra ID. Of the 317 unknown ones, zero were. Those 317 applications didn't benefit from Conditional Access, didn't have centralized offboarding, didn't appear in access reviews, and in many cases held corporate data that nobody was managing.

The distinction between a cloud application that's integrated with Entra ID and one that isn't is the difference between a resource in your security perimeter and a blind spot.

## ☁️ What a Cloud Application Is in Entra ID

In the Entra ID context, a cloud application is a Software-as-a-Service (SaaS) application or web application that has been integrated with Entra ID for authentication and access management. It appears in the tenant as an Enterprise Application and is subject to the identity governance and security controls available through Entra ID.

This is distinct from any cloud application an employee signs up for on their own. A Salesforce instance integrated with Entra ID is a cloud application in your tenant. A Trello account an employee created with their work email is not, regardless of what data they put in it.

The integration is what brings a cloud application under the tenant's security umbrella.

## 📋 Categories of Cloud Applications in Entra ID

**Microsoft first-party applications** 🔵: Microsoft 365 services (Exchange Online, SharePoint, Teams, OneDrive), Azure services, and other Microsoft products are pre-integrated. They appear in every tenant's enterprise applications list automatically.

**Gallery applications** 📚: Third-party SaaS applications that Microsoft has pre-configured integration templates for. Thousands of applications including Salesforce, ServiceNow, Workday, GitHub, Slack, DocuSign, and others. Adding them to your tenant is mostly configuration, not custom development.

**Custom applications** 🔧: Applications your organization has developed or vendor applications without gallery templates. Registered in Entra ID and configured manually.

**Microsoft Defender for Cloud Apps discovered applications** 🔍: MDCA can discover and analyze the cloud applications being used in your environment, including shadow IT, even before those applications are formally integrated with Entra ID.

## 🔒 What Integration Gives You

When a cloud application is integrated with Entra ID, you gain:

**Conditional Access control** 🚦: The application becomes a target in Conditional Access policies. You can require MFA, compliant devices, or specific locations for access to the application. Without integration, Conditional Access doesn't see the application.

**User provisioning and deprovisioning** 👤: For SCIM-compatible applications, Entra ID can automatically create accounts when users are assigned and disable them when access is removed. Offboarding a user from Entra ID propagates to integrated applications automatically.

**Access governance** 📋: Application access appears in access reviews. The question "who has access to Salesforce and do they still need it?" can be answered and enforced through Entra ID Governance.

**Sign-in visibility** 👀: All sign-ins to integrated applications appear in Entra ID's sign-in logs. You can see who is accessing what, from where, and at what time.

**SSO** 🔐: Users access integrated applications through the My Apps portal or directly, using their Entra ID credentials, without separate application-specific passwords.

## 🎯 Assignment and Access Control

For many cloud applications, you can configure whether all users in the tenant can access it or only assigned users:

**Assignment required** 🎫: Only users or groups explicitly assigned to the application can access it. Users who aren't assigned see an access error. This is the appropriate setting for applications with specific licenses, sensitive content, or role-specific access.

**Assignment not required** 🌐: Any authenticated user in the tenant can access the application. Appropriate for general productivity tools available to all employees.

Assignment control combined with Conditional Access gives you layered application access governance: who is allowed to access the application (assignment) and under what conditions they can access it (Conditional Access).

## ⚠️ The Shadow IT Problem

The 317 unmanaged applications from the opening scenario represent a real and common challenge. Employees use cloud services to get work done. If the approved application catalog doesn't meet their needs, they find alternatives.

Shadow IT means:
- Corporate data in systems without data governance
- Access that persists after offboarding (the Trello boards don't get cleaned up)
- No MFA or Conditional Access on application access
- No visibility into what's being shared or with whom

The solution isn't blocking all unapproved applications (that creates friction without actually stopping usage). It's a combination of discovering what's in use, formalizing integration for high-risk high-usage applications, and providing governance tools that make the approved alternatives good enough that shadow IT usage decreases.

---

💬 **How many cloud applications are formally integrated with Entra ID in your tenant?** The gap between the number IT knows about and the number actually in use is almost always larger than expected. Has your organization done a shadow IT discovery exercise, and what did the results look like?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← App Integration](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-1-app-integration.md) | [🏠 Contents](/README) | [Federated Application →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-3-federated-application.md)
