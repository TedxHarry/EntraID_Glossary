# Hybrid Identity
*Living in Two Worlds at Once*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#1.6 - Hybrid Identity**

---

## 🎯 TL;DR

- Hybrid identity connects on-premises Active Directory with Entra ID so users have one identity in both places
- Entra Connect Sync replicates AD objects to Entra ID; Entra Cloud Sync is the lighter modern replacement
- Three auth models: Password Hash Sync (most resilient), Pass-Through Auth, or Federation (most complex)


If I had to pick one concept that trips up aspiring Entra ID specialists more than any other, it's hybrid identity. Not because it's complicated in theory, the theory is actually pretty clean. It's because the *reality* is messier than the diagrams suggest, and when it breaks, it tends to break in the quietest, most confusing ways possible.

Let me give you the real picture.

## 🔄 What Hybrid Identity Is

Most large organizations don't get to choose between Active Directory and Entra ID. They've had AD for 10, 15, 20 years. Their file servers, their legacy apps, their computer management, all built around it. And now they need Entra ID for Microsoft 365, for cloud apps, for modern authentication.

Hybrid identity is what you call it when both systems exist simultaneously and share the same user identities. One person. One username. One password. But their account exists in *both* Active Directory and Entra ID, and those accounts are synchronized to stay consistent.

When done right, the user doesn't notice. They log in at their desk the same way they always have. They open Teams, it signs them in automatically. They try to access Salesforce, same sign-in. The seam between on-premises and cloud is invisible to them.

When it breaks, they call the help desk.

## 💡 Why Organizations End Up Here

Nobody architects hybrid identity because it's their dream state. They end up here because:

**They can't migrate everything at once.** Moving identity is a multi-year project for large organizations. During that journey, old systems and new systems coexist. Hybrid identity is the bridge.

**Legacy apps require AD.** As we covered in the last article, plenty of enterprise software needs Kerberos, NTLM, or LDAP. Until those apps are replaced or reconfigured, AD has to stay.

**Devices are still domain-joined.** Thousands of Windows laptops joined to an on-premises domain don't become Entra-joined overnight. The device fleet migrates gradually.

**The business keeps running.** You can't take everyone offline for an identity migration. Change happens while the organization operates, which means both systems run simultaneously for years.

## 🔄 How Synchronization Works

The primary tool is Microsoft Entra Connect (previously called Azure AD Connect). You install it on a server in your on-premises environment, connect it to your AD and your Entra ID tenant, and it handles synchronization.

Every 30 minutes by default, Entra Connect reads changes from Active Directory and writes them to Entra ID. New user created in AD? Appears in Entra ID within 30 minutes. User's department changed? Updated in Entra ID. User disabled in AD? Disabled in Entra ID.

The flow is one-directional for most attributes: AD is the source of truth, Entra ID receives. You don't create users in Entra ID and have them sync back to AD in a standard hybrid setup. You create them in AD and let sync do the rest.

Entra Cloud Sync is the newer, lighter-weight alternative. It doesn't require a dedicated server, agents are installed on domain controllers, and it handles some scenarios Entra Connect doesn't, like multi-forest environments. Many organizations are migrating from Connect to Cloud Sync now.

## 🔄 What Syncs and What Doesn't

This is where people get caught out. Not everything in AD syncs to Entra ID.

**What does sync:** User accounts, group memberships, contact objects, basic attributes (name, email, department, manager), password hashes (if you configure Password Hash Sync).

**What doesn't sync:** Group Policy, Kerberos tickets, computer accounts (in most configurations), service account passwords, fine-grained password policies, and AD-specific features like managed service accounts.

Entra ID isn't a cloud copy of Active Directory. It's a synchronized subset of the identities, focused on the attributes needed for cloud access management.

## ⚠️ The Failure Points I've Actually Seen

Three failure scenarios come up over and over in hybrid environments:

**Sync is broken but nobody noticed.** The synchronization service runs quietly in the background. If it stops, a server went down, a certificate expired, a port was blocked, users don't see an immediate error. They see it when they change their password on-premises and it doesn't update in the cloud. Or when a new employee is created in AD and can't access Microsoft 365 three days later because they never synced.

**The connector account's permissions got changed.** Entra Connect uses a service account with specific permissions in AD. If someone tightens AD permissions during a security audit without knowing what breaks, sync can fail silently on specific object types.

**Attribute conflicts.** Two objects in AD that sync to Entra ID and collide on a unique attribute, usually email address or UserPrincipalName. Entra ID quarantines one of them. Nobody notices until someone can't sign in.

Monitor your sync health. Set up alerts. Check the synchronization status regularly, it's in the Entra admin center under Identity > Hybrid Management. Don't let it run unmonitored for months and find out about a problem through a user complaint.

## 📍 This Is Where Most Organizations Actually Are

If you're studying Entra ID to work in enterprise IT, you will almost certainly be working in a hybrid environment. Pure cloud-only tenants exist, mostly startups and newer organizations, but the majority of enterprises are hybrid, and that's unlikely to change completely within the next few years.

Understanding hybrid identity isn't advanced material. It's practical reality. 🔄

---

🔗 **Related Terms:**
- [Glossary#1.5 - Active Directory](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-5-active-directory.md) (the on-premises side of hybrid identity)
- [Glossary#1.4 - Cloud-Based Identity](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-4-cloud-based-identity.md) (the cloud side of the equation)
- [Glossary#8.1 - Directory Synchronization](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-1-directory-synchronization.md) (the technical mechanism behind sync)
---

💬 **Where are you in your hybrid journey?** Are you managing a hybrid environment right now, planning a migration toward cloud-only, or starting fresh with cloud-first? What's the hardest part you've run into, the technology or convincing stakeholders that it's worth the effort?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Active Directory](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-5-active-directory.md) | [🏠 Contents](/README) | [Identity →](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-1-identity.md)
