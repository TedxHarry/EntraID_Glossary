# Consent Experience
*What Users See When an App Asks for Permission*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#13.15 - Consent Experience**

---

## 🎯 TL;DR

- The Consent Experience is the UI dialog that appears when a user or admin grants permissions to an app
- It shows: app name, publisher, requested permissions — users should review carefully before consenting
- Phishing apps often request excessive permissions — train users to be suspicious of unexpected consent prompts


A user got a consent prompt for an application they'd never seen before. It was requesting permissions to read their email, read their contacts, and read files shared with them. The application was called "QuickProductivityHelper." The publisher was listed as "Unverified."

The user clicked Accept because they thought someone from IT had sent them the link. The application collected their OAuth token and began reading their email for credential information to use in further attacks.

The consent experience is the moment between "an application wants access to your data" and "the application has access to your data." That moment is a security control. Whether users make informed decisions at that moment determines whether it works as intended.

## 🖥️ What Users See in the Consent Prompt

The Entra ID consent dialog presents specific information about the application requesting permissions:

**Application name and logo** 📱: The display name and icon registered in the app registration. Unscrupulous applications often use names and logos that imply trustworthiness or impersonate known applications.

**Publisher information** 🏢: Whether the publisher is verified (a blue checkmark indicating Microsoft has verified the publisher's identity against their business records) or unverified. Unverified publishers are a risk signal. All Microsoft first-party apps and well-established ISVs appear as verified.

**What the app will be able to do** 📋: A plain-language list of the permissions being requested, translated from technical scope names into user-readable descriptions. `Mail.Read` becomes "Read your mail." `Contacts.Read` becomes "Read your contacts." The quality of these descriptions matters: good permission descriptions help users make informed decisions.

**Who the consent applies to** 👤: For user consent, a note that this grants access to the user's data only. For admin consent on behalf of the organization, a clear statement that the permission is being granted for all users in the organization.

## 🔒 The Security Signal in the Experience

The consent prompt is designed to contain risk signals that help users and administrators make informed decisions:

**Publisher verification status** ✅: Verified publishers have gone through a process confirming their business identity. Seeing "Unverified" should raise suspicion, especially for an application the user wasn't expecting.

**Permission sensitivity** ⚠️: Some permissions have a specific "high privilege" indicator in the consent UI. Permissions that access data across all users (not just the signed-in user) or that allow data modification carry additional prominence in the dialog.

**Application source** 🌐: For applications from outside the tenant, the tenant-of-origin is indicated. An application from an unfamiliar tenant requesting sensitive permissions is a warning.

**Consent scope** 🏢: Admin consent prompts explicitly state that the consent applies to all users in the organization, which is a meaningful signal that the decision affects more than just the user making it.

## 🔑 Admin Consent Experience

When an administrator grants consent on behalf of the organization (through the Enterprise Applications admin consent workflow or directly), the consent experience is different from user consent:

**Explicit "consent on behalf of your organization" checkbox**: The admin must actively acknowledge they're granting permissions for all users, not just themselves.

**Full permission list with technical details**: Administrators see the complete list of permissions including their technical scope names and a description of what each allows. Less simplified than the user-facing version.

**Application information summary**: The application ID, tenant of origin, publisher details, and any Microsoft 365 certification status.

The admin consent experience is designed for a more informed audience than the user consent experience, with more technical detail and explicit acknowledgment requirements.

## 📊 Improving the Consent Experience for Your Users

Organizations control several aspects of the consent experience for applications they build:

**Application branding** 🎨: The logo and display name in the consent prompt come from the app registration. A well-branded application with a recognizable logo reduces confusion.

**Publisher verification** ✅: ISVs distributing applications to other tenants should go through publisher verification. It adds the blue checkmark and builds trust with users in the target organizations.

**Permission minimization** 🔑: Each permission in the consent prompt is a reason a user might hesitate or decline. Requesting only the permissions the application actually needs reduces consent friction and builds user trust.

**Permission descriptions** 📝: The permission descriptions users see come from the scope definitions in the app manifest. Clear, honest descriptions of what each permission allows help users understand what they're consenting to.

**Incremental consent** 📋: Requesting permissions only when the corresponding feature is used (rather than all at sign-up) means users see smaller, more contextual consent prompts with clear reasons for each permission.

## ⚠️ Consent Phishing

Illicit consent grant attacks (also called consent phishing) are a significant threat vector. An attacker creates a malicious application, registers it in any Entra ID tenant, and sends targeted users a link to consent to it. If the user consents, the attacker has an OAuth token for the user's data that persists even after a password change.

Defending against consent phishing: limit user consent to verified publishers, train users to scrutinize consent prompts and never consent to unexpected applications, and periodically audit consented applications to find and revoke unauthorized grants.

---

💬 **Does your organization train users to evaluate consent prompts before accepting, and have you had any consent phishing incidents?** The consent phishing attack is underappreciated relative to credential phishing because it bypasses MFA. A consented OAuth token works regardless of the user's MFA registration. What's your organization's approach to consent phishing defense?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Consent Framework](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-14-consent-framework.md) | [🏠 Contents](/README) | [Enterprise Application (Advanced) →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-16-enterprise-application-advanced.md)
