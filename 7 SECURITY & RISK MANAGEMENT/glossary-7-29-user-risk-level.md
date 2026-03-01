# User Risk Level: Understanding the Number Behind the Flag

**Part of Entra ID Glossary Series: Glossary#7.29 - User Risk Level**

---

An admin opened the Identity Protection dashboard and saw 14 users at High risk level, 47 at Medium, and 312 at Low. She had an hour before a meeting. She needed to know: which ones actually required immediate action?

The answer wasn't "all the High ones." Two of the High risk users were on a penetration test the organization had contracted. Three of the Medium risk users had credentials in a breach database that matched their current passwords. One of the Low risk users had just signed in from the same IP as a confirmed attacker.

User Risk Level is an input to decision-making, not the decision itself. Understanding what drives each level and what it means changes how you respond.

## 📊 What User Risk Level Is

User Risk Level is a classification assigned by Entra ID ID Protection to a user account, representing the system's confidence that the account itself is compromised. It's separate from sign-in risk, which evaluates individual authentication events.

User risk is account-level. It persists until it's explicitly dismissed or remediated. A user who triggered a risk detection last week still has that risk level today unless something cleared it.

The three levels:

**Low** 🟡: Weak signals of potential concern. The account shows some anomalous signals but confidence in active compromise is limited. Examples: suspicious browser sign-in patterns, weak threat intelligence signals against the account's email address, atypical usage patterns that haven't risen to higher confidence levels.

**Medium** 🟠: More substantial signals. A combination of lower-confidence detections, or a single detection with moderate confidence. Examples: multiple unfamiliar sign-in properties over a short period, moderate threat intelligence signals, behavioral anomalies that are concerning but not definitive.

**High** 🔴: Strong indicators of account compromise. High confidence. Examples: credentials found in a confirmed breach database matching current account credentials, anomalous user activity indicating data exfiltration, token issuer anomalies suggesting active attack.

## 🔢 How the Level Is Calculated

User Risk Level is not a single score that crosses thresholds. It's the system's aggregate confidence assessment based on:

**Detection types present**: High-severity detection types (leaked credentials, anomalous user activity) carry more weight than lower-severity types (suspicious browser).

**Combination of signals**: Multiple medium-severity signals can combine to a High aggregate. A single High-severity detection produces a High level directly.

**Detection confidence**: Each detection has its own confidence assessment. Higher confidence detections contribute more to the level.

**Historical context**: The account's overall risk history affects how new signals are weighted.

Entra ID doesn't publish the exact scoring formula. The level reflects the system's assessment, not a precise calculation that can be independently verified.

## 🔒 Risk Level in Conditional Access

User Risk Level feeds directly into Conditional Access conditions:

**High user risk + Require password change**: The recommended response for high user risk. Block access until the user resets their password, which confirms the legitimate user is present and clears the compromised credential.

**Medium user risk + Require MFA**: Step up to MFA to confirm the legitimate user is present. Lower disruption than password change. Appropriate when there's concern but not confirmed compromise.

**Low user risk**: Often no automated response unless other conditions also apply. Low risk may feed into monitoring or logging rather than blocking.

The Conditional Access response should be calibrated to the level. Requiring password reset for Low risk creates excessive friction for a large number of false positives. Requiring only MFA for High risk (when credentials are confirmed leaked) is insufficient because the attacker may have MFA access through SIM swapping or phishing.

## 🔍 Investigating Risk Levels

The risk level tells you there's a signal. Investigation tells you whether it's real.

For each risky user, the Identity Protection portal shows:

- The detection types driving the risk
- The timeline of when detections occurred
- The sign-in history around the detection period
- Suggested investigation steps

**For leaked credentials** 🔑: The user's password matched credentials in breach data. The question is whether they've changed their password since the breach. If the current password is different from the leaked one, the leaked credential may no longer be usable. If it matches, immediate reset is required.

**For anomalous user activity** 📊: Review the specific activity. What was downloaded, accessed, or sent? Was there a legitimate business reason? Context often changes the assessment.

**For false positives**: Dismiss the risk event as "safe." This teaches the system this pattern is normal for this user and reduces future false positives for similar behavior.

## ⚠️ Risk Level Persistence

Unlike sign-in risk (which resets after a session), user risk persists until:

- An admin dismisses it as safe or confirmed compromised
- The user completes a remediation action specified by a risk policy (password reset, MFA)
- The risk detections age out (some detections have time-based expiry)

An account at High risk that no one has investigated or remediated stays at High risk indefinitely. This is by design: the risk doesn't go away because time passes. It goes away when someone addresses it.

---

💬 **What's your current process for triaging risky users in Identity Protection?** The gap between "we have Identity Protection deployed" and "we have a process for responding to risk events" is significant in many organizations. How often do you review the risky users list, and what's your SLA for investigating High risk accounts?
<!-- nav -->

---

[← Insider Risk: When the Threat Already Has a Badge](glossary-7-28-insider-risk.md) | [Home](../README.md) | [Sign-In Risk Level: Reading the Signals in a Single Authentication →](glossary-7-30-sign-in-risk-level.md)
