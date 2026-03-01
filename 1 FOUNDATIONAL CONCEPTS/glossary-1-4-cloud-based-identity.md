# Cloud-Based Identity
*What It Actually Means When the Servers Aren't Yours*

> **Difficulty:** 🟢 Beginner

📚 **Part of Entra ID Glossary Series: Glossary#1.4 - Cloud-Based Identity**

---

## 🎯 TL;DR

- Cloud-based identity means your identity store lives in Microsoft's globally distributed datacenters, not your servers
- Unlike on-premises AD, cloud identity scales instantly, requires no infrastructure, and integrates natively with SaaS apps
- The tradeoff: you need internet connectivity; the benefit: built-in HA, compliance, and 99.99% SLA


I remember the exact moment "cloud-based" stopped being a buzzword for me and became something concrete. I was standing in a server room at 11 PM, watching a blinking drive activity light on the domain controller, waiting to see if a failed hardware component was going to corrupt the Active Directory database. It didn't. We got lucky.

Six months later, that same company started moving to Entra ID. The first time I had to troubleshoot an identity issue from home, on my laptop, at 2 PM on a Tuesday, without a VPN, I finally understood what "cloud-based" meant in practice: *that server room moment is no longer my problem.*

## 📌 What "Cloud-Based" Actually Means

When we say Entra ID is cloud-based, we mean Microsoft runs the infrastructure. The servers, the databases, the replication between data centers, the hardware failures, the patching, the backups, the disaster recovery, Microsoft handles all of it.

You don't install Entra ID. You don't patch it. You don't upgrade it. Microsoft continuously updates it and you get new features automatically, usually without any action on your part.

Think of the difference between owning a car and using a taxi service. With a car you handle maintenance, insurance, fuel, repairs. With a taxi you get in, tell them where you're going, and get out. You're not thinking about the engine.

On-premises Active Directory is the car. Entra ID is the taxi. You're still in charge of *where you're going*, your users, your policies, your security decisions. But you're not maintaining the engine.

## 🏗️ The Infrastructure Shift, Practically Speaking

With on-premises AD, your identity infrastructure lived on domain controllers in your offices or data centers. Those servers needed to be:

- Physically secured in locked rooms
- Redundant (at least two, typically three or more in larger orgs)
- Patched regularly, and patches tested carefully before applying
- Backed up and the backups tested
- Monitored for performance and health
- Replaced when hardware aged out (usually every 3-5 years)

When an office loses internet, the local domain controller still handles authentication for on-site resources. But when the domain controller itself goes down, users can't log in to anything.

With Entra ID, Microsoft maintains 99.99% uptime SLA across geographically distributed data centers. Your users authenticate against Microsoft's infrastructure, not your own. If your internet connection goes down, yes, that's a problem. But you're not racing to restore a domain controller at midnight.

## 🛡️ What Changes in the Security Model

This is where beginners sometimes make assumptions that get them in trouble.

With on-premises AD, perimeter security made sense. You had a firewall, a VPN, an internal network. The assumption was: if you're on the internal network, you're probably authorized. Trust the perimeter.

Cloud-based identity assumes the opposite. Entra ID doesn't know or care whether a user is sitting in your office or a coffee shop in another country. Every access request gets evaluated on its own merits, who is the user, what device are they on, where are they signing in from, how risky does this sign-in look?

This shift, from "trust the network" to "verify every request", is the foundation of Zero Trust. Cloud-based identity doesn't just *support* Zero Trust, it more or less *requires* thinking this way.

## 📌 Scalability and What That Means for You

On-premises identity scales with hardware. Need to support more users? Buy more servers, scale your domain controllers, plan capacity. That takes months.

Entra ID scales automatically. When a company I worked with was acquired and needed to onboard 2,000 users from the acquired organization over a weekend, we didn't provision new infrastructure. We invited them as guests, set up synchronization, and got to work. The platform handled the load.

The cost model shifts too. You're not buying hardware. You're paying for licenses, per user, per month. Costs become predictable. Unused capacity isn't sitting in a rack consuming electricity.

## 📖 The Real Migration Challenges

I'll be honest here because the "cloud is easy" narrative glosses over real friction.

**Network dependency is real.** Your applications now authenticate against an internet endpoint. If your internet connection is unreliable, users feel it. Redundant internet connections stop being optional.

**The mental model shift takes time.** Admins who've managed AD for a decade have deeply ingrained habits. The way you troubleshoot problems, the tools you use, the logs you read, all different in Entra ID. There's a genuine learning curve.

**Not everything migrates cleanly.** Legacy applications that use Kerberos authentication, NTLM, or LDAP queries don't just "work with Entra ID." They often need the on-premises AD to stick around, or need significant application changes. That's where hybrid identity comes in, which we'll cover in the next article.

Cloud-based identity isn't universally easier. It's a different kind of work, with different failure modes and different advantages. Understanding both sides is what makes you effective. ☁️

---


**Tell me about your journey:** Is your organization cloud-only with Entra ID, still on-premises with AD, or somewhere in between? What's been the biggest adjustment in moving identity to the cloud, technical or cultural?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Tenant](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-3-tenant.md) | [🏠 Contents](/README) | [Active Directory →](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-5-active-directory.md)
