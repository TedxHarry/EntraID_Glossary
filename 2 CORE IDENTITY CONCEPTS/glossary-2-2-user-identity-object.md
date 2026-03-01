# The User Object: What's Actually Inside (And Why It Matters More Than You Think)

**Part of Entra ID Glossary Series: Glossary#2.2 - User (Identity Object)**

---

"Just create a user" is one of those phrases that sounds simple until you've done it wrong a few times.

I've seen user accounts created with the wrong UPN domain and then locked out of their own email. Accounts where the display name and the actual mailbox name don't match, causing calendar invite confusion for months. Accounts that were created enabled when they should have started disabled. Accounts where the usage location was missing and licenses couldn't be assigned.

None of these are exotic failure modes. They're what happens when you treat user creation as a form to fill out rather than understanding what the object actually is and which fields actually drive behavior.

So let's open the hood.

## A User Is a Directory Object with Over 100 Attributes

When you create a user in Entra ID, you're creating a directory object — a structured record with dozens of properties. Most of them you'll never touch. But the ones you do touch matter.

Here's what actually drives how the account works:

---

**UserPrincipalName (UPN)**
This is the user's sign-in identifier. Format: `firstname.lastname@yourdomain.com`. It's used for authentication — when someone types their username on the sign-in page, this is what Entra ID matches against.

Common mistake: the UPN domain has to be a verified domain in your Entra ID tenant. If you add `@contoso.com` as the UPN suffix but `contoso.com` isn't verified in your tenant, things go wrong — especially in hybrid environments where AD and Entra ID UPNs need to match.

**Mail / ProxyAddresses**
The email address. Often the same as the UPN, but not always. In Exchange-connected environments the `proxyAddresses` attribute holds all email aliases. This is separate from the UPN and can trip up hybrid sync configurations.

**Object ID**
The immutable unique identifier assigned by Entra ID. Never changes. Never reused. If you're building any integration that references users, build it against Object ID, not display name or email. People change their names and email aliases. The Object ID doesn't move.

**AccountEnabled**
True or false. If false, the user can't sign in, period. Doesn't matter if their credentials are correct, their device is compliant, or Conditional Access says go — a disabled account is blocked at the first step. This is the right way to handle offboarding: disable before delete, because deletion is permanent and you often need to recover access to data.

**UsageLocation**
A two-letter country code. Easy to overlook, impossible to ignore when you need to assign licenses. Microsoft 365 licenses are usage-location-dependent due to data residency and legal requirements. If the usage location isn't set, you can't assign most licenses. I've seen new hire onboarding break on exactly this.

**AssignedLicenses**
What Microsoft 365 and other Microsoft subscriptions the user has. Licenses unlock features — no Exchange Online license, no mailbox. No Entra ID P2 license, no Privileged Identity Management or Identity Protection.

---

## Member Users vs. Guest Users

All user objects in Entra ID have a `userType` property. Two values matter:

**Member** — a user homed in your tenant. Typically your employees. Full directory read access by default. Can be assigned roles, licenses, and app access without restriction.

**Guest** — a user from outside your organization, invited via B2B collaboration. Their identity is managed by their home tenant or identity provider (Google, email OTP, etc.). Your tenant holds a reference to them. By default, guests have limited directory read access — they can't enumerate all users and groups, for example.

This distinction matters for Conditional Access. You can write policies that apply to members only, guests only, or both. You can require guests to always use MFA while giving members more flexibility based on device trust. Knowing which `userType` you're targeting is a basic requirement for policy authoring.

## The UPN vs. Email Confusion

Let me save you the hour I lost on this during my second month working with hybrid identity.

In an on-premises Active Directory world, users have:
- A **SAMAccountName** (old-style logon: `DOMAIN\username`)
- A **UserPrincipalName** (`user@domain.com`)
- A **mail** attribute (their actual email address)

These *can* all be the same but often aren't, especially in organizations with legacy naming conventions. When syncing to Entra ID, the UPN from AD becomes the UPN in Entra ID — and that's the sign-in username.

If the AD UPN is `jsmith@contoso.local` (an internal domain, not internet-routable) and their email is `john.smith@contoso.com`, the user's Entra ID sign-in won't work with their email address. The UPN needs to be updated to a verified domain before sync.

This is one of the most common hybrid identity headaches, and it's entirely preventable if you check UPN domains before you start syncing.

## When a User Can't Sign In: Your First Four Checks

The account is the foundation. When access breaks, start here before reaching for more complex explanations:

1. **Is `accountEnabled` true?** Disabled accounts fail silently to the user — they just get an error.
2. **Is the UPN domain verified in the tenant?** An unverified domain means authentication fails.
3. **Is the right license assigned?** No license, no service.
4. **Is `usageLocation` set?** Missing, and license assignment fails with a cryptic error.

Four checks. Covers a substantial majority of basic user access problems. 👤

---

**Related Terms:**
- Glossary#2.1 - Identity (the broader concept the user object is an instance of)
- Glossary#2.4 - Group (how users are organized for access management at scale)
- Glossary#6.1 - User Provisioning (how users get created automatically)

---

**Tell me:** What's the most unexpected user attribute issue you've had to troubleshoot? The UPN domain mismatch? A missing usage location blocking licenses? Or something stranger? I've seen some creative ones over the years.

#EntraID #IdentityManagement #MicrosoftEntra #CloudSecurity #Microsoft365 #ITAdmin #BeginnerContent
