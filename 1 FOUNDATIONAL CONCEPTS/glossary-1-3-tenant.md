# What Is a Tenant? (And Why Getting This Wrong Causes Real Problems)

**Part of Entra ID Glossary Series: Glossary#1.3 - Tenant**

---

The first time I had to explain tenants to a room full of IT pros, I used the wrong analogy. I said a tenant was "like a database." The blank stares told me I'd made a mistake. Then someone at the back said, "Is it like a virtual machine?" Closer, but no.

Here's the analogy that actually works: a tenant is your organization's dedicated office floor in a massive shared skyscraper.

Microsoft owns the building (the cloud infrastructure). Your organization rents a floor (the tenant). You can arrange your floor however you like — put desks wherever, set your own access rules, hang your own badge readers on the doors. The people on your floor are yours to manage. Microsoft manages the building itself: the elevators, the electricity, the security of the shared spaces.

Crucially, you can't see into the other floors. A tenant in Entra ID is logically isolated from every other tenant in the world. Your users, your apps, your policies — none of it is visible or accessible to anyone outside your tenant unless you explicitly allow it.

## What Lives Inside Your Tenant

When you sign up for Microsoft 365 or Azure, Microsoft creates a tenant for you automatically. From that moment, it's your organization's dedicated space in Entra ID, and here's what it holds:

**Users** — every person who has an account in your organization. Each one is a directory object with properties: name, email, job title, group memberships, assigned licenses, and authentication methods.

**Groups** — collections of users (and other objects). Groups are how you manage access at scale. Instead of assigning a permission to 200 individual users, you put them in a group and assign the permission once.

**Applications** — every app registered to use your tenant for authentication. When an app is registered, it creates a service principal in your tenant — basically the app's identity. Entra ID tracks what that app is allowed to do and who's consented to it.

**Devices** — laptops, phones, tablets that have been registered or joined to your tenant. Device registration lets Entra ID enforce device compliance as part of access decisions.

**Policies** — Conditional Access policies, authentication methods policies, password policies. These define the security rules that govern what happens when any identity in your tenant tries to access anything.

All of this is scoped to your tenant and only your tenant.

## Why Boundaries Matter

The isolation isn't just convenient — it's the security model.

I once worked with an organization that had accidentally created two tenants. One for their main business, one that a developer had spun up years ago for testing and then never deleted. Users existed in one tenant, apps were registered in the other, and nobody could figure out why Single Sign-On wasn't working. The apps and the users were in different tenants. They were in different buildings entirely.

Tenant boundaries mean that an admin in one tenant can't affect another tenant's users or policies. A Conditional Access policy you write applies to your tenant and only your tenant. A guest user from another organization brings their identity from their tenant — they authenticate there, and your tenant trusts the result.

## One Tenant or Multiple?

Most organizations start with one tenant and stay there. It's simpler to manage, and Entra ID has features like Administrative Units to create management boundaries within a single tenant without splitting into multiple.

But sometimes multiple tenants make sense:

- **Subsidiaries with different security requirements** — a parent company that doesn't want its subsidiary to inherit its policies
- **Mergers and acquisitions** — two companies joining forces often have two existing tenants that need to coexist while IT figures out consolidation
- **Strict compliance isolation** — some regulated industries require separate identity environments

Multiple tenants add complexity. Cross-tenant access settings, B2B collaboration, separate licensing costs. I've seen organizations create extra tenants for what felt like good reasons at the time and then spend years wishing they hadn't. Think carefully before you split.

## The Beginner Misconception I See Most

New practitioners often confuse a tenant with a subscription or a specific Microsoft product. "We're on Microsoft 365, so is our tenant just for Microsoft 365?" No. Your Entra ID tenant is the identity backbone for everything — Microsoft 365, Azure, Intune, third-party SaaS apps, custom-built applications. All of them authenticate through the same tenant.

The tenant is the foundation. Everything else sits on top of it. 🏢

---

**Related Terms:**
- Glossary#1.1 - Microsoft Entra ID (the service that your tenant is an instance of)
- Glossary#8.1 - Directory Synchronization (how on-premises AD objects get into your tenant)
- Glossary#9.17 - Cross-Tenant Access (how tenants can trust each other)

---

**Question for you:** Does your organization run one tenant or multiple? And if you're running multiple — was that a deliberate architectural decision, or something that evolved over time without a plan? I've seen both and the stories are always interesting.

#EntraID #CloudSecurity #IdentityManagement #CloudIdentity #Microsoft365 #AzureAD #ITArchitecture
<!-- nav -->

---

[← The Microsoft Entra Product Family: Why There's More Than Just Entra ID](glossary-1-2-microsoft-entra-product-family.md) | [Home](../README.md) | [Cloud-Based Identity: What It Actually Means When the Servers Aren't Yours →](glossary-1-4-cloud-based-identity.md)
