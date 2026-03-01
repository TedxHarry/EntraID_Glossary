# Risky User
*When the Account Itself Is Flagged, Not Just One Sign-In*

📚 **Part of Entra ID Glossary Series: Glossary#7.3 - Risky User**

---

The IT team got the alert on a Tuesday morning. An account in their tenant had been flagged as high user risk. The reason: Microsoft's threat intelligence had found the account's credentials in a fresh breach database published on a criminal forum the night before.

The user hadn't done anything wrong. They'd reused a password from a personal account that had been compromised in a breach of a different service entirely. Their corporate credentials weren't leaked from the corporate environment. They were leaked from a gaming site they'd signed up for five years ago with the same password.

The user risk flag caught it before anyone tried to use those credentials. The Conditional Access policy for high user risk blocked sign-in and required a password reset. The password was changed before any attacker had a chance to try it.

## 👤 User Risk vs Sign-In Risk

Understanding risky user requires understanding what makes it different from risky sign-in:

**Sign-in risk** is assessed per authentication event. Did this specific sign-in look suspicious? It evaluates the signals from a single login attempt: the location, the IP, the device, the behavior during that session.

**User risk** is assessed at the account level. Has something happened that suggests this account itself is compromised, regardless of what the current sign-in looks like? It persists across sessions. A user can have a high risk level even if their most recent sign-in from a familiar location on a trusted device looks completely clean.

The distinction matters because some compromises don't show up in sign-in signals at all. Credentials found in a breach database are a perfect example: the attacker isn't trying to sign in yet. The account is already at risk. Sign-in risk won't catch it until an attack is actually attempted.

## 🔴 What Drives User Risk

Entra ID ID Protection generates user risk from several detection types:

**Leaked credentials** 🔑: Microsoft's threat intelligence continuously monitors dark web forums, paste sites, and breach databases. When a username/password combination matching an Entra ID account is discovered in breach data, the account is flagged as high user risk. This is the most common high-severity user risk detection.

**Anomalous user activity** 🚨: Patterns of activity after sign-in that are inconsistent with the user's historical behavior. Bulk file downloads, mass email sends to external recipients, unusual administrative actions, accessing data outside the user's normal patterns. These behaviors after authentication suggest the account is being used by someone other than the legitimate owner.

**Possible attempt to access Primary Refresh Token** 🎫: Suspicious activity suggesting an attacker may be attempting to steal the user's PRT, which would give persistent access without requiring the password.

**Anomalous token** 🎟️: Abnormal token claims or usage patterns suggesting token theft or replay.

User risk is cumulative. Multiple medium-severity signals on the same account can push the aggregate user risk to high, even if no single signal would qualify on its own.

## 📊 User Risk Levels

Like sign-in risk, user risk is assessed as Low, Medium, or High. Unlike sign-in risk (which can drop to None after a session ends), user risk persists until it's explicitly cleared.

**Low** 🟡: Some signals of concern but low confidence of active compromise. May prompt for MFA or password change depending on policy.

**Medium** 🟠: More significant indicators. Conditional Access policies typically require MFA and may restrict access to sensitive resources.

**High** 🔴: Strong indicators of account compromise. Conditional Access policies should block access entirely and require a password reset before re-access is allowed.

High user risk doesn't automatically resolve. An account flagged at high risk stays high risk until the risk is remediated and either the admin dismisses it or the policy-required remediation (password reset) has occurred.

## 🔒 User Risk in Conditional Access

The standard Conditional Access configuration for user risk mirrors the sign-in risk approach but responds to the account-level risk:

- If user risk is High: Require password change (not just MFA, because MFA confirms the user but doesn't change the compromised credential). Block access until the password is reset.
- If user risk is Medium or Low: Require MFA as confirmation.

The critical design point for high user risk: requiring only MFA isn't enough. If credentials are confirmed leaked, an attacker who has the password can potentially satisfy MFA through social engineering or SIM swapping. The password itself needs to change. The Conditional Access policy should require a password reset to clear the risk state.

When a user resets their password through SSPR in response to a user risk policy, the risk state is automatically cleared (or reduced, depending on configuration). The reset confirms the legitimate user was present and changes the compromised credential.

## 💡 Investigating and Remediating Risky Users

The Identity Protection portal lists all users currently flagged with risk, their risk level, and the detection types driving the risk. For each risky user, the investigation should determine whether the risk is genuine or a false positive.

**For confirmed compromise**:
- Block the user immediately to stop ongoing access
- Require password reset (clears the compromised credential)
- Review all activity since the account was first at risk: what was accessed, what was changed, what was sent
- Check for persistence mechanisms: new MFA methods registered, new app consents granted, forwarding rules created in email
- Dismiss the risk event as "confirmed compromised" (this increases the weight of user risk signals and improves detection accuracy)

**For false positives**:
- Investigate why the detection fired: was it a legitimate bulk download for a project, travel that looked anomalous, credentials shared with a personal account that appeared in breach data?
- If confirmed legitimate: dismiss the risk event as "safe" (this teaches the system what normal looks like for this user)

## ⚠️ The Delay Problem

Some user risk detections are offline: they're generated after analysis that takes hours to complete. An account can have been at risk for hours before the risk level appears in the portal. When risk is confirmed, reviewing the full window of access since the detection period began (not just since the alert appeared) is important.

---

💬 **Have you had an account flagged for leaked credentials that were actually from an external breach, not your environment?** The credential reuse scenario is one of the most common user risk detections. How did you handle the conversation with the user about why their work account was at risk because of a gaming site they'd forgotten about?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Risky Sign-In](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-2-risky-sign-in.md) | [🏠 Contents](/README) | [ID Protection →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-4-id-protection.md)
