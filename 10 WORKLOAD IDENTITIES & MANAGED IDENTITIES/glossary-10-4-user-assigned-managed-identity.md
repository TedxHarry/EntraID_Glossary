# User-Assigned Managed Identity: One Identity Shared Across Many Resources

**Part of Entra ID Glossary Series: Glossary#10.4 - User-Assigned Managed Identity**

---

A platform team was building a shared logging service. Fourteen microservices, all deployed as separate Azure Container Apps, all needed to write to the same Azure Storage account and the same Log Analytics workspace.

The first instinct was system-assigned managed identity on each Container App. That meant 14 identities in Entra ID and 28 role assignments across the two Azure services.

When they rebuilt the staging environment two weeks later with fresh deployments, all 14 system-assigned identities were deleted. New identities, new Principal IDs, and all 28 role assignments had to be recreated from scratch.

The second time they set it up, they used one user-assigned managed identity. Fourteen Container Apps, one identity, two role assignments. Rebuilding the environment didn't touch the identity or its role assignments. The role assignments just worked with the new deployments because the identity hadn't changed.

## 🔷 What User-Assigned Managed Identity Is

A user-assigned managed identity is a standalone Azure resource that exists independently of any compute resource. You create it directly as its own resource, assign it to one or more Azure resources (VMs, Function Apps, Container Apps, App Service, etc.), and it persists regardless of what happens to those resources.

The identity has its own lifecycle in Entra ID, separate from anything it's assigned to. Delete the Container App: the identity remains. Replace the VM: the identity remains. The role assignments the identity holds continue to exist, and the next resource assigned that identity inherits those permissions immediately.

It appears in Entra ID as a service principal, just like a system-assigned managed identity. The difference is in its origin and lifecycle. It was created independently, and it lives independently.

## ⚙️ How to Create and Use One

Creating a user-assigned managed identity is an ARM resource creation, not a toggle on an existing resource:

```
az identity create --name my-shared-identity --resource-group my-rg
```

This creates the identity and outputs its `clientId`, `principalId`, and resource ID. The `principalId` is used for role assignments. The `clientId` is used when code explicitly specifies which identity to use for token acquisition (relevant when a resource has multiple identities assigned).

Assigning it to a resource:

```
az webapp identity assign --name my-app --resource-group my-rg --identities /subscriptions/.../my-shared-identity
```

The resource can now use that identity for token acquisition. If the resource also has a system-assigned managed identity, both are available, and code must specify which one to use by providing the `clientId`.

## ✅ When User-Assigned Is the Right Choice

**Multiple resources, shared access** 🔄: When more than a couple of resources need the same permissions, sharing a user-assigned identity is far more maintainable than individual role assignments per resource. One role assignment, any number of resources using it.

**Resources with short or unpredictable lifecycles** 🔁: Container-based workloads, frequently replaced VMs, blue/green deployment environments. The identity persists across resource replacements, so role assignments survive infrastructure changes.

**Workload federation** 🔗: User-assigned managed identities support federated identity credentials for keyless authentication from external systems like GitHub Actions. System-assigned managed identities don't support federated credentials.

**Shared application identity** 🎯: When multiple services represent a single logical application with a consistent identity, user-assigned lets you express that: one identity that represents "the billing service" regardless of how many instances or deployments implement it.

## ⚠️ What to Watch Out For

**Lifecycle management is now your job** 🗑️: The automatic cleanup advantage of system-assigned is gone. User-assigned identities don't delete themselves when unused. If you build a feature, create a user-assigned identity for it, and then retire the feature, the identity stays until someone explicitly deletes it. Building a governance process to track and remove unused user-assigned managed identities is necessary at scale.

**Over-permissioned shared identities** 🔐: The convenience of sharing an identity can slide into over-permissioning. One identity for "all the microservices" starts accumulating permissions as each microservice adds what it needs. Six months later, the shared identity has access to twelve Azure services and nobody's sure which service needs which permission. Shared identities need clear ownership and periodic permission reviews.

**Multi-identity resources need explicit selection** 💻: A resource with both a system-assigned and one or more user-assigned identities requires code to specify which identity to use. Relying on defaults with multiple identities assigned leads to unpredictable token acquisition behavior.

## 📊 The Practical Pattern

Most teams end up with a mix. System-assigned for simple, single-resource workloads where automatic cleanup is valuable. User-assigned for shared infrastructure, stable application identities, and workloads with short compute lifecycles.

The choice isn't permanent. Starting with system-assigned and migrating to user-assigned when operational friction appears is a reasonable progression.

---

💬 **Does your team have a standard for when to use system-assigned versus user-assigned managed identity, or is it decided case by case?** Having an explicit policy saves the debate each time a new workload is built. What criteria does your team use to make the call?

#EntraID #ManagedIdentity #UserAssignedManagedIdentity #WorkloadIdentity #AzureSecurity #MicrosoftEntra #CloudSecurity
<!-- nav -->

---

[← System-Assigned Managed Identity: One Resource, One Identity, One Lifecycle](glossary-10-3-system-assigned-managed-identity.md) | [Home](../README.md) | [Workload Federation: Authenticating to Azure Without Storing Azure Credentials →](glossary-10-5-workload-federation.md)
