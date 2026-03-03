# Actor (Deep Dive)
*When an Application Acts as the Middle Layer Between User and API*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #11.6 - Actor (Deep Dive)

---


A three-tier application had a problem. The frontend called a middle-tier API. The middle-tier API called Microsoft Graph to read the user's calendar. But the Graph token the middle-tier received identified the middle-tier service itself, not the original user.

Calendar access that should have been user-specific was running under the service identity. The Calendar API returned everything the service had access to, not just what the user had access to. Audit logs showed the middle-tier service accessing calendars, not the individual users who initiated the requests.

The On-Behalf-Of flow and the actor claim exist to solve exactly this scenario.

## 🎭 What actor means in OAuth

In OAuth and token terminology, the actor is the application or service making requests. The subject is the user whose resources are being accessed.

In a simple two-party flow (user authenticates to an app, app calls an API), the subject and the actor are closely related: the user authenticated, the token represents the user's authorization, and the app is just carrying that authorization.

In a three-party flow (user authenticates to a frontend, frontend calls a middle-tier API, middle-tier API calls a downstream API), there are now two actors: the frontend application that the user delegated to, and the middle-tier service that received the delegation.

The `act` claim in a token captures this actor chain. When the middle-tier service uses the On-Behalf-Of flow to get a token for the downstream API, the resulting token carries both the user's identity (subject) and the middle-tier service's identity (actor). The downstream API can see not just who the user is, but which service is acting on their behalf.

## 🔄 The on-behalf-of flow in detail

The OBO flow is how actor chains are established in practice.

**Step 1**: User authenticates to the frontend, receives an access token for the middle-tier API. This token has the user as the subject and the frontend as the authorized party.

**Step 2**: The frontend calls the middle-tier API, passing the token in the Authorization header.

**Step 3**: The middle-tier API needs to call Microsoft Graph or another downstream API as the user, not as itself. It presents the incoming user token to Entra ID's token endpoint as an assertion, using the `urn:ietf:params:OAuth:grant-type:jwt-bearer` grant type with `requested_token_use=on_behalf_of`.

**Step 4**: Entra ID validates the incoming token, validates the middle-tier's client credentials, and issues a new access token for the downstream API. This new token has the original user as the subject. The `act` claim carries the middle-tier service's identity.

**Step 5**: The middle-tier calls the downstream API with the new token. The downstream API sees the original user as the subject and enforces user-level permissions.

## 🔑 Why actor matters for audit and authorization

The actor claim enables two important capabilities:

**Downstream authorization** 🔐: The downstream API can make authorization decisions based on both who the user is and which application is acting for them. An API that should only be called through a trusted front-end service can validate the actor claim to ensure the request came through the expected application chain, not directly from a client that shouldn't have access.

**Audit fidelity** 📋: Without actor tracking, audit logs show the downstream API being called by the middle-tier service. With the OBO flow and actor claims, audit logs can show: "this user's data was accessed, via this middle-tier service, originating from this user's session." The full chain is captured, not just the immediate caller.

For compliance scenarios where knowing the full request chain matters (financial services audit trails, healthcare data access logs, regulated data processing records), actor claims provide the traceability that direct service identity doesn't.

## ⚙️ Token claims in practice

A token issued via OBO might contain:

- `sub`: The user's subject claim (stable, application-specific user identifier)
- `oid`: The user's object ID in Entra ID
- `name`, `preferred_username`: User identity claims
- `azp`: The immediate client that requested the token (the middle-tier service)
- `act`: The actor, containing a `sub` claim identifying the middle-tier service

The downstream API sees all of these and can enforce policy based on the full context.

## ⚠️ The consent requirement

OBO flows require that both the original scope (the token presented to start OBO) and the downstream scope (the token requested for the downstream API) have been consented. If the user consented to the frontend's permissions but not to the downstream permissions the middle-tier needs, OBO fails with a consent error.

This is the most common OBO implementation failure: the downstream API permission wasn't included in the original consent or wasn't granted as an application permission by an admin.

---

💬 **Does your organization use On-Behalf-Of flows in any API-to-API call chains, and have you had to trace a request through a multi-tier actor chain in audit logs?** OBO is common in architectures where user context needs to propagate through API tiers, but the consent and permission setup can be tricky. What was the hardest OBO configuration challenge your team worked through?
✍️ TedxHarry

<!-- nav -->

---

[← Authorization Grant (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-5-authorization-grant-deep-dive.md) | [🏠 Contents](/README) | [Subject (Deep Dive) →](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-7-subject-deep-dive.md)
