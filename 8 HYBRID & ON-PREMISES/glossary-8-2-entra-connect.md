# Entra Connect: The Engine Behind Hybrid Identity

**Part of Entra ID Glossary Series: Glossary#8.2 - Entra Connect**

---

A migration project I worked on had a deceptively simple requirement: synchronize 8,000 users from on-premises Active Directory to Entra ID, preserving all existing Microsoft 365 licenses, mailbox configurations, and group memberships.

The challenge was that 400 of those users had been manually created in Entra ID years earlier before the sync project was planned. The UPN format in AD was different from the cloud accounts. And the AD was five years old with inconsistent attribute data.

Entra Connect handled most of it. The UPN matching, the soft matching of on-premises accounts to existing cloud accounts, the attribute transformation rules. What should have been a weeks-long manual migration was completed in a week including testing. Understanding how Entra Connect works made the difference between guessing and knowing which configuration decisions to make.

## 🔧 What Entra Connect Is

Microsoft Entra Connect (formerly Azure AD Connect) is the on-premises software component that implements directory synchronization between on-premises Active Directory and Entra ID. It runs as a Windows service on a server in your on-premises environment.

Entra Connect is the primary synchronization tool for the majority of hybrid organizations. It handles:

- Directory object synchronization (users, groups, contacts, devices)
- Password Hash Sync (copying password hashes to the cloud)
- Pass-Through Authentication agent hosting
- Seamless Single Sign-On configuration
- Device writeback for Hybrid Entra Join
- Password writeback for SSPR

It's a substantial piece of software with a significant configuration surface. The Express Settings path for a single-forest environment makes initial setup straightforward. Complex environments with multiple forests, non-standard UPN configurations, or custom attribute requirements need the Custom installation path.

## 🏗️ The Sync Architecture

Entra Connect operates through three components:

**Connector space** 📦: A local staging area that holds a copy of objects from both the on-premises AD and Entra ID. When sync runs, it reads from AD into the AD connector space and reads from Entra ID into the cloud connector space.

**Metaverse** 🔀: The central staging area where objects from both connector spaces are joined and attribute flows are applied. The metaverse is where the "this on-premises user maps to this cloud user" decision is made and attribute transformation rules are evaluated.

**Sync rules engine** ⚙️: The configurable logic that determines what gets imported from AD, how attributes are transformed, how objects are joined (matched) between AD and Entra ID, and what gets exported to Entra ID.

The sync cycle runs every 30 minutes by default. A full sync (re-reads everything) and a delta sync (reads only changes since last sync) alternate. Delta syncs are faster; full syncs ensure nothing is missed.

## 🔑 Password Hash Sync

Password Hash Sync (PHS) is Entra Connect's mechanism for enabling cloud authentication with on-premises passwords:

1. Entra Connect reads the NT hash of the user's password from AD
2. The NT hash is further hashed using a salted SHA256 process
3. The resulting hash is sent to Entra ID over encrypted HTTPS
4. When the user authenticates to Entra ID, the submitted password is hashed using the same process and compared

The original password never leaves on-premises. Microsoft never sees the password. The hash stored in Entra ID is not the same as the hash stored in AD. This is specifically designed so that a breach of Entra ID's hash storage doesn't expose on-premises AD credentials.

PHS also enables the leaked credentials detection in ID Protection. Microsoft can compare the hashes in Entra ID against hashes found in breach databases. This comparison is done securely and the results inform user risk without exposing the actual credentials.

## 🔄 Entra Connect vs Cloud Sync

Entra Connect is the established, feature-complete synchronization tool. Microsoft has introduced a newer option:

**Entra Connect Cloud Sync**: A lighter-weight synchronization agent that offloads the synchronization logic to the cloud rather than running it locally. Simpler to deploy and maintain. Useful for organizations with straightforward single-forest environments and lighter requirements.

**When to use Connect**: Multiple forests, complex attribute transformation requirements, full feature set including device writeback, Pass-Through Authentication hosting.

**When to use Cloud Sync**: Single forest, straightforward requirements, preference for cloud-managed sync logic, simpler deployment.

Both tools synchronize the same objects and support PHS. The choice depends on environment complexity and operational preference.

## ⚠️ Entra Connect Operational Considerations

**Single active server**: Entra Connect should run on a single active sync server. Running multiple servers in active mode causes conflicts. A staging mode server (passive) is supported for high availability: the staging server runs sync but doesn't export to Entra ID, ready to be activated if the primary fails.

**Version maintenance**: Entra Connect requires regular updates. Microsoft releases new versions that include bug fixes, new features, and security updates. Running outdated versions can cause sync failures or security issues. Check the version and update schedule regularly.

**Service account permissions**: Entra Connect uses a service account in on-premises AD with specific permissions to read directory data. These permissions must be maintained. Changes to AD permissions that affect the sync account cause sync failures.

**Server sizing**: The Entra Connect server must have sufficient resources. Large directories (100,000+ objects) need more RAM and CPU than default VM sizes. Microsoft publishes sizing guidance.

**Monitoring**: Entra Connect Health (requires Entra ID P2) provides alerting for sync issues. At minimum, monitor the sync server's Windows event log and configure alerts for sync failures.

---

💬 **What was the most challenging Entra Connect configuration decision you've made in a complex hybrid environment?** The multi-forest scenarios, the UPN mismatches between AD and existing cloud accounts, or the custom attribute mapping requirements are where Connect's complexity becomes visible. What required the most troubleshooting to get right?
<!-- nav -->

---

[← Directory Synchronization: Bridging On-Premises Identity with the Cloud](glossary-8-1-directory-synchronization.md) | [Home](../README.md) | [Cloud Sync: The Lighter Path to Hybrid Identity →](glossary-8-3-cloud-sync.md)
