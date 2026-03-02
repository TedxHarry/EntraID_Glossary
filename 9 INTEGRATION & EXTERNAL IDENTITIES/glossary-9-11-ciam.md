# CIAM
*Identity Management Designed for Customers, Not Employees*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #9.11 - CIAM

---

## 🎯 TL;DR

- CIAM (Customer Identity and Access Management) is the identity discipline for customer-facing applications
- Microsoft's CIAM solution: Entra External ID in external tenants (successor to Azure AD B2C)
- CIAM needs: low-friction registration, branded UI, social login, progressive profiling, fraud prevention


A product manager asked the question that leads to CIAM: "Can we use our corporate Active Directory for customer accounts?"

It's a reasonable question. Active Directory is the identity system the organization has. Why buy something else?

The answer is a long list of mismatches. AD doesn't support self-registration. AD doesn't support social logins. AD wasn't designed for millions of accounts. AD applies corporate security policies that make no sense for customer experiences. AD licenses at a per-user cost that's untenable at consumer scale. AD's admin-centric model breaks when users are managing their own identity.

Every item on that list is a reason CIAM exists as a distinct category.

## 🎯 What CIAM is

Customer Identity and Access Management (CIAM) is a specialized category of identity management designed for the specific requirements of consumer-facing applications. It handles the identities of an organization's customers or end users: the people who use your products and services, not the people who work for you.

CIAM addresses fundamentally different requirements than workforce identity (managing employees) or B2B identity (managing business partners). The differences aren't minor configuration choices. They're architectural requirements that shape every aspect of how the system works.

## 📊 The CIAM design requirements

**Scale** 📈: Workforce identity handles thousands to hundreds of thousands of accounts. Consumer applications can have millions or tens of millions of customers. Spotify has 600 million users. A regional bank might have two million online banking customers. CIAM platforms are built and priced for this scale. Enterprise IAM platforms are not.

**Self-service everything** 👤: Customers sign themselves up. Customers reset their own passwords. Customers manage their own profile. Customers merge or close their accounts. There's no IT department for customers to call. Every account lifecycle operation must be fully self-service.

**Social identity** 🌐: Most consumers don't want to create another username and password. They have Google accounts. Apple ID. Facebook. Microsoft consumer accounts. CIAM supports "sign in with" these social providers as first-class options. Enterprise IAM doesn't need this capability.

**Consumer-grade UX** 🎨: The sign-in and sign-up experience is part of the product. Friction in the authentication flow is customer attrition. CIAM platforms provide fully brandable, fully customizable sign-in and registration experiences. Enterprise IAM sign-in pages are functional, not consumer-grade.

**Privacy compliance** 🔐: Consumer data is subject to GDPR, CCPA, and other privacy regulations in ways that employee data often isn't. CIAM must handle consent management, data residency, right to deletion, and other privacy requirements as first-class features.

**Flexible MFA** 📱: Consumer MFA must be accessible to people who aren't security professionals. SMS is common in CIAM despite its weaknesses because it works for consumers who don't have an authenticator app. The security model for customers is different from the security model for administrators.

## 🔒 CIAM in the Microsoft ecosystem

Microsoft offers two CIAM-oriented products:

**Azure AD B2C** (the established product): A dedicated Azure service for consumer identity. Separate from enterprise Entra ID. Supports social logins, self-registration, user flows (pre-built policy templates), custom policies (complex flow customization), and token issuance for customer-facing applications. Currently supported and widely deployed.

**Microsoft Entra External ID** (the successor): Microsoft's newer CIAM platform, built on a more modern architecture. Consumer-tenant model (separate Entra ID tenant configured for external/consumer identities). Designed to replace B2C over time with a more integrated identity platform.

Both address the core CIAM requirements. The choice for new implementations is between them. B2C for organizations with existing B2C expertise and deployed applications. External ID for greenfield implementations that want the newer architecture.

## 🏗️ What CIAM needs to provide

A CIAM solution needs to handle the full customer identity lifecycle:

**Registration** 📝: New customers create accounts. CIAM validates the email, prevents duplicates, handles social login linking.

**Sign-in** 🔐: Returning customers authenticate. Social login, email/password, MFA if required. Smooth, branded experience.

**Account management** ⚙️: Customers update their profile, change their email, reset their password, manage connected social accounts, review their data.

**Session management** 🔄: Token issuance, token refresh, session duration appropriate for a consumer application (longer sessions than enterprise, often "remember me" functionality).

**Progressive profiling** 📋: Collecting customer information incrementally across multiple interactions rather than requiring a complete profile on first registration.

**Account recovery** 🔑: Customers who lose access to their registered methods need a recovery path that's self-service and secure.

**Account deletion** 🗑️: Regulatory requirements (GDPR right to erasure) mean customers must be able to request account deletion and the system must honor it.

---

💬 **Has your organization evaluated CIAM requirements for a customer-facing application?** The moment when someone says "can we just put customers in our company's Active Directory?" is the moment CIAM becomes a real conversation. What requirements drove your organization to look at a dedicated CIAM platform?
✍️ TedxHarry

<!-- nav -->

---

[← B2C](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-10-b2c.md) | [🏠 Contents](/README) | [External User →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-12-external-user.md)
