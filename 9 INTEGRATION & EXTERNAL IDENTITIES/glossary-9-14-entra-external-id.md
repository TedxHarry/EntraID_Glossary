# Entra External ID
*Microsoft's Unified Platform for Non-Employee Identities*

📚 **Part of Entra ID Glossary Series: Glossary#9.14 - Entra External ID**

---

Microsoft's external identity landscape used to have multiple separate products: Azure AD B2C for customers, Azure AD B2B for business partners, and a growing number of overlapping features between them. Organizations building both customer-facing applications and partner collaboration tools had to learn two different systems with two different architectures.

Microsoft Entra External ID is the consolidation of these scenarios under a single product umbrella. One brand, two deployment models: an external tenant for customer-facing applications and B2B collaboration features built into workforce tenants for business partner access.

Understanding what changed and what stayed the same is important for anyone working in this space.

## 🌐 What Entra External ID Is

Microsoft Entra External ID is the product family that covers identity management for people who aren't employees of your organization. It encompasses:

**B2B collaboration** for workforce tenants: The B2B guest invitation and collaboration capabilities that have been in Entra ID for years, now branded as part of External ID. Business partners, vendors, and contractors invited as guests. Not a new product; existing B2B features under the External ID umbrella.

**External tenants** for customer-facing applications: A new tenant type specifically designed for CIAM scenarios, replacing Azure AD B2C for new implementations. A separate Entra ID tenant configured for managing customer or consumer identities, with self-registration, social logins, and consumer-grade authentication experiences.

## 🏗️ The Two Deployment Models

**Within a workforce tenant** (B2B collaboration):

Your organization's corporate Entra ID tenant. Employees are Member users. Business partners, vendors, and collaborators are Guest users, added via B2B invitation. They authenticate with their home organizational or consumer identity. The workforce tenant grants them access to specific resources.

This is the model for: consulting firm clients needing project portal access, vendor engineers needing SharePoint access, audit firms needing financial system read access, partners collaborating in Teams.

**External tenant** (CIAM, replacing B2C):

A separate Entra ID tenant created specifically for customer identity. Not the corporate tenant. Has a different configuration profile focused on consumer-facing identity. Supports self-registration flows, social identity providers (Google, Facebook, Apple), branded sign-up and sign-in pages, and token issuance for customer-facing applications.

This is the model for: retail customer accounts, banking app users, insurance policy holder portals, consumer SaaS product authentication.

## 🔄 Entra External ID vs Azure AD B2C

For organizations evaluating or migrating CIAM solutions:

**Azure AD B2C**: The established CIAM product. Widely deployed, mature feature set, extensive documentation and community. Based on Identity Experience Framework with user flows and custom policies. Still fully supported. New features are being added.

**External Tenant (Entra External ID for CIAM)**: The newer architecture. Unified with the Entra ID platform rather than being a completely separate service. More modern developer experience. Uses Microsoft Entra identity platform APIs (MSAL, same endpoints as enterprise Entra ID). User flows are available but the custom policy engine (IEF) that B2C is known for is not yet fully available in external tenants.

For new CIAM implementations, Microsoft recommends evaluating external tenants as the forward-looking architecture. For existing B2C deployments, migration is not yet required; B2C remains supported.

## ⚙️ Key Features of External Tenants

**Self-service sign-up** 📝: Users can register themselves using email/password or linked social accounts. Verification and approval flows are configurable.

**Social identity providers** 🌐: Google, Facebook, and Apple as sign-in options for consumers who don't want another password.

**Custom branding** 🎨: Fully customizable sign-in pages, backgrounds, logos, and copy to match the consumer application's brand.

**MSAL compatibility** 💻: External tenants use the same Microsoft Authentication Library that enterprise applications use. Developers familiar with MSAL can apply the same skills to consumer identity.

**Multi-language support** 🌍: Sign-up and sign-in pages in multiple languages based on browser settings.

**MFA options** 📱: Email OTP, SMS, and authenticator apps available for consumer MFA requirements.

## 🔒 Cross-Tenant Access Settings

For workforce tenants with B2B collaboration, cross-tenant access settings control the trust relationship between your tenant and specific partner tenants:

**Inbound settings**: What to trust from guest users coming into your tenant. Trust the home tenant's MFA completion, trust home tenant's compliant device claim.

**Outbound settings**: What your users can access in other tenants. Which applications in partner tenants your users are allowed to access.

This setting is particularly important for organizations with strong partner relationships where the default "require our own MFA from all guests" creates unnecessary friction for partners using well-managed Entra ID tenants.

---

💬 **Is your organization evaluating the transition from Azure AD B2C to Entra External ID external tenants, or is B2C meeting your needs well enough that migration isn't a priority?** The consolidation of Microsoft's external identity products is still in progress. What feature gap would have to close before you'd consider migrating an existing B2C deployment?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← External Identity](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-13-external-identity.md) | [🏠 Contents](/README) | [Workforce Tenant →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-15-workforce-tenant.md)
