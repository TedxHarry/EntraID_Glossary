# What Is Microsoft Entra ID?
*Before you touch a single setting, understand the problem it solves*

> 🟢 **Beginner** · Unit 1, Module 1 · ⏱️ 30 minutes

---

## What You Will Learn

By the end of this module you will:

- Understand what Entra ID does and **why it exists**
- Have a **free practice environment** set up and ready
- Know your way around the **Entra admin center**
- Have created your **first test user**
- Know where to look when **something goes wrong**

No prior experience needed. Start here.

---

## The Problem That Created Entra ID

Imagine it's 2005. You join a 300-person company. On your first day, IT hands you a printout with a list of credentials:

| System | Username | Password |
|---|---|---|
| Windows login | john.smith | Welcome@1 |
| Email | jsmith@company.com | Qwerty123 |
| HR system | johnsmith | Company2005 |
| Project tool | j.smith | Pass1234 |
| Finance system | jsmith2 | Finance05 |

Every few months, each system forces a password change independently. You call the helpdesk every time you forget one. The helpdesk spends 40% of their week resetting passwords.

When you leave the company, IT has to go into each system and manually disable your account. One system gets missed. Three months later, you still have access to the company's financial data.

This was not unusual. This was how most companies worked.

---

## What Changed

Cloud services arrived. A 300-person company now uses 50+ applications: Microsoft 365, Salesforce, Slack, GitHub, Zoom, Workday, ServiceNow. If every app gets its own username and password, the 2005 problem gets ten times worse.

**Entra ID is the solution.** It is Microsoft's cloud identity platform — one central system that:

- Stores every identity in your organization (people, apps, devices)
- Handles authentication (proving who you are) for every connected app
- Enforces access policies (deciding what you're allowed to do)
- Gives every user one sign-in that works everywhere

The result: Sarah signs in once in the morning. Entra ID issues her a digital pass. That pass works for Teams, SharePoint, Salesforce, and every other connected app — without signing in again. When Sarah leaves the company, one action in Entra ID removes her access everywhere, instantly.

That is what you are learning to build and manage.

---

## The Name Confusion — Let's Clear It Up Now

You will constantly see these names used interchangeably. They are the **same product**:

| Name | When you'll see it |
|---|---|
| **Microsoft Entra ID** | Current official name (since 2023) |
| **Azure Active Directory** | Old name — still everywhere in docs, videos, job postings |
| **Azure AD** | Shortened version of the old name |
| **AAD** | Abbreviation — still used in PowerShell, APIs, code |

If a YouTube tutorial says "Azure AD," it means Entra ID. If a job posting requires "Azure AD experience," they want Entra ID knowledge. Same thing.

> ⚠️ **Don't confuse with on-premises Active Directory (AD DS)** — that is a completely different product. It runs on servers inside a building, uses older protocols (Kerberos, LDAP), and predates cloud computing. We cover the relationship between them in Unit 9. For now: "Active Directory" in a cloud context = Entra ID.

---

## Three Things Entra ID Manages

Every concept in this series, every lab, every setting you configure — it all belongs to one of these three categories.

**🪪 Identities**
The accounts. Users, apps, service accounts, and devices. Each one gets an entry in Entra ID with a unique permanent ID.

**📦 Resources**
The things identities want to access. Microsoft 365 apps (Teams, SharePoint, Outlook), third-party SaaS apps (Salesforce, GitHub), your own applications, Azure services.

**📋 Policies**
The rules that decide what identities can do with resources. Who can sign in. From where. Using which device. After proving identity how. **Conditional Access** is where most policies live — we build these in Unit 4.

When you are confused about where something fits, ask: *Is this about an identity, a resource, or a policy?*

---

## Lab 1.1 — Set Up Your Free Practice Environment

You need a place to practice. Microsoft provides a completely free Microsoft 365 E5 developer tenant — a full enterprise environment with every Entra ID feature unlocked, 25 user licenses, and no credit card required.

> 💡 **Why E5?** The developer tenant includes **Entra ID P2** — the highest license tier. This means every feature in this series (Identity Protection, Privileged Identity Management, Access Reviews, etc.) is available to you for free during learning. In a real job you'll often work with P1 or P2. Here you have everything.

---

**Step 1 — Create your developer tenant**

1. Go to: `developer.microsoft.com/microsoft-365/dev-program`
2. Click **Join now**
3. Sign in with any personal Microsoft account (Outlook.com, Hotmail, Live). If you don't have one, create one — it's free.
4. Fill in the registration form:
   - Country: yours
   - Company: put "Learning" or your own name
   - Developer focus: choose "IT admin / administrator"
5. Click **Next** → choose **Instant sandbox**
6. Choose your admin username — something like `admin` and a domain like `yourname.onmicrosoft.com`
7. Set a strong password. **Write it down. You will need it.**
8. Click through the remaining steps and wait 2–5 minutes for provisioning

You now have a fully functional Microsoft 365 E5 tenant. It renews every 90 days automatically as long as you use it (just sign in occasionally — it detects activity).

> ⚠️ **This is a learning environment.** Do not put real personal data in it. It will eventually expire. It's only for practice.

---

**Step 2 — Sign in to the Entra admin center**

1. Open your browser and go to: `entra.microsoft.com`
2. Sign in with the admin account you just created (`admin@yourname.onmicrosoft.com`)
3. You are now in the **Microsoft Entra admin center**

This is your primary workspace throughout this series. Take a moment before clicking anything. Look at the left navigation panel. It has a lot of options — but you only need to know five areas for now.

---

## Lab 1.2 — The Admin Center Tour

Find each of these sections and click into them. Don't change anything yet — just look.

---

**Area 1 — Users** `Identity → Users → All users`

This is the identity directory. Every person in your organization will have a row here. Right now you see one user: your admin account.

Click on your admin account. Look at the panel that opens on the right:

- **Object ID** — a long code like `a1b2c3d4-e5f6-...`. This is the permanent, unique identifier for this user. It never changes, even if the name or email changes.
- **User principal name (UPN)** — this is the sign-in name, formatted as an email address
- **Account enabled** — if this is set to No, the user cannot sign in

The **Object ID** is the most important identifier in Entra ID. Applications, logs, and PowerShell commands use it to refer to users — not the display name, not the email, but this ID.

---

**Area 2 — Groups** `Identity → Groups → All groups`

Groups let you manage access at scale. Instead of giving each of 500 people individual access to a SharePoint site, you create a group, put the 500 people in it, and give the group access. When someone new joins, you add them to the group — they instantly have the right access. When someone leaves, you remove them from the group.

You'll build your first groups in Module 1.3.

---

**Area 3 — Conditional Access** `Protection → Conditional Access → Policies`

This is the policy engine — the place where you define the rules for who can access what, from where, and under what conditions. This is where most of an Entra ID admin's security work happens.

Right now it's mostly empty. By Unit 4 you'll have a complete, working policy stack here.

Notice the **What If** button in the top toolbar. This tool lets you simulate: "If this user tried to sign in to this app from this device and this location — what would happen?" You will use this constantly when building and testing policies.

---

**Area 4 — Enterprise Applications** `Identity → Applications → Enterprise applications`

Every application connected to your tenant appears here. When you connect Salesforce, GitHub, or any SaaS app to Entra ID for single sign-on, it shows up in this list. Microsoft's own apps (Teams, SharePoint, etc.) are already here.

We build here in Unit 5.

---

**Area 5 — Sign-in Logs** `Identity → Monitoring & health → Sign-in logs`

Every sign-in attempt to your tenant is recorded here. Success or failure. Which user. Which app. Which device. Which authentication method. Which Conditional Access policies evaluated and what they decided.

This is your **diagnostic tool**. When a user says "I can't get in," you come here first. When a security alert fires, you come here to investigate. When something is broken and you don't know why, this log tells you.

> 💡 **Do this now:** Open a new tab, go to `portal.office.com`, sign in as your admin account. Come back to the Entra admin center and go to Sign-in logs. Wait about 60 seconds and refresh. Find the sign-in you just made. Click on it. Look at the tabs: **Basic info**, **Authentication Details**, **Conditional Access**. You just read your first sign-in log entry.

---

## Lab 1.3 — Create Your First Test User

Throughout this series you need test accounts to experiment with — accounts you can sign in as, lock out, assign policies to, and reset, without affecting your main admin account.

Let's create the first one.

---

**Navigate to:**
`Identity → Users → All users → + New user → Create new user`

---

**Fill in the form:**

**Basics tab:**

| Field | Enter this |
|---|---|
| User principal name | `alex.lee` (the part before the @ symbol) |
| Mail nickname | `alex.lee` (auto-fills) |
| Display name | `Alex Lee` |
| Password | Tick "Auto-generate password" |
| Account enabled | Yes (ticked) |

Click **Next: Properties**

**Properties tab:**

| Field | Enter this |
|---|---|
| First name | Alex |
| Last name | Lee |
| Job title | Analyst |
| Department | Finance |
| Usage location | Your country |

> ⚠️ **Usage location is required** before you can assign licenses to a user. Always fill this in when creating users — you'll get an error later if you don't.

Click **Review + create** → **Create**

---

**Now find Alex in the user list.**

Go to `Identity → Users → All users`. You'll see Alex Lee listed. Click on the account.

Look at the **Properties** section on the Overview page:

- **Object ID** — Alex's permanent unique ID. This never changes.
- **User principal name** — `alex.lee@yourname.onmicrosoft.com`. This is the sign-in name.
- **Department** — Finance (you set this). This attribute drives dynamic group membership rules — we'll use it in the next module.
- **Account enabled** — Yes

Now look at the left menu on Alex's profile — notice the tabs: **Groups**, **Roles**, **Licenses**, **Devices**, **Sign-in logs**. Each of these will become important as you progress through the series.

Right now: no groups, no roles, no licenses, no devices. A blank identity.

---

**Sign in as Alex.**

Open a new **incognito / private browser window** (important — use a separate window so you don't sign out of your admin account).

Go to `portal.office.com`. Sign in as `alex.lee@yourname.onmicrosoft.com`.

You'll be prompted to change the auto-generated password. Set a new one — something you'll remember, like `Learning@2024!`.

What does Alex see? Almost nothing — a largely empty Microsoft 365 home page with no apps. This is expected. Alex has no licenses assigned, so no apps are available.

That empty screen is your starting point. Over the next modules you'll assign licenses, add Alex to groups, grant app access, configure MFA, and apply security policies. By the end of Unit 4, you'll control exactly what Alex can access and from where.

---

**Check Alex's sign-in in the logs.**

Back in your admin browser:

`Identity → Monitoring & health → Sign-in logs`

Wait 1–2 minutes, then filter by:
- **User** = `alex.lee`

Find the sign-in. Click on it. Look at each tab:

- **Basic info** — sign-in time, app accessed (Office Portal), status (Success), authentication method used
- **Authentication Details** — shows Alex signed in with a password. No MFA — because you haven't required it yet.
- **Conditional Access** — empty or "No policies applied." Because you haven't created any policies yet.

That empty Conditional Access tab represents a security gap. Any user, any device, any location can sign in with just a password. Fixing that gap is what Unit 4 is about.

---

## The Scenario You're Building Toward

Here is a real scenario you should be able to handle completely by the end of Unit 4:

> **The new employee brief:**
> Jordan starts on Monday as a Finance Analyst.
> - Needs a user account
> - Needs Microsoft 365 access (email, Teams, SharePoint)
> - Should only be able to sign in using MFA — password alone is not enough
> - Should only be able to access company resources from a managed device
> - Their access should be reviewed every 90 days
> - Their account should automatically disable on their contract end date

Right now you can do step one: create the user account.

By the end of Unit 2 — users, groups, licenses all handled automatically.
By the end of Unit 3 — MFA required, no exceptions.
By the end of Unit 4 — managed device requirement enforced via Conditional Access.
By the end of Unit 7 — 90-day access review running automatically, contract end date handled.

Every module adds a layer to this scenario. Keep Jordan in mind as you build.

---

## ✅ Check Your Understanding

Go through this list. If you can't do something, go back and do it — don't just read it.

- [ ] Can you explain in one sentence what Entra ID does?
- [ ] Can you explain the difference between Entra ID and on-premises Active Directory?
- [ ] Can you navigate to Sign-in logs and find a specific user's sign-in?
- [ ] Do you know what an Object ID is and why it's used instead of a display name?
- [ ] Can you create a second test user (`morgan.chen`, Department: Engineering) from memory — without following these instructions?

That last one matters. If you need to re-read the steps, do it again until you don't.

---

## Common Questions

**Q: Is this actually free?**
Yes. The Microsoft 365 Developer Program is genuinely free. Microsoft offers it so developers and learners can build and test in a real environment. No credit card, no trial period — just sign in occasionally to keep it active.

**Q: What if my tenant expires?**
You can create a new one and start fresh. Your learning doesn't depend on the tenant — it depends on the skills you're building. Tenants are replaceable.

**Q: Do I need to know PowerShell?**
Not yet. We introduce PowerShell gradually. The first few units use only the admin portal. PowerShell gets introduced in Unit 2 as a second way to do things you already know how to do in the portal — which is the right order to learn it.

**Q: Can I use an existing Microsoft 365 tenant instead of the dev tenant?**
You can — but be careful. Some labs in this series involve changing security policies. Doing that in a real production tenant with real users is risky. The developer tenant is the safe, consequence-free environment to learn in.

---

## What's Next

**Module 1.2 — Understanding Tenants**

You created a user. You toured the admin center. In the next module we go one level deeper: what exactly *is* a tenant, who owns it, what lives inside it, and why some early decisions about your tenant are very difficult to change later.

---

> 📚 **Entra ID — Zero to Admin** · Unit 1: Getting Started
>
> ← *Start of series* | [🏠 Series Home](#) | [Module 1.2 — Understanding Tenants →](./1-2-understanding-tenants.md)
