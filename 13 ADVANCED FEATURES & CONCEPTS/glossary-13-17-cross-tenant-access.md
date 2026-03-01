# Cross-Tenant Access
*Controlling How Your Tenant Interacts With Other Entra ID Tenants*

**Part of Entra ID Glossary Series: Glossary#13.17 - Cross-Tenant Access**

---

A company with 3,000 employees acquired a company with 800 employees. Both had Entra ID tenants. The combined organization needed the acquired company's employees to collaborate in Microsoft Teams, access SharePoint, and use shared applications, all while maintaining separate tenants for the integration period.

The default B2B configuration would work for inviting individual guests. But the security team wanted something more specific: trust the acquired company's Entra ID MFA completion (so their users don't get prompted for MFA twice), restrict which applications they can access, and ensure their users appear with their actual organization name rather than showing as generic guests.

This is what cross-tenant access settings are designed to control.

## ⚙️ What Cross-Tenant Access Settings Are

Cross-tenant access settings are a framework in Entra ID that controls how your tenant interacts with specific other Entra ID tenants or with all external Entra ID tenants by default. They define the trust relationship and access boundaries between tenants at a more granular level than the old blanket B2B configuration.

The settings are organized along two dimensions:

**Default settings vs partner-specific settings** 🌐: Default settings apply to all external tenants not explicitly configured. Partner-specific settings override the default for a specific tenant. You can have a permissive default and restrictive settings for specific partners, or a restrictive default and permissive settings for trusted partners.

**Inbound vs outbound** 🔄: Inbound settings control what external users from other tenants can do when accessing your resources. Outbound settings control what your users can do when accessing resources in other tenants.

## 🔐 Inbound Settings: What You Trust From External Tenants

**Trust their MFA** ✅: When a guest from the partner tenant authenticates with MFA at their home tenant, trust that MFA completion without requiring them to re-complete MFA in your tenant. Without this setting, every guest gets an MFA prompt regardless of whether they just completed MFA for their own organization. With this setting, guests from well-managed partner tenants have a smoother experience.

**Trust their compliant device claim** 💻: When a guest's device is marked compliant in their home tenant's Intune, trust that compliance state in your Conditional Access policies. Allows device-based Conditional Access policies to apply meaningfully to guests who have managed devices.

**Trust their Hybrid Joined device claim** 🔗: Trust the partner tenant's Hybrid Azure AD Join device registration. Relevant for organizations where Hybrid Join is the device management model.

**Application access restrictions** 📱: Which applications in your tenant external users from this tenant are allowed to access. Block access to specific sensitive applications while allowing collaboration in Teams and SharePoint.

## 🔄 Outbound Settings: What Your Users Can Do in External Tenants

**B2B collaboration** 👥: Whether your users can be invited to and collaborate in other tenants. Restrict outbound collaboration to specific trusted tenants, preventing your users from accepting guest invitations to unknown external tenants.

**B2B direct connect** 🔗: Whether your users can participate in shared channels with specific partner tenants without full guest account creation.

**Application access in external tenants** 📱: Which external tenant applications your users can access. Complements tenant restrictions controls.

## 🔄 Cross-Tenant Synchronization

Beyond access control, cross-tenant settings also enable cross-tenant synchronization: provisioning users from one Entra ID tenant into another as guest accounts, automatically, using the same SCIM-based provisioning engine as application provisioning.

For multi-tenant organizations (post-merger integration periods, companies that maintain separate tenants for different business units), cross-tenant synchronization allows automatic provisioning and deprovisioning of user accounts across tenants without manual invitation workflows.

A user in Tenant A gets provisioned as a B2B guest in Tenant B automatically when they join a cross-tenant sync scope. When they leave the organization or are removed from scope, the guest account is deprovisioned automatically.

## 🔒 B2B Direct Connect

B2B Direct Connect is a specific cross-tenant access scenario for shared Microsoft Teams channels. Instead of inviting users as guests (creating guest objects in your directory), B2B Direct Connect allows users from a partner tenant to access shared channels directly using their home tenant identity.

Requires explicit cross-tenant access configuration on both sides: both tenants must configure inbound/outbound B2B Direct Connect settings for each other. More seamless for users than traditional B2B, but requires administrative coordination between both tenant administrators.

---

💬 **Has your organization needed to configure partner-specific cross-tenant access settings for a major collaboration or post-acquisition scenario, and what was the most complex trust configuration you had to work through?** The cross-tenant access settings framework replaced a lot of manual workarounds for trusted partner scenarios. What was your B2B collaboration experience like before these controls were available?
<!-- nav -->

---

[← Enterprise Application (Advanced)](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-16-enterprise-application-advanced.md) | [🏠 Contents](/README) | [Tenant Restrictions →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-18-tenant-restrictions.md)
