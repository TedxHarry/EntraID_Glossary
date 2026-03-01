# Multi-Factor Authentication: Why 99.9% Attack Prevention Still Has an Asterisk

**Part of Entra ID Glossary Series: Glossary#3.4 - Multi-Factor Authentication (MFA)**

---

Microsoft published a statistic that gets quoted constantly in security circles: enabling MFA blocks 99.9% of automated account compromise attacks. That number is real and remarkable.

What the headline doesn't say is that "MFA" covers a spectrum from "significantly better than a password" to "essentially unbreakable by remote attackers." The 99.9% figure applies across all MFA types. Against targeted attacks using real-time phishing or MFA fatigue techniques, the number for weaker MFA methods is much lower.

This article covers what MFA actually is, how it works in Entra ID, and what distinguishes the kinds that hold up under pressure from the kinds that don't.

## 🔑 The Three Factors

Authentication factors fall into three categories:

- 🧠 **Something you know:** password, PIN, security question
- 📱 **Something you have:** phone, hardware token, smart card, security key
- 👁️ **Something you are:** fingerprint, face, iris

Single-factor authentication uses one. Multi-factor authentication requires two or more from different categories.

The security gain comes from the combination. Stealing someone's password doesn't help if you also need their physical phone. Stealing their phone doesn't help if you need to know their password. The attacker has to successfully attack two independent systems simultaneously, which is dramatically harder than attacking one.

💡 Note: using a password plus a security question is not MFA. Two things from the same category ("something you know") don't count as two factors.

## ⚡ How MFA Works in Entra ID

When a Conditional Access policy requires MFA for a sign-in, here's what happens:

1. User provides their first factor (usually a password)
2. Entra ID pauses and issues an MFA challenge
3. The challenge goes to the user's registered authentication method (a push notification to Authenticator, a code from a TOTP app, a prompt on a FIDO2 key, etc.)
4. User responds to the challenge
5. Entra ID validates the response
6. Sign-in proceeds if valid, denied if not

The claim that MFA was satisfied gets recorded in the sign-in token. Conditional Access policies and individual applications can check that claim to verify MFA happened, and using which method.

## 🧱 MFA Fatigue: When Volume Becomes the Attack

MFA fatigue (also called push bombing) is an attack technique that became significantly more common in 2022-2023. The attack is straightforward:

The attacker has the user's password (from a breach, phishing, or guessing). They initiate repeated login attempts, triggering a flood of push notification approvals to the user's phone. Dozens of "Did you just sign in?" notifications arrive at all hours. Eventually, many users tap "Approve" just to make them stop.

⚠️ This attack has successfully compromised organizations including Uber in 2022. It requires no technical sophistication. It just requires patience and a stolen password.

**Entra ID's mitigations:**

**Number matching** requires the user to enter a number displayed on the sign-in screen into the Authenticator app before approving. A flood of identical notifications still arrives, but approving any of them requires actively typing a matching number, which the user won't have if they didn't initiate the sign-in. Microsoft enabled number matching by default in Authenticator starting in 2023.

**Additional context** shows the application name and geographic location in the push notification, making it obvious when an approval request is suspicious ("Sign in to Outlook from Minsk?" is harder to accidentally approve than a generic "Sign in?" prompt).

**Sign-in frequency limits** can force re-authentication after a set period, and Conditional Access can block sign-ins from impossible-travel locations before they ever reach MFA.

## 🎯 MFA Registration: The First Battle

MFA only works for users who have registered their authentication methods. In environments where registration isn't enforced, some percentage of users are signing in with password only, whether the policy intends it or not.

Two approaches to handle this:

**Registration campaign:** Entra ID can run an MFA registration nudge, prompting users who haven't registered during sign-in and giving them a limited number of skips before the requirement becomes mandatory.

**Combined registration:** The My Security Info page (mysignins.microsoft.com) lets users register all authentication methods in one place. You can require users to visit this page during onboarding.

Track registration coverage in Entra ID under Protection > Authentication Methods > User registration details. Until the number is at or very near 100%, you have users without MFA protection regardless of what your Conditional Access policies say.

## 📈 Which Accounts Should Require MFA First

If you're rolling out MFA to a tenant that doesn't have it yet, prioritize:

1. 👑 All administrator accounts, immediately, with phishing-resistant methods
2. 🔒 All users accessing sensitive applications (finance systems, HR data, admin portals)
3. 🌐 All users signing in from outside the corporate network
4. 🏢 All users, eventually

Administrators without MFA are the highest-value targets for attackers. Get that covered first, then expand.

---

💬 **Where is your organization on MFA coverage?** Are you at 100% for all users, or are there holdouts? What's been the biggest obstacle to full deployment?
<!-- nav -->

---

[← Authentication Methods: Not All Proof Is Created Equal](glossary-3-3-authentication-method.md) | [Home](../README.md) | [Passwordless Authentication: Fixing the Right Problem →](glossary-3-5-passwordless-authentication.md)
