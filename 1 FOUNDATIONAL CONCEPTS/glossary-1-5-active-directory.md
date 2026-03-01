# Active Directory
*Here's Why That Matters.*

📚 **Part of Entra ID Glossary Series: Glossary#1.5 - Active Directory**

---

Every few months someone posts something along the lines of "Active Directory is legacy technology, just move everything to Entra ID." And every time, the comments fill up with experienced IT professionals gently (and sometimes not so gently) explaining why that's not how it works.

I get where the sentiment comes from. Entra ID is modern, cloud-native, built for the way organizations actually work now. Active Directory was designed in 1999 for a world where everyone worked in the office and the biggest security threat was someone plugging in an unauthorized laptop.

But here's what those "just migrate" takes miss: most large organizations are running Active Directory right now, today, in 2026, and they're going to be running it for years. Understanding what it is and how it relates to Entra ID isn't optional knowledge for an Entra ID specialist. It's foundational.

## 📌 What Active Directory Actually Is

Active Directory (AD) is Microsoft's on-premises directory service. It's been around since Windows 2000 and it runs on servers inside your organization's network, physical servers, virtual machines, or both.

Its core job is the same as Entra ID's: managing identities and controlling access. It holds user accounts, computer accounts, groups, and policies. When an employee sits down at a Windows computer and logs in, AD authenticates them. When they open a file share, AD checks whether they're authorized. When Group Policy pushes security settings to all the laptops in the company, AD is delivering those settings.

For about 20 years, AD was the identity backbone of almost every enterprise with more than a handful of employees. It's not going anywhere quickly.

## 💡 Why AD Hasn't Gone Away

Several reasons, and they're all practical:

**Applications built for AD.** Lots of enterprise software was designed to work with Kerberos authentication, NTLM, or LDAP, protocols that Entra ID doesn't natively support. That ERP system from 2012, the manufacturing floor software, the custom-built internal tools, they often *need* AD. Migrating them requires either rewriting the apps, buying replacements, or keeping AD around to serve them.

**Group Policy.** AD's Group Policy is deeply embedded in how Windows devices get managed in large organizations. Tens of thousands of policy settings, software installations, security baselines, printer mappings, drive mappings, delivered through Group Policy. Entra ID has its own modern equivalents via Intune, but migrating years of Group Policy configuration is a significant project.

**Organizational inertia.** A 10,000-person company with AD running for 15 years has processes, runbooks, tribal knowledge, and staff expertise built around it. You don't replace that overnight, or even over a year.

**It actually works.** AD is mature, stable, and well understood. The failure modes are known. The troubleshooting tools are familiar. For many organizations, it's working exactly as expected, and "working as expected" isn't a strong argument for a major migration.

## 📌 The Old vs. New Comparison

| | Active Directory | Microsoft Entra ID |
|---|---|---|
| Location | On-premises servers | Microsoft's cloud |
| Authentication protocols | Kerberos, NTLM, LDAP | OAuth 2.0, OIDC, SAML |
| Device management | Group Policy | Intune/MDM |
| Infrastructure | You manage it | Microsoft manages it |
| Access to modern apps | Limited (via federation) | Native |
| Access to legacy apps | Native | Limited (via hybrid) |

Neither column is universally better. The right answer for any organization depends on what they're running and where they're going.

## 📌 AD's Role Is Changing, Not Ending

The honest picture: AD's role in most organizations is shifting from primary to supporting actor.

Where it used to be the center of everything, it's increasingly becoming the source of truth for on-premises resources, file servers, printers, legacy apps, while Entra ID handles cloud access, modern authentication, and security policy.

Entra Connect (or Cloud Sync) synchronizes users from AD to Entra ID, so an account created in AD automatically appears in Entra ID. The user's on-premises identity and their cloud identity are linked. This is hybrid identity, which we'll cover in the next article.

I still work with Active Directory weekly. I troubleshoot replication, clean up stale computer objects, investigate failed Kerberos authentications. It's not glamorous, but it matters. The organizations running hybrid environments, which is most of them, need people who understand both sides.

## 📖 Real Scenarios Where AD Still Does the Work

- A manufacturing plant where machines authenticate to a local domain controller, even when internet is down
- A law firm where file server access is controlled by AD security groups
- A bank where the core banking application requires LDAP queries against AD for user lookups
- A university where computer lab workstations join the domain for Group Policy management

In all of these, Entra ID exists alongside AD. They're not competitors in these environments, they're partners, each handling what it does best. 🖥️

---

🔗 **Related Terms:**
- Glossary#1.6 - Hybrid Identity (when AD and Entra ID work together)
- Glossary#1.4 - Cloud-Based Identity (what Entra ID is, by contrast)
- Glossary#8.1 - Directory Synchronization (how AD and Entra ID stay in sync)

---

**I'm curious:** Are you still managing on-premises Active Directory, or has your organization gone cloud-only? If you're hybrid, what's making the full migration difficult? The technical barriers are usually more interesting than people expect.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Cloud-Based Identity](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-4-cloud-based-identity.md) | [🏠 Contents](/README) | [Hybrid Identity →](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-6-hybrid-identity.md)
