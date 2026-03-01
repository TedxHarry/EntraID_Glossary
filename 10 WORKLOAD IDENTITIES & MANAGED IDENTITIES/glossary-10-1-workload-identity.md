# Workload Identity
*When the Thing Connecting to Your Systems Isn't a Person*

**Part of Entra ID Glossary Series: Glossary#10.1 - Workload Identity**

---

A security engineer ran an audit of the Entra ID tenant and found 847 service principals. She knew about maybe 200 of them. The rest had been created over years by developers, DevOps pipelines, vendors, and automated processes. Some had owner accounts that no longer existed. Some had secrets that were years past their stated rotation policy. Several had permissions scoped to entire subscriptions.

Not one of them was a person.

This is the workload identity problem. The non-human identities in your environment often outnumber the human ones. They're harder to govern. They have no natural lifecycle tied to an employment status. They don't have a manager to review their access. And when a secret leaks, it doesn't trigger the same response that a compromised user account would.

## 🤖 What Workload Identity Is

Workload identity is the category of identity used by software: applications, services, scripts, containers, pipelines, and automated processes. These identities exist so that code can authenticate to other systems, just as users authenticate to applications.

In Entra ID, workload identities include:

**Applications and service principals** 🔷: When you register an application in Entra ID, it gets an app registration (the application object) and, in each tenant where it's used, a service principal (the local representation of that app). The service principal is what actually authenticates. Applications authenticate with client secrets (passwords) or certificates.

**Managed identities** 🔵: Azure-provided identities for Azure resources. No credentials to manage; Azure handles the underlying credential rotation automatically. A VM, Function App, or Container App can use a managed identity to authenticate to other Azure services without any secrets in the code.

**Workload federation identities** 🔗: Non-Azure workloads (GitHub Actions, GitLab, Kubernetes service accounts) that are granted access to Entra ID-protected resources through OIDC token exchange, without storing Azure credentials in those external systems.

## 🔐 Why Workload Identity Is Hard to Govern

Human identities have natural governance anchors. A new employee triggers provisioning. A departing employee triggers deprovisioning. A manager can certify their reports' access in an access review. Conditional Access can require MFA, a compliant device, a known location.

Workload identities have none of that.

**No lifecycle trigger** 📋: A service principal created for a vendor integration in 2021 doesn't automatically get removed when the vendor relationship ends in 2023. There's no offboarding event. The identity just persists.

**No MFA** 🔑: Code can't complete an MFA challenge. Workload identities authenticate with secrets or certificates. This means a leaked secret is an uninterrupted authentication capability, not a first factor that still needs a second.

**Broad permissions** ⚠️: Developers often scope workload identity permissions generously to avoid repeated permission errors during development, then those broad permissions make it to production unchanged. A service principal with Contributor on a subscription is a significant blast radius if that credential is compromised.

**Orphaned identities** 👻: Service principals whose owning applications no longer exist. App registrations whose original developers have left the organization. Managed identities for deleted resources. These identities persist because nothing and no one is responsible for cleaning them up.

## 📊 The Scale Problem

Enterprise environments accumulate workload identities faster than user identities. Every SaaS application granted API access creates a service principal. Every Azure DevOps pipeline creates an identity. Every ARM template deployment may create managed identities. Every vendor integration adds an app registration.

The 847 service principals in the opening scenario isn't unusual for an enterprise that's been in Azure for five or more years. Organizations that have counted carefully often find more non-human identities than human ones.

## 🔧 Governing Workload Identities

Microsoft Entra Workload ID (the product layer on top of the base workload identity capabilities) adds governance features:

**Workload Identity lifecycle** 🔄: Policies that flag service principals with no recent sign-in, expired secrets, or missing owners. The equivalent of access reviews for non-human identities.

**Conditional Access for workloads** 🔐: Policies that restrict where workload identities can authenticate from. A service principal used only by an Azure Function doesn't need to be able to authenticate from an IP in another country.

**Managed identity preference** ✅: Where possible, replacing service principals with client secrets with managed identities removes the credential management problem entirely. The governance work is moving existing workloads to credential-less authentication wherever Azure supports it.

---

💬 **How many workload identities does your organization have in Entra ID, and how many of them are actively owned and governed?** The gap between "service principals that exist" and "service principals that someone is responsible for" is one of the hardest problems in enterprise identity security. What's your approach to workload identity governance?
<!-- nav -->

---

[← External Tenant](../9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-16-external-tenant.md) | [Home](../README.md) | [Managed Identity →](glossary-10-2-managed-identity.md)
