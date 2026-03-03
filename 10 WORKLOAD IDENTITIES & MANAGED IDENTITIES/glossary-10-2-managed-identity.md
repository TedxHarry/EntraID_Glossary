# Managed Identity
*Credentials That Azure Manages So You Don't Have To*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #10.2 - Managed Identity

---


The connection string in the app config file had the Key Vault secret embedded in plain text. Not encrypted. Not in a secrets manager. Just sitting there, checked into the repository, visible to anyone with read access to the codebase.

The developer who put it there wasn't careless. They were solving a real problem: the application needed to authenticate to Key Vault to retrieve secrets. To authenticate, it needed credentials. The credentials had to live somewhere. The app config file was where they ended up.

This is the credential bootstrapping problem. You need credentials to get credentials. Managed identity is how Azure breaks that loop.

## 🔑 What managed identity is

A managed identity is an identity in Entra ID that Azure creates and manages for an Azure resource. Instead of a developer creating credentials and storing them somewhere, Azure creates a service principal in Entra ID, handles the underlying credential entirely, and makes a token available to code running on that resource through a local endpoint.

The application code doesn't handle a secret or certificate. It calls a local Azure endpoint, gets a token for the requested service, and uses that token. Azure manages what's behind that endpoint. The credential rotation, the certificate lifecycle, the credential storage: all handled by the platform.

The application developer's job becomes: enable managed identity on the resource, grant the managed identity the RBAC permissions it needs, and write the code to request a token from the local endpoint. No credential to store. No rotation schedule to maintain. No secret to leak.

## ⚙️ How managed identity works

The mechanism is the Instance Metadata Service (IMDS), an Azure endpoint at `169.254.169.254` that's only reachable from within Azure resources. It's not accessible from the internet or from on-premises networks. Only code running on the Azure resource itself can reach it.

When code requests a token, it calls the IMDS endpoint specifying which resource it needs a token for (Key Vault, Storage, SQL, etc.). Azure validates that the resource has a managed identity, issues a token scoped to the requested resource, and returns it. The code uses that token in the Authorization header of API calls to the target service.

The SDKs handle this transparently. `DefaultAzureCredential` in the Azure SDK for Python, .NET, Java, and JavaScript will automatically attempt managed identity token acquisition when running in an Azure environment. The developer doesn't call IMDS directly; the SDK does.

## 🔐 What managed identity can authenticate to

Managed identity works with any Azure service that supports Entra ID authentication and RBAC:

**Azure Key Vault** 🔑: The primary use case. App retrieves secrets, keys, and certificates without storing credentials to reach Key Vault.

**Azure Storage** 📦: Blobs, queues, tables, and files. Assign Storage Blob Data Reader or Contributor to the managed identity instead of sharing storage account keys.

**Azure SQL Database** 🗄️: Database connections authenticated via managed identity token instead of SQL credentials.

**Azure Service Bus and Event Hubs** 📨: Message producers and consumers authenticating without connection strings containing shared access signatures.

**Any Azure service supporting Entra auth** ✅: The pattern applies broadly across Azure services. If the service supports Entra ID authentication, a managed identity can authenticate to it.

## ⚠️ What managed identity doesn't solve

Managed identity is powerful within Azure but has scope limitations:

**Non-Azure targets** 🌐: If your application needs to authenticate to a third-party API, a GitHub repository, or an on-premises system, managed identity won't cover that directly. Those external services need to be able to validate Microsoft-issued tokens, which most third-party services don't support natively.

**Non-Azure compute** 💻: Managed identity is for Azure resources. Code running on-premises, in a developer's local environment, or in a non-Azure cloud doesn't have access to IMDS. `DefaultAzureCredential` handles this by falling back to other credential types in local environments (developer credentials, environment variables), but it requires the developer to understand the fallback chain.

**Service-to-service without Azure hosting** 🔄: If a service running outside Azure needs to call an Azure service, managed identity isn't an option. Workload federation or service principal with certificate authentication is the appropriate pattern.

## 🏗️ System-Assigned vs user-assigned

Managed identities come in two variants with different lifecycle characteristics. System-assigned identities are tied to a single resource and deleted when that resource is deleted. User-assigned identities are standalone resources that can be assigned to multiple Azure resources and persist independently.

The choice between them comes down to whether the identity needs to be shared across multiple resources or tied to a single resource's lifecycle.

---

💬 **Has your team moved from service principal secrets to managed identity for Azure workloads, or are connection strings and secrets still the primary authentication pattern?** The transition is usually incremental: one application at a time, starting with the highest-risk stored credentials. What was the first managed identity migration that made the pattern click for your team?
✍️ TedxHarry


### 🔧 Quick reference: managed identity token

```bash
# Get a token from IMDS (run inside an Azure VM or App Service)
curl -H "Metadata: true" \
  "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://management.azure.com/"

# PowerShell equivalent (inside Azure VM)
$response = Invoke-WebRequest -Uri "http://169.254.169.254/metadata/identity/oauth2/token?api-version=2018-02-01&resource=https://graph.microsoft.com/" -Headers @{Metadata="true"}
($response.Content | ConvertFrom-Json).access_token
```

<!-- nav -->

---

[← Workload Identity](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-1-workload-identity.md) | [🏠 Contents](/README) | [System-Assigned Managed Identity →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-3-system-assigned-managed-identity.md)
