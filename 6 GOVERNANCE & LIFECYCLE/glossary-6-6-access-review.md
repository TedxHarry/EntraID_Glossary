# Access Review: The Audit That Finds What Accumulates Over Time

**Part of Entra ID Glossary Series: Glossary#6.6 - Access Review**

---

A finance director completed an access review of her team's SharePoint permissions. She'd expected it to take 20 minutes. It took 2 hours because she kept stopping to ask questions.

"Why does this person have edit access? They transferred to marketing 8 months ago."

"This person left. Why are they still showing up?"

"I don't recognize this account at all."

By the end, she'd denied access for 11 of the 34 people on the list. Nearly a third of the access being reviewed turned out to be inappropriate. None of it had been removed without the review prompting it.

That's what access reviews find: the access that accumulates over time and nobody removes because nobody has a reason to look.

## 🔍 What an Access Review Is

An access review is a periodic, structured process where designated reviewers evaluate whether users still need the access they have. Reviewers examine the list of who has access to a specific resource, group, or role, and they confirm or deny each access assignment as still appropriate.

In Microsoft Entra ID Governance, access reviews are configured as recurring campaigns:

- **What's being reviewed**: A group membership, an application role assignment, a privileged directory role, or an entitlement management access package
- **Who reviews it**: Resource owners, group owners, user's manager, or the users themselves (self-review)
- **How often**: Monthly, quarterly, semi-annually, or annually depending on sensitivity
- **What happens if the reviewer doesn't respond**: The review can auto-approve (status quo) or auto-deny (default to removing access)

## 🔄 How a Review Works in Practice

When a review period starts, Entra ID sends email notifications to reviewers. Reviewers open the My Access portal or the Entra admin center and see a list of access assignments to evaluate.

For each entry, the reviewer sees:
- Who has the access (name, email, department)
- What they have access to
- When they were last active in the system (sign-in date)
- How long they've had this access
- Their manager (useful context)

The reviewer clicks Approve (access stays) or Deny (access is removed). They can add a justification. They can also request information if they're unsure.

At the end of the review period, all denials are applied: access assignments are removed. Reviewers who didn't respond trigger the configured fallback behavior (auto-approve or auto-deny).

## 📋 What Access Reviews Commonly Find

**Role accumulation** 🔼: Employees who change roles accrue new access for each new position without losing old access. A 5-year employee who has changed teams three times may have access from all three teams still active.

**Orphaned access** 👻: Access that was correct when granted but whose owner has left, the project ended, or the business requirement changed. Nobody has a reason to revoke it, so it persists.

**Contractor and guest access** 👤: External users who completed their engagement but were never offboarded from specific resources. Their Entra ID account may be disabled, but group or app access lingers.

**Privileged role holders** 🔑: People in admin roles (User Administrator, Security Reader, etc.) who no longer need that privilege. Reviews of privileged roles often reveal role assignments from previous projects or from "I'll just give them admin access to unblock them" decisions that were never reversed.

## ⚠️ The Rubber Stamp Problem

Access reviews only work if reviewers actually review. The most common failure mode: a manager receives 80 access review emails, clicks "Approve All" without reading any of them, and the review completes with 100% approval.

Signs of rubber-stamp reviewing:
- 100% approval rate across all reviewers
- Review completed in under 2 minutes for 50+ entries
- No denials on any review, ever

Mitigations:
- Require justification for approvals of access the user hasn't used in 90 days
- Show last active date prominently to make stale access visible
- Start with smaller review scopes (20-30 entries) so reviewers aren't overwhelmed
- Train reviewers on what the review is for before sending the first campaign

## 💡 Automating the Consequence

Access reviews are most valuable when denials automatically trigger access removal. If reviewers deny access but someone has to manually remove group memberships afterward, the access review is disconnected from enforcement.

Entra ID access reviews can be configured to automatically apply review results: when the review period closes, all denials are immediately applied. Group memberships removed. App role assignments revoked. No manual follow-up required.

---

💬 **Has your organization run an access review and been surprised by how much access turned out to be inappropriate?** The first review of any group or application almost always surfaces more stale access than expected. What's the highest percentage of "should not have this" you've found in a single review?
<!-- nav -->

---

[← Lifecycle Management: Identity Automation for the Entire Employee Journey](glossary-6-5-lifecycle-management.md) | [Home](../README.md) | [Access Certification: When "Reviewed" Has to Mean Something to an Auditor →](glossary-6-7-access-certification.md)
