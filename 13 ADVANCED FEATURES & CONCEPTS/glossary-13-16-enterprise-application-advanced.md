# Enterprise Application (Advanced)
*Governing the Applications in Your Tenant Beyond Basic Integration*

**Part of Entra ID Glossary Series: Glossary#13.16 - Enterprise Application (Advanced)**

---

A tenant audit found 847 enterprise applications. The IT team recognized about 200 of them. The rest had been created by developers, added from the gallery, granted by OAuth consent, or automatically provisioned by various Azure and Microsoft 365 features.

Some had no owners assigned. Some had application permissions that hadn't been reviewed in years. Some were integrated applications for products the company had stopped using. Several were custom applications built by former employees with no current owner.

Enterprise applications in Entra ID accumulate. The advanced work is governing what's there, not just integrating new things.

## 🏗️ Enterprise Application vs App Registration

The distinction trips up most developers early on. Both objects exist for every application, but they serve different purposes:

**App registration** 🔵: The global definition of the application. Created once in the developer's home tenant. Defines the application's identity, permissions it can request, redirect URIs, token configuration, and branding. This is where you configure what the app is.

**Enterprise application (service principal)** 🟢: The local representation of the application in each tenant where it's used. Created automatically when an app registration is used in a tenant, or when an admin adds an application from the gallery. This is where you configure how the app is used in your tenant: who can sign in, which users have been assigned, what permissions have been consented, how users are provisioned.

Every application in your tenant has an enterprise application object. First-party Microsoft applications (Teams, SharePoint, Exchange Online) appear as enterprise applications in your tenant even though you don't manage their app registrations.

## 🔑 Key Enterprise Application Configuration

**User assignment required** 🎯: When enabled, only users and groups explicitly assigned to the application can sign in. When disabled, any user in the tenant can sign in if they have a valid Entra ID account (and the application itself doesn't restrict access). For business applications that should only be accessible to specific populations, enabling user assignment is the right default.

**Visible to users** 👀: Controls whether the application appears in My Apps (myapps.microsoft.com) and the Microsoft 365 app launcher. Applications that are infrastructure (APIs, background services) should be hidden. Applications that users directly access should be visible for easy discovery.

**App roles** 🔷: Custom roles defined in the application's manifest that can be assigned to users and groups. When a user with an assigned app role signs in, their token contains the role claim. The application uses this to determine what the user can do within the application. Example: `SalesManager`, `ReadOnly`, `Administrator` app roles assigned to groups, with the application rendering different views and granting different capabilities based on the role in the token.

## ⚙️ Application Provisioning

Many enterprise applications support automated user provisioning via SCIM. When provisioning is configured, Entra ID automatically creates, updates, and disables user accounts in the application based on Entra ID user status.

The provisioning configuration for an enterprise application includes:

**Scope** 📋: Which users to provision. All users assigned to the application, or all users in the tenant (with sync filters applied).

**Attribute mapping** 🔄: How Entra ID attributes map to application attributes. Which Entra ID field becomes the application's `userName`, `email`, `givenName`, etc.

**Provisioning status** 📊: The current provisioning cycle status, when it last ran, how many users were processed, and any errors for specific users.

The provisioning log (separate from the sign-in log and audit log) records each provisioning action: user created, updated, skipped, or failed to provision. Essential for troubleshooting why a user's account wasn't created in an application they were assigned to.

## 📋 Enterprise Application Governance

**Application owners** 👤: Each enterprise application should have designated owners who are responsible for it: understanding what it does, reviewing access periodically, and being the point of contact when questions arise. Applications without owners are ungoverned.

**Access reviews for app assignments** 🔍: Entra ID Identity Governance supports access reviews targeting enterprise application assignments. Quarterly reviews where application owners confirm whether each assigned user still needs access. Users who reviewers don't confirm as needed are automatically unassigned.

**Consent review** 🔐: The permissions consented for enterprise applications should be reviewed periodically. Application permissions granted years ago for integrations that are no longer active are a security risk. The Enterprise Applications blade shows consented permissions per application; unused or over-privileged consents should be revoked.

**Activity monitoring** 📊: The sign-in logs include enterprise application sign-in activity. Applications with zero sign-in activity over the past 90 days are candidates for review: is the application still needed, or was it set up and never used?

---

💬 **Do you know how many enterprise applications are in your Entra ID tenant right now, and when the last ownership and permission review was conducted?** The enterprise application sprawl problem is common: every SaaS subscription, every developer experiment, every gallery app added for evaluation contributes to the count. What's your team's approach to keeping the enterprise application inventory current and governed?
<!-- nav -->

---

[← Consent Experience](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-15-consent-experience.md) | [🏠 Contents](/README) | [Cross-Tenant Access →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-17-cross-tenant-access.md)
