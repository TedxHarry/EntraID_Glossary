# External Tenant: The Entra ID Tenant Type Built for Your Customers

**Part of Entra ID Glossary Series: Glossary#9.16 - External Tenant**

---

A retail company has 5,000 employees and 3 million loyalty program members. Both populations need digital accounts. Both need to sign in to applications. Both need identity management.

But they can't share a tenant.

Employees belong in the workforce tenant: corporate Entra ID, Conditional Access policies, managed devices, MFA enforcement, PIM for elevated access. Putting 3 million retail customers into that tenant would be architecturally wrong, operationally unmanageable, and commercially absurd from a licensing standpoint.

The external tenant is what Microsoft built for the customer side of that equation.

## 🏗️ What an External Tenant Is

An external tenant is a specific Entra ID tenant type created for managing non-employee identities in consumer-facing applications. It's a purpose-built identity environment for customers, not a modified version of the workforce tenant.

When you create a tenant through the Entra admin center and select the external tenant option, you get an Entra ID tenant with a configuration profile tuned for consumer identity: self-registration flows enabled, social identity providers available, customizable branded sign-in pages, token issuance configured for customer-facing applications, and pricing structured for consumer-scale account volumes.

It's not the same as a workforce tenant with guest users. Guests in a workforce tenant are business partners who collaborate with your employees. Accounts in an external tenant are customers who use your product.

## 🔄 External Tenant vs Workforce Tenant

The two tenant types sit side by side in the Entra External ID architecture, but they're built for completely different jobs:

**Workforce tenant** 👔: Employees are Member accounts, provisioned by IT. Corporate security policies apply: Conditional Access, device compliance, FIDO2 and Microsoft Authenticator for MFA. B2B guest invitations for business partner access. Licensing at per-user rates. Admin-centric: IT provisions, IT removes, IT reviews.

**External tenant** 🛍️: Customers self-register. No IT provisioning involved. Social identity providers (Google, Facebook, Apple) as first-class login options alongside email and password. Consumer-friendly MFA options. Fully branded sign-in and registration pages that match your application's look. Pricing per authentication, not per user. Customer-centric: self-service account creation, self-service password reset, self-service account deletion.

You don't configure a workforce tenant to become an external tenant. They're different tenant types selected at creation. An organization with both a customer-facing application and an internal employee base runs both types, managed from separate admin portals.

## ⚙️ What External Tenants Provide

**Self-service registration** 📝: Customers create their own accounts through configurable sign-up flows. Email verification, attribute collection, social account linking. No admin action required for account creation.

**Social identity providers** 🌐: Google, Facebook, and Apple as sign-in options. Customers use identities they already have rather than creating another username and password. Each social provider requires configuration in the external tenant, but Microsoft has reduced this to a supported, documented setup rather than a custom integration.

**Branded experience** 🎨: Sign-in and sign-up pages that look like your application, not like a Microsoft login screen. Custom backgrounds, logos, colors, and copy. Multi-language support based on browser settings.

**User flows** 🔄: Pre-built, configurable authentication policy templates for sign-up and sign-in, password reset, and profile editing. Define the registration fields, MFA requirements, and social provider options through admin configuration rather than custom code.

**MSAL compatibility** 💻: External tenants use Microsoft Authentication Library and the same Microsoft identity platform endpoints that enterprise applications use. Developers already familiar with MSAL can apply the same patterns to customer-facing applications built against external tenants.

**MFA for consumers** 📱: Email OTP and SMS as consumer-accessible MFA options, in addition to authenticator apps for customers who use them.

## 🔮 External Tenant and Azure AD B2C

For anyone coming from Azure AD B2C: the external tenant is the architectural successor. Not a direct replacement that requires immediate migration, but the forward-looking platform that Microsoft is building CIAM features into going forward.

B2C uses the Identity Experience Framework for its custom policy engine, which allows complex multi-step authentication flows, external API calls during sign-in, and custom claims transformations. That IEF-based custom policy engine isn't yet fully available in external tenants. For new implementations, external tenants offer a more integrated, modern architecture. For existing B2C deployments with complex custom policies, migration isn't yet straightforward and isn't required.

The external tenant is where Microsoft's CIAM investment is going. Over time, the feature gap with B2C will close.

## 🔐 Keeping the Populations Separate

The architecture question that comes up in practice: can the workforce tenant and external tenant share anything?

The administration is separate. External tenants have their own admin portal. IT teams managing the workforce tenant are typically different from (or at least operating differently than) teams managing the external tenant.

The identities don't cross. A customer account in the external tenant isn't a guest in the workforce tenant. There's no automatic federation between them. If a customer also happens to be an employee, they have separate accounts in separate tenants. That's by design.

Applications can be multi-tenant and registered in either tenant depending on their audience. A customer-facing application registers its application object in the external tenant. Internal tools register in the workforce tenant.

---

💬 **Is your organization running both a workforce tenant and an external tenant today, or is customer identity still handled separately from your Entra ID environment?** The decision to adopt external tenants versus continuing with B2C or a third-party CIAM platform comes up differently for every organization. What would have to be true about external tenants for you to migrate an existing B2C deployment?

#EntraID #ExternalTenant #EntraExternalID #CIAM #CustomerIdentity #MicrosoftEntra #WorkforceTenant
