# Password Hash Sync
*How On-Premises Passwords Work in the Cloud*

> **Difficulty:** 🟡 Intermediate

📚 **Part of Entra ID Glossary Series: Glossary#8.4 - Password Hash Sync**

---

## 🎯 TL;DR

- Password Hash Sync (PHS) syncs a hash of password hashes from AD to Entra ID
- It's the most resilient hybrid auth option — authentication happens in the cloud even if on-prem is down
- PHS also enables leaked credential detection — Microsoft can compare hashed passwords against breach databases


An administrator asked a question that I hear often: "If we sync our passwords to the cloud, doesn't that mean Microsoft has our passwords?"

It's a reasonable concern. The answer is no, and understanding why requires understanding what actually gets synchronized. It's not passwords. It's a transformed hash of a hash, processed in a way specifically designed so that the original password cannot be recovered from what's in the cloud.

That distinction matters for security architecture decisions in hybrid environments.

## 🔑 What Password Hash Sync Does

Password Hash Sync (PHS) is a feature of Entra Connect (and Cloud Sync) that enables hybrid users to authenticate against Entra ID using the same password they use on-premises, without requiring on-premises infrastructure to be available for every authentication.

Without PHS, a hybrid user's authentication against cloud services would need to contact on-premises AD infrastructure every time (Pass-Through Authentication) or be redirected to on-premises Federation Services (ADFS). Both approaches create a dependency on on-premises infrastructure for every cloud sign-in.

With PHS, Entra ID holds enough information to validate the user's password directly. Cloud authentication becomes independent of on-premises infrastructure availability.

## 🔐 What Actually Gets Synchronized

The process is specific and security-conscious:

1. On-premises AD stores passwords as an NT hash (MD4 of the Unicode password)
2. Entra Connect reads the NT hash from AD (requires Domain Controller access with appropriate permissions)
3. The NT hash is processed through a salted SHA256 HMAC algorithm
4. The result is synchronized to Entra ID over an encrypted TLS connection
5. In Entra ID, the value is stored as part of the user's authentication data

Microsoft never receives the original password. The NT hash from AD is not transmitted. What's stored in Entra ID is a derived value that:
- Cannot be reversed to recover the original password
- Cannot be used to authenticate against on-premises AD (it's not the AD hash)
- Is only usable by Entra ID's authentication system to verify submitted passwords

When a user signs in to a cloud service, Entra ID applies the same hash process to the submitted password and compares it to the stored value.

## 🔄 Sync Frequency and Propagation

PHS doesn't run on the same schedule as directory object sync. Password changes propagate more aggressively:

**Real-time propagation**: When a user changes their password in AD, Entra Connect detects the change and synchronizes the new hash within approximately 2 minutes. Users who change their on-premises password have that change reflected in Entra ID quickly.

**Initial sync**: When PHS is first enabled, all current password hashes are synchronized. This initial sync is a full pass of all in-scope user accounts.

**Ongoing delta**: Subsequent syncs capture only changed passwords, making the ongoing sync efficient.

## 🛡️ Security Implications and Benefits

**Leaked credentials detection** 🔍: Because PHS stores a representation of the password in Entra ID, ID Protection can compare that representation against breach databases. When credentials matching an Entra ID account appear in breach data, the system can generate a leaked credentials detection. This specific benefit is not available with Pass-Through Authentication or Federation, because the password representation doesn't exist in Entra ID.

**Resilience** 💪: Cloud services remain available even if on-premises infrastructure (domain controllers, PTA agents, ADFS) is offline. Users can sign in to Microsoft 365 even during an on-premises outage.

**Password Protection** 🔒: Entra ID Password Protection (which blocks commonly used and compromised passwords) can be enforced on-premises for synchronized users when PHS is enabled. The protection runs at the on-premises DC level and integrates with Entra ID's banned password list.

**Smart Lockout coordination** 🛡️: With PHS, Entra ID's Smart Lockout applies to cloud authentication. Attack patterns on cloud sign-ins are blocked without necessarily locking out the on-premises account.

## ⚠️ Considerations and Trade-offs

**On-premises AD as the source of truth**: With PHS, compromising on-premises AD potentially affects cloud identities. A domain admin who knows the hash extraction process could theoretically stage a pass-the-hash-style attack. This is a real concern for organizations with sophisticated threat models.

**Password sync latency**: The ~2-minute propagation window means there's a brief period after an on-premises password change where the old cloud password may still work. This is generally acceptable but worth knowing.

**Account disable propagation**: When an on-premises account is disabled, that state syncs to Entra ID through directory sync (not PHS). The disable propagation follows the normal sync schedule (up to 30 minutes). For security incidents requiring immediate account disable, admins should also disable the account directly in Entra ID to ensure immediate cloud effect.

## 💡 PHS as the Recommended Starting Point

Microsoft recommends Password Hash Sync as the default authentication method for most hybrid organizations. It provides the best balance of simplicity, resilience, and security features (leaked credentials detection, Smart Lockout, Password Protection).

Pass-Through Authentication and Federation are appropriate for specific requirements: regulatory mandates that passwords must not leave on-premises in any form, or existing ADFS investments where federation-specific features are in use.

---

💬 **When you evaluated authentication methods for your hybrid environment, what drove your decision between PHS, PTA, and Federation?** The "passwords in the cloud" concern often comes up during PHS evaluations. How did you address that concern, and did the leaked credentials detection capability factor into your decision?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Cloud Sync](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-3-cloud-sync.md) | [🏠 Contents](/README) | [Pass-Through Auth →](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-5-pass-through-auth.md)
