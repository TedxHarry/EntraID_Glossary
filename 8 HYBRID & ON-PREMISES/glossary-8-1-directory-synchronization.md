# Directory Synchronization
*Bridging On-Premises Identity with the Cloud*

**Part of Entra ID Glossary Series: Glossary#8.1 - Directory Synchronization**

---

A 3,000-person organization had run on-premises Active Directory for 12 years. Every user account, every group, every password was in their domain controllers. When they moved to Microsoft 365, they had a choice: recreate all 3,000 accounts in Entra ID manually, or synchronize them from AD.

They chose synchronization. Over a weekend, Entra Connect ran its initial sync. Monday morning, every user signed into Microsoft 365 with the same username and password they'd been using for years. Nothing changed from the user's perspective. Everything was now in the cloud from IT's perspective.

Directory synchronization is the bridge that makes hybrid identity work for organizations that can't or won't leave Active Directory behind.

## 🔄 What Directory Synchronization Is

Directory synchronization is the process of copying identity objects (users, groups, contacts) and their attributes from on-premises Active Directory to Entra ID, and keeping them in sync as changes occur.

It's not a one-time migration. Sync is ongoing. When a new user is created in AD, sync copies them to Entra ID. When an attribute changes (name, phone, department), sync updates it in Entra ID. When an account is disabled in AD, sync propagates the disabled state to Entra ID.

The source of truth is on-premises AD. Entra ID is the cloud representation. Synchronized objects in Entra ID are marked as synced, which means most attributes can only be modified from the on-premises source. The cloud representation reflects the on-premises object.

## 🏗️ What Gets Synchronized

**Users** 👤: The primary sync object. User attributes, including displayName, userPrincipalName, mail, department, manager, and hundreds of other attributes. The UPN is critical: it determines the cloud sign-in identifier.

**Groups** 👥: Both security groups and distribution lists can be synchronized. Group membership is synced alongside the group definition. Synchronized groups can be used in Entra ID for license assignment, application access, and Conditional Access.

**Contacts** 📇: External contacts from the on-premises GAL (Global Address List) can be synced for address book purposes.

**Devices** 💻: Hybrid Entra Join syncs device objects, giving devices a presence in both AD and Entra ID. Covered separately from directory sync for users.

**What doesn't sync by default**: Passwords (handled separately by Password Hash Sync), certain privileged attributes, objects in specific OUs if filtered out.

## 🎯 Sync Rules and Attribute Filtering

Directory synchronization is configurable. Organizations can control:

**OU filtering** 📁: Specify which Organizational Units in AD are included in sync scope. Users in excluded OUs don't appear in Entra ID. Useful for keeping service accounts, test accounts, or legacy objects out of the cloud.

**Attribute filtering** 🔧: Control which attributes are synchronized for each object type. Some attributes should be included (name, department, manager). Some may be excluded for privacy or policy reasons.

**Group scoping** 👥: Sync all groups or only specific groups. For large ADs with thousands of groups, syncing only the groups relevant to cloud services reduces noise.

**Sync rules engine** ⚙️: Entra Connect has a rules engine that allows custom transformation of attribute values during sync. A user's AD attribute can be mapped to a different Entra ID attribute, or computed from a combination of AD values.

## ⚠️ The Source of Truth Problem

Synchronized objects can't be fully managed from Entra ID. When an attribute is managed on-premises and synced to the cloud, changes made directly in Entra ID are overwritten on the next sync cycle.

This creates operational confusion:

- An admin changes a user's department in the Entra admin center
- The next sync runs and overwrites the change with the on-premises value
- The admin's change disappears silently

Understanding which attributes are "in-scope" for sync (managed on-premises, displayed in cloud) versus "out-of-scope" (can be modified in cloud) is important for administrators working in hybrid environments.

## 🔗 The Authentication Question

Directory sync copies identity objects. It doesn't automatically solve authentication. Users whose accounts are synced to Entra ID still need a way to authenticate against the cloud. The authentication method depends on the sync configuration:

**Password Hash Sync (PHS)**: Passwords are hashed on-premises and the hash is copied to Entra ID. Users authenticate directly against Entra ID. No on-premises infrastructure required for authentication.

**Pass-Through Authentication (PTA)**: Entra ID passes the authentication request to on-premises agents. The password is validated against on-premises AD. Passwords never exist in the cloud.

**Federation (ADFS)**: Authentication is redirected to on-premises Federation Services. The most complex option, increasingly replaced by PHS and PTA.

Directory sync without a configured authentication method leaves synced users without a working cloud sign-in.

## 💡 Sync Health and Monitoring

Directory sync is infrastructure that needs monitoring. Common failure scenarios:

- Sync agent service stops running
- Network connectivity between the sync server and Entra ID fails
- AD permissions issues prevent the sync account from reading objects
- Attribute conflicts when an object in AD matches an existing cloud object
- Object exceeding sync rules (objects that fail sync rules are silently skipped)

Entra Connect Health (available with Entra ID P2) provides monitoring dashboards, alerts, and error reporting for sync issues. The basic sync status is visible in the Entra admin center without P2. Error-level events should be investigated promptly: a stopped sync means changes in AD (new hires, terminations, role changes) are not reaching Entra ID.

---

💬 **What was the first directory sync issue that caused a visible incident in your organization?** The sync failure that delays a new hire's access on their first day, or the attribute conflict that causes a user's email address to be wrong in the GAL, are the ones that get noticed quickly. What was your earliest sync incident and what did it change about how you monitor sync health?
<!-- nav -->

---

[← CAE (Continuous Access Evaluation)](../7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-32-cae.md) | [Home](../README.md) | [Entra Connect →](glossary-8-2-entra-connect.md)
