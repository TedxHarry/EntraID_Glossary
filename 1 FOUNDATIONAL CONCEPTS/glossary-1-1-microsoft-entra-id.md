# Microsoft Entra ID
*The Foundation of Modern Identity*

📚 **Part of Entra ID Glossary Series: Glossary#1.1 - Microsoft Entra ID**

---

Three years ago, a colleague called me in a mild panic. She'd just started a new IT role and her manager told her to "get up to speed on Azure AD before Monday." By Friday afternoon she'd read six different Microsoft docs, watched four YouTube videos, and was somehow *more* confused than when she started. "What does it actually *do*?" she asked. "Like, in real life?"

That question is where I want to start with you.

## 📌 So What Is It, Actually?

Microsoft Entra ID is a cloud-based identity and access management service. Break that sentence down and you get everything you need to know.

**Identity management** means Entra ID keeps track of who exists in your organization, your employees, contractors, guests, apps, and devices. Every one of them gets a digital record.

**Access management** means Entra ID decides what each of those identities can actually do. Can this user open SharePoint? Can that app read emails? Can this laptop connect to the VPN? Entra ID is the system making those calls.

The two questions it answers, every single time something tries to connect to anything: *Who are you?* and *What are you allowed to do?*

## 💡 Why This Matters to You as a Beginner

When I started working with Entra ID, back when it was still called Azure Active Directory, I made the mistake of thinking it was basically just a user list. A fancier Excel sheet of names and passwords. I was wrong in a way that caused me real problems.

Entra ID isn't a list. It's a decision engine. Every time someone signs in, it checks credentials, evaluates risk signals, applies security policies, and issues a token, all in a few hundred milliseconds. Understanding that changes how you think about identity problems.

If a user can't access an app, the answer isn't always "reset their password." It might be a Conditional Access policy blocking them, a missing group membership, a license not assigned, or a device that's not compliant. Entra ID touches all of those.

## 📅 What It Handles Day-to-Day

Here's what Entra ID actually does in a real organization:

**Authentication** is verifying identity. When someone types their email and password, or approves a phone notification, or scans their fingerprint, that's Entra ID checking credentials and saying yes or no.

**Authorization** happens right after. Once Entra ID knows who you are, it determines what you're allowed to access. It issues a token, a short-lived digital pass, that says "this person can access Teams, SharePoint, and this specific app."

**Device management integration** means Entra ID tracks which devices exist, whether they're compliant with your security policies, and whether they should be trusted. A laptop without disk encryption might be blocked from sensitive data even if the user's credentials are fine.

**Conditional Access** is the security logic layer. It evaluates context, where is the user signing in from? What device? What's the risk level of this sign-in?, and decides whether to allow access, block it, or step up to MFA. This is where real security happens.

## 💭 The Name Change Confusion (Let's Clear This Up)

Quick note before we go further: Entra ID and Azure Active Directory are the same thing. Microsoft rebranded Azure AD to Microsoft Entra ID in 2023. If you see "Azure AD" in older documentation, tutorials, or job postings, that's this service. The features, the underlying technology, the tenant you already have, all the same. Just a new name.

I still sometimes call it Azure AD by accident when I'm talking fast. You'll meet plenty of experienced admins who do the same.

## 📖 A Real Implementation Story

Early in my career, I worked with a 400-person company moving from a legacy VPN setup to Entra ID-based access. The old system: users had one password for the VPN, a different one for email, and a third for the HR system. Password reset tickets were the IT team's second biggest time sink after printer problems.

After setting up Entra ID with Single Sign-On, users had one identity. One sign-in got them into Teams, SharePoint, Salesforce, and the custom internal app. Password reset tickets dropped by 60% in the first month. Not because the passwords got harder to remember, but because there was only one to remember.

That's Entra ID working as designed.

## 💡 Why This Is Your Starting Point

Every other concept in identity and access management, Conditional Access, device compliance, roles and permissions, MFA, hybrid identity, connects back to Entra ID as the foundation. You can't understand why Conditional Access policies work the way they do without understanding what Entra ID is doing underneath. You can't troubleshoot access problems without knowing what decisions Entra ID is making.

Start here. Get this solid. Everything else builds on it. 🔑

---

💬 **Over to you:** When did you first encounter Entra ID (or Azure AD)? Were you thrown in the deep end like my colleague, or did you have time to learn it properly? Drop your story in the comments, I read every one.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

← *Start of series* | [🏠 Contents](/README) | [Microsoft Entra Product Family →](/1%20FOUNDATIONAL%20CONCEPTS/glossary-1-2-microsoft-entra-product-family.md)
