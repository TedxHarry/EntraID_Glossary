# Groups in Entra ID: The Access Management Tool You Should Be Using More

**Part of Entra ID Glossary Series: Glossary#2.4 - Group**

---

Early in my career I inherited an environment where permissions had been assigned directly to individual users for years. SharePoint sites, Teams channels, app roles, Azure resource access — all of it assigned user by user.

When I needed to remove access for all contractors, I ran a script to find every permission assignment across the tenant. It returned 4,700 individual entries to review. One by one.

That job took a week. It should have taken twenty minutes.

Groups exist to prevent exactly this kind of pain. If every contractor had been a member of a "Contractors" group, and every resource had been granted to that group, removing their access would've been: remove them from the group. Done.

If you're assigning permissions directly to users in Entra ID, stop. This article is for you.

## What a Group Is, Technically

A group in Entra ID is a directory object that holds references to other objects — users, devices, service principals, even other groups. When you assign a permission, a license, or an app role to a group, every member of that group gets that permission, license, or app role automatically.

Add someone to the group: they get access. Remove them: it's gone. The resources themselves never change.

Groups are the fundamental unit of access management at scale.

## Security Groups vs. Microsoft 365 Groups — Pick the Right One

Entra ID has two main group types and they're used for fundamentally different purposes.

**Security Groups** are for access control. Assigning Azure RBAC roles, Entra ID directory roles, app roles, SharePoint permissions, Conditional Access policies — anything where you need to control *who can do what*. Security groups are the workhorse. They have no collaboration features — no shared inbox, no Teams channel, no SharePoint site attached. Just a list of members and a way to assign permissions to that list.

**Microsoft 365 Groups** are collaboration objects. When you create a team in Microsoft Teams, a group site in SharePoint, or a shared mailbox, you're creating an M365 Group under the hood. They automatically come with a Teams channel, a SharePoint site, a shared mailbox, and a shared calendar. M365 Groups can also be used for access control, but their primary purpose is collaboration.

The mistake I see most: trying to use Microsoft 365 Groups as security groups for Azure RBAC or Conditional Access, and then hitting limitations or unexpected behavior. If your use case is "grant these people access to this resource," use a Security Group.

## Assigned vs. Dynamic Membership: This Changes Everything

Here's the decision that determines whether group management scales or becomes a maintenance burden.

**Assigned membership** means you manually add and remove members. You decide who's in, you decide who's out. This is fine for small, stable groups or groups with unusual membership criteria. But it requires ongoing attention — someone leaves the company, someone forgets to remove them, they retain access.

**Dynamic membership** means Entra ID automatically adds and removes members based on user or device attributes. You write a rule; Entra ID enforces it continuously.

Examples of dynamic membership rules:
- All users where `department` equals "Finance"
- All users where `jobTitle` contains "Manager"
- All users where `companyName` equals "Contoso" and `country` equals "UK"
- All devices where `deviceOSType` equals "Windows"

The power of dynamic groups is immediate: when someone joins the Finance team, their `department` attribute gets set, and Entra ID automatically adds them to the Finance group. Their SharePoint access, their app permissions, their license assignment — all handled without a single manual step. When they transfer out of Finance, they're automatically removed.

This is the right model for most large organizations. Dynamic groups turn access management from an ongoing task into a one-time configuration.

One important caveat: dynamic groups require Entra ID P1 licensing. And membership updates aren't instant — there's typically a delay of minutes to tens of minutes as Entra ID processes attribute changes and recalculates memberships.

## Nested Groups and the Gotcha

You can add groups as members of other groups. This is useful for building hierarchical access structures — a parent group that represents "All Sales" with child groups for "Sales EMEA," "Sales Americas," and "Sales APAC."

The gotcha: not every Entra ID feature honors nested group membership.

Azure RBAC does honor nesting — if you're in a nested group, you get the role. Microsoft 365 app roles often don't — only direct group membership counts. Conditional Access policies target direct membership by default. Entra ID directory role assignments don't support nesting.

Check the specific feature's documentation before relying on nesting. It works in some places and silently doesn't in others — and "silently doesn't" is the worst kind of failure.

## Role-Assignable Groups: A Critical Security Feature

One more thing worth knowing: if you need to assign an Entra ID directory role to a group (so all group members get that role), the group must be created as a **role-assignable group**. This is a specific property set at creation time that can't be changed later.

Role-assignable groups are deliberately restricted — they can only be managed by specific privileged roles, and they don't support dynamic membership. This is intentional: groups with directory roles assigned to them are high-value targets. Making them harder to accidentally misconfigure is a good thing. 🗂️

---

**Related Terms:**
- Glossary#2.2 - User (the primary member type in most groups)
- Glossary#2.8 - Permission (what groups are most commonly used to assign)
- Glossary#6.6 - Access Review (how you periodically verify group membership is still appropriate)

---

**Over to you:** Are you using dynamic groups in your environment? If you're still on assigned membership for most things, what's holding you back — licensing, complexity, or just hasn't been prioritized yet? I'd genuinely like to know what the common blockers look like in practice.
<!-- nav -->

---

[← Service Principal: The Most Misunderstood Object in Entra ID](glossary-2-3-service-principal.md) | [Home](../README.md) | [Enterprise Applications: What the Portal Is Actually Showing You →](glossary-2-5-enterprise-application.md)
