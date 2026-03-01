# Access Control
*What It Actually Means When Everything Is Everywhere*

📚 **Part of Entra ID Glossary Series: Glossary#2.7 - Access Control**

---

I once inherited an environment where the IT manager's answer to every access request was "just add them to the All Staff group." SharePoint permissions, Teams channels, Azure resources, application access, all of it collapsed into one giant group that eventually contained every person who'd ever worked there, including contractors who left two years ago.

When I asked how people got *removed* from access when they left, there was a pause. Then: "HR sends us an email and we try to catch it."

Try.

That's an environment with no real access control. And it's more common than you'd think.

## 🔐 What Access Control Means in Entra ID

Access control is the system that answers one question across your entire organization: *who is allowed to do what, to which resources, under what conditions?*

That question sounds simple. In practice it has four dimensions, each handled differently in Entra ID:

**Who**, the identity. A user, a group, a service principal, a device. Covered by your directory objects.

**What**, the permission or role. What action is being authorized? Read? Write? Delete? Manage? Reset passwords? Deploy to production?

💬 **Which resource**, where. The specific SharePoint site, Azure subscription, application, API, or directory object being accessed.

**Under what conditions**, the context. Is the device compliant? Is the sign-in from a trusted location? What's the risk level? This is where Conditional Access enters the picture.

Access control in Entra ID isn't one switch. It's a stack of layers, each contributing to the final answer.

## 📋 The Four Layers That Work Together

**Layer 1, Directory roles** control who can administer Entra ID itself. Who can create users, manage groups, configure policies, read audit logs. These are the keys to the identity plane. Get this wrong and someone can modify any identity in your tenant.

**Layer 2, Azure RBAC** controls who can do what with Azure resources. Owner, Contributor, Reader, and 100+ specialized built-in roles, assignable at management group, subscription, resource group, or individual resource level. Separate from directory roles entirely, controlling the resource plane rather than the identity plane.

**Layer 3, Application roles and permissions** control what users and apps can do inside specific applications. An internal expense tool might have "Expense.Submitter" and "Expense.Approver" roles defined by the developer. Microsoft Graph has "Mail.Read," "User.ReadWrite.All," and hundreds of others. Access within the application is governed by what roles or permissions the identity has been granted.

**Layer 4, Conditional Access** controls whether access is *allowed at all* based on context. Even if a user has the right role in the right application, a Conditional Access policy can require MFA, require a compliant device, or block the request entirely if the sign-in is high-risk. This is the enforcement layer that wraps around everything else.

A complete access decision runs through all four layers. A user might have the right application role (layer 3), but if their device isn't compliant and a policy requires it (layer 4), they're blocked.

## 💡 Why Access Without Structure Becomes Unmanageable

The "All Staff group gets everything" model has a half-life. It works fine at 20 people. At 200, you start noticing that the wrong people see things they shouldn't. At 2,000, you have a compliance audit problem. At 20,000, you have a breach waiting to happen and nobody who can explain the current state of access.

Access control isn't about saying no to people. It's about being able to say *yes confidently*, knowing exactly who has access, why they have it, when it was granted, and whether it's still appropriate. That requires structure: defined roles, groups with clear ownership, policies with documented purposes, and a way to review and clean up over time.

The organizations I've seen handle this well have three things in common. First, they assign permissions to groups, never to individuals directly. Second, they use descriptive group names that make the purpose obvious, "APP-Salesforce-Users" instead of "Group7." Third, they run access reviews on a schedule rather than relying on humans to remember to remove access when circumstances change.

## 🔐 Access Control as a Foundation, Not an Afterthought

The mistake most organizations make is treating access control as something to fix *after* things go wrong. A compliance audit finds issues, or a departing employee retains access for months, and suddenly there's urgent remediation work.

Building access control structure from the start, even imperfectly, is dramatically cheaper than retrofitting it into an environment where permissions have accumulated organically for years.

Start with groups. Define what each group grants before you create it. Assign permissions to groups. Build from there. 🔒

---

🔗 **Related Terms:**
- Glossary#2.8 - Permission (the specific rights that access control grants or denies)
- Glossary#2.9 - Role (Identity Role) (the named collections of permissions used in RBAC)
- Glossary#7.8 - Conditional Access (the contextual enforcement layer of access control)

---

**Honestly:** When you look at your current environment's access control, do you know why every permission exists? Or are there things that have accumulated over time that nobody quite remembers the reason for? That gap between "what we have" and "what we intended" is where access reviews come in.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Directory Role](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-6-directory-role.md) | [🏠 Contents](/README) | [Permission →](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-8-permission.md)
