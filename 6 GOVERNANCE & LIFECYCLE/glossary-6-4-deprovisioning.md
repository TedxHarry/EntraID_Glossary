# Deprovisioning: Disabling the Entra ID Account Is Not Enough

**Part of Entra ID Glossary Series: Glossary#6.4 - Deprovisioning**

---

An IT admin walked me through their offboarding process. It was clear and documented: disable the Entra ID account, revoke sessions, remove licenses. Done in under 10 minutes.

I asked about Salesforce. Blank look.

ServiceNow? Another blank look.

GitHub? "Oh, we have a separate process for that. Someone sends an email to the GitHub admin."

The Entra ID account was disabled. The person's identity to the organization's cloud directory was closed. But their accounts in a dozen business applications were sitting open, accessible to anyone who knew the login details or could reactivate them.

Deprovisioning is about more than the Entra ID account.

## 🗑️ What Deprovisioning Actually Means

Deprovisioning is the process of removing or disabling user accounts in applications when that access is no longer needed. It's the downstream complement to disabling the central identity.

The distinction matters because of how SSO works. When an application is integrated with Entra ID for SSO, the user authenticates through Entra ID. If the Entra ID account is disabled, they can't authenticate. So far, so good.

But many applications have their own user databases. Disabling the Entra ID account blocks SSO logins. It doesn't delete the account inside the application. That application account still exists. In some applications, it can be reactivated by the application's own admin. In some, it has its own API key or password separate from SSO. In some, it has shared data or permissions that need to be reassigned before the account can be safely removed.

Deprovisioning handles the application account, not just the identity layer.

## 🔧 Automated Deprovisioning via Provisioning

For applications with SCIM provisioning configured in Entra ID, deprovisioning is automatic. When a user is unassigned from the application in Entra ID (or their account is disabled), the Entra provisioning service sends a DISABLE or DELETE operation to the application's SCIM endpoint. The application account is deactivated or removed without any manual intervention.

This is why provisioning matters for offboarding, not just onboarding. The same provisioning connection that creates the account when someone joins removes it when they leave.

Applications with SCIM provisioning in Entra ID's app gallery: Salesforce, ServiceNow, Workday, SAP, Box, Slack, Zoom, GitHub Enterprise, and hundreds of others.

## 📋 The Non-SCIM Application Problem

For applications without SCIM provisioning, deprovisioning requires manual action. This is the category that generates abandoned accounts.

Common scenarios:

**SSO-only integration**: The application uses Entra ID for SSO but doesn't support SCIM. Disabling the Entra ID account blocks SSO logins. The application account remains active with its own credentials intact.

**Legacy applications**: On-premises systems with no modern API. No automated connection possible.

**Shadow IT applications**: Applications IT doesn't know about, procured by individual teams without going through IT. No integration, no automation, no visibility.

**Third-party SaaS with separate user management**: The vendor's admin console has its own user list. It may sync with Entra ID for login, but account creation and deletion are managed separately.

For these, organizations typically rely on:
- Periodic access reviews that surface active accounts in non-provisioned apps
- Application owner responsibility (designated owners are responsible for deprovisioning in their app)
- Automated ticket creation on departure, with the application owner as the assignee
- Regular reports comparing active app accounts to active Entra ID accounts

## ⚠️ The License Leak Problem

Abandoned accounts in SaaS applications often mean abandoned license seats. Salesforce licenses at $150/user/month. ServiceNow at $100+. GitHub Enterprise at $19. Each former employee who wasn't deprovisioned is a license fee being paid for access no one is using.

I've seen organizations save five figures monthly by running their first serious deprovisioning audit. The cost of not having automated deprovisioning isn't just security risk. It's a recurring operating expense.

## 💡 Building the Application Inventory

You can't deprovision accounts in applications you don't know about. The first step for organizations without mature deprovisioning is an application inventory:

- Which SaaS applications does the organization use?
- Which are connected to Entra ID (SSO and/or provisioning)?
- Which have their own user databases separate from SSO?
- Who is the application owner responsible for user management in each?

That inventory is the map for building deprovisioning coverage, app by app.

---

💬 **How many of your organization's SaaS applications have automated deprovisioning configured through Entra ID?** The gap between "we disabled the Entra ID account" and "all app accounts are removed" is where most offboarding security risk lives. What does your current deprovisioning coverage look like?
<!-- nav -->

---

[← User Offboarding: The Day Someone Leaves Is the Day Access Has to Stop](glossary-6-3-user-offboarding.md) | [Home](../README.md) | [Lifecycle Management: Identity Automation for the Entire Employee Journey →](glossary-6-5-lifecycle-management.md)
