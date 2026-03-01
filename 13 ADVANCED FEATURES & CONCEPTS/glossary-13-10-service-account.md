# Service Account
*The Legacy Pattern That Managed Identity Is Replacing*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#13.10 - Service Account**

---

## 🎯 TL;DR

- Service accounts are non-human accounts used by applications and services to run processes and call APIs
- In Entra ID, use managed identities or service principals instead of user accounts for service accounts
- If legacy service accounts must exist: use long random passwords, never interactive login, audit regularly


A penetration tester found a set of credentials in a configuration file on a compromised server. Username: `svc_reporting`. Password: `Reporting2019!`. The account had been created in 2019. The password had never been changed.

The security team checked the account. It was an Entra ID account used by a reporting application to call Microsoft Graph. It had `Reports.Read.All` and `AuditLog.Read.All` application permissions. No MFA (applications can't complete MFA). No Conditional Access targeting it specifically. The account's sign-in history showed the attacker had been using it for 11 days before detection.

`svc_reporting` is a service account. The pattern is common, the security posture is poor, and for applications running in Azure, there's almost always a better answer.

## 🤖 What Service Accounts Are

In the context of Entra ID, service accounts are user accounts created for applications and automated processes rather than human users. They're the legacy pattern for giving non-human workloads an identity to authenticate with.

The service account pattern originates from on-premises Active Directory, where creating a dedicated user account for a service was the standard way to give that service an identity. The service account got permissions, its password was set to something long and complex, and "never expires" was checked.

This pattern migrated into cloud environments where it doesn't fit as well. Entra ID user accounts weren't designed for non-human authentication:

**No MFA support** 🔑: Applications authenticating with a service account can't complete MFA challenges. If Conditional Access requires MFA for all users, service accounts need an explicit exclusion or they break. Exclusions from MFA policies are security gaps.

**Shared credentials problem** 📋: The application needs the service account's password to authenticate. That password ends up in configuration files, environment variables, secrets stores, or in the memory of developers who deployed the application. Multiple people and systems know the credential.

**No rotation discipline** 🔄: Service account passwords have a rotation schedule in theory. In practice, they're changed when someone remembers or when there's a security incident, because rotating the password requires updating every system that uses it, which is often undocumented.

**No lifecycle tied to purpose** 🗑️: Service accounts created for a project that ended remain active because nobody knows it's safe to disable them. The account accumulates in the directory indefinitely.

## ✅ The Modern Alternative

For applications running in Azure, managed identity is the right answer. No credentials, automatic rotation by Azure, no secrets to manage, no rotation schedule to forget. If the application can run in Azure, it should use a managed identity.

For applications running outside Azure that need to call Azure services, a service principal with certificate authentication or workload federation is the appropriate pattern. A service principal (not a user account) with a certificate credential that has a defined expiry and rotation schedule, or federated to the CI/CD system's OIDC tokens with no stored Azure credentials at all.

Service principals exist specifically for non-human authentication. They're separate from user accounts, have no mailbox, can't be targeted by user-focused Conditional Access policies in the same way, and their credential types (certificates, client secrets, federated credentials) are appropriate for machine authentication.

## 🔧 When Service Accounts Are Unavoidable

Not every scenario can immediately move to managed identities or service principals. Some cases where service accounts persist:

**Legacy applications** 📦: Applications that authenticate with username/password and can't be modified to use modern auth. Third-party applications that predate OAuth/OIDC support. In these cases, the service account is unavoidable in the short term.

**On-premises workloads calling cloud services** 🏢: Processes running on-premises that need to call Entra ID-protected APIs. Managed identity requires Azure compute. A service principal with certificate auth is the right answer, but if certificate management isn't implemented, a service account may exist.

## 📋 Governing Existing Service Accounts

For service accounts that must exist, the governance requirements:

**Dedicated Conditional Access policy** 🔐: A CA policy targeting all service accounts (grouped by a naming convention or group membership) that restricts allowed IP ranges (only authenticate from known service infrastructure IPs), and blocks interactive sign-in if the account is never used interactively.

**Sign-in inactivity monitoring** 👀: Service accounts that haven't authenticated in 90 days are candidates for review. Either the application they serve is no longer running, or the account has been replaced and not disabled.

**Regular password rotation** 🔄: If the account must use password auth, quarterly rotation enforced through a documented process with all dependent systems updated.

**Clear ownership** 👤: Every service account should have a named owner responsible for it. Anonymous service accounts with no responsible party are the ones that linger indefinitely.

---

💬 **How many service accounts (user accounts used by applications) does your organization still have in Entra ID, and what's the plan for transitioning them to service principals or managed identities?** The count of legacy service accounts in an enterprise Entra ID tenant is often surprising. What's the biggest obstacle to converting your highest-risk service accounts to modern workload identity patterns?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Global Secure Access](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-9-global-secure-access.md) | [🏠 Contents](/README) | [Sync Agent →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-11-sync-agent.md)
