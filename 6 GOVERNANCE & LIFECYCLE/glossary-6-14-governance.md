# Governance: The System That Keeps Access from Running Away from You

**Part of Entra ID Glossary Series: Glossary#6.14 - Governance**

---

An organization had 4,200 users and roughly 340 Entra ID groups. Nobody had a clear picture of which groups granted access to what. Group owners had turned over. Several groups had no owner at all. The membership rules for dynamic groups hadn't been reviewed in two years.

One group called "Project Alpha Temp Access" had 67 members. Project Alpha had ended 14 months earlier.

This is what happens without governance: access accumulates, becomes unclear, and persists long past its useful life. Governance is the set of controls that prevents this.

## 📋 What Identity Governance Is

Identity governance is the discipline of ensuring that the right people have the right access to the right resources, for the right reasons, for the right amount of time. It's not a product. It's an outcome, supported by tools, processes, and policies working together.

Microsoft Entra ID Governance is the product family that provides the tooling for this outcome. It brings together:

- **Access Reviews**: Periodic verification that existing access is still appropriate
- **Entitlement Management**: Structured, auditable process for requesting and approving access
- **Lifecycle Workflows**: Automation for joiner, mover, and leaver events
- **Privileged Identity Management (PIM)**: Just-in-time activation for privileged roles
- **Access Certification**: Formal attestation of access appropriateness for compliance

Each piece addresses a different dimension of the governance challenge. Used together, they create a lifecycle for access: structured acquisition, active maintenance, periodic review, and systematic removal.

## 🔒 The Four Governance Questions

Good identity governance enables organizations to answer four questions at any point in time:

**Who has access to what?** 🔍
An organization should be able to produce, on demand, a list of who has access to any given resource. Without governance tooling, this often requires querying multiple systems, manually correlating data, and hoping nothing was missed.

**Why do they have it?** 📝
Access should be traceable to a business decision: a request was submitted, a justification was provided, an approver signed off. Without audit trails, access exists without documented reason.

**Is it still appropriate?** ✅
Access that was right 12 months ago may not be right now. Governance includes the recurring processes (access reviews, recertification) that verify continued appropriateness.

**How do we remove it?** 🗑️
When access is no longer appropriate, there should be a clear, automated, auditable way to remove it. Not "someone sends an email and hopes."

## 🏗️ Governance as a Maturity Journey

Most organizations don't implement full governance overnight. It's a maturity journey with distinct stages:

**Stage 1 - Visibility**: Know what access exists. Inventory groups, applications, role assignments, guest accounts. Before you can govern access, you have to see it.

**Stage 2 - Cleanup**: Remove obvious excess. Groups with no owner, memberships from departed employees, privileged role holders who haven't used their privileges in 6 months.

**Stage 3 - Process**: Establish structured request and approval workflows for new access. Stop granting access ad-hoc.

**Stage 4 - Review cycle**: Start periodic access reviews for sensitive resources. Build the evidence trail for compliance.

**Stage 5 - Automation**: Automate joiner/mover/leaver events through HR integration. Use lifecycle workflows to remove the manual dependency on IT for routine lifecycle changes.

Most organizations I've worked with are somewhere between Stage 1 and Stage 3. Moving from manual processes to structured governance takes 12 to 18 months for a mid-sized organization.

## ⚠️ Governance Without Enforcement

Governance tools without enforcement are reporting tools. An access review that surfaces inappropriate access but doesn't remove it when denied has no security value. Entitlement management that allows users to request access through the official channel but also lets managers add them to groups directly creates a governance bypass.

The enforcement piece matters as much as the tool. Conditional Access policies that require access package membership for sensitive apps close the bypass path. Removing self-service group join capabilities for sensitive groups ensures requests flow through the approval process.

## 💡 The Compliance Dividend

Governance investment pays a compliance dividend. SOX requires access reviews for financial systems. ISO 27001 requires access control management. SOC 2 requires access provisioning and deprovisioning evidence. The same tools that improve operational security also produce the audit evidence that external auditors need.

Organizations that implement governance to solve a compliance requirement often discover it improves operational security simultaneously. Organizations that implement it for security often discover the compliance documentation comes as a side effect.

---

💬 **Where would you place your organization on the governance maturity scale?** Most teams know they have a governance gap somewhere: too many permanent admin assignments, groups without owners, app accounts that outlast the Entra ID account. What's the gap you're most aware of?
<!-- nav -->

---

[← Just-in-Time Access: Admin Privileges Should Be Borrowed, Not Owned](glossary-6-13-just-in-time-access.md) | [Home](../README.md) | [Certification Campaign: Access Review at Scale, on a Schedule →](glossary-6-15-certification-campaign.md)
