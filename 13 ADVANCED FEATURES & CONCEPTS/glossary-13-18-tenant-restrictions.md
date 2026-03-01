# Tenant Restrictions: Controlling Which Microsoft Tenants Your Users Can Access

**Part of Entra ID Glossary Series: Glossary#13.18 - Tenant Restrictions**

---

A data governance team discovered that several employees had been uploading files to their personal OneDrive accounts from work devices. The files included customer data that should never leave corporate systems.

The employees weren't trying to exfiltrate data maliciously. They were trying to work from home and found it easier to upload to personal OneDrive than to deal with VPN issues. The result was the same: corporate data in personal Microsoft accounts outside the organization's control.

The security team's question: how do you prevent users from authenticating to personal or non-corporate Microsoft tenants while still allowing them to access corporate Microsoft 365?

Tenant Restrictions is the answer.

## 🔒 What Tenant Restrictions Are

Tenant Restrictions is a feature that restricts which Entra ID tenants users can authenticate to from your network or managed devices. You define a list of allowed tenants. Authentication attempts to tenants not on that list are blocked.

A user on the corporate network can authenticate to `contoso.com` (corporate Entra ID tenant) but not to their personal `outlook.com` account or to a partner's tenant that isn't on the allow list. The authentication attempt to the blocked tenant fails before any data is accessed.

This prevents the most common data exfiltration scenario using Microsoft's own services: logging into a personal OneDrive, personal Teams, or any other Microsoft 365 application using personal or unauthorized corporate accounts.

## 🔧 Tenant Restrictions v1: Proxy-Based Enforcement

The original Tenant Restrictions implementation (v1) works by injecting HTTP headers into traffic to Microsoft's authentication endpoints. Organizations route Microsoft authentication traffic through a corporate proxy that adds a header specifying allowed tenants:

```
Restrict-Access-To-Tenants: contoso.com, partner.com
Restrict-Access-Context: {tenant-id}
```

Microsoft's login endpoint reads these headers and rejects authentication attempts to tenants not on the allowed list.

This approach requires routing authentication traffic through a controlled proxy. It works for corporate networks and managed devices configured to use the proxy. It doesn't work for unmanaged devices or networks not routing through the proxy.

## 🌐 Tenant Restrictions v2: Identity-Based Enforcement

Tenant Restrictions v2 shifts enforcement from the network layer to the identity layer, using the Global Secure Access client or specific token claims. This approach:

**Works without network-level proxy** 💻: Enforcement happens through the client or through signals in the authentication request rather than requiring traffic routing through a corporate proxy.

**Supports per-application granularity** 🎯: Instead of an all-or-nothing allow list, v2 supports more granular policies specifying which users can access which tenants for which applications.

**Integrates with Conditional Access** 🔐: The Compliant Network condition in Conditional Access can require that Microsoft 365 access flows through the Global Secure Access client, which enforces Tenant Restrictions policies even for remote users not on the corporate network.

## 📊 What Tenant Restrictions Controls

Tenant Restrictions applies to authentication at Microsoft's identity endpoints. It controls:

**Personal Microsoft accounts** 🚫: Users can't authenticate to personal Outlook.com, Hotmail, or Live.com accounts from the corporate network or managed devices.

**Consumer-facing Microsoft services** 🚫: Services like personal OneDrive, consumer Teams, Xbox Live services that use personal Microsoft accounts.

**External organizational tenants** 🔒: By specifying only corporate tenants in the allow list, authentication to competitor tenants, unknown external tenants, or shadow IT tenants from other organizations is blocked.

## ⚠️ What Tenant Restrictions Doesn't Control

Tenant Restrictions stops authentication to blocked tenants. It doesn't:

**Control data within allowed tenants** 📁: Once authenticated to an allowed tenant, Conditional Access and DLP policies within that tenant control what the user can do. Tenant Restrictions only controls which tenants the user can reach.

**Prevent all data movement** 🔄: Users could still email data to external recipients or use non-Microsoft cloud storage services. Tenant Restrictions specifically addresses the Microsoft identity and services vector.

**Control web browsing** 🌐: Tenant Restrictions doesn't restrict general web access, only authentication to Microsoft's identity platform.

The complementary controls for complete data governance: DLP policies in Microsoft Purview for data classification and movement controls, and network-level filtering for non-Microsoft services.

---

💬 **Has your organization implemented Tenant Restrictions to control which Microsoft tenants corporate devices and networks can authenticate to, and what data governance requirement drove the decision?** The personal OneDrive data leakage scenario is the most common driver. Organizations in regulated industries often implement Tenant Restrictions as part of broader DLP programs. What's the biggest gap in your current control set for preventing data movement through Microsoft services?

#EntraID #TenantRestrictions #DataGovernance #DLP #ZeroTrust #MicrosoftEntra #CloudSecurity
<!-- nav -->

---

[← Cross-Tenant Access: Controlling How Your Tenant Interacts With Other Entra ID Tenants](glossary-13-17-cross-tenant-access.md) | [Home](../README.md) | [CA Optimization Agent: Automated Recommendations for Conditional Access Policy Gaps →](glossary-13-19-ca-optimization-agent.md)
