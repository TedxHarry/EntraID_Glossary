# User Provisioning: Accounts That Create Themselves (When It's Done Right)

**Part of Entra ID Glossary Series: Glossary#6.1 - User Provisioning**

---

A new hire started on a Monday. By Wednesday, she still didn't have access to Salesforce. IT said her account was in Entra ID. HR confirmed she was in the HR system. The Salesforce admin said they'd never received a request to create her account.

The gap was the provisioning step. Entra ID knew she existed. Salesforce didn't. Someone was supposed to manually create her account in Salesforce during onboarding, and it fell through the cracks in a busy week.

Automated provisioning is the fix for that gap. When it works, accounts in connected applications appear automatically, without anyone having to submit a request or remember to do something.

## ⚙️ What Provisioning Is

User provisioning is the process of automatically creating, updating, and disabling user accounts in applications based on changes in the authoritative identity system (Entra ID for cloud, or HR system for joiner/mover/leaver events).

When provisioning is configured between Entra ID and an application:

- ✅ New user added to Entra ID (or assigned to the app) → account created in the app automatically
- ✅ User's department changes in Entra ID → app account updated with new attributes
- ✅ User is disabled or unassigned from the app → app account disabled or deleted automatically

The key word throughout: automatically. No tickets. No manual steps. No dependency on someone remembering.

## 🔧 How Entra ID Provisioning Works

Entra ID provisioning uses the SCIM protocol (System for Cross-Domain Identity Management, covered in Glossary#9.8) to communicate with application provisioning endpoints. SCIM is a standardized REST API for user and group management.

The provisioning flow:

1. **Admin configures provisioning** in Entra ID for the target application (Salesforce, ServiceNow, Workday, etc.)
2. **Scope is defined**: which users or groups should be provisioned to this app
3. **Attribute mapping is configured**: which Entra ID attributes map to which fields in the target app
4. **Entra ID provisioning service runs** on a 40-minute cycle (or triggered manually)
5. **Changes detected**: new assignments, attribute changes, removed assignments
6. **API calls made to the app**: CREATE, UPDATE, or DISABLE/DELETE operations

Apps that support SCIM natively (most modern SaaS applications) have a standard provisioning endpoint. Apps without SCIM support require a custom connector or a gallery connector built by Microsoft or the vendor.

## 📋 Provisioning vs Single Sign-On: Two Different Things

This distinction catches people out regularly.

**Single Sign-On (SSO)**: Controls how users authenticate to an application. The user already has an account in the app. SSO means they sign in using their Entra ID identity instead of a separate username/password.

**Provisioning**: Controls whether the user has an account in the application at all. Provisioning creates that account (or removes it) without manual intervention.

You can have SSO without provisioning: users authenticate through Entra ID, but someone manually creates their accounts in the app first. This is where the new hire problem happens.

You can have provisioning without SSO: accounts are created automatically, but users still log in with local credentials.

Ideally, both are configured. Provisioning handles the account lifecycle. SSO handles the authentication experience.

## 🔄 Inbound Provisioning: HR as the Source

A more advanced provisioning pattern goes in the other direction. Instead of Entra ID pushing to apps, an HR system (Workday, SAP SuccessFactors, BambooHR) pushes to Entra ID.

Inbound provisioning means:
- New hire created in Workday → Entra ID user object automatically created
- Employee's job title changes in Workday → Entra ID attributes automatically updated
- Employee terminates in Workday → Entra ID account automatically disabled

This makes the HR system the source of truth and removes the manual step of creating Entra ID users for new hires. Combined with outbound provisioning to apps, the entire joiner/leaver process becomes automated end-to-end.

## ⚠️ What Breaks in Manual Provisioning

The new hire who waited two days for her Salesforce account is the mild case. Other consequences of manual-only provisioning:

- Departed employees retain active accounts in applications for weeks after their Entra ID account is disabled (because nobody deprovisioned the app accounts)
- Contractors get broader app access than they should because the provisioning request was easier to approve generically
- License costs are higher because abandoned accounts are never cleaned up

Automated provisioning solves all three.

---

💬 **How many of your organization's applications have automated provisioning configured vs relying on manual account creation?** The gap between "Entra ID knows the user" and "every app the user needs has their account" is where most new hire friction lives. What was the first application you automated provisioning for?

#EntraID #UserProvisioning #SCIM #IdentityGovernance #MicrosoftEntra #LifecycleManagement #Automation
