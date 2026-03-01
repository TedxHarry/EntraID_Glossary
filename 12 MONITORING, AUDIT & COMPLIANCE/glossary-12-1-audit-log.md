# Audit Log: The Record of Every Identity Operation in Your Tenant

**Part of Entra ID Glossary Series: Glossary#12.1 - Audit Log**

---

A Security Operations team got a ticket: a user's account had been granted Global Administrator two weeks ago, and nobody could explain who authorized it. The change had been made. The role was assigned. But there was no change management ticket, no approval record, no memory of the decision.

The audit log had the answer. Who made the change. When. From which IP address. Which service principal or admin account performed the operation. Whether it was done through the portal, PowerShell, or the Graph API. All of it, timestamped and immutable.

The problem wasn't finding the information. The problem was that nobody had looked at it until two weeks after the fact. The audit log had the answer the whole time.

## 📋 What Entra ID Audit Logs Capture

The Entra ID audit log is a record of administrative and management operations in the tenant. Every time something in the identity plane changes, an audit event is written.

Operations captured include:

**User management** 👤: User created, user deleted, user updated (attribute changes, license assignments), password reset, account enabled or disabled, MFA registration changes.

**Group management** 👥: Group created, deleted, membership added or removed, group type changed.

**Application management** 📱: App registration created or deleted, service principal created, application permissions granted or revoked, consent granted or removed, client secrets added or removed.

**Role management** 🔑: Directory role assigned or removed, PIM role activation, PIM role assignment added or removed, custom role created.

**Policy management** 🔐: Conditional Access policy created, updated, enabled, disabled, or deleted. Authentication methods policy changes. Token lifetime policy changes.

**Governance operations** 📋: Access review started or completed, entitlement management access package created or assigned, lifecycle workflow triggered.

Each audit event includes: the date and time, the actor (who or what performed the operation), the target (which object was modified), the operation name, and the result (success or failure).

## ⏰ Retention and Export

Audit log retention in Entra ID depends on the license tier:

**Microsoft Entra ID Free and M365 Basic**: 7 days
**Microsoft Entra ID P1 or P2**: 30 days

For most compliance requirements, 30 days of built-in retention isn't enough. HIPAA, SOX, and ISO 27001 audit requirements typically require a year or more of logs.

The solution is exporting to a durable store via Diagnostic Settings:

**Log Analytics workspace** 📊: Interactive querying with KQL, integration with Microsoft Sentinel for correlation and alerting. Retention configurable up to 2 years (longer with archive tiers).

**Azure Storage account** 📦: Immutable storage for long-term retention. Cheap per GB. Not interactive; requires separate tooling to query. Good for compliance archive requirements.

**Azure Event Hub** 🔄: Streaming export to SIEM systems (Splunk, QRadar, Elastic) or custom processing pipelines. Near-real-time.

Export to Log Analytics is the most operationally useful for teams that want to query, alert on, and correlate audit events with other security data.

## 🔍 Useful Audit Queries

In Log Analytics (with the Entra ID audit logs exported), KQL enables powerful queries:

Finding all role assignments in the past 7 days:
```kql
AuditLogs
| where TimeGenerated > ago(7d)
| where OperationName == "Add member to role"
| project TimeGenerated, InitiatedBy, TargetResources
```

Finding all Global Administrator activations (PIM):
```kql
AuditLogs
| where OperationName == "Add member to role"
| where TargetResources[0].modifiedProperties has "Global Administrator"
```

Finding all application consent grants:
```kql
AuditLogs
| where OperationName == "Consent to application"
| project TimeGenerated, InitiatedBy, TargetResources
```

## ⚠️ What Audit Logs Don't Capture

Audit logs cover the identity plane (identity administration operations). They don't cover:

**Sign-in events** 🔐: Who signed in when is the sign-in log, not the audit log. Two separate log streams.

**Data access** 📁: What data a user accessed after authenticating is in the application's own logs or Microsoft Purview audit, not the Entra ID audit log. The audit log shows the role assignment; it doesn't show what the user did with that role.

**Resource operations** ☁️: Azure resource management operations are in the Azure Activity Log, not Entra ID audit. Deleting a VM shows up in Activity Log; assigning a managed identity to a VM shows up in Audit Log.

---

💬 **How far back can your organization query Entra ID audit logs today, and is that sufficient for your compliance requirements?** The gap between "we have 30 days of built-in audit logs" and "our compliance requirement is 12 months" is common and fixable with diagnostic settings export. Has your organization set up long-term audit log retention, and what drove the decision to do it (or not)?
<!-- nav -->

---

[← Scope: Defining and Validating What Applications Are Allowed to Do With Your API](../11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-12-scope-deep-dive.md) | [Home](../README.md) | [Sign-In Log: The Authentication Record Your Security Team Needs to Know Cold →](glossary-12-2-sign-in-log.md)
