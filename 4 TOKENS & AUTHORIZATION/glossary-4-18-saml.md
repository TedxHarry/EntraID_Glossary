# SAML
*The Protocol That Refuses to Die (and Sometimes Shouldn't)*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #4.18 - SAML

---


I was brought in to help a company migrate their enterprise applications to Entra ID. Most of the modern SaaS apps integrated within a day or two using OIDC. Then we got to a 15-year-old on-premises HR system, still in active daily use by 400 employees. The vendor maintained it. SAML only. No OIDC support, no modern auth, no roadmap to add either.

We integrated it via SAML. It worked. It's still working.

SAML isn't the future, but declaring it dead would be premature.

## 📜 What SAML is

Security Assertion Markup Language (SAML) is an XML-based protocol for exchanging authentication and authorization data between an identity provider and a service provider. SAML 2.0, published in 2005, is the version you'll encounter in enterprise environments today.

Where OIDC uses JSON web tokens and REST APIs, SAML uses XML assertions and browser redirects. The core concept is identical: the identity provider vouches for the user's identity and the service provider grants access based on that voucher. The implementation is entirely different.

In the Entra ID context: Entra ID is the **Identity Provider (IdP)** and the application is the **Service Provider (SP)**.

## 🔄 How SAML works

**SP-initiated flow** (the most common pattern):

1. User tries to access the application
2. Application detects no session exists, redirects to Entra ID with a SAML authentication request
3. User authenticates at Entra ID (MFA enforced here, before the assertion is issued)
4. Entra ID issues a signed SAML assertion (an XML document) and POSTs it to the application
5. Application validates the signature and extracts identity claims
6. Application creates its own session for the user

**IdP-initiated flow**:

1. User clicks an app tile in the Entra ID My Apps portal
2. Entra ID issues a SAML assertion without a specific SP authentication request
3. Application receives and validates the assertion

## 📋 Inside a SAML assertion

The assertion is an XML document signed by Entra ID. It contains:

- **Name identifier**: How the application identifies this user. Could be email address, employee ID, or a generated persistent identifier depending on configuration.
- **Attributes**: Additional user properties like display name, department, group memberships, and any custom attributes your application needs.
- **Authentication context**: How the user authenticated (password, MFA, etc.).
- **Conditions**: Validity window and intended audience (the service provider's entity ID).
- **Digital signature**: Entra ID's signature over the assertion content.

Applications validate the signature using Entra ID's signing certificate, which is downloaded during initial SAML setup in the Entra admin portal.

## ⚠️ Where SAML integration goes wrong

**Entity ID mismatches**: Both the IdP and SP have entity IDs (essentially string identifiers). These must match exactly what's configured on both sides. A mismatch results in immediate rejection. Case sensitivity has caused multi-hour debugging sessions for teams who didn't realize `https://example.com/SAML` and `https://EXAMPLE.COM/SAML` are different values.

**Attribute mapping**: Applications expect specific attributes in the assertion (email, display name, group memberships, employee ID). If the attribute names or formats don't match what the app expects, features break silently. You need to know exactly what the vendor's application expects before configuring the claims.

**Certificate rotation**: Entra ID periodically rotates its SAML signing certificate. When this happens, applications must be updated with the new certificate, or all SAML logins for that application will fail with signature validation errors. This is a scheduled maintenance item that teams sometimes miss.

**Clock skew**: SAML assertions have validity windows. If the SP's clock differs significantly from the IdP's clock, assertions may arrive looking expired or not-yet-valid. A 5-minute window is standard, but this can still cause issues.

## 💡 SAML vs OIDC: when to use which

| Scenario | Choose |
|----------|--------|
| New application you're building | OIDC |
| Modern SaaS (Salesforce, ServiceNow current versions) | Often OIDC available, check first |
| Legacy SaaS with SAML-only configuration | SAML |
| On-premises app, vendor-maintained | Usually SAML |
| Mobile or single-page application | OIDC (SAML doesn't work here) |
| Vendor says "we support both" | OIDC |

For new integrations where you have a choice, OIDC. For existing applications that support only SAML, SAML. The protocol matters less than getting the integration working securely.

---

💬 **What's the SAML integration that took you the longest to get working?** Attribute mapping problems and entity ID mismatches are the usual culprits. There's something about debugging a SAML authentication failure from a wall of XML that concentrates the mind. What was the eventual fix?
✍️ TedxHarry

<!-- nav -->

---

[← OIDC (OpenID Connect)](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-17-oidc.md) | [🏠 Contents](/README) | [Token Security →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-19-token-security.md)
