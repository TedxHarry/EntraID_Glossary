# Scope (Deep Dive)
*Defining and Validating What Applications Are Allowed to Do With Your API*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #11.12 - Scope (Deep Dive)

---


An API was built with a single scope: `api://my-api/access`. Every application that needed to call the API got this scope. Three months later, the security team asked: "Can you show us which applications can only read data versus which ones can modify it?"

They couldn't. One scope for everything meant no granularity. Every application had every capability. The API had to be retrofitted with fine-grained scopes, all existing app permissions had to be reviewed and re-consented, and the API code needed updating to check which scope was present before allowing write operations.

Scope design is an architectural decision. Getting it right at the start avoids expensive retrofits.

## 📋 What scopes are in Entra ID

Scopes are named permission strings defined in an API's app registration. They represent specific capabilities the API exposes that client applications can request and users or admins can consent to.

When a client application requests a scope (like `api://my-api/data.read`), Entra ID asks the user to consent to that specific permission being granted to that application. If consent is granted, the resulting access token contains the `scp` claim listing the consented scopes. The API checks this claim to determine what the caller is allowed to do.

## 🔧 Defining scopes in the app registration

Scopes for a custom API are defined in the app registration under "Expose an API." Each scope has:

**Scope name** 📝: The permission identifier appended to the Application ID URI. Convention is `resource.action` or `resource.action.qualifier`. Examples: `data.read`, `orders.write`, `reports.read.all`. The naming convention matters for clarity and consistency.

**Admin consent display name and description** 📋: What admins see when reviewing consent for this scope. Clear, honest descriptions of what the scope allows. Don't minimize what the scope permits.

**User consent display name and description** 👤: What end users see in the consent dialog. Simpler language than the admin description, but equally honest.

**State** 🔵: Enabled or disabled. Disabled scopes prevent new consent without removing existing consented permissions.

**Who can consent** 🔑: Admins only, or admins and users. Scopes with access to sensitive data should be admin-only. Scopes for basic user data can be user-consentable.

## 📊 Delegated vs application permissions

There are two permission types for API access, and they appear differently in tokens:

**Delegated permissions (scopes)** 👤: Requested by confidential or public clients when a user is signed in. The token represents the user's delegated authority. The `scp` claim in the access token lists the delegated scopes. The effective permissions are the intersection of what the user can do and what the scope allows.

**Application permissions (app roles)** 🤖: Requested by clients acting without a user (client credentials flow). No user consent; admin consent required. The `roles` claim in the access token lists the granted application permissions. The application acts with its own authority, not delegated from a user.

An API that needs to support both human users and automated services needs both permission types defined.

## 🔑 Validating scopes in the API

Defining scopes is half the work. The API must actually validate them:

For delegated permissions, check the `scp` claim:
```csharp
// In ASP.NET Core with Microsoft.Identity.Web
[RequiredScope("data.read")]
public IActionResult GetData() { ... }
```

For application permissions, check the `roles` claim:
```csharp
if (!User.IsInRole("Data.Read.All"))
    return Forbid();
```

An API that validates the audience and signature but doesn't check scopes or roles accepts any token issued for it, regardless of which permissions were consented. The token validation proves the caller authenticated; the scope validation proves the caller has the specific permission needed for this operation.

## 🌐 The `.default` scope

When clients request the `.default` scope (e.g., `api://my-api/.default` or `https://graph.microsoft.com/.default`), Entra ID issues a token with all permissions that have been consented for the application for that API.

For client credentials flows, `.default` is required. The client credentials grant doesn't support requesting individual scopes; it requests all consented application permissions via `.default`.

For authorization code flows, requesting `.default` is convenient (gets all consented permissions at once) but less precise than requesting only the specific scopes needed for the current operation. Requesting minimal scopes is better practice for user consent transparency.

## ⚙️ Incremental consent

OAuth 2.0 with Entra ID supports incremental consent: requesting only the scopes needed for the current operation, and requesting additional scopes later when those capabilities are needed.

A user might initially consent to `profile` and `email` during sign-up. When they later use a feature that needs calendar access, the application requests `Calendars.Read` at that point, and the user sees a focused consent dialog explaining what's being requested and why.

Incremental consent improves user experience (users consent to manageable, contextual requests rather than a large upfront permission list) and reduces scope sprawl (applications only hold permissions they've actually requested for a specific feature).

---

💬 **How granular is the scope design in your organization's internal APIs?** The gap between "one scope to rule them all" and "precise, minimal scopes for each operation" varies widely across teams. What drove the scope design decisions in the APIs your team owns, and what would you design differently now?
✍️ TedxHarry

<!-- nav -->

---

[← Audience (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-11-audience-deep-dive.md) | [🏠 Contents](/README) | [Audit Log →](/12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-1-audit-log.md)
