# Admin Roles: The Keys to Your Tenant and Why You Need Far Fewer of Them

**Part of Entra ID Glossary Series: Glossary#2.11 - Admin Role**

---

The first thing I checked when I took over management of a new tenant was the Global Administrator list.

Eleven accounts. A company with 180 employees and eleven Global Administrators. I started going through the list. Two were people who'd left the company eight months earlier — their accounts were still enabled, still assigned Global Admin, still had valid passwords that had never been reset. One was a shared IT mailbox. `it@company.com`. No MFA. Global Admin. Password known by everyone who'd ever been on the IT team.

That shared mailbox had the keys to the entire tenant. Anyone who'd ever worked there and knew the email password — or found it in an old offboarding document — could have taken full administrative control of every user account, every application, every security policy in the organization.

Nobody had intended this. It had just accumulated over years, one assignment at a time.

## What Admin Roles Are

Admin roles in Entra ID are directory roles that grant administrative capabilities over the tenant — the ability to manage identities, policies, applications, and security settings. Every organization has at least a few people who need some form of admin access. The question isn't whether admin roles exist, it's how carefully they're assigned and protected.

At the top sits **Global Administrator** — unrestricted access to everything in the tenant and all Microsoft services connected to it. Global Admins can reset any password, assign any role, modify any policy, read any audit log, manage any application. In a breach scenario, a compromised Global Admin account is catastrophic. Microsoft's guidance is to have fewer than five, use them for break-glass scenarios and the most sensitive administrative tasks only, and protect them with the strongest available authentication methods.

That guidance exists for a reason. The eleven-admin tenant I described is unfortunately not unusual.

## The Specialized Roles That Should Replace Global Admin for Most Tasks

Before handing anyone Global Administrator, run through this list. There's almost always a specific role that covers exactly what they need.

**User Administrator** — create, read, update, delete users and groups. Manage licenses. Reset passwords for non-admin users. If someone's job is "manage the user accounts," this is usually the right role, not Global Admin.

**Helpdesk Administrator** — reset passwords and manage authentication methods for non-admin, non-privileged users. Narrower than User Administrator. Right for frontline IT support.

**Security Administrator** — read and configure security settings: Conditional Access policies, Identity Protection settings, security alerts, authentication methods. No user management powers.

**Conditional Access Administrator** — create and modify Conditional Access policies only. Useful when you want to separate policy management from broader security administration.

**Application Administrator** — manage app registrations and enterprise applications, including granting admin consent to API permissions. Be careful with this one — admin consent for `Directory.ReadWrite.All` is a significant privilege that Application Administrators can grant.

**Privileged Role Administrator** — assign and modify directory roles, including elevating others to Global Admin. Treat this almost like Global Admin itself.

**Authentication Administrator** — reset MFA methods and authentication settings for non-admin users. Can force re-registration of MFA. More focused than Helpdesk Administrator.

Matching the role to the actual job is the work. It takes more thought than "just give them Global Admin," but it produces a tenant you can actually audit and defend.

## Permanent vs. Eligible: PIM Changes Everything

Permanent role assignment means the role is active 24 hours a day, 7 days a week. The person has admin powers all the time, whether they need them or not. Most admin accounts have permanent assignments by default.

**Privileged Identity Management (PIM)** changes this model. With PIM, you make someone *eligible* for a role instead of permanently assigned to it. When they need to perform an admin task, they activate the role — optionally requiring MFA confirmation, approval from another admin, and a stated justification. The role is active for a defined time window, typically 1-8 hours, then it expires automatically.

The practical benefit: an admin's account isn't permanently holding Global Admin or Security Administrator. If that account is compromised during the hours they're not doing admin work — which is most hours — the attacker gets a regular user account, not a privileged one.

PIM requires Entra ID P2 licensing, but for any organization that takes privileged access seriously, it's the standard.

## Break-Glass Accounts: The Exception That Proves the Rule

After you've reduced Global Admins, scoped roles appropriately, and implemented PIM, you need exactly two accounts that are permanently Global Admin and excluded from all Conditional Access policies: break-glass accounts.

These exist for one purpose — recovering the tenant if normal admin access fails. PIM is down. MFA is broken. The normal admin accounts are locked out. You need a way in.

Break-glass accounts should be cloud-only (not synced from AD), use very long randomly-generated passwords stored physically and securely, have no MFA (by design, since they're for when MFA infrastructure fails), be monitored for any sign-in activity, and be tested for access occasionally without being used for anything else.

The right number of Global Admins for most organizations is two break-glass accounts plus a very small number of permanent admins who need that level of access. PIM handles the rest. 🔐

---

**Related Terms:**
- Glossary#2.6 - Directory Role (the full picture of directory roles beyond just admin roles)
- Glossary#2.10 - Delegation (how to give non-admins specific capabilities without full admin access)
- Glossary#6.13 - Just-in-Time Access (the PIM model of activating access only when needed)

---

**Check this now:** How many Global Administrators does your tenant have? Go to Entra admin center > Roles > Global Administrator > Assignments. If the number is higher than 5, you have work to do. What did you find?
<!-- nav -->

---

[← Delegation: Giving People Just Enough Access — No More](glossary-2-10-delegation.md) | [Home](../README.md) | [Authentication: The Question Behind Every Sign-In →](../3%20AUTHENTICATION/glossary-3-1-authentication.md)
