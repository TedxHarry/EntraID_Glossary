# Source of Authority
*Which System Gets to Say Who You Are*

**Part of Entra ID Glossary Series: Glossary#6.18 - Source of Authority**

---

An employee's name changed after marriage. She updated it in Workday herself, as HR had instructed. Two weeks later, her Entra ID display name still showed her old name. Teams showed the old name. Her email still delivered to the old address.

When I investigated, I found that Entra ID had inbound provisioning configured from Workday. But a well-meaning admin had also manually updated her display name in the Entra ID portal three months earlier for an unrelated reason, and the provisioning sync had been treating that manual change as authoritative. The Workday value wasn't overwriting the manually-set Entra ID value because the provisioning direction conflict hadn't been resolved.

Two systems both claimed to be the authority on her name. Neither was winning cleanly.

## 🏛️ What Source of Authority Means

The source of authority (also called source of record or authoritative source) is the designated system whose data is trusted as definitive for a specific attribute or identity. When multiple systems store the same data, the source of authority determines which system's value wins in case of conflict.

For identity data:

- **HR system (Workday, SuccessFactors)**: Authoritative for employment attributes. Name, department, job title, manager, hire date, termination date, employee type, employee ID. These facts exist in HR because HR is where employment decisions are recorded.

- **Entra ID**: Authoritative for authentication attributes, group memberships, application assignments, and access rights. Also the consumer of employment data from HR.

- **Active Directory (on-premises)**: In hybrid environments, may be the source of authority for certain attributes that flow from on-premises to Entra ID via Entra Connect.

## 🔄 Why It Matters in Provisioning

When inbound provisioning is configured from HR to Entra ID, the expectation is clear: Workday is the source of authority for employment data. Changes in Workday flow to Entra ID. Entra ID does not push those attributes back to Workday.

This breaks down when:

**Manual overrides**: An admin edits an attribute directly in Entra ID that should be managed by HR. On the next sync, should the HR value overwrite the manual change? Usually yes, if HR is the source of authority. But provisioning connectors need explicit configuration to enforce this.

**Partial sync**: Some attributes are configured to flow from HR, others are managed locally in Entra ID. Without clear documentation of which system owns which attribute, different administrators make contradictory changes.

**Multiple HR systems**: After mergers or in organizations with separate HR systems per region, no single HR system covers all employees. Each system is authoritative for its population. The provisioning logic must route correctly based on which HR system the user belongs to.

## 📋 Defining Authority by Attribute

A mature identity architecture defines source of authority at the attribute level, not just the identity level:

| Attribute | Source of Authority |
|-----------|-------------------|
| displayName | HR system |
| department | HR system |
| jobTitle | HR system |
| manager | HR system |
| userPrincipalName | IT (set at hire, not HR-managed) |
| accountEnabled | IT (HR termination triggers, IT controls) |
| groupMemberships | IT / Entitlement Management |
| mobilePhone | User self-service |
| mfaMethods | User self-service |

Documenting this table and configuring provisioning to enforce it prevents the conflict that created the name-change problem above.

## ⚠️ When Source of Authority Is Unclear

The absence of a documented source of authority creates predictable problems:

- HR updates a user's department, provisioning syncs it to Entra ID, but a local Entra ID admin had set a different department value for a dynamic group rule. Which value the dynamic group uses depends on which runs last.

- A user's manager changes in HR, but someone also updated the manager attribute in Entra ID directly for a PIM approval workflow. Approval notifications go to the wrong person until the sync catches up.

- An employee's name change sits in HR for two weeks because the provisioning sync is confused about which system owns the value.

## 💡 The Governance Implication

Source of authority is a governance question as much as a technical one. The technical configuration follows the governance decision: which team owns this attribute, from which system, and what happens if there's a conflict?

Making this explicit in your identity governance documentation means provisioning configurations, manual edit policies, and administrative procedures all point in the same direction.

---

💬 **Has your organization had a conflict between what the HR system says and what Entra ID shows for a user's attributes?** The name-change scenario is one of the most visible, but department, manager, and title conflicts cause quieter but equally real problems. How did you resolve the authority question?
<!-- nav -->

---

[← User Attributes](glossary-6-17-user-attributes.md) | [Home](../README.md) | [Identity Verification →](glossary-6-19-identity-verification.md)
