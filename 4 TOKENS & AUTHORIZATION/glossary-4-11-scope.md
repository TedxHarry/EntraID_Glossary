# Scope
*The Permission on the Label vs the Permission You Actually Need*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #4.11 - Scope

---


A developer asked me to approve an API permission request for their new HR integration. The app needed to read employee display names to populate a dropdown in a dashboard. They'd requested `User.ReadWrite.All`.

Full read and write access to every user in the directory. For a dropdown.

They didn't need write access to anything. They didn't need to read 99% of what that permission covers. They needed `User.Read.All`, and even that was broader than strictly necessary. The principle of least privilege had been abandoned at the very first step, before a single line of application code was written.

Scope is where least privilege either gets implemented or gets ignored.

## 🔍 What scope actually is

A scope is a string that represents a specific permission. When an application requests access to Microsoft Graph or any other API, it declares which scopes it needs. Entra ID validates the request, the user or admin consents to those specific scopes, and the resulting access token contains only what was granted.

The token's `scp` claim (for delegated permissions) lists every consented scope. The resource server reads this claim and decides whether the specific action is permitted. No scope in the claim, no access.

Scopes are defined by the resource being accessed. Microsoft Graph has hundreds of them. Your own custom APIs define their own. An application can only request scopes that the target resource has declared.

## 📋 How graph scopes are structured

Microsoft Graph scopes follow a naming pattern that tells you exactly what they cover:

**Resource.Action** or **Resource.Action.Scope**

- `Mail.Read` - Read the signed-in user's mail
- `Mail.ReadWrite` - Read and write the signed-in user's mail
- `User.Read` - Read the signed-in user's own profile
- `User.Read.All` - Read all users' profiles in the directory
- `User.ReadWrite.All` - Read and write all users' profiles
- `Directory.ReadWrite.All` - Read and write the entire directory

The `.All` suffix is a significant jump. It means the permission applies to all objects in the tenant, not just the current user's own data. An app requesting `Mail.Read.All` can read every mailbox, not just the signed-in user's. That's the difference between a personal key and a master key.

## 🔑 Delegated vs application scope

Scopes work differently depending on the permission type:

**Delegated scopes** (`scp` claim): The application acts on behalf of a signed-in user. The effective permissions are the intersection of what the user can do and what the app was granted. If a user can only read their own profile, giving the app `User.Read.All` doesn't let them read everyone else. The user's own access provides a natural ceiling.

**Application scopes** (`roles` claim): The application acts as itself, no user in context. If granted `Mail.Read.All` as an application permission, the app can read every mailbox because there's no user's access limiting it. Admin consent is always required for application permissions. This is why they get more scrutiny during security reviews: there's no natural ceiling.

## ⚠️ The scope creep problem

Every scope you request that you don't actually need is attack surface. If your application is compromised, the attacker inherits every permission the app had. An app with `Directory.ReadWrite.All` that gets compromised gives the attacker keys to your entire user directory.

I've audited enterprise applications that accumulated scopes over years of development. Features were added, scopes were requested to unblock developers, and nobody went back to remove the ones no longer needed. By the time I looked, one internal tool had `Directory.ReadWrite.All`, `Mail.ReadWrite.All`, `Files.ReadWrite.All`, and several others. Most had been requested "just in case" during initial development phases.

The cleanup took three months of careful testing to confirm what was actually in use. The risk had been sitting there the entire time.

## 💡 The right approach to scope selection

Before requesting any scope, answer these questions:

- ✅ What specific data does the application actually need to read?
- ✅ Does it need to write anything, or just read?
- ✅ Does it need access to all users' data, or just the signed-in user's own?
- ✅ Is there a narrower scope that covers the actual requirement?

For Microsoft Graph specifically, Graph Explorer shows you the minimum scopes each API endpoint requires. Start there. Test with the minimum. Only request broader scopes if you hit a genuine limitation in production.

For your own APIs, define scopes narrowly from the start. A scope of `orders.read` is better than `api.access`. When your API grows, you can add more specific scopes. Removing existing scopes later, after applications have been built around them, is much harder.

---

💬 **Have you audited the scopes your applications are using and found permissions that shouldn't be there?** Scope creep is one of the most common findings in identity security reviews: easy to accumulate over time, uncomfortable to clean up. What drove you to look, and what did you find?
✍️ TedxHarry

<!-- nav -->

---

[← Token Revocation](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-10-token-revocation.md) | [🏠 Contents](/README) | [Audience →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-12-audience.md)
