# CAE for Workloads
*Real-Time Token Revocation for Non-Human Identities*

**Part of Entra ID Glossary Series: Glossary#10.10 - CAE for Workloads**

---

A service principal had its permissions revoked at 9:47 AM. The security team revoked them because the associated application had a critical vulnerability disclosed that morning.

At 10:43 AM, the service principal was still calling the Azure Storage API successfully. The access token it had acquired at 9:30 AM was valid for one hour. Revoking the service principal's permissions in Entra ID doesn't immediately invalidate tokens already issued. It just prevents new ones from being issued after the old ones expire.

For workloads running continuously and holding access tokens, the gap between "permission revoked" and "access actually stops" can be significant. Continuous Access Evaluation for workloads is the mechanism that closes that gap.

## ⚡ What CAE for Workloads Is

Continuous Access Evaluation for workloads applies the same near-real-time enforcement model to workload identities (service principals, managed identities) that CAE applies to user sign-ins.

CAE works by establishing a protocol between the authorization server (Entra ID) and resource providers (Azure Storage, Microsoft Graph, and other CAE-capable services). When a policy change affecting a workload identity occurs, Entra ID notifies participating resource providers. Those providers then reject the existing token and require the workload to acquire a new one.

The workload's existing access token gets rejected in near-real-time by the resource. The workload tries to get a new token. If the policy change was a revocation, the new token request fails. Access stops.

## 🔄 The Difference from User CAE

CAE for user identities responds to events like: user account disabled, password changed, user risk elevated, session policy updated. When these events occur during a user session, the resource provider rejects the token and forces re-authentication.

CAE for workloads responds to events specific to workload identity states: service principal disabled, service principal's credentials revoked, Conditional Access policy applied to the service principal now blocks access, service principal added to a block policy.

The revocation scenarios are different because the triggering events are different. A user might be blocked because they were terminated. A workload might be blocked because the application it belongs to was compromised, its secret was leaked, or a policy change restricts the IP ranges it can authenticate from.

## 🔑 The Long-Lived Token Connection

CAE for workloads is what makes long-lived tokens (LLTs) viable. Without CAE, workload tokens are kept short-lived (one hour) because there's no reliable way to revoke them before expiry. A shorter lifetime limits the window of risk if a token is compromised or permissions need to be revoked.

With CAE, workload tokens can be issued with longer lifetimes (up to 24 hours) because the resource provider can reject them in near-real-time if a relevant policy event occurs. The longer lifetime reduces the authentication overhead for workloads that make frequent calls. Instead of re-authenticating every hour, a workload authenticates once and uses the token for its full valid period, unless revocation occurs.

This is the tradeoff: longer token lifetimes are safer when coupled with CAE than shorter lifetimes without it, because CAE provides a reliable enforcement mechanism that doesn't depend on token expiry.

## ⚙️ How Resource Providers Enforce It

CAE-capable resource providers validate tokens differently from standard token validation. In addition to standard signature verification, expiry check, and audience validation, they also check the current state of the service principal against Entra ID's signals.

When a workload presents a token, the resource provider can verify that no revocation events have occurred for that service principal since the token was issued. If a relevant event has occurred, the provider rejects the token with a specific response code that tells the workload client to get a new token.

The Azure SDKs handle this transparently. When a resource returns a CAE rejection response, `DefaultAzureCredential` and other Azure SDK credential implementations automatically trigger a new token acquisition attempt.

## 📊 Which Services Support It

CAE for workloads is supported by CAE-capable resource providers including Microsoft Graph, Azure Resource Manager, and key Azure data plane services. The specific set of supporting services continues to expand.

Workload access to services that don't support CAE falls back to standard token lifetime enforcement. For those services, shorter token lifetimes remain the primary revocation mechanism.

## ⚠️ Operational Implication

The practical implication for security teams: for services that support CAE, revoking a workload identity's access in Entra ID takes effect faster than the token's remaining lifetime. For services without CAE support, the token remains valid until it expires.

Knowing which Azure services support CAE matters when designing incident response procedures for compromised workload identities.

---

💬 **Has your team ever had to respond to a compromised service principal, and how long did it take before the service principal's access actually stopped?** The gap between "we revoked the permissions" and "access actually stopped" is a real operational problem in incident response. CAE for workloads is meant to close that gap. Has it changed how your team thinks about workload identity incident response timelines?
<!-- nav -->

---

[← Azure Resource Manager](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-9-azure-resource-manager.md) | [🏠 Contents](/README) | [LLTs (Long Lived Tokens) →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-11-llts.md)
