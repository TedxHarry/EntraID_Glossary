# SAML in App Integration: The Enterprise Protocol That Refuses to Retire

**Part of Entra ID Glossary Series: Glossary#9.7 - SAML (App Integration Focus)**

---

The Salesforce integration request came in. Standard enterprise SaaS. The IT team knew it would be SAML before they opened the documentation. It's always SAML with Salesforce.

The SAML configuration exchange: download Entra ID's federation metadata XML, upload it to Salesforce. Download Salesforce's metadata or manually configure the ACS URL and Entity ID in Entra ID. Map the NameID format to the user's email address. Test with a user who has the Salesforce profile assigned.

Twenty minutes to configure. Another ten to test. SSO working.

Understanding SAML well enough to debug it when it breaks is what separates administrators who can do enterprise app integrations from those who need to escalate every time.

## 🏗️ SAML 2.0 in the Application Integration Context

SAML 2.0 (Security Assertion Markup Language) is the dominant federation protocol for enterprise SaaS applications. While OIDC has become the preferred protocol for new application development, the majority of enterprise SaaS applications in production today use SAML for SSO integration. It's not going away.

From an app integration perspective, SAML works through an exchange of XML documents signed with certificates. Entra ID (the Identity Provider, IdP) produces a SAML assertion vouching for the user's identity. The application (the Service Provider, SP) validates that assertion and grants access.

## 📋 The Four Configuration Elements

Every SAML integration requires configuring four things correctly. Get all four right and it works. Miss any one of them and it fails.

**Entity ID (Issuer)** 🏷️: The unique identifier for the Service Provider. Entra ID sends this value in the SAML assertion's audience field. The application checks that the assertion is meant for it by validating this value. It's a URI, not necessarily a real URL. Must match exactly what the application expects. Find it in the application's SAML documentation.

**Assertion Consumer Service (ACS) URL** 🔄: The application endpoint where Entra ID posts the SAML assertion after authentication. Entra ID redirects the user's browser to this URL with the assertion. Must be exactly correct. Common mistake: HTTP vs HTTPS, trailing slash vs no trailing slash, or production vs staging URL.

**NameID format** 👤: How the user's identity is expressed in the assertion. The application expects a specific format: email address, persistent identifier, transient identifier, or UPN. Mismatched NameID format is one of the most common SAML configuration errors.

**Signing certificate** 📜: Entra ID signs assertions with its token signing certificate. The application validates the signature using the public key from Entra ID's metadata. When Entra ID rotates its certificate, the application's stored certificate must be updated. Certificate mismatch after rotation causes authentication failures.

## 🔧 The Attribute Claim Mapping

Beyond the basic four, the application may require specific attributes in the assertion:

**What the application might expect**:
- `emailaddress`: User's email, often as the primary identifier
- `givenname`: First name
- `surname`: Last name
- `displayname`: Full display name
- Custom attributes: department, employee ID, cost center

**What Entra ID sends by default**: The standard SAML assertion includes a limited set of claims. Custom claims require configuration in the Enterprise Application's "Attributes & Claims" section.

The most common integration failure after getting the four main elements right: the application receives the assertion successfully but can't find the user because the attribute it uses as the unique identifier isn't being sent, or is being sent with the wrong attribute name.

Read the application's SAML requirements documentation carefully before configuring. Every application has specific expectations about attribute names and formats.

## 🔍 Debugging SAML: The Browser-Based Trace

SAML is XML exchanged through the user's browser. This means it's visible and debuggable using browser developer tools without any server-side access:

**SAML-tracer** (Firefox/Chrome extension): Captures and decodes SAML requests and responses as they flow through the browser. Shows the raw XML assertion, the claims, the NameID, the signing certificate chain.

**Browser developer tools network tab**: The SAML assertion is posted to the ACS URL as a form parameter. In the network tab, find the POST request to the ACS URL and look at the form data. The SAMLResponse parameter is base64-encoded XML.

**Common findings when debugging**:
- Assertion expired (clock skew between Entra ID and the application server)
- Wrong NameID format or value
- Missing required attribute
- ACS URL doesn't match what's configured in Entra ID
- Certificate mismatch (assertion signed with old certificate)

## ⚙️ IdP-Initiated vs SP-Initiated

**SP-initiated** (most common) 🔄: User goes to the application first. Application detects no session, redirects to Entra ID with a SAML AuthnRequest. Entra ID authenticates, posts assertion to ACS URL.

**IdP-initiated** 📲: User launches the application from the Entra ID My Apps portal. Entra ID generates an assertion without a preceding AuthnRequest and posts it directly to the application. Some applications don't support IdP-initiated SSO, and some that do have security implications with it (no request correlation).

For most enterprise applications, SP-initiated is the standard flow and what should be tested first.

## ⚠️ Certificate Rotation

Entra ID periodically rotates its token signing certificate. When rotation happens, the application must be updated with the new certificate. If the application has the old certificate stored and Entra ID is now signing with the new one, assertion validation fails.

Some applications support automatic metadata refresh (they fetch Entra ID's metadata URL periodically and pick up new certificates automatically). Applications that have the certificate hardcoded require manual update. Know which type your integrations are before a rotation event causes an outage.

---

💬 **What's the SAML configuration mistake you've made the most times?** The ACS URL with an HTTP vs HTTPS mismatch, the NameID format that works in the test tenant but not production, or the attribute claim that the application insists is required but isn't documented anywhere. What's the error you can diagnose fastest because you've seen it before?

#EntraID #SAML #AppIntegration #SSO #MicrosoftEntra #EnterpriseApplications #IdentityFederation
<!-- nav -->

---

[← OIDC in App Integration: Building Modern Authentication the Right Way](glossary-9-6-oidc-app-integration.md) | [Home](../README.md) | [SCIM: The Standard That Automates User Provisioning Across Applications →](glossary-9-8-scim.md)
