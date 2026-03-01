# Conditional Access for Workloads
*Security Policies That Apply to Applications, Not Just People*

**Part of Entra ID Glossary Series: Glossary#10.12 - Conditional Access for Workloads**

---

A security team configured Conditional Access policies for every user sign-in scenario. MFA for all users. Device compliance for accessing sensitive data. Location-based restrictions for privileged roles. Months of policy design and testing.

Then someone pointed out that none of it applied to service principals.

The CI/CD pipeline authenticating with a service principal and calling Microsoft Graph. The data processing function authenticating with a managed identity and reading from Azure Storage. The vendor application authenticating from an unknown IP and accessing a SharePoint API. None of these were covered by user Conditional Access policies because Conditional Access policies for users don't apply to workload authentication.

Conditional Access for workloads is the answer.

## 🔐 What Conditional Access for Workloads Is

Conditional Access for workloads is a set of Conditional Access policy capabilities targeting workload identities: service principals and managed identities. It applies the same policy enforcement model to non-human identities that user-targeted Conditional Access applies to human identities.

Like user Conditional Access, workload CA policies follow the assignment/condition/control structure: which service principals the policy applies to, what conditions trigger it, and what the result is when conditions are met.

The key difference from user CA is what conditions are meaningful for workloads. Location (IP address range) is the primary condition for workload CA, because unlike users, workloads don't change locations, don't use devices in the traditional sense, and don't complete MFA challenges. The conditions available for workloads reflect this reality.

## 📍 Location as the Primary Condition

For user CA, location is one of several conditions: sign-in risk, user risk, device compliance, and authentication strength are all available. For workload CA, location is the primary enforceable condition because it's what makes sense for code.

A service principal used by an Azure Function App should authenticate from Azure datacenter IP ranges. If that service principal's credentials were stolen and are being used from a residential IP in another country, location-based workload CA can detect and block that.

A managed identity for a VM in a specific Azure region should authenticate from that region's IP range. A Conditional Access policy that requires workload authentications to come from expected IP ranges catches the scenario where a workload identity is used outside its expected compute environment.

This is the core security value: workload identities have predictable authentication patterns. Service principals don't roam like users do. A service principal authenticating from an unexpected location is a meaningful anomaly. Workload CA makes that anomaly enforceable.

## ⚙️ Policy Configuration

Workload CA policies are configured in the Conditional Access admin interface under the service principal assignment option. You can target:

**Specific service principals** 🎯: Name the exact service principal or managed identity the policy applies to. Useful for high-value service principals like those with broad Graph API permissions or privileged Azure RBAC roles.

**All service principals** 🌐: A catch-all policy that applies to every workload identity authentication. Useful for a baseline "must come from a known IP range" policy that applies to all service principals unless overridden by a more specific policy.

The condition is an IP-based named location. Define the expected IP ranges for your workloads: Azure datacenter ranges for Azure-hosted workloads, your corporate IP range for on-premises workloads, or specific CIDR ranges for known environments.

The control for workload CA is typically block access when conditions aren't met, since workloads can't complete interactive controls like MFA.

## 📊 Where Workload CA Adds Value

**High-privilege service principals** 🔑: Service principals with Microsoft Graph application permissions to read mail, access Teams data, or manage users are high-value targets. A workload CA policy that restricts their authentication to specific IP ranges limits the blast radius if credentials are compromised.

**Long-lived service principal credentials** 📋: Service principals with client secrets that aren't rotating frequently (a governance failure, but a common one) benefit from location-based restrictions that limit where those credentials can be used even if they're stolen.

**Third-party vendor integrations** 🏢: Service principals granted by external vendors should authenticate from those vendors' known IP ranges. A policy that blocks authentication from anywhere else limits what a vendor can do if their own systems are compromised.

## ⚠️ The Managed Identity Consideration

Managed identities present a nuance: they authenticate via IMDS from within Azure resources, and the source IP for IMDS-based token requests is internal to Azure's network. For managed identities, IP-based workload CA may not be practical because the authentication source IPs are Azure-internal rather than public.

Workload CA conditions for managed identities are an evolving area. The practical value today is primarily for service principals with explicit client credentials (secrets or certificates) that authenticate from predictable external or on-premises locations.

---

💬 **Does your organization have Conditional Access policies targeting service principals, or is your CA policy coverage limited to user identities?** The gap between user CA coverage and workload CA coverage is significant in most enterprise tenants. What would be the first service principal in your environment you'd want to put a location-based restriction on?
<!-- nav -->

---

[← LLTs (Long Lived Tokens)](glossary-10-11-llts.md) | [Home](../README.md) | [Authorization Code Flow →](../11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-1-authorization-code-flow.md)
