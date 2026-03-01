# B2C
*Identity Management for Your Customers, Not Your Employees*

**Part of Entra ID Glossary Series: Glossary#9.10 - B2C**

---

A retail bank built a mobile banking application. Their customers needed accounts. Not corporate Entra ID accounts with managed devices and Conditional Access policies. Not B2B guest accounts from partner organizations. Customer accounts: millions of them, self-registered, using personal email addresses and social logins, with a completely different experience than anything in their corporate identity infrastructure.

Building identity from scratch would take months. Maintaining it forever would be a permanent engineering commitment. Security vulnerabilities in home-rolled authentication are a constant risk.

Azure AD B2C (now being superseded by External Identities) gave them a dedicated customer identity platform: customizable sign-up and sign-in pages, support for social identity providers (Google, Facebook, Apple, Microsoft consumer accounts), MFA for customers, token issuance for their application, and a scalable backend managed by Microsoft.

## 👥 What B2C Is

Azure Active Directory B2C (Business-to-Consumer) is a customer identity and access management (CIAM) service designed specifically for consumer-facing applications. It manages the identities of an organization's customers or end users, as opposed to its employees (handled by Entra ID) or business partners (handled by B2B Collaboration).

B2C is a separate Azure service from Entra ID for enterprise users. Organizations create a B2C tenant specifically for their consumer identity use cases. The B2C tenant is dedicated to customer identity and operates independently from the corporate Entra ID tenant.

## 🎯 What B2C Is Designed For

**Scale** 📊: B2C is designed to handle millions of consumer accounts. Enterprise Entra ID is optimized for thousands to hundreds of thousands of organizational accounts. B2C's pricing and architecture scale to consumer-application loads.

**Self-registration** 📝: Consumers sign themselves up. B2C provides customizable sign-up flows where users enter their information, verify their email, and create their account without any admin involvement.

**Social identity providers** 🌐: Consumers don't want to create another username and password. B2C supports "Sign in with Google," "Sign in with Facebook," "Sign in with Apple," and "Sign in with Microsoft consumer account" out of the box. The consumer uses an identity they already have.

**Local accounts** 📧: For consumers who don't want to use a social identity, B2C supports email and password accounts managed within the B2C tenant.

**Customizable user experience** 🎨: The sign-in and sign-up pages are fully customizable to match the brand of the customer-facing application. No Microsoft branding required if not wanted.

**Consumer MFA** 📱: B2C supports MFA for consumers via SMS or authenticator apps, presented in a consumer-friendly way.

## 🔧 User Flows and Custom Policies

B2C authentication experiences are defined through policies:

**User flows** 🔄: Pre-built, configurable policy types for common scenarios: sign-up and sign-in, password reset, profile editing. Configure the experience through a UI without writing policy code. Limited but sufficient for common scenarios.

**Custom policies** ⚙️: Built on the Identity Experience Framework. XML-based policy definitions that allow complex, multi-step authentication flows, integration with external APIs, custom claims transformations, and scenarios that user flows don't support. Powerful but complex.

Custom policies are used for things like: integrating with an external CRM to look up customer data during sign-in, progressive profiling (collecting customer information incrementally over multiple sign-ins), complex step-up authentication scenarios, or migration from legacy identity systems.

## 📋 B2C vs Enterprise Entra ID

They're different products for different purposes:

| | Enterprise Entra ID | B2C |
|---|---|---|
| Who | Employees, partners | Customers |
| Scale | Thousands to hundreds of thousands | Millions |
| Registration | Admin-provisioned | Self-service |
| Identity providers | Corporate IdPs | Social + local |
| MFA | Microsoft Authenticator, FIDO2 | SMS, authenticator apps |
| Governance | PIM, Access Reviews | Customer profile management |
| Pricing | Per-user licensing | Per-authentication |

Running consumer-facing applications on enterprise Entra ID creates mismatches: employees and customers in the same directory, corporate security policies applied to consumer authentication, pricing structures misaligned with consumer scale.

## 🔮 B2C and Entra External Identities

Microsoft is transitioning the B2C product toward Microsoft Entra External ID, a newer CIAM platform that addresses some of B2C's architectural limitations with a more modern approach. Organizations starting new consumer identity projects should evaluate Entra External ID alongside B2C. Existing B2C deployments continue to be supported.

The underlying need remains the same: organizations building consumer-facing applications need a dedicated identity platform designed for consumer scale, self-registration, and social logins that's separate from their corporate identity infrastructure.

---

💬 **Has your organization used B2C (or Entra External ID) for a customer-facing application?** The decision between building identity in-house and using a managed CIAM service is one every team building consumer applications faces. What was the factor that most influenced the decision to use a managed service?
<!-- nav -->

---

[← B2B Collaboration](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-9-b2b-collaboration.md) | [🏠 Contents](/README) | [CIAM →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-11-ciam.md)
