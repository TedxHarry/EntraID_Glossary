# Permission
*Reading What You're Actually Granting*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #2.8 - Permission

---

## 🎯 TL;DR

- Permissions define what an app can do: delegated (on behalf of a user) or application (app acts as itself)
- Permissions must be both declared in App Registration AND granted via admin consent or user consent to take effect
- Scope strings like `User.Read` or `Mail.ReadWrite` are how permissions are expressed in OAuth2 tokens


A developer came to me once asking why their app wasn't working. They'd registered it in Entra ID, configured API permissions, even got admin consent granted. But the app kept getting 403 errors from Microsoft Graph.

I looked at their permission configuration. They'd requested `User.ReadWrite.All`. What their app actually needed was `User.Read`, the ability to read the profile of the signed-in user only.

Two things were wrong. First, they'd requested write access they didn't need. Second, they'd requested the `.All` variant, which means every user in the tenant, not just the person signing in. They'd been granted far more access than intended, and the app still wasn't working because they'd misconfigured *which* permission, not because they hadn't been granted enough.

Understanding how permissions work prevents both mistakes.

## 📌 What a permission is

in Entra ID, a permission is an explicit right to take a specific action on a specific type of resource. Permissions are defined by APIs, Microsoft Graph defines hundreds of them, and custom APIs can define their own.

Permission names follow a pattern: `Resource.Action` or `Resource.Action.Scope`.

- `User.Read`, read the profile of the signed-in user
- `User.ReadWrite`, read and write the profile of the signed-in user
- `User.Read.All`, read the profiles of all users in the tenant
- `User.ReadWrite.All`, read and write the profiles of all users in the tenant
- `Mail.Read`, read the signed-in user's email
- `Mail.ReadBasic.All`, read basic mail properties for all users

The `.All` suffix is significant. It means the permission applies tenant-wide, not just to the signed-in user's own data. `.All` permissions almost always require admin consent because no individual user can grant another app access to the entire tenant's data on their own.

## 📌 Delegated vs. application: the core distinction

Every permission in Entra ID falls into one of two categories. This distinction matters more than any other aspect of permissions.

**Delegated permissions** mean the app acts on behalf of a signed-in user. The app can do what the permission grants, but only for *that specific user*, and never more than that user can do themselves. If a user doesn't have access to a particular mailbox, an app with `Mail.Read` delegated permission can't access that mailbox either, even if the permission is granted.

This is important: delegated permissions are bounded by the user's own access. The app borrows the user's identity for that specific action.

**Application permissions** mean the app acts as itself, with no signed-in user involved. An app with `Mail.Read` application permission can read any mailbox in the tenant. There's no user context bounding what it can see. These permissions are designed for background services, daemons, and automation, jobs that run without a human present.

Application permissions are inherently higher privilege and always require admin consent. They shouldn't be used when a delegated permission will do the job, because delegated permissions carry a natural safety constraint the application permission doesn't have.

## 📌 Consent: who has to approve what

Not all permissions need the same level of approval to use.

Low-privilege delegated permissions, `User.Read`, `offline_access`, `openid`, can be consented to by the user themselves during sign-in. They'll see a prompt asking "Do you allow this app to access your profile?" and can click yes.

Higher-privilege delegated permissions, anything reading other users' data, accessing groups, writing to the directory, require an admin to approve. The user can't grant those on their own.

All application permissions require admin consent because they're tenant-wide by nature. There's no user to consent on behalf of "all users."

When admin consent is granted for an app, it's recorded on the service principal in your tenant and users won't be prompted individually. When it's not granted, users either get prompted (if the permission allows user consent) or the app fails with a consent required error.

## 📌 The least privilege rule for permissions

Request only what the app genuinely needs to function. This sounds obvious, but it's routinely violated, often because requesting broader permissions is easier than figuring out the precise minimum.

The cost of over-permissioning: if the app is compromised, the attacker inherits everything the app was granted. An app with `User.ReadWrite.All` application permission that gets compromised gives an attacker write access to every user account in the tenant. That's a very large blast radius for a permission that perhaps only needed to be `User.Read` delegated.

Before requesting any permission, ask: does this need to act on behalf of a user (delegated) or independently (application)? Does it need to read or write? Does it need access to one user's data or the entire tenant's? Those three questions will get you to the minimum necessary permission almost every time. 🔑

---


### 🔧 Quick reference: PowerShell

```powershell
# List OAuth2 permission grants (delegated permissions consented by users)
Get-MgOauth2PermissionGrant -All | Select-Object ClientId, Scope, ConsentType

# List app role assignments (application permissions)
Get-MgServicePrincipalAppRoleAssignment -ServicePrincipalId "<sp-object-id>"
```

🔗 **Related Terms:**
- [Glossary#2.7 - Access Control](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-7-access-control.md) (the broader system permissions operate within)
- [Glossary#2.3 - Service Principal](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-3-service-principal.md) (where permission grants are recorded in your tenant)
- [Glossary#4.11 - Scope](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-11-scope.md) (how permissions are expressed in OAuth2 token requests)
---

**Developer question:** What's the most over-privileged permission you've seen granted to an application, either something you inherited or something you caught before it went to production? The `Directory.ReadWrite.All` in a basic sign-in app is a classic.
✍️ TedxHarry

<!-- nav -->

---

[← Access Control](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-7-access-control.md) | [🏠 Contents](/README) | [Role (Identity Role) →](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-9-role-identity-role.md)
