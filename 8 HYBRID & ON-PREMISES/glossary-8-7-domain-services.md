# Domain Services
*Active Directory Without the Domain Controllers*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #8.7 - Domain Services

---


A company was migrating everything to Azure. Their infrastructure, their applications, their workloads. The goal was to eliminate their on-premises data centers entirely.

One problem: they had dozens of legacy applications that required domain join. Kerberos authentication. NTLM. LDAP directory lookups. Group Policy. These applications couldn't be changed. They were vendor products with no modern authentication support.

Decommissioning their on-premises Active Directory would break all of them.

Microsoft Entra Domain Services gave them a way out: a managed Active Directory service in Azure, fully compatible with Kerberos, NTLM, and LDAP, with no domain controllers to manage.

## 🏗️ What domain services is

Microsoft Entra Domain Services (formerly Azure AD Domain Services, often called AADDS) is a managed service that provides traditional Active Directory capabilities in Azure without requiring you to deploy or manage domain controllers.

When you enable Domain Services, Microsoft creates a managed domain in your Azure subscription with:

- Domain controllers (managed by Microsoft, running in Azure)
- Kerberos and NTLM authentication support
- LDAP directory access (read-only LDAP; secure LDAP is available for read)
- Group Policy support
- Domain join capability for Azure VMs

Virtual machines in Azure can join the Domain Services managed domain and behave as if they were in a traditional on-premises AD domain. Legacy applications running on those VMs can use Kerberos, authenticate against LDAP, and receive Group Policy.

## 🔗 How domain services relates to entra ID

Domain Services is not a replacement for Entra ID. It's a complement that adds traditional AD protocols on top of Entra ID's cloud-native identity.

When Entra ID synchronizes to Domain Services, users and groups from Entra ID are populated into the Domain Services managed domain. A user who exists in Entra ID (whether cloud-native or synchronized from on-premises AD) can sign in to a domain-joined VM in Azure using their Entra ID credentials.

The synchronization is one-way: Entra ID to Domain Services. You can't create users directly in Domain Services and have them appear in Entra ID. The source of truth for identities is Entra ID.

## 🎯 When to use domain services

**Legacy application lift-and-shift** 🏗️: Applications that require domain join, Kerberos, NTLM, or LDAP can run on Azure VMs joined to Domain Services without modification.

**Eliminating on-premises AD** 🌐: Organizations that want to go entirely cloud but have legacy dependencies on AD protocols can use Domain Services as a bridge. On-premises AD is decommissioned; Domain Services provides the traditional AD services in Azure.

**Development and test environments** 🔧: Domain Services provides a consistent, managed AD environment for dev/test workloads that need AD integration without the overhead of running domain controllers.

**SaaS applications that require LDAP** 📋: Some SaaS applications are configured to authenticate users via LDAP queries to a directory. Domain Services provides an LDAP endpoint that these applications can connect to.

## ⚙️ What domain services manages (and what you still control)

**Microsoft manages** 🔵:
- Domain controller VMs, including patching and updates
- AD replication between controllers
- Backup and recovery
- Health monitoring

**You manage** 🟢:
- Group Policy Objects applied within the domain
- Organizational Units (a limited set)
- Network configuration (the VNet where Domain Services is deployed)
- VM domain join configurations
- LDAP access permissions

**You cannot** 🔴:
- Access the domain controllers directly (no RDP to the DCs)
- Modify the AD schema
- Create domain or enterprise admin users in Domain Services
- Establish trust relationships with other domains

Domain Services is "AD-as-a-service." Microsoft handles the infrastructure. You configure the domain behavior within the managed constraints.

## ⚠️ Limitations and considerations

**Read-only LDAP** 📋: By default, LDAP access to Domain Services is read-only. Secure LDAP can be enabled for read access over a certificate-protected connection, but write access via LDAP is not supported.

**No domain admin in the traditional sense** 🔑: A specific group in the managed domain (AAD DC Administrators) has elevated permissions, but not the full Domain Admins rights that traditional AD environments have. Some administrative operations that require full domain admin aren't possible.

**Cost** 💰: Domain Services is a paid service billed hourly based on the SKU (Standard or Enterprise). Unlike on-premises DCs where the cost is hardware and Windows Server licensing, Domain Services appears as an Azure resource charge. Evaluate cost against the alternative of maintaining on-premises DCs.

**Not a path back to traditional AD management**: Domain Services is designed for workloads that need AD compatibility, not for organizations that want all the capabilities of a self-managed AD forest. If you need schema extensions, full domain admin, or trust relationships, you likely need traditional AD DCs in Azure or on-premises.

---

💬 **Have you used Domain Services to enable a legacy application lift-and-shift that couldn't use modern authentication?** The pattern of "everything modern goes to Entra ID, everything legacy gets Domain Services as a compatibility layer" is becoming common in cloud migrations. What was the application or workload that made Domain Services the right answer for your environment?
✍️ TedxHarry

<!-- nav -->

---

[← Federation](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-6-federation.md) | [🏠 Contents](/README) | [App Integration →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-1-app-integration.md)
