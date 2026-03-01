# SCIM
*The Standard That Automates User Provisioning Across Applications*

**Part of Entra ID Glossary Series: Glossary#9.8 - SCIM**

---

An HR manager described their offboarding process. When an employee left, IT received an email. IT would then manually disable accounts in Active Directory, Salesforce, ServiceNow, GitHub, Jira, Confluence, Slack, and seven other applications. Each application had a different admin interface. Each one took 3-5 minutes. The whole process took 45 minutes per offboarding.

With SCIM provisioning connected between Entra ID and each of those applications, offboarding an employee took under 2 minutes. Disable the account in Entra ID. SCIM propagated the disable to every SCIM-compatible application automatically. The 45-minute manual process became 90 seconds.

## 🔄 What SCIM Is

SCIM (System for Cross-Domain Identity Management) is an open standard API protocol that defines how identity systems communicate user and group data between each other. It provides a standardized way for an identity provider like Entra ID to automatically create, update, disable, and delete user accounts in connected applications.

Without SCIM, provisioning is manual: an admin creates the user in each application separately, using whatever interface that application provides. Changes (name changes, role changes, department transfers) must be replicated manually to each system. Offboarding requires visiting each application individually.

With SCIM, Entra ID is the provisioning orchestrator. When a user account is created, updated, or disabled in Entra ID, SCIM automatically propagates those changes to every application that has a SCIM connection configured.

## 🏗️ How SCIM Works

SCIM defines a REST API with standardized endpoints. Entra ID (the SCIM client) sends HTTP requests to the application's SCIM API (the SCIM server):

**Creating a user** ➕: Entra ID sends a POST request to the application's `/Users` endpoint with the user's attributes in JSON format. The application creates the account and returns the new account's ID.

**Updating a user** 🔄: Entra ID sends a PATCH or PUT request to `/Users/{id}` with the changed attributes. The application updates the account.

**Disabling/deleting a user** 🔴: Entra ID sends a PATCH request setting `active: false` (soft delete/disable) or a DELETE request (hard delete). The application disables or removes the account.

**Sync cycles** ⏱️: Entra ID periodically runs provisioning cycles, sending changes since the last sync to the application. The initial sync creates all in-scope users. Delta syncs apply incremental changes.

## 📋 Attribute Mapping

SCIM defines a standard schema for user attributes (userName, name, emails, phoneNumbers, etc.), but each application may use different attribute names or need different values.

The attribute mapping configuration in Entra ID's provisioning settings maps Entra ID attributes to the application's expected SCIM attributes:

- Entra ID's `userPrincipalName` → Application's `userName`
- Entra ID's `displayName` → Application's `name.formatted`
- Entra ID's `department` → Application's `urn:custom:department`

Some attributes require transformation: combining first and last name into a display name, formatting a phone number, extracting a domain from an email address. Entra ID's attribute mapping supports expressions for these transformations.

The default attribute mappings for gallery applications are pre-configured as a starting point. Most integrations require review and adjustment to match the application's actual requirements.

## 🔍 Scoping: Who Gets Provisioned

Not every user in Entra ID should be provisioned to every application. Scoping filters define who is in scope:

**Group-based scoping** 👥: Provision users who are members of specific groups. The group represents "has access to this application." Adding a user to the group provisions them; removing them triggers deprovisioning.

**Attribute-based scoping** 🎯: Provision users whose attributes meet specific conditions. Users in a specific department, users with a specific job title, users from a specific country.

**All users** 🌐: Provision everyone in the tenant to the application. Appropriate for organization-wide tools but creates large initial syncs for big tenants.

## ⚙️ The Provisioning Modes

**Automatic provisioning** 🤖: Entra ID manages the full provisioning lifecycle. Create on assignment, update on attribute change, disable on removal from scope. This is the target state.

**Manual provisioning**: Admin creates accounts manually. No SCIM connection. Each application is managed independently. This is what SCIM replaces.

## ⚠️ What SCIM Requires from the Application

For Entra ID to provision to an application via SCIM, the application must implement a SCIM 2.0-compliant API. Not all applications do this:

**Gallery apps with SCIM support** ✅: Many popular SaaS applications in the Microsoft Entra gallery have pre-built SCIM provisioning connectors. Salesforce, ServiceNow, Workday, GitHub, Slack, and others. Setup involves configuring the connection, reviewing attribute mappings, and enabling provisioning.

**Custom SCIM endpoint** 🔧: Applications can implement their own SCIM API. Entra ID connects to the custom endpoint. Requires development effort on the application side but provides full integration.

**No SCIM support** ❌: Some applications don't support SCIM and have no plans to. Options: MIM (Microsoft Identity Manager) for on-premises apps with specific connectors, custom automation scripts, or accepting manual provisioning for that application.

---

💬 **What's the application in your environment where SCIM provisioning would save the most manual work if you had it?** The application that's still on the manual offboarding checklist because it doesn't support SCIM is almost universal. What's keeping your highest-pain application from being automated?
<!-- nav -->

---

[← SAML (App Integration Focus)](glossary-9-7-saml-app-integration.md) | [Home](../README.md) | [B2B Collaboration →](glossary-9-9-b2b-collaboration.md)
