# Instance Metadata Service (IMDS)
*The Local Endpoint That Gives Azure Resources Their Identity*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #10.7 - Instance Metadata Service (IMDS)

---


A developer debugging a managed identity issue asked a fair question: "If there's no credential stored anywhere, how does the application actually get a token?"

The answer is a local HTTP endpoint at `169.254.169.254`.

Every Azure resource with a managed identity can reach this address. Nothing outside that resource can reach it. It's not on the internet. It's not on the virtual network. It's a link-local address that Azure makes available exclusively to the compute resource it's attached to.

The application calls it, asks for a token for a specific Azure service, and gets one back. No credential management, no certificate, no secret. The endpoint handles everything behind the scenes.

## 🌐 What IMDS is

The Azure Instance Metadata Service is an internal REST endpoint that provides information and authentication tokens to Azure compute resources. It's available at `http://169.254.169.254/metadata/` and is accessible only from within the Azure resource itself.

IMDS has two primary functions:

**Compute metadata** 💻: Information about the compute instance itself. The VM's subscription ID, resource group, region, VM name, VM size, operating system, network interface details, and tags. Available at the `/metadata/instance` path. Useful for application code that needs to know where it's running without reading from configuration files.

**Managed identity token acquisition** 🔑: The mechanism by which code running on an Azure resource gets Entra ID access tokens when managed identity is enabled. Available at the `/metadata/identity/oauth2/token` path. This is the function most relevant to identity engineering.

## ⚙️ How token acquisition works

When a managed identity is enabled on an Azure resource, Azure configures the IMDS endpoint to respond to token requests for that identity. The request is straightforward:

```
GET http://169.254.169.254/metadata/identity/oauth2/token
  ?api-version=2018-02-01
  &resource=https://vault.azure.net
Metadata: true
```

The `resource` parameter specifies which Azure service the token is for. Key Vault, Storage, SQL Database, ARM APIs, and other Azure services each have their own resource URI.

The response is a JSON object with `access_token`, `expires_in`, and `expires_on`. The application extracts the token and uses it in Authorization headers for subsequent calls to the Azure service.

If the resource has a user-assigned managed identity (or multiple identities), the request can specify which identity to use via a `client_id` or `object_id` query parameter. Without this parameter, the request uses the system-assigned managed identity if one exists.

## 🔐 Why IMDS is secure

The security model of IMDS rests on network accessibility. The `169.254.169.254` address is a link-local address, which means:

**Not internet-accessible** 🚫: No inbound request from outside the Azure datacenter can reach this address. It's not behind a firewall; it's simply not routable from external networks.

**Not VNet-accessible** 🔒: Requests to `169.254.169.254` don't traverse the virtual network. Another VM in the same subnet can't call your VM's IMDS endpoint. Each resource has its own IMDS endpoint that only that resource's processes can reach.

**Requires local process access** 💻: Only code running as a process on the Azure resource itself can call IMDS. If code is running on-premises and connecting to Azure over ExpressRoute, it can't reach IMDS. If code is running in a container on a non-Azure host, it can't reach IMDS.

This access restriction is what makes managed identity trustworthy. Azure knows the token request came from the resource because only code on that resource could reach the endpoint. There's no way to spoof this from outside.

## 📦 SDK abstraction

Most developers never call IMDS directly. The Azure SDKs handle it through `DefaultAzureCredential`, which tries a sequence of credential types based on the environment:

For code running on Azure with a managed identity enabled, `DefaultAzureCredential` automatically calls IMDS and returns the resulting token. The developer doesn't specify an endpoint or format a request. The SDK handles the IMDS call, the token caching, and the token refresh before expiry.

The direct IMDS call matters for:

**Non-SDK environments** 🔧: Shell scripts using `curl`, applications in languages without Azure SDK support, or scenarios where adding the Azure SDK is impractical.

**Debugging** 🐛: When token acquisition is failing and you need to verify that IMDS is returning a token before suspecting the application code or role assignments.

**Custom token handling** ⚙️: Applications that need to inspect token claims or handle multiple identities explicitly may call IMDS directly to control which identity and resource they're requesting.

## ⚠️ Container environments

In Azure Container Apps and AKS, IMDS-based token acquisition works but the access path differs slightly from VMs. Container workloads configured with workload identity (the AKS-native managed identity mechanism) use a different endpoint that the Azure Identity SDK handles transparently. The concept is the same; code requests a token without storing credentials, but the underlying endpoint isn't always raw IMDS.

---

💬 **Have you ever called IMDS directly to debug a managed identity token acquisition problem, or does your team rely entirely on SDK abstractions?** Knowing the raw IMDS call is useful when DefaultAzureCredential returns an error and you need to isolate whether the problem is in the identity configuration or in the application code. What was the last managed identity debugging scenario where dropping down to a direct IMDS call helped?
✍️ TedxHarry

<!-- nav -->

---

[← Federated Identity Credential](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-6-federated-identity-credential.md) | [🏠 Contents](/README) | [Principal ID →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-8-principal-id.md)
