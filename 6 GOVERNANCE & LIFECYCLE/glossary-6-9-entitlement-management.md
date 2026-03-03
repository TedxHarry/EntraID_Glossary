# Entitlement Management
*Self-Service Access Without the Security Compromise*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #6.9 - Entitlement Management

---


A project manager needed access to three things for a new initiative: a SharePoint site, a Teams channel, and a Jira project. She opened three separate tickets. IT processed them over three separate days. She could start the project on day four.

The project should have started on day one. The bottleneck wasn't a security decision. It was a queue.

Entitlement Management is Microsoft Entra ID Governance's answer to this problem: users request the access they need, appropriate approvers decide, and IT processes nothing until it requires IT judgment.

## 📦 What entitlement management is

Entitlement Management is a self-service access request and lifecycle system. It allows organizations to:

- **Package** related access rights (groups, app roles, SharePoint sites, Teams) into a single requestable unit
- **Define policies** for who can request that unit, who approves, how long access lasts, and what happens when it expires
- **Let users request** access through the My Access portal without opening IT tickets
- **Automate approval routing** so the right people make the right decisions
- **Automatically expire** access when it's no longer needed
- **Trigger access reviews** for access granted through the system

The core objects are the **catalog** and the **access package**:

**Catalog** 🗂️: A collection of resources (groups, applications, SharePoint sites) that can be included in access packages. A catalog groups related resources under an owner responsible for managing them.

**Access package** 📋: A bundle of resources from a catalog, combined with a policy defining who can request it, who approves, and how long it lasts.

## 🔄 The request flow

A user who needs access navigates to `myaccess.microsoft.com`. They see access packages available to them based on their user attributes (department, job title, employment type). They select the package they need, provide a business justification, and submit the request.

The request triggers an approval workflow. The approver (manager, resource owner, or specific designated approver) receives an email notification with the request details and the justification. They approve or deny directly from the email or from the My Access portal.

If approved, access is granted automatically. All the group memberships and app role assignments in the package are added to the user's account. If the package has an expiration policy (access granted for 90 days, for example), Entra ID automatically removes the access at expiration and notifies the user.

## 📋 Access package policies

What makes access packages powerful is the policy configuration. A single access package can have multiple policies targeting different populations:

**Policy for internal employees**:
- Who can request: all employees in the "Engineering" department
- Approver: user's manager, then department head
- Access duration: 90 days, renewable
- Access review: every 90 days, reviewed by manager

**Policy for external guests**:
- Who can request: guests from specific partner organizations
- Approver: project sponsor (specific named approver)
- Access duration: 30 days, non-renewable
- Access review: none (expires and is removed automatically)

Same resources, different rules for different requestors. IT defines the policies once. The system enforces them consistently.

## ⚡ What changes for IT

The shift in workload is significant. Before Entitlement Management, every access request routes through IT as the processor: create the ticket, add the group memberships, close the ticket. IT is a mandatory step in every access decision, even ones that have nothing to do with IT judgment.

With Entitlement Management, IT defines the packages and policies. Then IT gets out of the way. The manager approves or denies their own team member's access request. The department head approves cross-team access. IT only gets involved when the request falls outside a defined package (which is when IT judgment actually adds value).

IT becomes an access governance team rather than an access processing queue.

## 💡 Starting with entitlement management

The most practical starting point is identifying three or four common access request scenarios that generate high ticket volume and package them:

- "I need access to the Finance team's SharePoint and distribution list" → Finance Team Member package
- "I need access for a 3-month contractor engagement" → Contractor Standard Access package
- "I need read access to the Security Operations resources" → Security Read-Only package

Package the common requests. Leave the edge cases as IT tickets for now. The reduction in routine ticket volume is often visible within the first month.

---

💬 **What's the most common access request your IT team processes manually that could be packaged into an entitlement management access package?** The first package you create doesn't have to be complex. Even packaging one common three-group request eliminates a significant volume of tickets over a year. What would yours be?
✍️ TedxHarry


> 🔑 **Licensing:** Entitlement Management requires **Entra ID P2** or **Entra ID Governance**. Access packages, approval workflows, and auto-expiry are all P2 features.

<!-- nav -->

---

[← Recertification](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-8-recertification.md) | [🏠 Contents](/README) | [Access Request →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-10-access-request.md)
