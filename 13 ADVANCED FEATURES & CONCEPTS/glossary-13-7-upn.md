# UPN (User Principal Name)
*The Sign-In Name That Looks Like an Email But Isn't Always One*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #13.7 - UPN (User Principal Name)

---


A user tried to sign in to Microsoft 365 with their company email address. It failed. They tried with their old username format. Also failed. IT took 20 minutes to figure out what was happening.

The user's email address was `sarah.jones@contoso.com`. Their UPN was `sjones@contoso.com`. The email and the UPN had different prefixes because the email naming convention changed after the user was originally onboarded.

To sign in to Microsoft 365, you use the UPN. Not the email address. Not the display name. Not the SAMAccountName from on-premises AD. The UPN.

For most users in well-maintained environments, the UPN and the primary email address are the same. When they're not, it causes confusion that IT spends real time resolving.

## 📋 What a UPN is

The User Principal Name is the primary sign-in identifier for a user in Entra ID. It follows the format `localpart@domain`, resembling an email address but serving a different function.

in Entra ID, the UPN serves as:
- The identifier users type when signing in to Microsoft 365, Azure, and Entra ID-integrated applications
- The unique identifier for the user within the tenant (though `objectId` is more stable for programmatic use)
- The synchronization target for on-premises AD users brought into Entra ID

The UPN must use a domain that's verified in the Entra ID tenant. You can't have a UPN suffix that uses a domain your organization doesn't own and has registered in Entra ID.

## 🔗 On-Premises UPN vs cloud UPN

In hybrid environments, the on-premises AD UPN synchronizes to Entra ID. This is straightforward when the on-premises UPN suffix is a public, routable domain that's verified in Entra ID.

The complication: many organizations originally set up Active Directory with a non-routable internal domain suffix: `contoso.local`, `corp.contoso.com` (where `.corp` isn't publicly registered). These non-routable suffixes can't be verified in Entra ID.

The solution: configure an alternate UPN suffix in on-premises AD (adding `contoso.com` as a verified suffix), update users' on-premises UPN to use the routable suffix, then synchronize. This is a significant change operation if the organization has thousands of users with `.local` UPNs.

The alternative: use Alternate Login ID. Configure Entra Connect to synchronize the user's email address as the UPN in Entra ID, even though the on-premises UPN uses the non-routable suffix. Users sign in with their email address. The UPN in Entra ID matches the email. The on-premises AD UPN remains unchanged. This avoids mass UPN changes but adds configuration complexity.

## ⚙️ UPN changes and their impact

Changing a user's UPN sounds like an administrative task. It creates downstream problems that take time to discover.

**Existing tokens are invalidated** 🔑: The UPN change triggers sign-in sessions to be invalidated. Users who are actively signed in to applications will need to re-authenticate.

**Applications that stored the UPN as a user identifier break** 💻: Applications that used the UPN (rather than the object ID) as the primary key for their user records now have a mismatch. The user's application record still has the old UPN. The new token has the new UPN. The application can't find the user.

**MFA registrations remain valid** ✅: The user's MFA methods are tied to the user object, not the UPN. Authenticator app, FIDO2 key, phone number registrations all survive a UPN change.

**SSPR registrations remain valid** ✅: Same as MFA. The self-service password reset configuration isn't tied to the UPN.

**Application-specific effects vary** 📋: SharePoint permissions, Teams team membership, and other application-level configurations that reference UPN (rather than object ID) may need updating.

The practical guidance: UPN changes should be rare, planned, communicated, and tested in a non-production environment for impact on key applications before rolling out broadly.

## 🔑 The alternate login ID option

For organizations where the UPN and email address diverge significantly (different prefix formats, non-routable suffix migration, or merged organization scenarios), the Alternate Login ID feature allows users to sign in with their email address even when the UPN is different.

With Alternate Login ID configured, Entra ID accepts the user's email address (the `mail` attribute, which can be different from the UPN) as a valid sign-in identifier. Users don't need to know their UPN; they sign in with the address they use for email.

Alternate Login ID has limitations for some on-premises scenarios (Kerberos authentication, some Exchange hybrid configurations) and should be tested thoroughly before deployment.

---

💬 **Has your organization had to tackle a non-routable UPN suffix migration or a UPN/email alignment project, and what was the most disruptive part of the change?** The `.local` domain UPN migration is one of the most commonly underestimated hybrid identity remediation projects. What's the approach you took to minimize disruption to users and dependent applications?
✍️ TedxHarry

<!-- nav -->

---

[← Real-Time Remediation](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-6-real-time-remediation.md) | [🏠 Contents](/README) | [OID (Object ID) →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-8-oid.md)
