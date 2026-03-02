# Subject
*Whose Data Is This, Really?*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #4.15 - Subject

---

## 🎯 TL;DR

- The subject (`sub` claim) identifies the user the token was issued for : unique per user per app
- Unlike the Object ID (`oid`), the `sub` is app-specific (pairwise) to prevent cross-app user tracking
- For user identity across apps, use `oid` + `tid`; for single-app identification, `sub` is appropriate


A developer came to me with a collision problem. Their multi-tenant application was occasionally mixing up user identities. Two different people were being treated as the same user in the application database. The app stored the `sub` claim as the primary key.

They weren't wrong to use `sub` for user identification in principle. But they were wrong about what `sub` actually means. The subject claim has a property that catches people out when they haven't read the specification carefully: it's not globally unique.

## 🆔 What subject means in OAuth tokens

The `sub` (subject) claim identifies the principal that is the subject of the JWT. In user-context tokens, that's the user whose resources are being accessed. In application-context tokens (client credentials flow), that's the application itself.

For user tokens in Entra ID, `sub` is a unique identifier for the user within a specific application. The key phrase: **within a specific application**.

Entra ID generates the `sub` claim as a pairwise pseudonymous identifier. The same user gets a different `sub` value in different applications. Two different users from two different tenants can end up with the same `sub` value for a given application.

That's exactly what was breaking the multi-tenant app. The `sub` uniqueness guarantee is per-user-per-application, not globally unique.

## 🔄 Subject vs object id: the right identifier

Entra ID provides a second identifier that doesn't have this limitation: `oid` (Object ID).

The `oid` claim is the user's Object ID in their home Entra ID tenant. It's a GUID that's globally unique and consistent across all applications in the same tenant. The same user gets the same `oid` regardless of which application the token is for.

| Claim | Unique Per | Suitable For |
|-------|-----------|--------------|
| `sub` | User + Application combination | Single-app user identification |
| `oid` | User within their home tenant | Cross-app, cross-service identification |
| `oid` + `tid` | User + Tenant pair | Multi-tenant application user identification |

**Use `oid` as your database key for users.** It's stable, consistent, and won't cause collisions across your platform. For multi-tenant applications, the fully unique identifier is `oid` combined with `tid` (tenant ID). The same GUID appearing from two different tenants represents two different people.

## 🔒 Why pairwise subject was designed this way

The pairwise `sub` design is an intentional privacy feature. Users should be able to use different applications without those applications being able to silently track them across services by comparing identifier values.

If `sub` were a single globally consistent value, any two applications sharing data could correlate users across services without the user's knowledge or consent. The pairwise design prevents this: each application sees a different `sub` for the same person.

This matters particularly in B2C and consumer-facing scenarios where users interact with many third-party applications. The spec requires this behavior, and Entra ID implements it correctly.

## 📋 Subject in application tokens

When an application uses client credentials (acting as itself, no user), the `sub` in the resulting token refers to the service principal, not a human user. The subject of the token is the application.

APIs that accept both user-context and application-context tokens need to handle this difference. For user tokens, `sub` and `oid` refer to a human. For application tokens, they refer to a service principal. The presence of a `scp` claim reliably indicates a user is in context; its absence (with a `roles` claim instead) indicates application-only context.

## 💡 Fixing the multi-tenant collision problem

The fix for the database collision issue was a migration: change the primary key from `sub` to `oid` + `tid` (stored as a composite key or a concatenated string). All existing user records needed their identifiers recalculated using the correct claims.

For new applications, the fix is simply: never use `sub` alone as a persistent user identifier. The Microsoft documentation is explicit about this. Use `oid` for single-tenant apps. Use `oid` + `tid` for multi-tenant apps.

The `sub` claim is still useful. It's the right identifier to use when you specifically want the pairwise, application-scoped semantics, for example when you want user identifiers that are deliberately not correlatable across services. But as a database primary key, `oid` is the right choice.

---

💬 **Have you run into identifier issues where users were being confused or collisions were occurring in your application database?** The sub vs oid confusion is one of the more common mistakes in OAuth application development. What was the symptom that made you realize something was wrong?
✍️ TedxHarry

<!-- nav -->

---

[← Actor](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-14-actor.md) | [🏠 Contents](/README) | [OAuth 2.0 →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-16-oauth2.md)
