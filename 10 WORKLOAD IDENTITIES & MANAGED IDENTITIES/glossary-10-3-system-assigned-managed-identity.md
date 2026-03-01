# System-Assigned Managed Identity
*One Resource, One Identity, One Lifecycle*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#10.3 - System-Assigned Managed Identity**

---

## 🎯 TL;DR

- System-assigned managed identity is created with and deleted with the Azure resource it's attached to
- One system-assigned identity per resource — can't be shared or reused across resources
- Best for: VMs, App Services, Functions that need their own distinct identity


Enabling managed identity on an Azure VM takes about ten seconds in the portal. A toggle. You enable it, Azure creates an identity in Entra ID with the same name as the VM, and that identity exists for exactly as long as the VM exists.

When the VM is deleted, the identity is deleted.

That's the whole model of system-assigned managed identity. The resource owns the identity. The identity lives and dies with the resource. One-to-one, no shared references, no orphaned identities in Entra ID after the resource is gone.

## 🔗 What System-Assigned Means

A system-assigned managed identity is created by Azure when you enable managed identity on a specific Azure resource, and it's tied exclusively to that resource's lifecycle. One identity per resource, inseparable from that resource.

The identity appears in Entra ID as an enterprise application (service principal) with the same name as the Azure resource that owns it. You'll find it listed in Entra ID under Enterprise Applications with an application type of "Managed Identity." You can't create it independently; you enable it on a resource, and Azure creates it.

This contrasts with user-assigned managed identities, which are standalone Azure resources you create separately and then attach to one or more compute resources.

## ⚙️ How It Works in Practice

An Azure Function App needs to read blobs from an Azure Storage account. The steps:

1. Enable system-assigned managed identity on the Function App. Azure creates the service principal in Entra ID.
2. In the Storage account's IAM settings, assign the Storage Blob Data Reader role to the Function App's managed identity (referenced by its object ID, the Principal ID).
3. In the Function App code, use `DefaultAzureCredential` to acquire a token for Azure Storage. No connection string. No account key. The IMDS endpoint handles token acquisition.

When the Function App is deleted months later, Azure automatically removes the service principal from Entra ID. The role assignment on the Storage account becomes an orphaned assignment referencing a deleted principal, which Azure cleans up automatically.

No identity cleanup task. No Entra ID service principal persisting after the resource is gone. The lifecycle management happens automatically.

## ✅ When System-Assigned Is the Right Choice

System-assigned managed identity fits well when:

**Single-resource use** 🎯: The identity is used only by one resource and there's no reason for multiple resources to share the same identity. A web application that only needs to reach its own Key Vault is a natural fit.

**Automatic cleanup matters** 🧹: Environments where resource turnover is frequent (dev/test environments, short-lived containers, frequently replaced VMs) benefit from automatic identity cleanup. You don't need to track and remove identities manually as resources come and go.

**Simple scenarios** 📋: When the resource has straightforward, non-shared access needs and the one-to-one relationship between resource and identity is a feature rather than a limitation.

## ⚠️ The Limitations

System-assigned managed identity has real constraints that matter at scale:

**No sharing across resources** 🔄: Each resource gets its own identity. If 20 Azure Functions all need the same Key Vault access, that means 20 separate role assignments on the Key Vault. With user-assigned managed identity, it would be one identity and one role assignment shared across all 20 Functions.

**Role assignments lost on deletion** 🗑️: When a resource is deleted, the identity is deleted, and the role assignments it held are gone. If you recreate the resource (a new VM with the same name, for example), it gets a new identity with a new Principal ID. You have to redo every role assignment. This trips up teams that regularly replace VMs or redeploy resources.

**Not shareable with external systems** 🔗: System-assigned managed identities can't be used with workload federation configurations the way user-assigned managed identities can. Federated identity credentials for GitHub Actions or Kubernetes, for example, work with user-assigned managed identities or app registrations.

## 📊 At What Point to Switch to User-Assigned

The inflection point is usually one of these:

Multiple resources need the same access. When you're copying the same role assignment to more than two or three resources, user-assigned becomes more maintainable.

Resources have short lifecycles. When VMs or containers are regularly replaced and recreating role assignments becomes operational overhead, a shared user-assigned identity is more practical.

The identity needs to persist across resource replacements. If the same logical "application identity" needs to survive infrastructure changes, user-assigned decouples the identity from any single resource's lifecycle.

---

💬 **When did you first switch from system-assigned to user-assigned managed identity for a workload, and what drove the decision?** The transition usually happens when the one-to-one model creates operational friction, either through role assignment duplication or through losing assignments when resources are replaced. What scenario made user-assigned the better fit?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Managed Identity](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-2-managed-identity.md) | [🏠 Contents](/README) | [User-Assigned Managed Identity →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-4-user-assigned-managed-identity.md)
