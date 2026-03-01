# Attribute-Based Access Control (ABAC)
*Access Decisions That Go Beyond Role Membership*

**Part of Entra ID Glossary Series: Glossary#13.1 - Attribute-Based Access Control (ABAC)**

---

A financial services company had a data governance problem. Analysts in the Research department needed access to financial models. But not all financial models: only the ones tagged as belonging to their division, and only when those models were classified as internal or lower. Confidential-rated documents required a separate approval.

With pure RBAC, the options were: one broad role with access to everything, or dozens of narrow roles for every combination of division and classification. Neither was practical.

ABAC solved it with one role and conditions: "Storage Blob Data Reader for blobs where the blob's division tag matches the user's division attribute AND the classification tag is not Confidential."

One role. Dynamic access based on attributes. No role proliferation.

## 🏗️ What ABAC Is

Attribute-Based Access Control is an authorization model where access decisions are made based on attributes: characteristics of the user, the resource being accessed, and the environment or context of the request. Rather than asking "does this user have the right role?", ABAC asks "do this user's attributes, this resource's attributes, and this context satisfy the access policy?"

RBAC says: "Members of the Finance Analyst role can read blobs in this storage account."
ABAC says: "Members of the Finance Analyst role can read blobs in this storage account where the blob's department tag matches the user's department attribute."

The same role covers many users, but what each user can access is filtered by their individual attributes and the attributes of the specific resources they're requesting.

## ⚙️ ABAC in Azure and Entra ID

Microsoft has introduced ABAC capabilities in two areas:

**Azure RBAC with conditions** 🔷: Role assignment conditions on Azure Storage that restrict which blobs a role grants access to based on blob index tags and request attributes. The Storage Blob Data Reader role with a condition that limits access to blobs where a specific tag matches a specific value. This is Azure RBAC + conditions, available in Azure Portal when assigning storage roles.

Example condition: grant read access only to blobs where the tag `Project` equals `Alpha`. Users with this role assignment can only read blobs tagged with that specific project. Other blobs in the same container are inaccessible to them despite having the role.

**Custom security attributes** 🔵: Entra ID supports custom security attributes on user objects and service principal objects. These are organization-defined attributes (like `ClearanceLevel`, `Division`, `ProjectAccess`) that can hold values and be used in access policies and attribute conditions. They're separate from standard directory attributes and are restricted by who can read and write them.

Custom security attributes allow organizations to extend Entra ID's user object with identity attributes that drive attribute-based access decisions in connected applications or in Azure RBAC conditions.

## 📊 When ABAC Beats RBAC

The practical trigger for ABAC is role proliferation: when managing access requires creating an unsustainable number of roles to handle attribute-based distinctions.

**Data segmentation** 📁: Multi-tenant SaaS platforms where different customers' data must be isolated within the same storage infrastructure. ABAC with customer-specific tags on blobs allows one storage access role with conditions per customer, rather than separate role assignments for every customer's data partition.

**Classification-based access** 🔐: Document and data classification systems where access depends on both role and classification level. ABAC conditions can enforce "this role can access documents classified at Internal or lower" without separate roles for each classification level.

**Dynamic team membership** 👥: Project-based access where users should be able to access resources tagged with their current project assignments. As project assignments change (via HR system updates to user attributes), access adjusts without manual role reassignment.

## 🔧 Attribute Sets for Custom Security Attributes

Custom security attributes in Entra ID are organized into attribute sets, which are logical groupings of related attributes. An organization might have an attribute set called `SecurityClearance` with attributes like `Level`, `ExpiryDate`, and `GrantingAuthority`.

Attribute sets have their own permission model. Not every Entra ID administrator can read or write custom security attributes: reading requires the Attribute Assignment Reader role, writing requires the Attribute Assignment Administrator role. This separation ensures sensitive attributes (clearance levels, access authorizations) aren't visible to general user administrators.

## ⚠️ The Operational Reality

ABAC requires more planning than RBAC because the conditions and attributes must be consistently maintained. An attribute-based condition is only as reliable as the attribute values it depends on.

If user department attributes in Entra ID aren't kept in sync with the HR system, users end up in the wrong ABAC bucket. If resource tags aren't applied consistently when new resources are created, some resources fall through the conditions. The access model is more powerful, but the data quality requirements are higher.

---

💬 **Has your organization hit the point where RBAC role proliferation is a management problem, and have you evaluated ABAC conditions as a solution?** The tipping point is usually when managing access requires creating more roles than teams can reasonably administer. What data segmentation or classification requirement is driving the most role proliferation in your environment?
<!-- nav -->

---

[← Compliance](../12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-5-compliance.md) | [Home](../README.md) | [Cloud-Based Sync (Advanced) →](glossary-13-2-cloud-sync-advanced.md)
