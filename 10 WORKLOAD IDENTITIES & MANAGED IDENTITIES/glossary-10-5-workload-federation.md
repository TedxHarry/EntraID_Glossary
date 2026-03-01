# Workload Federation: Authenticating to Azure Without Storing Azure Credentials

**Part of Entra ID Glossary Series: Glossary#10.5 - Workload Federation**

---

A GitHub Actions workflow was deploying infrastructure to Azure. The workflow needed credentials to authenticate to Azure. The team stored a service principal client secret in GitHub Secrets.

The secret was valid for two years. It was rotated once, manually, when someone remembered. It was visible to anyone with admin access to the GitHub repository. When a developer accidentally logged the environment variables during debugging, the secret appeared in the workflow run logs. The secret had to be immediately revoked and recreated, which broke three other workflows that shared it.

Workload federation is the architecture that eliminates this problem. The GitHub Actions workflow doesn't need an Azure credential stored in GitHub at all.

## 🔗 What Workload Federation Is

Workload federation is an authentication pattern where an external system's existing identity token is exchanged for an Entra ID token, without requiring that external system to store any Azure credentials.

The external system (GitHub, GitLab, Kubernetes, another cloud provider's identity system) already has an identity for its workloads. GitHub knows which repository and which workflow is running. Kubernetes knows which service account is making the request. These systems issue OIDC tokens asserting that identity.

Workload federation lets you tell Entra ID: "Trust tokens from this external identity provider, specifically tokens asserting this identity. When you see one, issue an Entra ID token in exchange."

The result: the GitHub Actions workflow presents its GitHub-issued token, Entra ID validates it against your federation configuration, and issues an Azure token. No Azure credential was ever stored in GitHub. There's nothing to leak, nothing to rotate, nothing to accidentally log.

## ⚙️ How It Works

The flow has four steps:

**Step 1: Configure trust in Entra ID** 🔧: Create a Federated Identity Credential on an app registration or user-assigned managed identity. This configuration specifies the external token's issuer URL (GitHub's OIDC endpoint), the subject (which specific GitHub repo and workflow), and the expected audience.

**Step 2: Workflow requests a GitHub token** 📋: The GitHub Actions workflow uses a built-in GitHub action (`azure/login` or directly via OIDC) to request a GitHub-issued OIDC token. GitHub generates this token automatically; it contains claims about the repository, branch, workflow, and environment.

**Step 3: Token exchange at Entra ID** 🔄: The workflow presents the GitHub token to Entra ID's token endpoint, referencing the app registration or managed identity it wants to authenticate as. Entra ID validates the token (signature, issuer, audience, subject) against the Federated Identity Credential configuration.

**Step 4: Azure token issued** ✅: Entra ID issues an access token for the Azure resources the identity has been granted access to. The workflow uses this token for Azure CLI, Azure SDK, or ARM API calls. The GitHub token is discarded; the Azure token is ephemeral and scoped to the workflow run.

## 🌐 What Systems Support It

Workload federation works with any external system that can issue OIDC tokens with consistent, verifiable claims. The most common implementations:

**GitHub Actions** 🐙: The most widely adopted use case. GitHub Actions workflows in specific repositories, branches, and environments can authenticate to Azure without secrets. Microsoft provides the `azure/login` action which handles the token exchange.

**GitLab CI/CD** 🦊: GitLab generates OIDC tokens for CI/CD pipelines. Federated identity credentials can be configured to trust tokens from specific GitLab projects and ref names.

**Kubernetes service accounts** ☸️: Azure Kubernetes Service and other Kubernetes clusters can issue OIDC tokens for service accounts. Pods running with specific service accounts can authenticate to Azure without secrets mounted in the pod.

**Terraform Cloud and other CI/CD platforms** 🏗️: Any platform that supports OIDC token generation for its workloads can be configured as a trusted issuer.

## 🔐 The Security Improvement

The security properties of workload federation are meaningfully better than stored credentials:

**Nothing to leak** 🚫: There's no Azure credential in the external system. A GitHub secret that doesn't exist can't be exposed in logs, compromised in a breach, or accidentally committed.

**Automatic scoping** 🎯: The federated identity credential can be configured to trust only tokens from a specific repository, branch, or environment. A compromised workflow in a different repository gets nothing because it doesn't match the subject claim.

**Token lifetime** ⏰: The exchanged Azure token is short-lived. The GitHub token that triggers the exchange is also short-lived. There's no long-lived credential that an attacker could reuse days or weeks after obtaining it.

**Audit trail** 📊: Entra ID sign-in logs show every token exchange, including the subject claim from the external token. You can see exactly which repository and workflow authenticated, not just "service principal X authenticated."

---

💬 **Has your team migrated GitHub Actions or CI/CD pipelines from stored service principal secrets to workload federation?** The migration is usually straightforward and the security improvement is significant. What held your team back from making the switch, or what finally prompted you to do it?

#EntraID #WorkloadFederation #GitHubActions #ManagedIdentity #ZeroTrust #MicrosoftEntra #DevSecOps
<!-- nav -->

---

[← User-Assigned Managed Identity: One Identity Shared Across Many Resources](glossary-10-4-user-assigned-managed-identity.md) | [Home](../README.md) | [Federated Identity Credential: The Trust Configuration That Makes Keyless Auth Work →](glossary-10-6-federated-identity-credential.md)
