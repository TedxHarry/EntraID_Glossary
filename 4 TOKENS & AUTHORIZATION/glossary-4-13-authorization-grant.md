# Authorization Grant
*Four Ways to Get a Token (and When to Use Each)*

**Part of Entra ID Glossary Series: Glossary#4.13 - Authorization Grant**

---

A developer asked me which OAuth flow they should use for their new application. Before I could answer, I needed to ask three questions back at them: Does the application have a user signing in? Is it server-side or running in a browser? Does it need to act as itself, or on behalf of the user?

The answers determine the grant type. The grant type determines the security properties. Picking the wrong one isn't just a technical mistake; it has security consequences that persist as long as the application runs.

## 🗺️ What an Authorization Grant Is

An authorization grant is a credential representing the resource owner's permission for an application to access protected resources. Practically speaking, it's the mechanism the application uses to prove to Entra ID that it's entitled to receive tokens.

OAuth 2.0 defines multiple grant types, each designed for a different application scenario. Entra ID supports the current recommended ones and retains limited support for deprecated ones for backward compatibility.

## 🔑 The Four Grant Types

**Authorization Code Grant** is the one you reach for first when a user is involved. The user authenticates at the authorization endpoint, the app receives a short-lived, single-use code, and exchanges that code server-side for tokens. PKCE (Proof Key for Code Exchange) extends this flow to work securely for public clients like mobile apps and single-page applications where client secrets can't be kept confidential. Microsoft recommends Authorization Code with PKCE for all user-facing applications today.

The security property: tokens never appear in browser history or URL logs. The code exchange happens over a back-channel server-to-server request that the browser never sees.

**Client Credentials Grant** is for applications acting as themselves, with no user involved. A background service, a daemon, an automated pipeline: these authenticate using the application's own credentials (client secret or certificate) and receive a token in the application's name. No user context exists.

The security property: the application authenticates with Entra ID directly using a secret or certificate. No user interaction occurs and no user can be impersonated.

**Resource Owner Password Credentials (ROPC)** allows an application to collect the user's username and password directly and exchange them for tokens, skipping the redirect to the Entra ID sign-in page. Entra ID supports this but explicitly discourages it.

The security problem: the application sees the user's password in plaintext. MFA cannot work with this flow. All the phishing-resistant properties of the modern sign-in experience are bypassed. Microsoft marks this as a legacy flow and recommends against it for any new application.

**Implicit Grant** was designed for browser-based apps before PKCE existed, returning tokens directly in the URL fragment. Entra ID still supports it for backward compatibility but it's deprecated. The replacement is Authorization Code with PKCE, which achieves the same goal with substantially better security.

## 🏗️ How to Choose

A practical decision tree:

**Is a user signing in?**
- Yes, server-side web app: Authorization Code (with client secret or PKCE)
- Yes, SPA or mobile app: Authorization Code with PKCE
- No, background service or daemon: Client Credentials

**Is there legacy code using ROPC or Implicit?**
- Plan a migration to Authorization Code with PKCE

## 🔍 What the Token Represents

The client credentials vs authorization code distinction matters most when thinking about what the access token represents and who appears in audit logs.

Client credentials tokens represent the application. The `oid` in the token belongs to the service principal, not any human. Audit log entries show the application's identity.

Authorization code tokens represent the user (with the application acting on their behalf). The `oid` belongs to the user. The `appid` claim identifies which application was acting. Audit logs show who actually initiated the action.

I've reviewed applications using client credentials when they should have been using authorization code. The result: audit logs showed application identity where user identity was needed. Compliance reviewers couldn't determine which humans had performed which actions. The fix required rearchitecting the authentication model.

## ⚡ Why This Matters for Background Processing

The reverse also happens: applications using delegated (user) credentials for background jobs, which breaks when no user is signed in or when the token expires mid-job and no one is available to re-authenticate interactively. Background services that process data must use client credentials so they can authenticate independently.

The grant type determines what the token represents, who is accountable in audit logs, and what happens when tokens expire. Get it right from the start.

---

💬 **Have you inherited an application using the wrong OAuth grant type and had to migrate it?** ROPC to Authorization Code is particularly painful in older enterprise apps. What drove the decision to migrate and how did you handle the transition?
<!-- nav -->

---

[← Audience](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-12-audience.md) | [🏠 Contents](/README) | [Actor →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-14-actor.md)
