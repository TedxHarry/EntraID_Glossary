# Subject (Deep Dive)
*The User Identifier in Tokens That Isn't What You'd Expect*

📚 **Part of Entra ID Glossary Series: Glossary#11.7 - Subject (Deep Dive)**

---

An application was using the `sub` claim from the access token as a stable user identifier to look up records in its database. It worked for a year. Then the application was reregistered in Entra ID with a new client ID for a security reason. Suddenly the `sub` values for every user changed. The user lookup logic broke for all 40,000 existing users.

The developer had used the wrong identifier. The `sub` claim in Entra ID tokens is application-specific by design. The same user gets a different `sub` value for every application. Reregistering the application is equivalent to creating a new application identity, which means new `sub` values.

Understanding what `sub` is, what it isn't, and which identifier to use for what purpose is one of the more subtle aspects of working with Entra ID tokens.

## 🔑 What the Subject Claim Is

In OAuth and OIDC, the subject (`sub`) claim identifies the resource owner: the user whose data is being accessed or whose identity is being asserted. It's the user as seen from the perspective of the authorization server.

In Entra ID, the `sub` claim is a pairwise pseudonymous identifier. It's derived from the combination of the user's identity and the application's identity. The same user authenticating to two different applications gets two different `sub` values. This is an intentional privacy design: different applications can't correlate a user's activity across applications using the `sub` claim alone.

For Microsoft's v2.0 token endpoint (which all modern Entra ID integrations use), the `sub` value is consistent for the same user and the same application over time. It's stable within the application context. It changes if the application registration changes.

## 🆔 Sub vs OID: The Right Identifier for Each Use Case

Entra ID tokens contain two user identifiers that serve different purposes:

**`sub` (Subject)** 🎯: Pairwise pseudonymous identifier. Consistent for a given user within a given application. Changes if the application changes. Use this when: you're storing user-specific data within your own application and you want the identifier to be application-scoped.

**`oid` (Object ID)** 🔵: The user's actual object ID in Entra ID. A GUID that's the same regardless of which application the user authenticates to. This is the directory object identifier for the user. Use this when: you need to identify the user across multiple applications, look up the user in the directory, or correlate the user across systems that share the same Entra ID tenant.

The `oid` is the cross-application stable identifier. The `sub` is the application-scoped stable identifier.

For the database key scenario in the opening example: the correct identifier to use as a persistent user key that survives application changes is `oid`, not `sub`. The `oid` is stable across application reregistrations because it's a property of the user in the directory, not a derived value that includes the application identity.

## 📋 Subject in ID Tokens vs Access Tokens

Both ID tokens and access tokens contain a `sub` claim, but their semantics are slightly different:

**ID token `sub`** 👤: The subject of the identity assertion. The user being authenticated. Pairwise, as described above. Stable for the same user and client application.

**Access token `sub`** 🔐: The subject of the authorization. Who is delegating access. For user-delegated flows (authorization code, OBO), this is the user. For client credentials flows (no user), the `sub` is the service principal (the application itself is both the actor and the subject).

When building resource APIs that validate access tokens, the `sub` claim identifies whose authorization the token represents. For client credentials tokens, the `sub` and `oid` both refer to the service principal's object ID, not any user.

## 🔒 Pairwise Identifiers and Privacy

The pairwise design of `sub` reflects OIDC's privacy model. If two relying parties share the same `sub` values for their users, those parties can cross-correlate user activity: they know that "user A on application 1" is the same as "user A on application 2." Pairwise subjects prevent this by giving each application a different identifier for the same user.

In enterprise Entra ID contexts, cross-application correlation is often explicitly needed and the `oid` serves this purpose. The pairwise `sub` is more relevant in consumer OIDC deployments where user privacy against application correlation is a design goal.

For Entra ID workforce tenants, always use `oid` for persistent user identification in application data stores. Use `sub` only for session-level user identification within a single application session, where the session doesn't need to survive application reregistration.

## ⚠️ Multi-Tenant Application Subject Values

For multi-tenant applications (where users from any Entra ID tenant can sign in), the same user will have the same `oid` and the same `sub` regardless of which of their organization's tenants they're in. But users from different tenants can share the same `sub` value (an unlikely collision in practice, but possible in theory). For multi-tenant apps, the stable cross-tenant user key is the combination of `oid` and `tid` (tenant ID), not `sub` or `oid` alone.

---

💬 **Has your application ever stored `sub` as a user identifier and then had to migrate to `oid` after a reregistration or multi-tenant expansion?** This data migration is painful. The right architecture decision is to use `oid` + `tid` from the start for persistent user keys in application databases. What identifier does your application currently use for user records?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Actor (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-6-actor-deep-dive.md) | [🏠 Contents](/README) | [Bearer Token (Deep Dive) →](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-8-bearer-token-deep-dive.md)
