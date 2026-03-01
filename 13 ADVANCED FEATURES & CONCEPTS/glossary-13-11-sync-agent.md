# Sync Agent
*The On-Premises Software That Bridges Your Directory to the Cloud*

📚 **Part of Entra ID Glossary Series: Glossary#13.11 - Sync Agent**

---

A hybrid identity team got an alert on a Tuesday morning: directory synchronization had failed. Users created in on-premises Active Directory in the last four hours hadn't appeared in Entra ID. The helpdesk was getting calls from new starters who couldn't access Microsoft 365.

The investigation found the issue in under five minutes: the sync agent service had stopped on the synchronization server after a Windows update that required a restart. The server had restarted automatically overnight. Nobody had checked whether all services came back up.

The sync agent is the component that makes hybrid identity work. When it's healthy, nobody thinks about it. When it stops, identity synchronization stops with it.

## ⚙️ What the Sync Agent Does

The sync agent is a software component installed on-premises that performs the actual work of directory synchronization between on-premises Active Directory and Entra ID. It reads identity data from AD, applies transformation rules and filtering, and pushes the processed data to the Entra ID provisioning service in the cloud.

Microsoft provides two sync agent implementations with different architectures:

**Entra Connect Sync agent** 🔵: The full-featured synchronization engine, part of Microsoft Entra Connect. Runs as a Windows service on a dedicated server. Imports the full directory from on-premises AD, processes synchronization rules, and exports changes to Entra ID. Manages a local SQL database (SQL Server Express by default) for the connector space and metaverse. Supports complex synchronization scenarios including device synchronization and Exchange hybrid.

**Cloud Sync provisioning agent** ☁️: The newer, lighter-weight agent. A small Windows service that connects to the cloud-based provisioning engine, where synchronization logic runs. The agent itself doesn't process rules locally; it's a relay between on-premises AD and the cloud service. Simpler to deploy, update, and support. Supports multiple agents per forest for high availability without the active/passive complexity of Entra Connect.

## 🏗️ Installation and Server Requirements

Both agents run on Windows Server (2016 or later recommended). The server must be:

**Domain-joined** 🔗: The agent authenticates to Active Directory as part of synchronization. It needs to be a member of the domain it's synchronizing.

**Not a domain controller** ⚠️: The sync server should be a dedicated member server, not a domain controller. Running the sync agent on a DC creates operational risk: problems with the sync software can affect the DC, and DC security hardening can interfere with the sync agent.

**Network connectivity** 🌐: Outbound HTTPS to Microsoft's identity endpoints. No inbound firewall ports required. The agent initiates the connection to the cloud; the cloud doesn't reach back to the on-premises server.

**Service account** 🔑: The agent runs under a service account with appropriate permissions: read access to the Active Directory objects being synchronized, and permissions to write back attributes if writeback features (password writeback, device writeback) are configured.

## 🔄 Agent Health and Monitoring

The Entra ID portal shows sync agent health in Entra Connect Health (for Entra Connect agents) and in the Cloud Sync monitoring section (for provisioning agents). Each agent's status, last sync time, and any errors are visible.

Sync errors are categorized:
- **Export errors**: Changes couldn't be applied to Entra ID (attribute conflicts, duplicate values)
- **Import errors**: The agent couldn't read data from AD (permissions, connectivity)
- **Synchronization errors**: The sync rule processing failed for specific objects (usually attribute transformation issues)

Individual object errors don't stop synchronization for other objects. The sync engine logs the error for the specific user or group and continues. A daily email digest (configurable in Entra Connect Health) summarizes new errors.

## 🔀 High Availability

**Cloud Sync**: Supports multiple provisioning agents per AD forest. Multiple agents handle synchronization; if one fails, the others continue. No primary/secondary designation; all agents are active. Adding a second agent for high availability is strongly recommended for production environments.

**Entra Connect**: Uses an active/passive staging mode. One server is active, a second is in staging mode (running sync logic but not exporting to Entra ID). If the active server fails, an administrator manually promotes the staging server to active. Failover isn't automatic; it requires deliberate administrator action.

## ⚠️ Agent Updates

Microsoft releases updates to the sync agents. Entra Connect can be configured for auto-upgrade or manual upgrade. Cloud Sync provisioning agents support auto-upgrade, which is enabled by default.

Keeping agents updated matters: security fixes, bug fixes, and new feature support all come through updates. An outdated sync agent running on an unmonitored server is a common finding in hybrid identity health assessments.

---

💬 **What monitoring do you have in place for your sync agent health, and how quickly does your team get alerted when synchronization fails?** The sync agent is critical infrastructure: when it fails, identity operations fail. But it's often under-monitored compared to other infrastructure. What's the longest synchronization outage your environment has experienced, and what caused it?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Service Account](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-10-service-account.md) | [🏠 Contents](/README) | [Custom Role →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-12-custom-role.md)
