# Workforce Tenant
*The Corporate Identity Foundation Behind Every Employee Account*

**Part of Entra ID Glossary Series: Glossary#9.15 - Workforce Tenant**

---

When Microsoft introduced external tenants as part of Entra External ID, they needed a term for the thing that already existed: the standard Entra ID tenant that every organization uses to manage its employees.

That term is workforce tenant.

It's not a new product. It's not a new configuration option. It's the name Microsoft gave to the identity tenant type organizations have been running for years: the corporate Entra ID directory where employees authenticate, access resources, and get managed by IT.

Understanding what makes a workforce tenant distinct matters now because there are two kinds of Entra ID tenants, and the differences between them are architectural.

## 🏢 What a Workforce Tenant Is

A workforce tenant is a standard Microsoft Entra ID tenant configured for managing organizational identities. It's the corporate directory. The thing your IT department provisions employee accounts into. The system your Conditional Access policies run against. The directory that connects to your on-premises Active Directory through Entra Connect or Cloud Sync.

Every organization that uses Microsoft 365, Azure, or any Entra ID-integrated application has one. Most organizations have exactly one. Large enterprises with complex structures might have a handful, federated together.

The workforce tenant serves two identity populations:

**Member users** 👤: Employees. Full organizational accounts provisioned by IT. Subject to all corporate policies: Conditional Access, device compliance requirements, MFA enforcement, Intune management, Privileged Identity Management for elevated roles. These are the accounts the organization owns and controls.

**Guest users** 🤝: External collaborators invited via B2B. Business partners, vendors, consultants, auditors. Guest accounts authenticate against their home identity (their own organization's Entra ID, or a personal account) and are granted access to specific resources in your workforce tenant. The workforce tenant doesn't own these identities; it just grants them access.

This is the tenant where your employees live. The external tenant (the other Entra ID tenant type) is where customers live.

## 🔄 Workforce Tenant vs External Tenant

The distinction that made "workforce tenant" necessary as a term is the introduction of external tenants for customer identity.

Before external tenants existed, there was essentially one kind of Entra ID tenant (plus the older Azure AD B2C service, which was architecturally separate). When Microsoft built external tenants as part of Entra External ID's CIAM offering, they needed to differentiate: the existing corporate tenant type became the "workforce tenant," and the new CIAM-optimized tenant type became the "external tenant."

The configuration profiles are different:

**Workforce tenant** 🏢: Optimized for employee identity management. Strong device trust (compliant device requirements, Intune integration). PIM for elevated access. Privileged role governance. Entitlement Management for access packages. Connect and Cloud Sync for on-premises integration. B2B guest collaboration features. Cross-tenant access settings for partner relationships.

**External tenant** 🌐: Optimized for customer identity management. Self-registration flows. Social identity provider integration (Google, Facebook, Apple). Consumer-focused MFA options. Branded sign-in and registration pages. Designed for millions of accounts, not thousands. No device compliance requirements (customers don't have managed devices). Token issuance for customer-facing applications.

You can't turn a workforce tenant into an external tenant by changing configuration. They're different tenant types created at provisioning time for different purposes.

## ⚙️ What's Built Into a Workforce Tenant

The features that define workforce tenant operation:

**Identity lifecycle management** 📋: Employee provisioning through HR system integration (Lifecycle Workflows), attribute synchronization from on-premises AD, role assignments, license allocation, and offboarding automation. The full employee identity lifecycle from day one to departure.

**Conditional Access** 🔐: Policy enforcement based on user identity, device compliance state, location, application, and risk signals. This is the workforce tenant's primary security enforcement plane. Policies that would be inappropriate for customer-facing applications (requiring compliant devices to access email, for example) are standard in workforce tenants.

**B2B collaboration** 🤝: The workforce tenant's mechanism for external collaboration. Business partners are invited as guests. Cross-tenant access settings define which partner tenants are trusted, whether to honor their MFA completion, and which applications external users can access. This is the workforce tenant's model for external access, as distinct from the external tenant's model for customer access.

**PIM and role governance** 🔑: Just-in-time elevation for administrative roles. Approval workflows for sensitive access. Time-limited role assignments. The workforce tenant is where your Global Administrators, Exchange Administrators, and Security Administrators manage their elevated access.

**Audit and monitoring** 👁️: Sign-in logs, audit logs, risky user reports, risky sign-in detection. The workforce tenant's identity security monitoring feeds into Entra ID Protection and Microsoft Sentinel for SOC operations.

## 🏗️ Workforce Tenants in the External ID Architecture

When Entra External ID describes its deployment models, the workforce tenant is one of the two options:

Using **External ID within a workforce tenant** means B2B collaboration: inviting external business users as guests, managing their access through cross-tenant settings and Entitlement Management, and treating partner access as an extension of corporate identity governance.

Using an **external tenant** (separate from the workforce tenant) means consumer identity: customers self-register in a purpose-built CIAM environment, authenticate with social logins, and are completely separate from the corporate directory.

A single organization doing both things runs both. The retail bank with 3,000 employees and 2 million online banking customers has a workforce tenant for the employees and an external tenant for the customers. The two populations don't mix. The corporate IT team manages both, but through entirely different administration surfaces and governance processes.

---

💬 **How many distinct Entra ID tenant types does your organization operate today?** Many organizations started with a single workforce tenant and have added external tenants, sandbox tenants, or B2C tenants as their identity needs expanded. What drove the first time your organization had to manage more than one Entra ID tenant?
<!-- nav -->

---

[← Entra External ID](glossary-9-14-entra-external-id.md) | [Home](../README.md) | [External Tenant →](glossary-9-16-external-tenant.md)
