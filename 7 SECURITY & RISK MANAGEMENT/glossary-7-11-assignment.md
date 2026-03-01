# Assignment
*Who and What Your Conditional Access Policy Actually Covers*

📚 **Part of Entra ID Glossary Series: Glossary#7.11 - Assignment**

---

A team deployed a Conditional Access policy requiring MFA. They targeted "All users." They tested it, confirmed MFA was required, and marked the task complete.

Three months later, during an incident investigation, they discovered that service accounts used for application-to-application authentication had been silently excluded from the policy because they kept failing MFA. The exclusions had been added as a quick fix during initial testing and never reviewed. The service accounts had full access to Exchange Online, SharePoint, and Teams with no MFA requirement.

The policy said "All users." The assignment effectively meant "all users except the ones we excluded." The excluded accounts were the ones most likely to be targeted for privilege escalation.

Assignments are the most important part of a Conditional Access policy. Get them wrong and nothing else matters.

## 👥 What Assignments Define

The assignment section of a Conditional Access policy defines two things:

**Who the policy covers** 👤: Which identities are in scope.

**What the policy covers** 📱: Which applications or resources the policy applies to.

A policy only fires when both sides of the assignment match. A user in scope trying to access an app in scope: the policy evaluates. A user in scope trying to access an app not in scope: the policy doesn't fire.

## 👤 User and Group Assignments

The user assignment includes and excludes users from policy scope:

**Include** ✅:
- **All users**: Every identity in the tenant, including guests
- **All guest and external users**: Only external identities
- **Directory roles**: All users holding a specific Entra ID role (Global Administrator, User Administrator, etc.)
- **Users and groups**: Specific named users or specific security groups

**Exclude** 🚫:
- Same options as include: specific users, groups, or directory roles

**Workload identities** 🤖: Service principals and managed identities. These are configured separately within the assignment and require different policy structures because they don't authenticate with user MFA flows.

The include/exclude interaction determines the effective scope. Include "All users," exclude a specific group, and the policy covers all users who aren't in that group.

### The Exclusion List Problem

Exclusions feel like a solution. They're actually a risk accumulation mechanism.

Every exclusion is a gap in policy coverage. Exclusions are added when something breaks: a service account that can't do MFA, a device that fails compliance checks, a user who needs temporary access. They're added quickly and reviewed rarely.

Good practice: maintain exclusions in a dedicated Entra ID group with a documented owner and quarterly review. Every account in the exclusion group should have a documented reason and an expiry date. Exclusions without owners become permanent.

Emergency access accounts (break-glass) are the legitimate standing exclusion. Everything else should have an expiry or regular review.

## 📱 Cloud Apps and Actions

The app assignment defines what resources the policy covers:

**All cloud apps** 🌐: Every application registered in Entra ID that uses it for authentication. The broadest scope.

**Select apps** 🎯: Specific applications. Target individual apps when you need different controls for different resources. A policy requiring MFA for Microsoft 365 doesn't affect your internal HR application if that application is a separate app assignment.

**Exclude apps** 🚫: Remove specific apps from a broader scope. A policy targeting "All cloud apps" except Microsoft Intune enrollment is a common pattern to ensure device enrollment isn't blocked by device compliance requirements.

**User actions** ⚙️: Some policies target actions rather than apps. Registering security information. Registering devices. These are configuration actions, not application access, and need separate policy coverage.

## 🏗️ Assignment Design Patterns

**Risk-based coverage by sensitivity** 🔴: Apply stricter controls to high-value resources. Microsoft 365 with MFA and compliant device. Internal low-risk apps with MFA only. Public-facing read-only resources with no additional requirements beyond authentication.

**Role-based differentiation** 👑: Administrators get different policies than standard users. Directory role targeting lets you apply more stringent controls (MFA always, privileged access workstations only) to accounts with elevated permissions without disrupting all users.

**Guest and external identity separation** 🌍: External users often authenticate through their home tenant. Applying policies designed for internal users to guest accounts can generate unexpected behavior. Separate policies for "All guest and external users" with appropriate controls for external identity scenarios.

**Workload identity separation** 🤖: Service principals can't satisfy user MFA. Policies targeting workload identities use different grant controls: IP-based restrictions, named location requirements, or managed identity verification. Don't include service principals in user MFA policies and then add them as exclusions. Design separate policies for them.

## ⚠️ Assignment Testing Before Enforcement

The "What If" tool in the Conditional Access portal lets you test policy evaluation for a specific user, app, and condition combination. It shows which policies would fire, which would be skipped, and what the outcome would be.

Before pushing any new policy to enforcement, run What If for:
- Typical users in the target scope
- Users in exclusion groups (confirm they're excluded)
- Service accounts (confirm they're not inadvertently caught)
- Emergency access accounts (confirm they're excluded)

Report-Only mode provides the same validation at scale across real sign-ins rather than hypothetical scenarios.

---

💬 **What's the largest exclusion list you've inherited on a Conditional Access policy?** The "we'll clean it up later" exclusion group that never gets reviewed is a common pattern in tenants that have been running CA policies for a few years. How did you approach rationalizing it?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Zero Trust](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-10-zero-trust.md) | [🏠 Contents](/README) | [Condition →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-12-condition.md)
