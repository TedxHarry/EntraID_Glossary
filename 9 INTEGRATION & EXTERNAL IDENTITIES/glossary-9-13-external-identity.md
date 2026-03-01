# External Identity
*The Broader Category Behind Every Non-Employee*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#9.13 - External Identity**

---

## 🎯 TL;DR

- External Identity refers to identities managed outside your Entra ID tenant: B2B guests, B2C customers, or federated IdP users
- Microsoft's External ID product consolidates B2B and B2C scenarios under one platform
- Design external identity with lifecycle in mind — external accounts should expire, not persist indefinitely


A company's Entra ID tenant had four types of people accessing it:

1. Employees (Members): 2,400 people, managed corporate accounts, full Conditional Access policies
2. B2B guests: 180 business partners, vendors, auditors with guest accounts authenticating via their home organizations
3. B2B direct connect users: 15 people from a strategic partner accessing shared Teams channels without full guest invitations
4. External customers: 50,000 people using a customer portal, managed in a separate External ID tenant

All four categories involve people who don't work for the company. Each category has a different identity model, different authentication experience, and different governance requirements. The umbrella term for all of them is external identities.

## 🌐 What External Identity Means

External identity is the broad category encompassing any identity scenario where people outside your organization access your resources or use your applications. Microsoft's products for this category are grouped under the "Microsoft Entra External ID" umbrella, which includes both B2B collaboration (business partner access) and CIAM (customer-facing applications).

Understanding external identity means understanding the distinct scenarios within it and which tools apply to each.

## 🗂️ The External Identity Scenarios

**B2B Collaboration** 🤝: Business partners, vendors, auditors, and contractors who access your corporate resources. They sign in with their own organizational or consumer identity. Your tenant grants them access to specific resources. The focus is collaboration between organizations, not customer relationships.

**B2B Direct Connect** 🔗: A specific B2B scenario where users from a partner organization access shared channels in Microsoft Teams without requiring a full guest invitation and redemption flow. Requires cross-tenant access settings configured between both organizations' Entra ID tenants. Seamless for users; they experience the shared channel as part of their own Teams environment.

**Customer identity (CIAM)** 👥: Customers of a product or service who need accounts for a consumer-facing application. Managed in a separate External Tenant configured for customer identity (not in the corporate workforce tenant). Self-registration, social logins, consumer-grade UX.

**External service account access** 🤖: Non-human external identities. Managed identities from partner Azure subscriptions, federated credentials from external CI/CD systems (GitHub Actions, etc.). These are workload identity scenarios for external systems, not human identities.

## 🔧 Microsoft's External Identity Product Architecture

Microsoft has been consolidating external identity capabilities under a unified architecture:

**Microsoft Entra External ID** is the current product umbrella. Within it:

**For workforce tenants** (your corporate Entra ID): B2B collaboration features. Invite guests, manage cross-tenant access settings, configure federation with partner organizations.

**For external tenants** (a separate tenant type, formerly CIAM/B2C territory): Consumer-facing application identity. Self-registration, social logins, user flows, branded sign-in pages. This is where customers live, not employees.

The external tenant concept is the architecture that replaced Azure AD B2C for new CIAM implementations. An external tenant is an Entra ID tenant configured specifically for managing non-employee identities for a consumer-facing application.

## 🔒 Governance Differences Between External Identity Types

Each external identity type has different governance requirements:

**B2B guests** 📋: Governed through Access Reviews, Entitlement Management access packages, and cross-tenant access settings. Access is granted and reviewed by internal administrators and resource owners.

**Customer accounts (CIAM/External Tenant)** 👤: Governed through the customer-facing application. Self-service account creation and deletion. Privacy compliance (GDPR right to erasure, consent management). Volume at consumer scale means individual account governance isn't feasible; policy-based and automated governance is required.

**B2B Direct Connect** 🔗: Governed through cross-tenant access settings between specific tenant pairs. More wholesale (applies to all users from the partner tenant) than individual guest management.

## ⚠️ The Identity Sprawl Risk

External identity is where identity sprawl is hardest to control:

- Guest accounts created for projects that have ended
- Customer accounts for products that have been sunset
- Federation configurations with partner organizations whose partnership ended
- External service accounts for vendor systems that are no longer in use

Each category requires a different cleanup mechanism. B2B guests need access reviews and activity monitoring. Customer accounts need account deletion APIs and data retention policies. Federation configurations need periodic review of active partnerships. External service accounts need workload identity governance.

The common failure mode: external identity was set up to enable collaboration and was never governed. Years later, the external identity environment reflects the entire history of the organization's external relationships with no cleanup.

---

💬 **Which type of external identity is most problematic to govern in your organization?** The B2B guest lifecycle is the most common pain point in corporate tenants. But organizations with CIAM deployments often find customer account management at scale to be the harder problem. Which external identity scenario generates the most operational challenges for your team?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← External User](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-12-external-user.md) | [🏠 Contents](/README) | [Entra External ID →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-14-entra-external-id.md)
