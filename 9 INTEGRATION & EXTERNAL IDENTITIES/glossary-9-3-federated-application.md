# Federated Application
*When an App Trusts Entra ID to Prove Who You Are*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #9.3 - Federated Application

---

## 🎯 TL;DR

- Federated applications use SAML or WS-Federation and redirect authentication to Entra ID as the IdP
- Entra ID is the Identity Provider (IdP); the application is the Service Provider (SP)
- Federated SSO passes a signed SAML assertion to the app : no password exchange between user and app


An organization integrated their CRM system with Entra ID using SAML federation. The CRM had been running for eight years with its own internal user database: 6,000 user accounts, each with their own CRM-specific password that users had to manage separately.

After integration, users signed in to the CRM with their corporate credentials. The CRM stopped managing passwords entirely. Its user database shrank to containing only what was unique to CRM (roles, preferences), not what Entra ID now handled (identity, authentication).

The IT team deleted 6,000 CRM password records. 6,000 accounts that couldn't be leaked, couldn't go stale, couldn't lock out, and didn't need a separate password reset process.

That's what a federated application actually means for operations.

## 🤝 What a federated application is

A federated application is an application configured to delegate user authentication to an external identity provider, in this case Entra ID, using a federation protocol (SAML 2.0 or OpenID Connect). Instead of maintaining its own authentication system, the application trusts Entra ID to verify user identity and passes responsibility for the sign-in flow to Entra ID.

The application accepts a security token from Entra ID as proof of authentication. The token contains claims about the user (name, email, roles, attributes). The application uses those claims to identify the user, determine their access level, and establish their session.

"Federated" specifically means the application and Entra ID have established a trust relationship. The application trusts Entra ID's assertions. Entra ID knows what claims to issue for this application.

## 🔑 SAML 2.0 federation

SAML (Security Assertion Markup Language) 2.0 is the predominant federation protocol for enterprise SaaS applications. The integration flow:

**SP-initiated SSO** (most common) 🔄:
1. User navigates to the application (Service Provider)
2. Application detects no active session, redirects to Entra ID with a SAML AuthnRequest
3. Entra ID authenticates the user (sign-in prompt, MFA if required by Conditional Access)
4. Entra ID issues a SAML assertion containing user claims, signed with Entra ID's certificate
5. The assertion is posted back to the application's ACS (Assertion Consumer Service) URL
6. Application validates the assertion signature against Entra ID's certificate, extracts claims, creates a session

**IdP-initiated SSO** 📲:
1. User launches the application from My Apps portal in Entra ID
2. Entra ID directly issues a SAML assertion and posts it to the application
3. Application validates and creates a session

SAML configuration requires exchanging metadata between Entra ID and the application: Entra ID's signing certificate (so the application can validate assertions) and the application's ACS URL (where Entra ID sends assertions).

## 🔐 OIDC/OAuth 2.0 federation

Modern applications more commonly use OpenID Connect (OIDC) for federation, which is built on OAuth 2.0. The flow is token-based rather than XML-assertion-based:

1. User clicks "Sign in with Microsoft" (or equivalent)
2. Application redirects to Entra ID's authorization endpoint with application details
3. Entra ID authenticates the user
4. Entra ID redirects back to the application with an authorization code
5. Application exchanges the code for tokens (ID token, access token, refresh token) at Entra ID's token endpoint
6. Application validates the ID token, extracts claims, establishes session

OIDC is generally simpler to implement for new applications and is the recommended path for custom application development.

## 📋 Attribute claims and claim mapping

A federated application receives claims about the user from Entra ID. Claims are the information in the token: the user's name, email address, object ID, group memberships, roles, and any custom attributes the application needs.

**Claim configuration** ⚙️: In the Enterprise Application configuration for each federated app, you configure which claims are included in the token and how they're mapped. The application expects specific claim types with specific values. Mismatched claim configurations are the most common cause of SAML integration failures.

**Required claims vary by application** 📋: One application needs the user's email as the unique identifier. Another needs the employee ID. A third needs group membership claims to determine the user's role. Each application's claim requirements are documented in its SAML configuration guides.

**Custom attribute mapping** 🔧: Extension attributes, custom directory attributes, or transformed values can be included in claims. If the application needs a value that doesn't exist as a standard Entra ID attribute, extension attributes can hold it.

## ⚠️ What federation doesn't eliminate

Federation moves authentication to Entra ID. It doesn't eliminate all identity management in the application:

**Authorization** 🔑: What the user is allowed to do within the application is usually still managed in the application. Role assignments, permissions, feature access. Claims from Entra ID can seed this (passing a "Global Admin" claim that the application uses to grant admin access), but often some in-application configuration remains.

**Application-specific profile data** 👤: Display preferences, personalization, history. The application still manages data that's unique to the user's application experience.

**Provisioning the account** 📋: In some SAML integrations, the application creates a user profile on first successful SSO login (Just-In-Time provisioning). In others, the account must exist in the application before SSO will work. SCIM provisioning solves this by automatically creating accounts.

---

💬 **What SAML attribute mapping issue took the longest to debug in your environment?** The claim type mismatch where the application expects `http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress` but Entra ID is sending `email` is a classic one. What was the configuration issue that required reading the SAML trace to find?
✍️ TedxHarry

<!-- nav -->

---

[← Cloud Application](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-2-cloud-application.md) | [🏠 Contents](/README) | [Application Proxy →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-4-application-proxy.md)
