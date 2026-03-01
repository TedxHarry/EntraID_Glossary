# Cloud Sync
*The Lighter Path to Hybrid Identity*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#8.3 - Cloud Sync**

---

## 🎯 TL;DR

- Entra Cloud Sync is the lightweight agent-based sync engine — no dedicated sync server required
- It's installed as a small agent on AD domain controllers or member servers
- Cloud Sync supports multi-forest and is the recommended approach for new hybrid deployments


A mid-size organization was running Entra Connect on a dedicated Windows Server. The server needed patching, updates, and occasional troubleshooting. Every time Entra Connect released a new version, someone had to schedule maintenance to upgrade it. The sync infrastructure itself had become a thing to manage.

When they evaluated Cloud Sync for a new subsidiary that was joining the Microsoft 365 environment, the difference was immediate. The Cloud Sync agent installed in 20 minutes. The synchronization logic ran in the cloud. Updates to the sync agent happened automatically. The subsidiary's users were syncing within an hour of starting.

The dedicated sync server wasn't needed. The maintenance overhead wasn't there.

## ☁️ What Cloud Sync Is

Microsoft Entra Cloud Sync is a synchronization service that connects on-premises Active Directory to Entra ID, with the synchronization logic running in the Microsoft cloud rather than entirely on an on-premises server.

Where Entra Connect runs a full synchronization engine locally (connector spaces, metaverse, sync rules engine), Cloud Sync uses a lightweight on-premises agent that connects to Entra ID and delegates the processing to the cloud.

The agent's job is to:
- Establish a secure outbound connection to Entra ID
- Read directory changes from on-premises AD
- Pass those changes to the cloud-hosted sync engine
- Apply any writebacks from cloud to on-premises (like password writeback)

The sync engine, configuration UI, and rules processing all live in Entra ID. The on-premises footprint is minimal.

## ⚖️ Cloud Sync vs Entra Connect: The Comparison

Both tools synchronize the same core objects (users, groups, contacts) and both support Password Hash Sync. The differences matter for choosing which to use:

**Deployment simplicity** 🚀: Cloud Sync wins. A lightweight agent, no SQL dependency, auto-updating, manageable from the cloud portal. Entra Connect requires a Windows Server with more substantial resource requirements and manual version management.

**Multi-forest support** 🌳: Cloud Sync supports synchronizing multiple disconnected AD forests to a single Entra ID tenant. This is a significant capability that previously required Entra Connect with complex configuration. Each forest gets its own agent.

**Feature completeness** ⚙️: Entra Connect currently has a broader feature set. Device writeback (for Hybrid Entra Join via sync), Pass-Through Authentication hosting, certain advanced sync rule customizations, and some niche synchronization scenarios are supported only in Entra Connect.

**High availability** 🔄: Cloud Sync natively supports multiple agents for the same domain. If one agent goes down, others continue syncing. Entra Connect requires a separate staging server configuration for equivalent resilience.

**Attribute customization** 🔧: Entra Connect's sync rules engine allows deep customization of attribute flows and transformations. Cloud Sync's attribute mapping is simpler and doesn't support all the same transformation scenarios.

## 📋 When to Choose Cloud Sync

**New deployments with straightforward requirements**: If you're setting up hybrid sync for the first time and you don't need the advanced features unique to Entra Connect, Cloud Sync is the recommended path.

**Multiple disconnected forests**: Cloud Sync's native multi-forest support and per-forest agents make this scenario more manageable than the equivalent Entra Connect configuration.

**Operational simplicity priority**: Organizations that want to minimize on-premises infrastructure management and prefer cloud-managed updates favor Cloud Sync.

**Existing Entra Connect environments**: Microsoft supports running both Cloud Sync and Entra Connect in the same tenant for different OUs or domains. Organizations can use Cloud Sync for new entities while keeping Entra Connect running for existing synchronized OUs.

## ⚙️ The Agent Architecture

Cloud Sync agents are lightweight Windows services. Multiple agents can be deployed for the same AD domain to provide redundancy. The agents communicate outbound to Entra ID over HTTPS on port 443. No inbound firewall rules are required, and no open ports need to be exposed to the internet.

Agent configuration and sync rules are managed entirely in the Entra admin center. The agent downloads its configuration from the cloud, reads AD changes, and sends them to the cloud. Updates to the agent are pushed automatically when Microsoft releases new versions.

## ⚠️ What Cloud Sync Doesn't Do Yet

The feature gap between Cloud Sync and Entra Connect has narrowed with each release. Check current documentation for the current state. Common limitations at time of writing:

**Hybrid Entra Join device writeback**: Device objects from Entra ID can't be written back to on-premises AD via Cloud Sync. Organizations that need Hybrid Entra Join for computer objects still need Entra Connect for that specific scenario.

**Pass-Through Authentication hosting**: PTA requires Entra Connect agents. Cloud Sync doesn't host PTA.

**Complex attribute transformation rules**: Cloud Sync's transformation capability is simpler than Entra Connect's full sync rules engine. Organizations with complex attribute mapping requirements may find Cloud Sync insufficient.

---

💬 **Have you migrated from Entra Connect to Cloud Sync, or deployed Cloud Sync for a new environment?** The operational overhead reduction is the most commonly cited benefit: no more scheduled maintenance windows for Connect upgrades, no more capacity planning for the sync server. What was the driver for your Cloud Sync adoption?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Entra Connect](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-2-entra-connect.md) | [🏠 Contents](/README) | [Password Hash Sync →](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-4-password-hash-sync.md)
