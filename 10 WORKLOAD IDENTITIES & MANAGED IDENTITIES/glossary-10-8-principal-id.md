# Principal ID: The Identifier You Use When Giving a Managed Identity Permission

**Part of Entra ID Glossary Series: Glossary#10.8 - Principal ID**

---

A developer enabled a managed identity on an App Service and then went to assign it the Key Vault Secrets User role on a Key Vault. In the role assignment dialog, under "Select members," they searched for the App Service name.

Nothing came up.

They tried variations of the name. Still nothing. The App Service was there, running, with managed identity enabled. Why couldn't they find it?

The role assignment UI searches Entra ID users, groups, service principals, and managed identities. The managed identity was created, but you have to know how to find it. The identifier that ties everything together is the Principal ID.

## 🔑 What Principal ID Is

The Principal ID is the object ID of the service principal that represents a managed identity in Entra ID. It's a GUID, and it's the identifier used when assigning RBAC roles to a managed identity.

When Azure creates a managed identity (system-assigned or user-assigned), two things happen in parallel:

In the Azure resource layer: the managed identity is configured on the Azure resource (or created as a standalone resource for user-assigned). It has a resource ID, a name, and a `clientId` (also called the application ID).

In Entra ID: a service principal is created to represent that managed identity. This service principal has an object ID. That object ID is the Principal ID.

RBAC role assignments in Azure are made against object IDs of principals in Entra ID. Users have object IDs. Groups have object IDs. Service principals have object IDs. The Principal ID of a managed identity is the service principal's object ID, which is what RBAC uses.

## 📋 Principal ID vs Client ID

Managed identities have two identifiers that serve different purposes and are commonly confused:

**Principal ID (Object ID)** 🔷: The object ID of the service principal in Entra ID. Used for RBAC role assignments. This is what you put in the "Select members" field when assigning a role. It's in the GUID format Entra ID uses for all object IDs.

**Client ID (Application ID)** 🔵: The application ID of the managed identity, also a GUID but a different one. Used by application code when explicitly specifying which managed identity to use for token acquisition. When a resource has multiple managed identities assigned, the `client_id` parameter in IMDS requests tells Azure which identity to get a token for.

Same managed identity, two different GUIDs, two different use cases. Using the Client ID where the Principal ID is expected (or vice versa) is a common source of confusion when first working with managed identities.

## 🔍 Where to Find the Principal ID

**For system-assigned managed identities** 💻: In the Azure portal, go to the resource (VM, App Service, Function App, etc.), then Identity in the left menu. The system-assigned tab shows the Object ID, which is the Principal ID. This is only visible after managed identity is enabled.

**For user-assigned managed identities** 🔷: Go to the managed identity resource directly in the portal. The Overview page shows the Object ID (Principal ID) and the Client ID.

**Via Azure CLI**:
```
# For user-assigned managed identity
az identity show --name my-identity --resource-group my-rg --query principalId

# For system-assigned managed identity on a resource
az webapp identity show --name my-app --resource-group my-rg --query principalId
```

The CLI output explicitly calls it `principalId`. The portal calls it Object ID. They're the same value.

## ⚙️ Using Principal ID in Role Assignments

Once you have the Principal ID, assigning a role looks like this in the portal: navigate to the target resource (Key Vault, Storage account, etc.), go to Access Control (IAM), then Add role assignment. Choose the role, then in the Members tab, select "Managed identity" as the member type. Search by the managed identity name, or enter the Principal ID directly.

Via CLI:
```
az role assignment create \
  --role "Key Vault Secrets User" \
  --assignee-object-id <principal-id> \
  --assignee-principal-type ServicePrincipal \
  --scope /subscriptions/.../resourceGroups/.../providers/Microsoft.KeyVault/vaults/my-vault
```

The `--assignee-principal-type ServicePrincipal` flag is important. Without it, the CLI may try to look up the principal type and fail for managed identities, especially in automation contexts without full Entra ID read permissions.

## ⚠️ System-Assigned Identity Lifecycle Implication

For system-assigned managed identities, the Principal ID changes when the resource is deleted and recreated. A new resource, even with the same name, gets a new system-assigned managed identity with a new Principal ID. All role assignments referencing the old Principal ID are orphaned and must be recreated.

This is a real operational issue for teams that regularly rebuild resources (testing environments, blue/green deployments). User-assigned managed identities avoid this problem because the Principal ID persists as long as the managed identity resource exists, independently of any compute resources it's assigned to.

---

💬 **What's your team's approach to tracking managed identity Principal IDs and their associated role assignments?** The role assignment audit trail is straightforward in the Azure portal, but at scale, knowing which managed identities have which permissions across which resources requires deliberate tracking. Do you use Terraform state, ARM templates, or another mechanism to maintain that mapping?
<!-- nav -->

---

[← Instance Metadata Service: The Local Endpoint That Gives Azure Resources Their Identity](glossary-10-7-imds.md) | [Home](../README.md) | [Azure Resource Manager: The Management Plane Where Managed Identity Permissions Live →](glossary-10-9-azure-resource-manager.md)
