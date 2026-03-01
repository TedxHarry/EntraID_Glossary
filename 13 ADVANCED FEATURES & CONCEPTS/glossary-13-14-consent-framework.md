# Consent Framework
*How Applications Get Permission to Access Your Data*

📚 **Part of Entra ID Glossary Series: Glossary#13.14 - Consent Framework**

---

A developer registered an application that requested `Mail.ReadWrite.All` at the application level. Application-level permissions don't require a user to consent; they require an administrator to consent on behalf of the entire organization.

The developer tested it by granting admin consent themselves, since they had Global Administrator rights in the dev tenant. They deployed to production and the app worked. Then a security engineer ran a review of consented application permissions and flagged the app: one application with read/write access to every mailbox in the organization.

The developer's intent was to read and write mail for a service account only. The permission they requested gave them access to every employee's email.

The consent framework is what stood between "application requests permission" and "application actually has permission." The problem was that the framework's consent step was performed without understanding what the permission actually granted.

## 🔑 What the Consent Framework Is

The consent framework is the mechanism in Entra ID that governs how applications gain permission to access organizational data and user data through the Microsoft identity platform.

When an application requests access to Entra ID-protected resources, it must obtain consent before it can receive tokens with those permissions. Consent is the record of authorization: this application is allowed to access this data, granted by this user or administrator.

Technically, consent results in an OAuth 2.0 permission grant stored in Entra ID: the service principal for the application gains a delegated permission grant (representing a user's consent) or an application permission grant (representing admin consent).

## 📊 User Consent vs Admin Consent

The consent framework distinguishes between two consent paths based on the sensitivity of the permissions requested:

**User consent** 👤: For lower-sensitivity delegated permissions, users can consent individually. When a user signs in to an application and sees a consent prompt listing what the app is requesting, clicking "Accept" creates a delegated permission grant for that user. Only that user's data is accessible under this grant; other users haven't consented.

**Admin consent** 🔑: For higher-sensitivity permissions (read all users' profiles, access all mailboxes, write to the directory), only a Privileged Role Administrator, Application Administrator, or Global Administrator can consent. Admin consent on behalf of the organization grants the permission for all users. No individual user consent prompts appear when signing in to that application.

The distinction between what requires admin consent vs user consent is configured in the Entra ID admin consent settings: which permissions are classified as requiring admin approval, and which users (if any) can consent on their own.

## ⚙️ Admin Consent Policies

Entra ID's user consent settings control the consent experience across the tenant:

**Do not allow user consent**: No user can consent to any permission. Every application requires admin consent. Maximum control, maximum friction.

**Allow user consent for apps from verified publishers**: Users can consent to applications from publishers who have gone through Microsoft's publisher verification process. Reduces risk of consenting to malicious apps.

**Allow user consent for selected permissions**: Administrators configure a consent policy classifying specific permissions as user-consentable or requiring admin consent. Fine-grained control.

**Allow user consent to all apps**: Users can consent to any permission for any app. Minimum control, maximum risk.

Most enterprise organizations use either "verified publishers only" or a custom policy defining which permissions users can consent to.

## 🔒 Admin Consent Workflow

When a user tries to sign in to an application that requests permissions requiring admin consent, and admin consent hasn't been granted yet, they can't proceed. They see a message indicating that admin approval is required.

Entra ID supports an admin consent workflow: users can submit a request explaining why they need the application. Designated reviewers (configured in the Enterprise Applications settings) receive the request, review it, and either grant admin consent or deny the request. This creates an auditable approval process for new application onboarding.

Without the admin consent workflow, users are simply blocked and must contact IT manually.

## 🔍 Reviewing Granted Consents

Consents accumulate over time. A periodic audit of what permissions have been granted to which applications is essential:

**Delegated permission grants**: What applications have been granted access to which permissions for which users. The Enterprise Applications blade in Entra ID shows this per application.

**Application permission grants**: Which applications have admin-consented application permissions. These are the broadest grants: permissions that apply organization-wide without any user involvement.

High-risk grants to look for: application permissions for `Mail.ReadWrite.All`, `User.ReadWrite.All`, `Directory.ReadWrite.All`, or `RoleManagement.ReadWrite.Directory` on applications that aren't well-known or explicitly approved.

---

💬 **Does your organization have a formal process for reviewing admin consent requests and auditing existing application permission grants?** Consent sprawl is a real governance problem in mature Entra ID tenants: applications accumulate over-permissioned consents that nobody reviews. What's the most surprising over-privileged application consent your team has found during an audit?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Admin Unit](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-13-admin-unit.md) | [🏠 Contents](/README) | [Consent Experience →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-15-consent-experience.md)
