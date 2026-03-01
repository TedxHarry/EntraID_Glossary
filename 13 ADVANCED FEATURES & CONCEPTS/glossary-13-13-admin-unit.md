# Administrative Unit: Scoped Administration Without Multiple Tenants

**Part of Entra ID Glossary Series: Glossary#13.13 - Admin Unit**

---

A university had 47 colleges within a single Entra ID tenant. Each college had its own IT support staff. The IT staff at the School of Medicine needed to manage users in their college: reset passwords, update attributes, manage group memberships. But they shouldn't be able to touch users in the School of Engineering.

The options without Administrative Units: give Medicine IT a User Administrator role scoped to the entire tenant (too much access), or create a separate tenant for each college (47 tenants to manage). Neither was acceptable.

Administrative Units made the correct option possible: scope the User Administrator role to the Medicine college's Admin Unit. Medicine IT can do everything they need for their users and only their users.

## 🏢 What Administrative Units Are

An Administrative Unit (AU) is a grouping mechanism in Entra ID that creates a scope boundary for administrative permissions. Users, groups, and devices can be members of an Administrative Unit. When you assign an Entra ID role to someone scoped to an AU, that role only applies to the objects within that AU.

The role assignment has two parts: the role (what permissions) and the scope (what objects those permissions apply to). Administrative Units provide the scope boundary.

An administrator assigned User Administrator scoped to the "London Office" AU can:
- Reset passwords for users in that AU
- Update user attributes for users in that AU
- Manage groups in that AU

But they can't touch users, groups, or devices that aren't in the AU. The role is the same; the scope limits where it applies.

## 🏗️ AU Membership Management

Objects are added to Administrative Units through several methods:

**Manual assignment** 📋: An administrator with AU management permissions adds specific users, groups, or devices to the AU. Works for stable, small populations.

**Dynamic membership** 🔄: Rules-based membership using user attributes. Users with `department = "London"` are automatically added to the London AU. As the HR system updates the department attribute, AU membership adjusts automatically. This is the scalable approach for large or frequently changing populations.

**Lifecycle Workflows** ⚙️: Workflows triggered by joiner/leaver events can add or remove users from AUs as part of the onboarding and offboarding process.

## 🔑 Roles That Support AU Scoping

Not every Entra ID role can be scoped to an Administrative Unit. The supported roles for AU-scoped assignment include:

**User management** 👤: User Administrator, Helpdesk Administrator, Authentication Administrator (for resetting MFA methods), Password Administrator.

**Group management** 👥: Groups Administrator.

**Device management** 💻: Intune Administrator, Cloud Device Administrator (limited to devices in the AU).

**License management** 📋: License Administrator scoped to users in the AU.

Roles that affect the entire directory (like Global Administrator or Conditional Access Administrator) can't be AU-scoped because their permissions inherently span the whole tenant.

## 📊 The Education and Distributed Enterprise Use Case

Administrative Units are most commonly deployed in two scenarios:

**Education** 🎓: Universities and school districts with autonomous colleges, schools, or districts that share a tenant but need independent IT administration. Each school gets an AU. Each school's IT staff gets helpdesk or user administrator roles scoped to their school's AU. The central IT team retains global administration. Student and faculty IT support is delegated without security boundaries breaking down.

**Global enterprises with regional IT** 🌐: Organizations with regional IT teams in different countries. The EMEA IT team gets User Administrator scoped to the EMEA AU. APAC IT manages their region. The corporate IT team handles global policy and privileged roles. Regional teams have operational autonomy without access to other regions' identities.

## ⚙️ Restricted Management Administrative Units

Standard Administrative Units create a scoped administration boundary. Restricted Management AUs go further: they prevent even Global Administrators from managing the objects in the AU without being explicitly added to the AU's management scope.

This is relevant for protecting specific high-sensitivity user populations: executive accounts, security team accounts, privileged administrators. Adding these accounts to a Restricted Management AU means that even a rogue Global Administrator can't easily modify or reset credentials for those accounts without detection.

Restricted Management AUs require explicit elevation to manage and log all administrative actions, adding an additional governance layer for the most sensitive identities.

## ⚠️ AU Limitations

Administrative Units scope role assignments but don't create full isolation. Objects in an AU are still visible to directory readers across the tenant. AU scoping is about administrative permissions, not data isolation. If data isolation between departments is a hard requirement, separate tenants remain the architectural answer.

---

💬 **Does your organization use Administrative Units for delegated administration, or do you manage all identity administration centrally?** The delegation model scales much better with AUs than with either global admin access or separate tenants. What organizational structure would benefit most from scoped administration in your environment?

#EntraID #AdminUnit #AdministrativeUnit #DelegatedAdministration #LeastPrivilege #MicrosoftEntra #IdentityGovernance
