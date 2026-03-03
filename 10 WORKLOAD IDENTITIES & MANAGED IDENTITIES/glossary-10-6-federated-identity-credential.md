# Federated Identity Credential
*The Trust Configuration That Makes Keyless Auth Work*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #10.6 - Federated Identity Credential

---


A developer configured workload federation for their GitHub Actions workflow. They set up the app registration, assigned the right Azure roles, ran the workflow, and got an authentication error.

The error: the subject claim in the GitHub token didn't match the subject configured in the Federated Identity Credential.

They'd configured the FIC with a subject for the `main` branch. The workflow was running on a pull request. Different subject. Entra ID rejected the token.

They added a second Federated Identity Credential for the pull request environment. Everything worked.

This is what a Federated Identity Credential actually is: a specific, precise trust configuration. Not "trust GitHub Actions." Trust this issuer, this subject, this audience. The precision is the security model.

## 🔧 What a federated identity credential is

A Federated Identity Credential (FIC) is a configuration object on an Entra ID app registration or user-assigned managed identity that defines a trust relationship with a specific external identity. It tells Entra ID exactly which external tokens to accept and exchange for Entra ID tokens.

FICs live on the app registration or managed identity, not on the external system. The external system (GitHub, Kubernetes, etc.) doesn't need to know about Entra ID specifically. It just issues its standard OIDC tokens. The FIC on the Entra ID side defines whether those tokens are accepted.

You can configure multiple Federated Identity Credentials on a single app registration or managed identity. Each one defines a different trust relationship.

## 📋 The three core fields

Every Federated Identity Credential is defined by three values:

**Issuer** 🌐: The URL of the external OIDC identity provider that issues the tokens. For GitHub Actions, this is `https://token.actions.githubusercontent.com`. For GitLab, it's the GitLab instance URL with the OIDC path. For AKS with OIDC enabled, it's the cluster's OIDC issuer URL. Entra ID uses this to find the external provider's public key and validate the token's signature.

**Subject** 🎯: The specific identity from the external system that this trust relationship covers. This is the most security-critical field. For GitHub Actions, the subject encodes the repository, workflow, and the trigger context. For example: `repo:myorg/myrepo:ref:refs/heads/main` for pushes to main, or `repo:myorg/myrepo:environment:production` for a specific GitHub environment. Only tokens whose `sub` claim matches exactly this value will be accepted.

**Audience** 🔊: The intended audience of the external token. For most Entra ID federations, this is `api://AzureADTokenExchange`. This value must match what the external system puts in the `aud` claim of its OIDC token. GitHub Actions defaults to this value when configured for Azure.

All three fields must match the claims in the presented external token. If any field doesn't match, Entra ID rejects the token.

## 🏗️ Where fics are configured

**On app registrations** 📱: In the Azure portal, navigate to the app registration, then Certificates & secrets, then Federated credentials. From here you can add a new federated credential. Microsoft provides templates for common scenarios: GitHub Actions, Kubernetes, and other common OIDC providers. You can also add custom configurations for providers not in the template list.

**On user-assigned managed identities** 🔷: Navigate to the managed identity resource in the portal, then Federated credentials. Same interface, same fields. Using a managed identity instead of an app registration means you don't need to manage the identity separately in Entra ID app registrations; it's an Azure resource with its own lifecycle.

The choice between app registration and user-assigned managed identity for workload federation is mostly operational. App registrations are in Entra ID. Managed identities are Azure resources. Teams already managing infrastructure as code with ARM/Bicep/Terraform often prefer managed identities because the FIC configuration can be part of the same IaC definition as the rest of the Azure resources.

## ⚠️ Common configuration mistakes

**Subject too broad** 🔓: Configuring `repo:myorg/*` or similar wildcard subjects if the external provider supports them. The subject should be as specific as possible. A wildcard subject that matches any repository in the organization means any repository could authenticate as this identity.

**Wrong subject format for the trigger type** 🔄: GitHub Actions subjects are different depending on whether the workflow is triggered by a push to a branch, a tag, a pull request, or a GitHub environment. The subject format changes. Getting this wrong causes the authentication failures described in the opening scenario.

**Multiple environments, single FIC** 📋: If a deployment pipeline has separate GitHub environments for staging and production, each environment needs its own FIC. You can't use one FIC for both environments unless you configure it with audience-level trust, which is less precise.

**Forgetting to assign roles after creating the FIC** 🔑: The FIC defines what tokens Entra ID will accept. It doesn't define what the identity can do. Role assignments on Azure resources are still required. Creating a FIC without assigning any RBAC roles gives the external workload an Entra ID token with no permissions.

---

💬 **What was the first Federated Identity Credential configuration that worked correctly in your environment, and what took the most troubleshooting to get right?** The subject claim field trips up most people the first time. Did you hit the branch vs environment subject mismatch, or a different configuration issue?
✍️ TedxHarry

<!-- nav -->

---

[← Workload Federation](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-5-workload-federation.md) | [🏠 Contents](/README) | [Instance Metadata Service (IMDS) →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-7-imds.md)
