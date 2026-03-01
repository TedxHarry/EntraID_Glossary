# Account Lockout
*How Entra ID Stops Password Guessing Without Locking Out Real Users*

📚 **Part of Entra ID Glossary Series: Glossary#6.22 - Account Lockout**

---

An attacker ran a credential stuffing attack against an organization's sign-in endpoint: 50,000 username/password combinations, all purchased from a previous breach. The attack ran for 6 hours.

Result: 0 successful logins, 0 legitimate users locked out.

The defender I was working with asked how that was possible. On-premises Active Directory would have locked out accounts after 5 failed attempts. Entra ID Smart Lockout had blocked the attack without locking out a single real user.

The mechanism is different from on-premises, and understanding it matters for anyone troubleshooting sign-in failures or designing authentication policies.

## 🔒 How Entra ID Smart Lockout Works

Smart Lockout is Entra ID's protection against brute force and credential stuffing attacks. Unlike traditional lockout (lock the account after N failed attempts), Smart Lockout uses a more sophisticated approach:

**Familiar vs unfamiliar locations** 🌍: Entra ID distinguishes between sign-in attempts from locations the user has successfully authenticated from before (familiar) and new locations (unfamiliar). Failed attempts from unfamiliar locations count toward lockout faster than failed attempts from familiar ones.

**Separate lockout counters** 📊: The lockout counter for familiar locations is separate from the counter for unfamiliar locations. An attacker hitting the account from a data center in a country the user has never signed in from accumulates lockout counts against the unfamiliar counter, while the user's own sign-ins from their normal location are unaffected.

**Lockout duration increases with each lockout** ⏱️: The first lockout lasts 1 minute. Subsequent lockouts last progressively longer. Persistent attack attempts eventually result in multi-hour lockouts on the attacker's path while the legitimate user can still sign in normally.

The result: an attacker trying 50,000 passwords against an account hits lockout on the attacker's side without the legitimate user being blocked.

## 🔧 Configurable Lockout Settings

Entra ID Smart Lockout has two configurable values (available to organizations with Entra ID P1 or P2):

**Lockout threshold**: The number of failed sign-in attempts before the account is locked. Default is 10 failed attempts. Can be set lower for higher security environments (5 is common for sensitive accounts), but setting it too low increases false positives for users who mistype passwords.

**Lockout duration (seconds)**: The initial lockout duration. Default is 60 seconds. This is the minimum; Smart Lockout increases duration for repeated lockouts.

These are configured in the Entra admin center under Security > Authentication Methods > Password Protection.

## 🔑 Smart Lockout vs On-Premises Lockout

For organizations with hybrid environments (Entra Connect synchronizing on-premises AD to Entra ID), the lockout behavior is separate for each system:

- **Entra ID Smart Lockout**: Applies to cloud authentication attempts
- **On-premises AD lockout policy**: Applies to on-premises authentication attempts (Group Policy-configured)

Pass-through authentication (PTA) and federation scenarios add complexity: authentication happens against on-premises AD, so on-premises lockout policies apply. Entra ID Smart Lockout may not be the active control in these configurations.

For Password Hash Sync (PHS), authentication happens against Entra ID for cloud resources. Smart Lockout applies. On-premises AD lockout policies apply separately to on-premises resources.

## 🔍 Investigating Lockout Events

When a user reports they're locked out, the Sign-in Logs in Entra ID are the starting point. Filter by the user's UPN and look for failed sign-in events with error code **50053** (account locked) or **50055** (password expired).

A pattern of failed attempts from an unfamiliar IP address followed by a lockout event suggests an attack, not a user error. A pattern of failed attempts from the user's normal device and location suggests the user is entering the wrong password.

The distinction matters for the response:

- **Attack pattern**: Review the source IPs, check if other accounts show similar patterns, consider blocking the IP range in Conditional Access Named Locations. The user's password may need to be reset if credentials were confirmed as compromised.

- **User error pattern**: Reset the password, walk the user through successful sign-in, check if MFA method issues are contributing.

## ⚠️ What Admins Cannot Do

Entra ID does not provide an admin tool to manually unlock a locked account in the same way on-premises AD does (the "Unlock Account" checkbox). Smart Lockout durations expire automatically.

For a user who is locked out due to Smart Lockout, the options are:
- Wait for the lockout duration to expire (usually minutes)
- Reset the user's password, which clears the lockout state and allows sign-in with the new password

Resetting the password is the fastest resolution for a user who needs immediate access.

---

💬 **Have you investigated a Smart Lockout event and found it was an actual attack rather than a user error?** The sign-in logs tell the story clearly when you know what to look for. What was the attack pattern, and what did your response look like?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Shared Accounts](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-21-shared-accounts.md) | [🏠 Contents](/README) | [Password Reset →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-23-password-reset.md)
