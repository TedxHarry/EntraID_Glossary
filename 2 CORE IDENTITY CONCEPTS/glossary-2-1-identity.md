# Identity: The Word Everyone Uses and Almost Nobody Defines

**Part of Entra ID Glossary Series: Glossary#2.1 - Identity**

---

I counted once. In a 45-minute meeting about a security architecture review, the word "identity" came up 31 times. The project manager used it to mean "user accounts." The security architect used it to mean "authentication credentials." The developer used it to mean "the token." And I was using it to mean something slightly different from all three of them.

Nobody stopped to define it. We moved forward assuming we were talking about the same thing. We weren't.

That meeting produced a design document with a serious flaw in it that took three weeks to untangle. The root cause wasn't technical — it was linguistic. We all said "identity" and meant different things.

So before we go any further in this series, let's define it properly.

## What Identity Means in Entra ID

In Microsoft Entra ID, an identity is a directory object that can be authenticated and authorized to access resources.

Break that down word by word:

**Directory object** — it's a record in Entra ID's database. It has attributes, a unique identifier, and a defined type. It exists as a thing you can look up, modify, and delete.

**That can be authenticated** — Entra ID can verify its claimed identity. The object has some way of proving it is who it says it is: a password, a certificate, a managed credential, or a federated trust relationship.

**And authorized** — once authenticated, that identity can be granted (or denied) access to specific resources based on permissions, roles, and policies.

If something in Entra ID meets all three of those criteria, it's an identity. If it can't be authenticated, it's just data.

## The Three Kinds of Identity You'll Manage

This is where the definition gets practical, because not all identities are people.

**Human identities** are what most beginners think of first: employees, contractors, guest users, customers. A person sits in front of a keyboard, proves who they are, and gets access to something. Human identities have passwords (or better, passwordless credentials), MFA methods, and a real human being accountable for their actions.

**Workload identities** are for software. Applications, services, scripts, automation pipelines, containers — all of them sometimes need to authenticate to access resources. Your Azure Function that reads from a storage account needs an identity to do that. Your GitHub Actions workflow that deploys to Azure needs an identity. These identities don't have humans attached to them. They authenticate using certificates, managed credentials, or federated tokens — never passwords if you're doing it right.

**Device identities** are for physical and virtual machines. When a laptop registers with Entra ID, it gets a device identity — a directory object that represents that specific machine. Entra ID can then make access decisions based on the device: is it compliant with security policies? Is it managed? Is it Entra-joined? The device's identity influences whether the human using it gets access.

## Why the Distinction Actually Matters

A common mistake I see: treating all identities the same way from a governance and security perspective.

Human identities need MFA. They need access reviews — periodic checks that a person still needs the access they have. They're subject to risk detection: if a human's sign-in behavior looks suspicious, Entra ID Protection flags it.

Workload identities don't sign in with MFA. They can't — there's no human to approve a phone notification. Their security model is completely different: you control what they can access through permissions scoping, you rotate their credentials (or use managed identities so you never have to), and you monitor what they're doing through logs.

Device identities tie into Conditional Access: your policies can require that a device is compliant before allowing access, regardless of how good the user's credentials are.

Mixing up which type of identity you're dealing with leads to applying the wrong security model. And applying the wrong security model means either gaps or friction — or both.

## The Object ID: The Thing That Never Changes

Every identity in Entra ID — user, service principal, managed identity, device — gets a globally unique Object ID (OID) assigned at creation. This is a GUID, something like `a1b2c3d4-e5f6-7890-abcd-ef1234567890`.

The Object ID never changes, even if everything else does. A user can change their name, their email address, their UPN, their department — the Object ID stays constant. Applications that reference identities reliably use Object IDs rather than display names or email addresses for exactly this reason.

I once spent two hours troubleshooting why an app kept losing its permissions. Turned out the app was looking up the admin group by display name. Someone had renamed the group. Object ID lookup would've been stable. Lesson learned.

## Identity Is the Starting Point for Everything

Every access decision in Entra ID starts with identity. Before Conditional Access can evaluate whether to allow or block access, it needs to know *who* is asking. Before permissions can be checked, the identity making the request has to be established. Before MFA can be required, there has to be an authenticated identity to require it *of*.

Get comfortable with identity as a concept — all three types, their distinct security models, and the attributes that make each one unique. Everything else in this series builds on it. 🪪

---

**Related Terms:**
- Glossary#2.2 - User (the most common human identity object)
- Glossary#2.3 - Service Principal (the workload identity object)
- Glossary#10.2 - Managed Identity (the preferred type of workload identity in Azure)

---

**Think about your own environment:** How many different types of identities are you managing right now? Most people underestimate the workload identity count — the apps and services quietly authenticating in the background. Do you know how many service principals are active in your tenant?
<!-- nav -->

---

[← Hybrid Identity: Living in Two Worlds at Once](../1%20FOUNDATIONAL%20CONCEPTS/glossary-1-6-hybrid-identity.md) | [Home](../README.md) | [The User Object: What's Actually Inside (And Why It Matters More Than You Think) →](glossary-2-2-user-identity-object.md)
