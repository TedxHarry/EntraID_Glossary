# Authorization Grant (Deep Dive)
*Matching the Right OAuth Flow to the Right Scenario*

📚 **Part of Entra ID Glossary Series: Glossary#11.5 - Authorization Grant (Deep Dive)**

---

A developer was asked to call the Microsoft Graph API from a background job. They found an example using the authorization code flow, built it, and hit a problem: the authorization code flow requires a user to authenticate interactively in a browser. A background job has no browser and no user.

Wrong grant type for the scenario. Every OAuth grant type exists for a specific context. Using the wrong one either doesn't work or creates security problems. The grant type is the first decision in any OAuth implementation.

## 🗂️ The Active Grant Types

**Authorization Code** 🔐: For applications where a user signs in interactively. A web application, a single-page application, a mobile app. The user's browser visits the authorization endpoint, the user authenticates, an authorization code is returned, and the application exchanges the code for tokens server-side (or via PKCE for public clients). The user's identity is in the token. All user-delegated scenarios use this flow.

**Client Credentials** 🤖: For service-to-service scenarios where there's no user. A background job, a data pipeline, an API calling another API with its own identity. The application authenticates directly with its client credentials (secret, certificate, or federated credential) and receives an access token representing the application itself, not any user. Use this flow for any automated, non-interactive workload.

**Device Code** 📺: For devices that can display text but can't run a browser or accept keyboard input efficiently. Smart TVs, IoT devices, CLI tools. The device displays a code and a URL. The user visits the URL on another device (phone or computer), enters the code, and authenticates. The device polls the token endpoint until the authentication is complete. Use this for input-constrained devices or CLI applications where browser sign-in isn't practical.

**Refresh Token** 🔁: Not a standalone flow, but a grant type used to obtain new access tokens silently using a refresh token obtained during a previous authorization code flow. The user authenticated once, got a refresh token, and subsequent token acquisitions use this grant type without any user interaction. The application presents the refresh token, Entra ID validates it, issues a new access token (and often a new refresh token). This continues until the refresh token expires, is revoked, or Conditional Access blocks it.

**On-Behalf-Of (OBO)** 🔗: For middle-tier APIs that receive a user's token and need to call downstream APIs as that user. The middle-tier service presents the incoming user token as an assertion and receives a new token for the downstream API, preserving the original user's identity and permissions. Used when an API calls another API and the downstream API needs to know who the original user was.

## ❌ The Deprecated Grant Types

**Implicit Grant** 🚫: Tokens were returned directly in the URL fragment from the authorization endpoint. No code exchange step. Tokens appeared in browser history, server logs, and referrer headers. Deprecated and disabled by default for new app registrations. If you see `response_type=token` or `response_type=id_token` in an authorization request, it's implicit flow, and it shouldn't be in new implementations.

**Resource Owner Password Credentials (ROPC)** 🚫: The application collects the user's username and password directly and posts them to the token endpoint. The user's credentials pass through the application rather than Entra ID handling them. No MFA support, no Conditional Access, breaks any identity federation. Still technically available for legacy migration scenarios but strongly discouraged. If Conditional Access requires MFA, ROPC fails.

## 🎯 Choosing the Right Grant Type

The decision tree is straightforward:

Is there a user interactively signing in? Authorization code flow (with PKCE if public client).

Is this automated with no user, running in Azure? Client credentials with managed identity (which uses client credentials under the hood via IMDS).

Is this automated with no user, running outside Azure? Client credentials with a certificate or federated identity credential.

Is the device input-constrained? Device code flow.

Does the API need to call another API as the original user? On-behalf-of flow.

Does the application have a token and need a new one silently? Refresh token grant.

The grant type determines the entire implementation path. Getting it right at the start avoids rework later.

## ⚠️ The Common Mismatch

The most frequent grant type mismatch in practice: using authorization code flow for service-to-service calls by embedding a service account's credentials and having that service account go through interactive sign-in on a schedule. This breaks when MFA is required for the service account, when the password changes, when Conditional Access updates, or when the service account's session expires in a way the automation doesn't handle.

The correct answer is client credentials. Service accounts are the wrong solution for service-to-service authentication; service principals and managed identities with client credentials are the right solution.

---

💬 **Which grant type do you see misused most often in your organization?** The service account doing interactive sign-in to simulate client credentials is common. So is ROPC for legacy migration that never got migrated. What grant type pattern in your environment would you most want to replace with something more appropriate?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Authorization Server (Deep Dive)](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-4-authorization-server-deep-dive.md) | [🏠 Contents](/README) | [Actor (Deep Dive) →](/11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-6-actor-deep-dive.md)
