# Microsoft Entra Product Family
*Why There's More Than Just Entra ID*

> **Difficulty:** 🟢 Beginner

📚 **Part of Entra ID Glossary Series: Glossary#1.2 - Microsoft Entra Product Family**

---

## 🎯 TL;DR

- The Entra family spans Identity (Entra ID), Permissions Management, Verified ID, Internet Access, and Private Access
- You can use individual products or buy the Entra Suite bundle for full coverage
- Most organizations start with Entra ID and add products as Zero Trust maturity grows


A while back I was helping a startup set up their identity infrastructure. Straightforward enough, 80 employees, Microsoft 365, a handful of SaaS apps. Entra ID handled everything beautifully.

Six months later, they acquired a smaller company. Suddenly they needed to let 40 external users from the acquired firm access their SharePoint and Teams without giving them full employee accounts. Then their dev team asked about securing service-to-service connections in Azure. Then marketing wanted a customer portal where users could create their own accounts.

Every one of those problems had a name. And every one of those names was part of the Microsoft Entra product family.

## 💡 Why One Product Isn't Enough

Entra ID is brilliant at managing your employees. It knows who works for you, what roles they have, what apps they're allowed into. That's its core job.

But modern organizations deal with three very different identity problems:

**Problem 1:** Employees, the people on your payroll who need access to internal systems.

**Problem 2:** External users, partners, contractors, vendors, suppliers. They're not employees, but they need controlled access to *some* of your resources.

**Problem 3:** Apps and services, your software itself needs an identity. When an Azure Function calls a database, or a GitHub Actions pipeline deploys to Azure, something needs to authenticate. That something isn't a person.

One product solving all three equally well turns out to be harder than it sounds. Microsoft's answer was to build a family of products, each optimized for a specific challenge, all sharing the same underlying identity platform.

## 📌 The Products and What They Actually Do

**Microsoft Entra ID** is the foundation. This is your employee directory, your SSO engine, your Conditional Access policy machine. If you only ever use one Entra product, it's this one. Everything else in the family extends or complements it.

**Microsoft Entra External ID** handles the "people outside your organization" problem. It merges what used to be two separate things, B2B collaboration (inviting partners as guest users) and B2C (building customer-facing login experiences). If you're inviting a contractor to collaborate on Teams, that's External ID. If you're building a customer portal where users sign up with their email or Google account, that's also External ID. Same product family, different configuration.

**Microsoft Entra Workload ID** is for non-human identities, apps, services, scripts, pipelines. When your application needs to authenticate to Azure Key Vault without storing a password anywhere, Workload ID is the answer. It includes managed identities and service principals, and adds governance features so you can track and secure what your apps have access to.

**Microsoft Entra Permissions Management** is a Cloud Infrastructure Entitlement Management (CIEM) tool. It watches your multi-cloud environment, Azure, AWS, GCP, and tells you who (or what) has permissions they're not using. Unused permissions are risk. This product identifies them.

**Microsoft Entra Verified ID** is decentralized identity. It lets organizations issue verifiable credentials, digital versions of things like employment verification or educational certificates, that users store in their own wallet and present to relying parties without the issuer being in the loop every time.

**Microsoft Entra Internet Access and Private Access** handle network security for the Zero Trust world. These are Secure Service Edge products that route and secure internet and private network access based on identity. They sit alongside the identity products to complete the access story.

## 🔧 How They Work Together, A Real Scenario

Let me connect this back to the startup I mentioned.

They used **Entra ID** for their 80 employees, SSO, MFA, Conditional Access, the whole package.

For the 40 external users from the acquired company, they configured **External ID** B2B collaboration. Those users kept their original identities but could access specific SharePoint sites and Teams channels as guests. IT didn't have to manage their passwords or licenses.

For the dev team's service-to-service problem, they used **Workload ID**, specifically managed identities so their Azure services could talk to each other without anyone storing a client secret in a config file.

And when the CTO asked "do any of our apps have permissions they don't need?", the answer came from **Permissions Management** after a two-week audit.

Four products. One coherent identity story.

## 📌 Entra ID Is Still the Core

You'll notice almost every scenario starts with Entra ID. That's intentional. It's the identity backbone. The other products extend it, add capabilities for specific use cases, or address security challenges that Entra ID alone doesn't cover.

When you're starting out, focus on Entra ID first, deeply. Understanding the foundation makes the rest of the family much easier to learn when you encounter the specific problems they solve. 🏗️

---


**Your turn:** Which Entra products are you working with right now? Are you purely on Entra ID, or has your organization started using other products in the family? Curious what problems drove those decisions.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Microsoft Entra ID](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-1-microsoft-entra-id.md) | [🏠 Contents](/README) | [Tenant →](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-3-tenant.md)
