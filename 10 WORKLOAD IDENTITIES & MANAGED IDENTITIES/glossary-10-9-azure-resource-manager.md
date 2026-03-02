# Azure Resource Manager
*The Management Plane Where Managed Identity Permissions Live*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #10.9 - Azure Resource Manager

---

## 🎯 TL;DR

- Azure Resource Manager (ARM) is the management layer for all Azure resources : it authenticates every API call
- Managed identities get tokens scoped to ARM (`https://management.azure.com`) to manage Azure resources
- ARM RBAC controls what the managed identity can do: Contributor, Reader, custom roles


A developer gave their managed identity the right role in Entra ID. The application still couldn't read from the Storage account.

The problem: they assigned an Entra ID directory role, not an Azure RBAC role. Two different RBAC systems. Entra ID directory roles control what you can do inside Entra ID: manage users, manage applications, read the directory. Azure RBAC roles control what you can do with Azure resources: read blobs, write to Key Vault, manage virtual networks.

The role assignment that gives a managed identity access to a Storage account doesn't happen in Entra ID. It happens in Azure Resource Manager.

## 🏗️ What Azure resource manager is

Azure Resource Manager (ARM) is the management plane for all Azure resources. Every resource you create in Azure, every configuration change, every role assignment for Azure services, every ARM template deployment: all of it goes through ARM.

When you use the Azure portal to create a storage account, you're calling the ARM API. When you use Terraform to deploy infrastructure, Terraform calls the ARM API. When you assign a managed identity the Key Vault Secrets User role, that assignment lives in ARM, not in Entra ID.

ARM is the consistent API layer that sits between every Azure management tool (portal, CLI, PowerShell, Terraform, Bicep, REST) and every Azure service. It handles authentication, authorization, throttling, and routing to the underlying service-specific resource providers.

## 🔐 ARM RBAC vs entra ID roles

The two RBAC systems in the Microsoft ecosystem serve different scopes:

**Entra ID directory roles** 🔷: Control identity plane operations. Global Administrator, User Administrator, Application Administrator, Privileged Role Administrator, etc. These roles govern who can manage identities, applications, and policies within Entra ID itself. They have no authority over Azure resources.

**Azure RBAC (ARM roles)** 🔵: Control data plane and management plane operations on Azure resources. Owner, Contributor, Reader, Storage Blob Data Reader, Key Vault Secrets User, Virtual Machine Contributor, etc. These roles are assigned at subscription, resource group, or individual resource scope. They govern who can do what with Azure resources.

A managed identity needs Azure RBAC roles, assigned through ARM, to access Azure services. It doesn't need Entra ID directory roles unless it's performing identity administration operations (which is rare and usually inadvisable).

## 📊 The ARM hierarchy

ARM organizes Azure resources in a hierarchy, and RBAC assignments can be made at any level:

**Management Group** 🌐: At the top. Multiple subscriptions grouped together. Role assignments at this level apply across all subscriptions in the group.

**Subscription** 📋: A billing and access boundary. Role assignments at subscription scope apply to all resource groups and resources within the subscription.

**Resource Group** 📁: A logical container for related resources. Role assignments at resource group scope apply to all resources in the group.

**Individual Resource** 🔑: The most granular scope. Role assignment applies only to that specific resource (a single Key Vault, a single Storage account, a single Service Bus namespace).

For managed identity permissions, the principle of least privilege means assigning the role at the narrowest scope possible. A managed identity that only reads from one specific Key Vault should have Key Vault Secrets User assigned on that vault, not on the resource group or subscription.

## ⚙️ ARM in the managed identity flow

When a managed identity requests a token from IMDS, it specifies the resource URI for the Azure service it wants to access (for example, `https://vault.azure.net` for Key Vault). Entra ID issues a token for that resource. When the managed identity uses that token to call Key Vault, Key Vault validates the token and checks the ARM role assignments to determine whether this identity has the right permissions.

The complete chain:

1. Managed identity is enabled on the Azure resource.
2. ARM role assignment grants the managed identity a role on the target Azure service.
3. Application code calls IMDS to get a token.
4. Application uses the token to call the Azure service API.
5. The Azure service validates the token with Entra ID and checks the ARM role assignment.
6. Request succeeds or fails based on the role assigned.

Steps 1 and 2 are configuration. Steps 3-6 are runtime.

## 📋 ARM templates and managed identity

Infrastructure-as-code through ARM templates (or Bicep, which compiles to ARM) can define managed identities and their role assignments as part of the same deployment that creates the compute resource and the target service.

This is the pattern that makes managed identity consistent across environments: the same template that creates the Function App and the Key Vault also creates the user-assigned managed identity and the role assignment that connects them. No manual portal steps. No role assignments that exist in production but were forgotten in staging.

Role assignments in ARM templates look like nested resources or separate resource declarations with type `Microsoft.Authorization/roleAssignments`. Getting role assignment definitions into IaC alongside the compute resources they relate to is the main operational improvement that prevents the "role assignments created manually and never tracked" problem.

---

💬 **Does your team manage ARM role assignments for managed identities through infrastructure-as-code, or are they still applied manually through the portal?** The gap between "we use Terraform for everything" and "role assignments are done manually and undocumented" is common, especially for managed identity permissions that were configured during initial setup and never formalized. What would it take to get role assignments for workload identities into your IaC pipeline?
✍️ TedxHarry

<!-- nav -->

---

[← Principal ID](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-8-principal-id.md) | [🏠 Contents](/README) | [CAE for Workloads →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-10-cae-for-workloads.md)
