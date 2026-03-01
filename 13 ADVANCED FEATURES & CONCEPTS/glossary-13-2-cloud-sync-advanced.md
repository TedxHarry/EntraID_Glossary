# Cloud-Based Sync (Advanced)
*Complex Synchronization Scenarios Beyond the Basics*

📚 **Part of Entra ID Glossary Series: Glossary#13.2 - Cloud-Based Sync (Advanced)**

---

A merger brought together two companies, each with its own on-premises Active Directory forest. The combined organization needed both forests synchronized to a single Entra ID tenant. One forest had 8,000 users. The other had 3,500. Their UPN suffixes overlapped. Their organizational unit structures were completely different.

This isn't a "install Entra Connect Cloud Sync and you're done in an afternoon" scenario. This is the advanced territory where the choices made in synchronization configuration have long-term consequences for every identity in both organizations.

## 🔧 Multi-Forest Synchronization

Entra Connect Cloud Sync supports synchronization from multiple Active Directory forests to a single Entra ID tenant. Each forest gets its own provisioning agent installed on a domain-joined server within that forest. Each agent connects to the cloud synchronization service and feeds identity data from its forest into Entra ID.

The challenge with multi-forest synchronization isn't the technical setup; it's the object matching. When a user exists in both forests (employees who've been in both organizations, or service accounts that were duplicated), Cloud Sync needs to know whether to create one Entra ID user or two.

The matching is controlled by the source anchor attribute. A common approach in merger scenarios: use the `objectGUID` from each forest as the source anchor, accept that merged users will have two Entra ID accounts until a deliberate cleanup is done, and plan the consolidation separately. Trying to automatically merge identities from different forests often creates more problems than it solves.

## 🎯 Scoping Filters

Cloud Sync doesn't have to synchronize an entire forest. Scoping filters control which objects are included in synchronization.

**Group-based scoping** 👥: Only synchronize users who are members of a specific Active Directory group. Useful for piloting Cloud Sync before full deployment, or for permanently excluding populations (service accounts, test users) from synchronization.

**OU-based scoping** 📁: Only synchronize users from specific Organizational Units. Useful when different OUs represent different business units with different synchronization needs.

**Attribute-based scoping** 🔷: Only synchronize users where a specific attribute has a specific value. `extensionAttribute1 = "SyncToCloud"`. Allows fine-grained control without OU restructuring.

Scoping filters can be combined. A common pattern in complex environments: synchronize users in specific OUs who are members of a specific group and have a specific attribute set, excluding all others.

## 🔄 Attribute Mapping and Transformations

Cloud Sync's attribute mapping configuration defines how on-premises AD attributes populate Entra ID user attributes. Default mappings handle the standard cases. Advanced scenarios require custom mappings.

**Direct mapping** 📋: `givenName` in AD maps to `givenName` in Entra ID. One-to-one.

**Expression-based mapping** ⚙️: Transformations applied during synchronization. Combining `givenName` and `sn` (surname) into `displayName` with formatting. Extracting a substring from a longer attribute. Normalizing email addresses that have inconsistent casing in the source.

**Constant mapping** 🔵: Setting an Entra ID attribute to a fixed value regardless of the source. Useful for setting attributes that indicate the synchronization source or the organizational unit for governance purposes.

The expression language for attribute mapping in Cloud Sync is the same as in Entra Connect sync rules, using functions like `Append`, `Replace`, `Join`, `Mid`, and `Switch`.

## 📦 Provisioning On-Demand

One of the most useful Cloud Sync features for advanced troubleshooting and testing: provisioning on-demand. You can trigger synchronization for a specific user or group without waiting for the next sync cycle.

This is invaluable for:
- Testing new attribute mapping rules against a specific user before rolling out to the full population
- Verifying that a specific user's on-premises attributes are being transformed correctly
- Diagnosing why a specific user isn't appearing in Entra ID after an on-premises change
- Confirming that scoping filter changes include or exclude the expected users

On-demand provisioning surfaces the full attribute mapping output and any errors, making it far easier to debug than waiting through sync cycles and checking logs.

## ⚠️ Cloud Sync vs Entra Connect for Complex Scenarios

Cloud Sync has grown significantly in capability, but some complex scenarios still require Entra Connect:

- Device synchronization (Hybrid Azure AD Join requires Entra Connect)
- Exchange hybrid (mailbox coexistence between on-premises Exchange and Exchange Online requires Entra Connect)
- Advanced sync rules with complex object transformations that exceed Cloud Sync's expression capabilities
- Organizations with very large directories where Entra Connect's full directory import has performance advantages

For new deployments without Exchange hybrid or device hybrid requirements, Cloud Sync is the preferred choice. For existing Entra Connect deployments, migration to Cloud Sync is possible but requires planning.

---

💬 **Has your organization's synchronization architecture evolved beyond a single forest to single tenant setup, and what were the most complex attribute mapping or scoping challenges you had to solve?** Multi-forest scenarios from mergers and acquisitions are the most common driver of advanced synchronization complexity. What decision in your sync configuration do you wish you'd made differently at the start?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Attribute-Based Access Control (ABAC)](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-1-abac.md) | [🏠 Contents](/README) | [Continuous Authorization (CAE) →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-3-continuous-authorization.md)
