# External User
*Managing Access for People Who Don't Work for You*

**Part of Entra ID Glossary Series: Glossary#9.12 - External User**

---

A compliance auditor asked for a list of everyone who had access to the financial reporting SharePoint site. The IT team pulled the access list. 47 users.

23 were internal employees who needed the access. 8 were external accountants from the audit firm. 5 were former employees whose accounts had been disabled but guest access hadn't been cleaned up. 6 were guests from a consulting engagement that had ended two years ago. 5 were unrecognizable email addresses from a previous partnership that no one could explain.

The compliance team's reaction: "You have almost as many external users with access as internal employees, and more than half the external ones shouldn't be there."

External users are not just a technical configuration. They're an identity governance challenge.

## 👤 What an External User Is

In Entra ID, an external user is any identity that originates outside your organization that has been granted access to your tenant's resources. External users appear in your directory as guest user objects, marked with a user type of "Guest" rather than "Member."

External users include:

**Business partners** 🤝: Contacts from partner organizations collaborating on projects, accessing shared resources, or participating in joint work.

**Vendors and contractors** 🔧: External service providers who need access to internal systems to deliver their work. IT vendors, consultants, managed service providers, legal firms.

**Auditors and regulators** 📋: External auditors who need time-limited access to financial systems, compliance documentation, or audit evidence.

**Clients** 💼: In professional services environments, clients may be given access to project workspaces, shared documents, or reporting portals.

**Former employees accessing transition resources** 🔄: Briefly, immediately after departure, while handover documentation is completed.

## 🔑 How External Users Authenticate

External users in Entra ID authenticate against their home identity, not against your tenant:

**Microsoft Entra ID account** 🔵: The most common case in enterprise B2B. The guest authenticates with their own organization's Entra ID account. If their organization requires MFA, they complete it against their home tenant.

**Microsoft consumer account** 🌐: Outlook.com, Hotmail, Live.com. Some external collaborators use personal Microsoft accounts.

**Google account** 🟡: B2B guests can authenticate with Google accounts if Google federation is enabled in the hosting tenant.

**Email one-time passcode** 📧: When none of the above applies, Entra ID can send a one-time passcode to the guest's email. The guest enters it to complete authentication. Doesn't require the guest to have any external account setup.

**Federated IdP** 🏢: If the guest's organization uses a different identity provider (Okta, Ping, ADFS), and cross-tenant federation is configured, guests can authenticate via their home IdP.

## 🔒 What External Users Can Access

External user access is controlled at multiple levels:

**Resource-level permissions** 📁: SharePoint site member, Teams channel access, application assignment. The most direct control. Remove the permission and the guest loses access to that resource.

**Cross-tenant access settings** ⚙️: Tenant-level settings governing what external users from specific tenants or all external tenants can access. Can restrict which applications external users can access, require MFA from external users, and define whether to trust the home tenant's MFA completion.

**Conditional Access policies** 🔐: Policies targeting "All guest and external users" apply across all guest access. Require MFA for all external users regardless of their home MFA, require specific authentication strengths, or restrict access to certain times or locations.

**Default external collaboration settings** 🌐: Controls whether guests can invite other guests, what parts of the directory they can see, and what actions they can perform within the tenant.

## ⚠️ The External User Governance Gap

External users are the most common identity governance failure point. The lifecycle problem:

**Onboarding** ✅: External user is invited and given access. This usually happens with appropriate process and approval.

**During engagement** 🔄: Access is used. This phase may or may not have ongoing review.

**Offboarding** ❌: Engagement ends. The internal sponsor changes roles or leaves the organization. No one thinks to remove the guest access. The guest object sits in the directory indefinitely.

Over time, tenants accumulate guest accounts that should have been removed months or years ago. The compliance audit finding from the opening scenario is common.

Governance mechanisms that help:

**Access reviews for guests** 📋: Periodic reviews (quarterly or annually) where resource owners confirm whether external users still need access. Auto-remove users whose reviewers don't respond or confirm as no longer needed.

**Access packages with expiry** ⏰: In Entitlement Management, access packages for external users can have configurable maximum durations. External access expires automatically without manual action.

**Sign-in inactivity** 👀: Monitor guest accounts with no recent sign-in. Accounts that haven't been used in 90 or 180 days are candidates for review and removal.

---

💬 **What does your external user governance process look like today?** The difference between organizations that have quarterly access reviews for guest accounts and those that haven't reviewed their guest list since it was created is often visible in the size and staleness of their guest user population. What would a clean-up of your current tenant's external users reveal?
<!-- nav -->

---

[← CIAM](glossary-9-11-ciam.md) | [Home](../README.md) | [External Identity →](glossary-9-13-external-identity.md)
