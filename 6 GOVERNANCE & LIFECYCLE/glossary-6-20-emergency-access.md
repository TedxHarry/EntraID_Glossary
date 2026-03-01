# Emergency Access
*The Account You Hope You Never Need*

📚 **Part of Entra ID Glossary Series: Glossary#6.20 - Emergency Access**

---

An organization's Global Administrator was traveling when a Conditional Access policy change locked out all admin accounts. The policy required compliant devices. The admin was working from a hotel laptop. Non-compliant. Blocked.

Every other admin account was subject to the same policy. Nobody could sign in to fix the policy that was blocking everyone from signing in.

They called Microsoft support. The resolution took 6 hours.

A properly configured emergency access account would have resolved this in minutes.

## 🔑 What Emergency Access Accounts Are

Emergency access accounts (also called break-glass accounts) are highly privileged Entra ID accounts designed to be used only when normal administrative access is unavailable. They exist specifically to recover from scenarios where all regular admin accounts are locked out.

Common scenarios that make emergency access necessary:

- **Conditional Access misconfiguration**: A policy that blocks all admins, as above
- **MFA provider outage**: If all admins rely on a single MFA method and that provider has an outage, nobody can complete MFA to sign in
- **Forgotten admin credentials**: The only admin account's password is unknown and there's no recovery path without admin access to fix it
- **Account deletion**: An admin account is accidentally deleted and the recovery window has expired
- **Identity provider federation failure**: If Entra ID is federated to an external IdP and the IdP goes down, federated accounts can't authenticate

Emergency access accounts are the last resort that prevents the organization from being completely locked out of its own tenant.

## 🔒 How to Configure Emergency Access Accounts

Microsoft's recommended configuration:

**Create two accounts** 🔑🔑: Two separate accounts ensure that if one has a problem (password forgotten, account deleted), the other still works. They should not share any authentication method or recovery path.

**Global Administrator role**: Both accounts should have permanent, active (not PIM-eligible) Global Administrator assignment. In an emergency, you can't afford to wait for a PIM activation process.

**Cloud-only accounts**: Use accounts that authenticate directly against Entra ID, not through federation or sync from on-premises AD. If the on-premises infrastructure is unavailable, federated accounts can't authenticate.

**UPN in a managed domain**: The UPN should use your organization's verified domain but should not depend on any external authentication service.

**Exclude from Conditional Access**: Emergency access accounts must be explicitly excluded from all Conditional Access policies. A policy that blocks all users for any reason would otherwise defeat the purpose. Create a named group containing only the emergency accounts and exclude that group from every policy.

**Phishing-resistant MFA only**: Protect the accounts with FIDO2 hardware keys or certificate-based authentication. Not phone-based MFA (the phone could be lost, the number could be ported). Two FIDO2 keys per account, stored separately, in physically secure locations.

**Strong, randomly generated passwords**: Stored in secure physical locations (a sealed envelope in a safe, a physical vault), not in a password manager that an admin might be locked out of.

## 📊 Monitoring and Alerting

Emergency access accounts should never be used in normal operations. Any sign-in event from these accounts should trigger an immediate high-priority alert to the security team.

Configure a Log Analytics alert rule or a Microsoft Sentinel analytics rule:

```
SigninLogs
| where UserPrincipalName in ("emergency1@contoso.com", "emergency2@contoso.com")
| project TimeGenerated, UserPrincipalName, IPAddress, ResultType
```

An alert on any successful or failed sign-in to these accounts: successful means someone is using it (investigate why), failed means someone is attempting to use it (investigate who).

## ⚠️ The Access Review for Emergency Accounts

Emergency access accounts are typically excluded from Conditional Access, not subject to MFA challenges, and have permanent Global Admin. This makes them the most sensitive accounts in the tenant.

Quarterly access reviews for these accounts should verify:
- Both accounts still exist and are enabled
- Both still have Global Administrator
- The FIDO2 keys are physically accounted for
- No sign-in activity has occurred since last review
- The password is still secured in the physical location

## 💡 Test Them Before You Need Them

Many organizations set up emergency access accounts and never test them. When a real emergency occurs, they discover the password is wrong, the FIDO2 key is missing, or the account was accidentally included in a Conditional Access policy after all.

Test emergency access accounts quarterly: sign in with each account, verify the Global Admin access is functional, then sign out immediately. Update the audit record confirming they work.

---

💬 **Does your organization have tested, documented emergency access accounts?** The organizations that don't find out the hard way, usually at the worst possible time. What was the scenario that convinced your organization to take break-glass accounts seriously?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Identity Verification](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-19-identity-verification.md) | [🏠 Contents](/README) | [Shared Accounts →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-21-shared-accounts.md)
