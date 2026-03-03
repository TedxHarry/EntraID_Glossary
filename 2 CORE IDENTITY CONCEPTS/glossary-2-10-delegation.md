# Delegation
*Giving People Just Enough Access, No More*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #2.10 - Delegation

---


The helpdesk team had one job that required admin access: resetting user passwords. That's it. Basic, common, essential. But the IT manager before me had solved this the easy way, just give them User Administrator. Problem solved.

Except User Administrator isn't just password resets. It's also the ability to create and delete user accounts, manage group memberships, assign licenses, and modify any non-admin user in the tenant. The helpdesk team had all of that capability sitting unused, ungoverned, and, if any of their accounts were compromised, exploitable.

Delegation is the answer to that problem. Give people exactly what they need, scoped to exactly where they need it, with nothing extra.

## 📌 Two meanings you'll encounter

Delegation shows up in Entra ID in two distinct contexts. Once you understand both, you'll hear the word differently depending on who's using it.

**Administrative delegation** is about giving a subset of admin capabilities to someone who isn't a tenant-wide administrator. A team lead can manage their own department's users. A regional IT person can reset passwords for their region. A helpdesk agent can unlock accounts but can't delete them. The capability is real, the scope is limited.

**Permission delegation** is the OAuth2 concept of an application acting *on behalf of* a signed-in user. The user authenticates, consents to what the app can do, and the app performs actions using the user's permissions, but only within the bounds of what that user is allowed to do. The app borrows a slice of the user's access.

Both are forms of delegation. Both answer the same underlying question: how do you give an actor (a person or an app) the minimum access needed for a specific purpose?

## 📖 Administrative delegation in practice

The tool that makes admin delegation work properly is **Administrative Units (AUs)** combined with scoped role assignments.

An Administrative Unit is a container that holds a subset of Entra ID objects, specific users, groups, or devices. You can then assign directory roles scoped to that AU. The role holder has full power of that role, but only over the objects inside the AU.

For the helpdesk scenario: I created an Administrative Unit called "Helpdesk-Scope" containing all non-admin user accounts. Then I assigned the Helpdesk Administrator role to the helpdesk team, scoped to that AU. Now they can reset passwords and manage authentication methods for every user in that container, and nothing else. They can't touch admin accounts, they can't manage groups, they can't see the full user list.

The old "User Administrator for everyone" situation dropped to a scoped role with a fraction of the blast radius. That's delegation done right.

You can also delegate specific tasks without using AUs, through built-in roles designed for narrower purposes. The **Authentication Administrator** can reset authentication methods for non-privileged users. The **License Administrator** can manage license assignments. The **Groups Administrator** manages groups without touching users or policies. Matching the right built-in role to the actual task is the first step, the AU scope is the second.

## 📌 Permission delegation (the OAuth 2.0 kind)

When an application signs a user in and then calls an API on their behalf, that's permission delegation.

Here's what happens mechanically: the user signs in and sees a consent prompt, "Allow this app to read your profile and email." They click yes. Entra ID issues a token to the app that says, in effect, "this app is authorized to do Mail.Read and User.Read on behalf of [this specific user]."

When the app calls Microsoft Graph with that token, Graph sees it's a delegated permission, it checks what the user is allowed to do, intersects that with what the app was granted, and allows or denies accordingly. The user's own access level acts as a ceiling. An app with delegated Mail.Read can't read emails from a mailbox the user doesn't have access to.

This is different from application permissions, where the app acts as itself with no user context. Delegated = acts as the user, within the user's limits. Application = acts independently, usually with tenant-wide scope.

## 💡 Why "just give them more" always costs you later

The reason delegation matters is the same reason least privilege matters: excess permissions don't sit harmlessly. They're risk waiting to be realized.

An overly-privileged helpdesk account that gets phished gives the attacker User Administrator across the entire tenant. An app with `Directory.ReadWrite.All` that has a vulnerability exposes every user's data. A regional admin with tenant-wide scope instead of a scoped role can accidentally delete objects outside their purview.

Delegation is what reduces those blast radii. It takes organizational work, identifying who needs what, building AUs, matching roles to tasks. But that investment in structure is always cheaper than the incident it prevents. 🛡️

---

🔗 **Related Terms:**
- [Glossary#2.6 - Directory Role](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-6-directory-role.md) (the roles used in administrative delegation)
- [Glossary#2.8 - Permission](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-8-permission.md) (the specific rights delegated in OAuth2 flows)
- [Glossary#6.10 - Access Request](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-10-access-request.md) (how users can request delegated access through Entitlement Management)
---

**Real question:** Does your helpdesk team have more directory role permissions than they actually use? If you're not sure, that's worth checking. Run a role assignment report for User Administrator and see who's in it, the answer might surprise you.
✍️ TedxHarry

<!-- nav -->

---

[← Role (Identity Role)](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-9-role-identity-role.md) | [🏠 Contents](/README) | [Admin Role →](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-11-admin-role.md)
