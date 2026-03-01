# Custom Role: Administrative Permissions That Fit What Your Team Actually Needs

**Part of Entra ID Glossary Series: Glossary#13.12 - Custom Role**

---

A helpdesk team needed to reset passwords for users. The built-in Helpdesk Administrator role did that, but it also let helpdesk staff reset passwords for other administrators, which the CISO was uncomfortable with.

The built-in User Administrator role was too broad: it allowed creating users, deleting users, and managing group memberships, which the helpdesk didn't need.

Neither built-in role was the right fit. The team needed exactly: reset passwords for non-admin users, view user properties, and nothing else.

That's what custom roles are for.

## 🔧 What Custom Roles Are

Custom roles in Entra ID are administrator-defined role definitions that specify exactly which permissions the role includes, assembled from Entra ID's permission catalog. Unlike built-in roles (which Microsoft defines and can't be modified), custom roles are created and managed by the organization.

A custom role is a named collection of permissions. You give it a display name, a description, and select permissions from the available catalog. Then you assign that role to users or groups just like built-in roles, using PIM for time-limited assignment if needed.

Custom roles require Entra ID P1 or P2 licensing.

## 📋 The Permission Catalog

Entra ID exposes a large permission catalog for custom roles, covering operations across:

**User management** 👤: Individual permissions for reading, creating, updating, and deleting users. Separate permissions for resetting passwords, updating credentials, viewing basic vs sensitive properties.

**Group management** 👥: Read groups, create groups, manage group membership, manage group owners.

**Application management** 📱: Read app registrations, create app registrations, update app credentials, manage app permissions.

**Policy management** 🔐: Read Conditional Access policies, create and update policies (typically not appropriate for helpdesk roles).

**Device management** 💻: Read device properties, enable/disable devices, delete devices.

**Role management** 🔑: Read role assignments and definitions (read-only role management visibility, not role assignment authority).

The granularity is meaningful. "Update users" is not a single permission; there are separate permissions for updating basic properties vs updating sensitive properties vs updating credentials. This granularity is what makes least-privilege custom roles achievable.

## 🎯 Common Custom Role Scenarios

**Helpdesk password reset** 🔑: Permissions to read user properties and reset passwords for non-admin users. No user creation, no deletion, no group management. Scoped to non-admin users using assignable scope or admin unit scoping.

**Application registration manager** 📱: Permissions to read and create app registrations, manage app credentials, and update app properties. No user management, no group management. For developer teams who need to manage their applications without broader directory access.

**Guest user inviter** 🤝: Permission to invite guest users and manage invitations. No ability to create member accounts or manage existing member users.

**Access review administrator** 📋: Permissions to create and manage access reviews. No broader identity management permissions. For governance teams running access review programs without needing full Identity Governance administrator rights.

**Named location manager** 📍: Permission to create and manage named locations for Conditional Access. For network teams who need to maintain trusted IP ranges without access to modify Conditional Access policies themselves.

## 🔒 Scoping Custom Roles

Custom roles can be scoped at different levels:

**Tenant-wide** 🌐: The role applies across the entire directory. The default scope.

**Administrative unit scope** 🏢: The role applies only to objects within a specific administrative unit. A custom helpdesk role scoped to the "London Office" administrative unit lets the London helpdesk reset passwords only for London users.

**Application scope** 📱: For application management roles, the scope can be limited to specific app registrations. A development team's application manager role applies only to their apps, not every app in the directory.

Scoped custom roles are the combination that achieves genuine least privilege: the right permissions AND the right scope, not permissions for everything.

## ⚙️ Custom Roles in PIM

Custom roles integrate with Privileged Identity Management just like built-in roles. Instead of permanent assignment, custom roles can be:

**Eligible**: The user can activate the role when needed, with approval workflow and justification if configured.

**Time-limited active**: The role is active for a defined period, then automatically expires.

This makes PIM-governed custom roles the right pattern for even helpdesk capabilities that carry some risk: the permission is available when needed, with a justification requirement, and reverts automatically when the activation expires.

---

💬 **Does your organization use custom Entra ID roles to implement least-privilege administrative access, or are built-in roles covering most scenarios?** The gap between "we use Helpdesk Administrator because it's close enough" and "we have a custom role that includes exactly the permissions our helpdesk needs" matters for security posture. What's the administrative permission gap that most warrants a custom role in your environment?

#EntraID #CustomRole #LeastPrivilege #RoleBasedAccessControl #PIM #MicrosoftEntra #IdentityGovernance
<!-- nav -->

---

[← Sync Agent: The On-Premises Software That Bridges Your Directory to the Cloud](glossary-13-11-sync-agent.md) | [Home](../README.md) | [Administrative Unit: Scoped Administration Without Multiple Tenants →](glossary-13-13-admin-unit.md)
