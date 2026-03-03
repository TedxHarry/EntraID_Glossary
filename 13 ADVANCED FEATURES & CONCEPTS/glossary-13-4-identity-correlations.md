# Identity Correlations
*Matching the Same Person Across Different Systems*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #13.4 - Identity Correlations

---


A company acquired a smaller firm. The acquired firm had 400 employees. The acquiring company had 12 of those same people already in their system: contractors who had been working for both companies simultaneously.

When the acquisition team began merging directories, they found 12 duplicate identity situations. The same real person, two accounts in Entra ID. Two email addresses. Two sets of permissions. Two license assignments. Merge the accounts and you lose one identity's history. Keep them separate and you have an identity sprawl problem.

Identity correlation is the practice of recognizing that two digital identities represent the same real person or entity, and managing that relationship deliberately.

## 🔗 What identity correlation means

Identity correlation is the process of linking, matching, or resolving identity records across different systems or directories. The goal is to answer: "Is this identity in System A the same entity as that identity in System B?"

In the context of Entra ID, correlation problems appear in several forms:

**On-premises to cloud matching** ☁️: During directory synchronization, the sync engine must match on-premises AD users to their existing Entra ID accounts. If the match fails, a new Entra ID account is created instead of linking to the existing one. This creates duplicate accounts.

**HR system to directory correlation** 👤: HR-driven provisioning systems (Workday, SAP SuccessFactors) must match HR records to directory accounts. The EmployeeId attribute is typically the correlation anchor: the HR system knows the employee's ID, the directory account contains the same ID, and the provisioning system uses this to link them.

**Cross-tenant user correlation** 🌐: In multi-tenant environments or after mergers, the same user may have accounts in multiple Entra ID tenants. Understanding which accounts belong to the same person is necessary for consolidation and governance.

**Application account correlation** 📋: A user in Entra ID needs to be matched to their account in connected applications (Salesforce, ServiceNow, GitHub) for provisioning and deprovisioning to work correctly.

## 🔑 The source anchor and immutableid

The primary correlation mechanism in hybrid identity synchronization is the source anchor: an immutable, unique attribute from the source directory that persists as the correlation key in Entra ID.

For Entra Connect and Cloud Sync, the default source anchor is derived from the on-premises `objectGUID`. This GUID is stable even if the user's name, UPN, or other attributes change. The Entra ID `immutableId` attribute stores this value.

When synchronization runs for the first time and an on-premises user doesn't match an existing Entra ID user by `immutableId`, a new Entra ID account is created. When the `immutableId` matches, the on-premises attributes update the existing account.

Getting this matching right is critical before the first synchronization run. Organizations that let synchronization run before thinking about correlation often end up with duplicate accounts that are difficult to clean up without user disruption.

## 📊 EmployeeId as the HR correlation anchor

For Lifecycle Workflows and HR-driven provisioning, the correlation attribute between the HR system and Entra ID is typically `employeeId`. The HR system knows who this person is (they have an employee ID from day one of employment). The IT system needs to create a directory account for them. The connection between those two records is the `employeeId`.

In practice, the HR system triggers the provisioning: "New employee, ID 84721, starts Monday." Entra ID provisioning looks for a directory account where `employeeId = 84721`. If found (a pre-existing contractor account), it updates it. If not found, it creates a new one.

The `employeeId` attribute is the correlation anchor that makes automated joiner-mover-leaver processes reliable. Without it, provisioning systems resort to name matching (fragile) or email matching (also fragile for movers and name changes).

## 🔄 Handling duplicate identities

When the same person has two identity records that should be one, the options are:

**Merge**: Combine the accounts into one, transferring access and data from one to the other. Requires determining which account is the "primary" and which is the "secondary." May require re-provisioning the user into applications under the new unified identity.

**Soft-match**: The sync engine can correlate an on-premises user to an existing Entra ID cloud-only user using `proxyAddresses` or `userPrincipalName` matching. If the email addresses match, the sync engine treats them as the same identity and links them. This is the mechanism for connecting existing cloud accounts to their on-premises counterparts without deleting and recreating.

**Manage separately**: For true separation of duties cases (the contractor who genuinely needs separate identities in different contexts), maintaining two accounts is the right answer. Document it explicitly as intentional.

## ⚠️ The governance gap

The most common identity correlation failure: nobody tracked that a contractor account exists when a permanent employee account is created for the same person. Contractors become full employees. The contractor account isn't disabled. Six months later, a governance audit finds the person has two active accounts with different permissions.

Correlation at joiner events (when a new account is created, check for existing accounts for this person) is as important as correlation during synchronization setup.

---

💬 **Does your organization have a process for detecting and resolving duplicate identities when a person's employment status changes (contractor to employee, acquisition, etc.)?** The identity duplication problem is common in environments with both contractor and employee populations, or after acquisitions. What's the most complex identity correlation scenario your team has had to resolve?
✍️ TedxHarry

<!-- nav -->

---

[← Continuous Authorization (CAE)](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-3-continuous-authorization.md) | [🏠 Contents](/README) | [Passwordless Auth (Advanced) →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-5-passwordless-auth-advanced.md)
