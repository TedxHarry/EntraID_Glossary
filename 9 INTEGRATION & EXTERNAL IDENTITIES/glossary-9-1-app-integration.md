# App Integration
*Connecting Applications to Entra ID for Authentication*

**Part of Entra ID Glossary Series: Glossary#9.1 - App Integration**

---

A company had 47 different applications across their environment. Each one had its own username and password. Users managed 47 separate sets of credentials. The helpdesk managed 47 separate password reset processes. Offboarding a departing employee required manually deprovisioning from 47 systems.

Over six months, they integrated 40 of those applications with Entra ID. Now users sign in to all 40 with their corporate credentials. MFA applies to all 40 through a single Conditional Access policy. Offboarding disables the Entra ID account and the user loses access to all 40 applications simultaneously.

The other 7 that couldn't be integrated are the ones that still generate most of the helpdesk tickets.

## 🔗 What App Integration Means

App integration is the process of connecting an application to Entra ID for authentication and, optionally, authorization and user provisioning. Instead of the application managing its own user database and authentication logic, it delegates identity to Entra ID.

A successfully integrated application:

- Uses Entra ID to authenticate users (sign in with Microsoft)
- Receives verified identity claims (who the user is, their attributes, their group memberships)
- Applies authorization decisions based on those claims
- Optionally receives users via automatic provisioning from Entra ID
- Is subject to Conditional Access policies for access control

From the user's perspective: one sign-in experience, one set of credentials, one MFA registration. From IT's perspective: one identity platform to manage, one offboarding process, one policy engine for access control.

## 🏗️ The Two Integration Models

**Gallery applications** 📚: Microsoft maintains an application gallery with pre-configured integration templates for thousands of popular SaaS applications (Salesforce, ServiceNow, GitHub, Slack, DocuSign, and thousands more). Gallery apps have pre-built SAML or OIDC configurations, attribute mappings, and often provisioning connectors. Integration setup is mostly configuration of provided templates rather than building from scratch.

**Custom applications** 🔧: Applications built in-house or by vendors without gallery templates. Custom integration using the Microsoft Identity Platform. The application is registered in Entra ID (creating an App Registration), and the application code uses Microsoft Authentication Library (MSAL) or OpenID Connect/OAuth 2.0 directly.

## 📋 The Integration Protocols

How an application integrates with Entra ID depends on the protocol it supports:

**Modern applications (OIDC/OAuth 2.0)** ✅: New applications, web apps, mobile apps, APIs. Register in Entra ID, implement OIDC or OAuth 2.0 authentication flow. The application redirects to Entra ID for authentication, receives tokens, and validates them. This is the recommended path for any new application development.

**Enterprise applications (SAML 2.0)** ⚙️: Common for older SaaS applications and enterprise software. The application and Entra ID exchange XML-based assertions for authentication. Most gallery applications use SAML. Doesn't require application code changes if the app already supports SAML.

**Legacy applications (Application Proxy)** 🔌: On-premises web applications that can't be modified to use modern auth or SAML. Application Proxy publishes them externally through Entra ID, adding authentication and SSO without touching application code.

**Password-based SSO** 🔑: Applications that have a username/password field but no SAML or OIDC support. Entra ID stores the credentials and auto-fills them when the user accesses the application. Not true federation, but provides SSO from the user's perspective.

## ⚙️ App Registration vs Enterprise Application

When integrating an application, Entra ID creates two related objects:

**App Registration** 📝: The application's configuration. Client ID, redirect URIs, permissions, secrets/certificates used for authentication. This is the identity of the application itself. For gallery apps, this is pre-configured. For custom apps, you create this in the App Registrations section.

**Enterprise Application (Service Principal)** 🏢: The local representation of the application in your tenant. This is where you configure user assignment (who can access the app), provisioning (auto-create users in the app), and single sign-on settings. Every integrated application has an Enterprise Application object in your tenant.

The relationship: App Registration defines what the app is. Enterprise Application defines how it behaves in your specific tenant.

## 🎯 What Integration Enables

**Single Sign-On** 🔐: Users sign in once to Entra ID and access all integrated applications without re-entering credentials.

**Conditional Access coverage** 🚦: Integrated applications are subject to Conditional Access policies. MFA requirements, device compliance, location restrictions all apply to application access.

**Automatic provisioning** 👤: For applications with SCIM support, Entra ID can automatically create, update, and disable user accounts in the application when users are added or removed.

**Centralized access governance** 📋: Access to integrated applications can be managed through Entitlement Management, Access Reviews, and role assignments from a central governance model.

---

💬 **What's the application in your environment that most needs Entra ID integration but hasn't been integrated yet?** The "we'll integrate it eventually" list exists in almost every organization. What's keeping the highest-value holdout from being connected, and what would it take to get there?
<!-- nav -->

---

[← Domain Services](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-7-domain-services.md) | [🏠 Contents](/README) | [Cloud Application →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-2-cloud-application.md)
