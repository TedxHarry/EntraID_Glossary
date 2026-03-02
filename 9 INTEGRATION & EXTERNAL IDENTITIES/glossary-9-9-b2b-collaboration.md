# B2B Collaboration
*Giving External Partners Access Without Managing Their Identity*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #9.9 - B2B Collaboration

---

## 🎯 TL;DR

- B2B Collaboration lets you invite guest users from other organizations to access your tenant's resources
- Guest accounts use the invited user's home organization credentials : you don't manage their passwords
- Control guest access with Entra ID B2B settings, Cross-Tenant Access policies, and Conditional Access


A consulting firm worked with 40 different client organizations simultaneously. Their consultants needed access to client SharePoint sites, Teams channels, and shared project tools. Their clients needed access to the consulting firm's project management platform.

The old approach: create internal accounts for each external person who needed access. An IT request, a temporary password, a manual account to manage and eventually clean up. With a rotating cast of 200+ external collaborators, this was a constant administrative burden.

B2B Collaboration changed the model. External collaborators sign in with their own organization's identity. The consulting firm grants access to specific resources. When the project ends, access is revoked. The external collaborators never needed a separate account in the firm's tenant.

## 🤝 What B2B collaboration is

Microsoft Entra B2B (Business-to-Business) Collaboration allows organizations to grant external users access to their resources by inviting them as guests, where those guests sign in using their own existing identity from their home organization or consumer identity.

The key distinction: the external user doesn't get a new account in your tenant. They bring their own identity. Your tenant grants them access to specific resources. They authenticate against their home identity provider. You control what they can access. They control their own credentials.

This is fundamentally different from creating internal accounts for external people. With B2B, identity remains where it belongs (with the user's home organization), while access to specific resources is governed by the hosting organization.

## 👤 Guest user objects in Entra ID

When an external user is invited via B2B, a guest user object is created in the hosting organization's Entra ID directory. This guest object:

- Has its own Object ID in the tenant
- Is marked with a user type of "Guest" (as opposed to "Member" for internal users)
- Contains the external user's email address and basic profile information
- Does NOT contain authentication credentials (the user authenticates against their home IdP)

The guest object is the anchor that allows the hosting organization to assign permissions, group memberships, and access packages to the external user. It's a reference to an external identity, not a full identity record.

## 🔐 How guest authentication works

When a guest user signs in to access a resource in the hosting tenant:

1. Guest navigates to a resource in the hosting tenant (SharePoint site, Teams channel, app)
2. Entra ID recognizes the user as a guest based on their email domain
3. Entra ID redirects to the guest's home identity provider for authentication
4. The guest authenticates with their home organization's credentials (including their home MFA)
5. The home IdP issues a token to Entra ID
6. Entra ID validates the token and issues access to the requested resource

If the external user doesn't have an organizational Microsoft account, they can authenticate with a Microsoft consumer account (Outlook.com), a Google account, or a one-time passcode sent to their email.

## 🔒 Access control for guest users

Guest users in Entra ID have reduced default permissions compared to member users. By default, guests:

- Can't enumerate other users in the directory
- Can't see other guests or groups they're not members of
- Have read-only access to their own profile
- Cannot register applications

Access to specific resources is granted explicitly: SharePoint site member, Teams channel member, application assignment, access package in Entitlement Management.

**Conditional Access for guests** 🔐: Conditional Access policies can target "All guest and external users" specifically. A common pattern: require MFA for guests who may not have strong home authentication. Even if a guest's home organization uses SMS OTP, your Conditional Access policy can require a stronger method for accessing your resources.

**Cross-tenant access settings** ⚙️: Configurable settings control what level of trust to place in the guest's home MFA. If the guest's home organization uses compliant managed devices and Entra ID, you can trust their MFA completion. If their home setup is unknown, requiring additional MFA for your resources is appropriate.

## 📧 Invitation and redemption

**Sending invitations** ✉️: Admins or (if allowed) users can send B2B invitations to external email addresses. The invitation email contains a redemption link.

**Redemption** 🔗: The external user clicks the link, authenticates with their home identity, and accepts the invitation. The guest object in the hosting tenant is activated.

**Direct federation** 🤝: For partner organizations with their own Entra ID tenants, cross-tenant access settings can be configured to allow more seamless collaboration: the guest authenticates against their home Entra ID without a redemption email flow.

## ⚠️ Guest access governance

The guest lifecycle requires active management:

- Guests accumulate when projects end and access isn't revoked
- Access reviews should include guest users, reviewing whether external access is still needed
- Entitlement Management access packages with expiry dates automate time-limited guest access
- Guest accounts with no recent sign-in (180+ days) are candidates for removal

---

💬 **What's your organization's process for managing the lifecycle of guest users in your tenant?** The "guests who stayed long after the project ended" problem is universal. How do you handle the review and cleanup of stale guest access, and what prompted you to formalize the process?
✍️ TedxHarry

<!-- nav -->

---

[← SCIM](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-8-scim.md) | [🏠 Contents](/README) | [B2C →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-10-b2c.md)
