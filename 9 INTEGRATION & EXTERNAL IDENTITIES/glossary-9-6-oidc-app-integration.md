# OIDC (App Integration Focus)
*Building Modern Authentication the Right Way*

📚 **Part of Entra ID Glossary Series: Glossary#9.6 - OIDC (App Integration Focus)**

---

A development team was building a new internal web application. Their first instinct was to add a login form: username, password, store it in their database. They'd done it before.

Their lead engineer stopped them. "We already have Entra ID. Everyone in the company has an account. Why are we building another login system?"

Three hours later, the application used OIDC to authenticate against Entra ID. Users signed in with their corporate credentials. The development team never wrote a single line of password storage, hashing, or reset logic. They got MFA for free from the existing Conditional Access policy. They got SSO with every other corporate application.

The login form they almost built would have added three months of development time for a system they would have had to maintain forever.

## 🔌 OIDC as the Modern Integration Protocol

OpenID Connect (OIDC) is the recommended protocol for integrating modern applications with Entra ID. It extends OAuth 2.0 by adding a standardized identity layer: not just "grant this app access to this resource" but "tell this app who just signed in and verify their identity."

From an application integration perspective, OIDC is the answer to: "How does my application know who the user is, and how does it verify that Entra ID confirmed their identity?"

The previous glossary entry on OAuth 2.0 covered the authorization framework. OIDC sits on top of that framework and adds authentication: specifically, the ID token, which is a signed assertion from Entra ID containing the user's verified identity claims.

## 🏗️ What the OIDC Integration Looks Like

When a user signs in to an OIDC-integrated application:

1. **Redirect to Entra ID** 🔀: Application sends the user to Entra ID's authorization endpoint with parameters including: client_id (the app's identifier), redirect_uri (where to send the response), scope (requesting `openid` plus any additional scopes), and response_type (typically `code` for the Authorization Code flow).

2. **User authenticates** 🔐: Entra ID presents the sign-in page. The user enters credentials, completes MFA if required by Conditional Access, and grants consent if required.

3. **Authorization code returned** 📬: Entra ID redirects back to the application's redirect_uri with an authorization code.

4. **Code exchange** 🔄: The application's backend sends the authorization code to Entra ID's token endpoint along with the client secret or certificate. Entra ID validates everything and returns an ID token, an access token, and optionally a refresh token.

5. **ID token validation** ✅: The application validates the ID token: checks the signature against Entra ID's public keys, verifies the audience (is this token meant for us?), verifies the issuer, and confirms the token hasn't expired.

6. **Session created** 🔐: The application extracts the user's identity claims from the validated ID token and creates a session.

## 🎫 The ID Token as Identity Proof

The ID token is the OIDC-specific element that distinguishes it from bare OAuth 2.0. It's a JSON Web Token (JWT) containing:

**Standard claims** 📋:
- `sub`: The user's unique, stable subject identifier in this application
- `iss`: The issuer (Entra ID's endpoint URL)
- `aud`: The audience (the application's client ID)
- `exp`: Expiration time
- `iat`: Issued at time
- `nonce`: Anti-replay value if provided in the request

**User identity claims** 👤:
- `name`: Display name
- `email` or `preferred_username`: Email address
- `oid`: Entra ID Object ID (the stable, unique identifier for the user)
- `tid`: Tenant ID

**Additional claims** (configured in the app registration or token configuration):
- `groups`: Group memberships
- `roles`: App roles assigned to the user
- Custom attribute claims

The application should use `oid` as the persistent unique identifier for the user, not `email` or `name`. Email addresses change. Names change. The Object ID never changes for the lifetime of the account.

## 🔧 App Registration Configuration

For OIDC integration, the App Registration in Entra ID needs:

**Redirect URIs** 🔄: The exact URL(s) where Entra ID will send the authorization code after authentication. Must match exactly. Supports multiple URIs for development/staging/production environments.

**Supported account types** 👥: Who can sign in. Single tenant (only your organization). Multi-tenant (any Microsoft organization). Multi-tenant plus personal Microsoft accounts.

**Authentication credentials** 🔑: Client secret or certificate for the backend code exchange. Client secrets expire and must be rotated. Certificates don't expire in the same way and are more secure.

**Token configuration** 🎫: Optional claims to include in the ID token or access token. Configure group claims, custom attributes, or additional standard claims your application needs.

## ⚙️ MSAL: Not Building OAuth/OIDC From Scratch

Microsoft Authentication Library (MSAL) handles the OIDC/OAuth 2.0 implementation details for common platforms (.NET, JavaScript, Python, Java, Go, etc.). It manages:

- Constructing authorization requests
- Handling redirects
- Token exchange
- Token validation
- Token caching and silent refresh
- Error handling

Applications built with MSAL don't implement the protocol directly. They call MSAL functions and receive validated, cached tokens. This prevents the common implementation errors (incorrect token validation, broken state parameters, insecure nonce handling) that make home-grown protocol implementations vulnerable.

---

💬 **Has your team integrated a custom application with Entra ID using OIDC?** The moment when the redirect-based sign-in flow clicks for a developer who's never seen it before is recognizable. What was the hardest part of the integration to get right: the redirect URIs, the token validation, or the group/role claims configuration?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← OAuth 2.0 (App Integration Focus)](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-5-oauth2-app-integration.md) | [🏠 Contents](/README) | [SAML (App Integration Focus) →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-7-saml-app-integration.md)
