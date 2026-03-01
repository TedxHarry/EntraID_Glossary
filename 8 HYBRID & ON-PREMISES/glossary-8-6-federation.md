# Federation
*When Entra ID Trusts Another Identity Provider for Authentication*

> **Difficulty:** 🔴 Advanced

📚 **Part of Entra ID Glossary Series: Glossary#8.6 - Federation**

---

## 🎯 TL;DR

- Federation (using AD FS or third-party IdP) delegates all authentication to the on-premises identity provider
- Entra ID redirects sign-in to the federated IdP, which issues a SAML/WS-Fed assertion
- Federation is the most complex option and creates a critical dependency on on-prem infrastructure


A university had authentication working exactly how they wanted for 15 years. On-premises Active Directory Federation Services (ADFS). Their own token signing certificates. Strict control over authentication policies, session lifetimes, and claim transformations. Thousands of configurations built around their specific requirements.

When they moved to Microsoft 365, their IT leadership's first instinct was: "Can we keep our authentication? We don't want to change it."

The answer was yes. Entra ID federation lets organizations keep their existing identity provider handling the actual authentication while Entra ID trusts the results. The Microsoft 365 move happened without touching the authentication infrastructure they'd spent a decade configuring.

## 🤝 What Federation Is

Federation is a trust relationship between Entra ID and an external identity provider (IdP) where Entra ID delegates authentication to the external IdP rather than validating credentials itself.

When a federated user signs in to a Microsoft 365 service:

1. Entra ID recognizes the user's domain as federated
2. Entra ID redirects the user to the configured IdP (typically ADFS)
3. The IdP handles the full authentication process (username, password, MFA, smart card, any configured policy)
4. The IdP issues a security token asserting the user's identity and claims
5. Entra ID receives the token, validates it against the trust configuration, and issues an Entra ID access token
6. The user accesses the Microsoft 365 service

The password never reaches Entra ID. The authentication decisions (what methods are required, session lifetime, step-up conditions) are made entirely by the IdP.

## 🏗️ Federation with ADFS

Active Directory Federation Services (ADFS) is Microsoft's on-premises identity provider, and historically the most common federation partner with Entra ID. ADFS gives organizations:

**Full authentication control** 🔐: Define authentication policies, required methods (smart card, RSA token, forms-based), and session policies entirely within on-premises infrastructure.

**Custom claim transformations** 🔧: Control what claims are included in tokens sent to Entra ID. Map on-premises attributes to specific claim types. Apply rules that add, remove, or transform claims based on group membership or other conditions.

**Compliance with specific regulations** ⚖️: Some regulatory frameworks require that all authentication decisions and credential validation happen within the organization's controlled infrastructure. ADFS satisfies this because authentication never leaves the on-premises environment.

**Integration with on-premises certificate infrastructure** 📜: Smart card authentication and certificate-based authentication are native capabilities.

## 🌐 Federation with Non-Microsoft Identity Providers

Entra ID can federate with any SAML 2.0 or WS-Federation compliant identity provider, not just ADFS. Common scenarios:

**Okta, Ping, or other enterprise IdPs**: Organizations using third-party identity providers as their primary IdP can configure Entra ID to trust that IdP for authentication.

**Inter-organizational B2B scenarios**: Two organizations with separate identity infrastructure can federate, allowing users from one organization to authenticate with their home IdP when accessing resources in the partner organization.

**Domain-specific federation**: Different domains within the same Entra ID tenant can be federated to different identity providers. contoso.com might use ADFS while subsidiary.contoso.com might be cloud-managed.

## ⚠️ The Operational Cost of Federation

Federation is powerful but operationally expensive:

**Infrastructure to maintain** 🔧: ADFS requires servers, load balancers, certificates with specific renewal schedules, WAP (Web Application Proxy) for external access, and regular patching. Each component is a potential point of failure.

**Certificate management** 📜: ADFS relies on token signing and decryption certificates. When these expire or need rotation, the federation trust must be updated in Entra ID. Missed certificate rotations have caused widespread authentication outages.

**Availability dependency** 💪: Just like PTA, federation means that if the IdP is unavailable, cloud authentication fails. ADFS unavailability means no one can sign in to Microsoft 365.

**Complexity without corresponding benefit for most organizations**: The controls that made ADFS essential ten years ago (advanced MFA, granular authentication policies) are now available natively in Entra ID Conditional Access. Many organizations that maintain ADFS do so for historical reasons rather than because they need capabilities that Entra ID lacks.

## 📉 The Migration Away from Federation

Microsoft's recommended direction for most organizations is to move away from federation to managed authentication (PHS or PTA). The reasons:

- Entra ID Conditional Access and ID Protection now provide sophisticated authentication policy controls natively
- PHS with leaked credentials detection provides security capabilities that aren't available with federation
- Eliminating ADFS removes the infrastructure and operational complexity
- Entra ID's resilience is typically better than maintaining separate on-premises federation infrastructure

The migration from ADFS to managed authentication is a defined process (staged rollout, domain conversion) with established tooling. Many organizations have completed this migration in the past five years.

---

💬 **Is your organization still running ADFS for Microsoft 365 authentication, or have you migrated to managed authentication?** The organizations that migrated often cite certificate rotation anxiety as the thing they're most glad to have eliminated. What's keeping ADFS in place for organizations that haven't made the move?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Pass-Through Auth](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-5-pass-through-auth.md) | [🏠 Contents](/README) | [Domain Services →](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-7-domain-services.md)
