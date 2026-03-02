# Approval Workflow
*Who Decides, in What Order, and What Happens If They Don't*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.11 - Approval Workflow

---

## 🎯 TL;DR

- Approval workflows route access requests through one or more approvers before granting access
- Approvers can be: specific users, group members, resource owners, or managers
- Time-limited approvals automatically expire access : reducing long-lived standing access


A sensitive access package had a two-stage approval: manager first, then the data owner. A manager approved in 2 hours. The data owner never responded. After 14 days, the request timed out and the user was denied access.

The user came back to IT frustrated. The data owner said they'd never received the email. IT investigated and found the data owner's inbox had a filter that was routing Entra ID notification emails to a "Notifications" folder they never checked.

The approval workflow had worked exactly as configured. The problem was a broken communication path to the approver. The workflow was correct. The delivery was not.

Approval workflows are both the logic of the access decision and the operational experience of the people making that decision.

## 🔗 What an approval workflow is

An approval workflow is the sequence of approvals required before an access request is fulfilled. It defines:

- **Who approves**: The specific people, roles, or automated conditions that must be satisfied
- **In what order**: Serial stages (one approver then another) or parallel (any one of several approvers)
- **What happens at each stage**: Approve, deny, request more information, or escalate
- **What happens if no one responds**: Timeout behavior after a configured window

In Microsoft Entra ID Governance access packages, approval workflows are configured as part of the access package policy. A request for that access package follows the defined workflow before access is granted.

## 📋 Approval stage options

**Single approver stage** 🔵: One person approves. Simple, fast, appropriate for lower-risk access.

**Multi-stage approval** 🔵🔵: Multiple sequential approvers. Stage 1 approves, then Stage 2 reviews, then access is granted. Used for sensitive access requiring multiple sign-offs. Common pattern: manager approval + resource owner approval.

**Any of multiple approvers** 🔵🔵🔵: Access is granted when any one of a group of designated approvers approves. Used when a team collectively owns a resource and any member of the team can approve. Reduces dependency on a single individual being available.

**Manager as approver**: Entra ID automatically routes to the requesting user's direct manager as identified in the manager attribute. No specific person needs to be named; the approval goes to whoever the user reports to.

**Self-approval with justification**: For lower-risk access, the policy can require a business justification without a human approver. The user provides the justification and access is granted automatically. Useful for resources that are broadly available but where an audit trail of stated justification is required.

## 📌 ⏱️ timeout and escalation

Every approval stage has a configured response window. If the approver doesn't respond within that window, one of three things happens depending on the policy:

- **Auto-approve**: Access is granted without an approval decision. Used only for the lowest-risk access where operational continuity matters more than the approval record.
- **Auto-deny**: Request is denied. User must resubmit. Most appropriate for sensitive access.
- **Escalate**: Request is forwarded to an alternate approver (manager's manager, resource owner, global approver). Reduces dependency on a single person being available.

The 14-day default timeout is often too long for time-sensitive requests. Organizations with operational access needs configure shorter windows (3-5 days) with escalation to ensure decisions happen on a business-relevant timeline.

## 🔧 Configuring approvers well

Common approval configuration mistakes:

**Named individual as sole approver** ⚠️: If the named person is on vacation or leaves the company, all requests pile up unanswered. Use a group of approvers (any can approve) or configure escalation to ensure coverage.

**Too many approval stages** ⚠️: Four or five sequential approvals for routine access creates friction that drives users to request less access than they need, find workarounds, or just give up. Reserve multi-stage for genuinely sensitive access.

**No alternative when approver is unavailable** ⚠️: Approvers get sick, take leave, and change roles. Access policies should always have a fallback approver path.

**Manager as approver when manager isn't meaningful** ⚠️: For external guest users or contractors, the "manager" attribute may not be populated or may not point to someone with relevant knowledge of the resource. Named approvers are better for guest access than dynamic manager routing.

## 💡 The audit value of approval workflows

Beyond the operational function, approval workflows create a documented record: who approved this access, when, with what justification. This is the evidence that access decisions were made deliberately, by appropriate people, with documented reasoning.

For compliance purposes, an audit trail showing "manager approved on March 15, data owner approved on March 16, access granted March 16" is the difference between demonstrable controlled access and access with no governance evidence.

---

💬 **Have you had an approval workflow fail operationally - an approver not reachable, a notification going to the wrong place, or a timeout expiring without anyone noticing?** The approval workflow design on paper and the approval workflow in practice often diverge significantly. What did you change to make it more reliable?
✍️ TedxHarry

<!-- nav -->

---

[← Access Request](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-10-access-request.md) | [🏠 Contents](/README) | [Auto-Provision →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-12-auto-provision.md)
