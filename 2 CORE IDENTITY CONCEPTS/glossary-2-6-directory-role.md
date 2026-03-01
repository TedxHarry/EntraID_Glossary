# Directory Roles: Why "Just Give Them Global Admin" Is the Worst Habit in Entra ID

**Part of Entra ID Glossary Series: Glossary#2.6 - Directory Role**

---

The first security audit I ran on an inherited Entra ID tenant turned up 23 Global Administrators.

Twenty-three. For a 300-person company. I opened the role assignments, stared at the screen for a moment, and then started scrolling. Former employees. Shared mailboxes. A service account that someone had apparently given Global Admin "just to test something" three years ago and never removed. Three people in accounts payable. The IT manager, the IT manager's backup, and the IT manager's backup's backup.

Nobody knew it had gotten this bad. Nobody had looked.

That audit is what taught me to actually understand directory roles — not just what they are, but why the difference between them matters enormously for security.

## What a Directory Role Is

A directory role in Entra ID is a collection of permissions that grants administrative capabilities over the Entra ID tenant and related Microsoft services. Assign a directory role to someone, and they can perform specific administrative actions — create users, reset passwords, manage Conditional Access policies, assign licenses, read security alerts, whatever the specific role allows.

Entra ID has over 100 built-in directory roles. Each one is scoped to a particular set of tasks. A **Helpdesk Administrator** can reset passwords and manage authentication methods for non-admin users. A **User Administrator** can create and manage users, reset passwords, and manage groups. A **Conditional Access Administrator** can read and write Conditional Access policies but has no user management powers.

These are distinct jobs. They map to distinct roles because not everyone who needs to do one of them should be able to do all of them.

## Directory Roles Are Not Azure RBAC Roles

This distinction trips up a lot of beginners, so let's settle it.

**Directory roles** control *who can administer Entra ID itself* — the identity plane. Creating users, managing groups, configuring security policies, assigning licenses, reading audit logs. These are actions in and on the directory.

**Azure RBAC roles** control *who can do what with Azure resources* — the resource plane. Creating storage accounts, managing virtual machines, deploying to App Service. These live in Azure subscriptions and resource groups.

A user can be a Global Administrator in Entra ID with zero access to any Azure subscription. A user can be Owner of an Azure subscription with no directory role at all. The two systems are separate. Confusing them leads to over-permissioning people in one plane thinking it'll fix a problem in the other.

## Scope: Tenant-Wide vs. Administrative Units

By default, directory role assignments are tenant-wide. A User Administrator can manage *all* users in the organization. For a 50-person company, that's fine. For a 50,000-person global enterprise with regional IT teams, it's a problem — you don't want the IT helpdesk in Germany resetting passwords for executives in Tokyo.

Administrative Units (AUs) fix this. An AU is a container that holds a subset of users, groups, or devices. You can assign a directory role *scoped to an AU*, which limits the role's reach to only the objects inside that container.

The EMEA helpdesk gets the Helpdesk Administrator role scoped to the EMEA Administrative Unit. They can reset passwords for EMEA users and nobody else. Same role, narrower blast radius.

This is how you give regional teams the access they need without turning them all into tenant-wide administrators.

## The Three Roles You'll See Misused Most

**Global Administrator** — full control over everything. The most dangerous role in the tenant. Microsoft recommends fewer than 5 Global Admins. In practice I see 20, 30, sometimes more. Every extra Global Admin is a potential breach vector with unlimited blast radius.

**Privileged Role Administrator** — can assign and modify directory roles. Whoever holds this role can elevate anyone, including themselves, to any role including Global Admin. Treat this with almost the same care as Global Admin itself.

**Application Administrator** — can create and manage app registrations and enterprise applications, including granting admin consent to API permissions. Often assigned when someone just needs to "manage apps," without realizing it includes granting permissions that could expose tenant data.

## The Right Approach

Before assigning any directory role, two questions:

1. What specific task does this person actually need to do?
2. Is there a built-in role that covers exactly that, and only that?

If the answer to question 2 is yes — and it usually is — assign that role. If no built-in role fits cleanly, custom roles (available with Entra ID P1) let you define exactly what permissions are needed.

Global Admin should be a last resort for break-glass scenarios and a small number of top-level administrators, protected by Privileged Identity Management and phishing-resistant MFA. Not a default answer to "how do I give this person admin access." 🔐

---

**Related Terms:**
- Glossary#2.11 - Admin Role (the most privileged directory roles and how to manage them safely)
- Glossary#2.10 - Delegation (how to scope admin capabilities to specific subsets of users)
- Glossary#2.9 - Role (Identity Role) (roles across Entra ID, Azure, and applications — they're different)

---

**Question for you:** When you inherited or audited an Entra ID tenant, what did the role assignments look like? Were there surprises? I've yet to run an audit where everything was clean on the first pass.

#EntraID #DirectoryRoles #CloudSecurity #IdentityManagement #MicrosoftEntra #LeastPrivilege #ITAdmin
<!-- nav -->

---

[← Enterprise Applications: What the Portal Is Actually Showing You](glossary-2-5-enterprise-application.md) | [Home](../README.md) | [Access Control: What It Actually Means When Everything Is Everywhere →](glossary-2-7-access-control.md)
