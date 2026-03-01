# Risky Sign-In
*When the Authentication Looks Suspicious*

📚 **Part of Entra ID Glossary Series: Glossary#7.2 - Risky Sign-In**

---

A senior manager's credentials had been phished three weeks earlier. She'd clicked a link in a convincing email, entered her password on a fake login page, and didn't realize it had happened. The attacker hadn't acted immediately.

When they finally used the credentials, they signed in from a residential IP address in Eastern Europe. The manager's normal sign-in pattern was from a corporate office in the UK, on a managed Windows device. The new sign-in was from an Android device, an unfamiliar IP, using a browser the account had never used.

Entra ID flagged it as a high-risk sign-in before the attacker finished loading their inbox. The Conditional Access policy required a password reset from a trusted device. The attacker had the old password. They couldn't satisfy the challenge. They were blocked.

## 🔴 What Makes a Sign-In "Risky"

A risky sign-in is an authentication event that Entra ID ID Protection has flagged as potentially not coming from the legitimate account holder. The risk assessment happens in real time, during the authentication, before the access decision is made.

Risk assessment evaluates signals from the specific sign-in event:

- Where is the sign-in coming from? (IP address, geographic location)
- Is this location consistent with the user's history?
- What device type and browser are being used?
- Is the IP associated with known malicious activity?
- Does the timing create an impossible travel scenario with a recent legitimate sign-in?
- Is the sign-in from an anonymizing proxy or Tor exit node?

No single signal triggers a risk flag in isolation. The combination and confidence level of signals determines the risk level.

## 📊 The Three Risk Levels

Entra ID assigns one of three risk levels to a risky sign-in:

**Low** 🟡: Something looks unusual but not necessarily malicious. The sign-in is from a device or browser the user hasn't used before, but the location is familiar. Or the IP has weak threat signals. Conditional Access policies may prompt for MFA as a confirmation step.

**Medium** 🟠: More concerning signals. An unusual combination of factors, or moderate threat intelligence signals on the IP. Conditional Access policies typically require MFA to proceed.

**High** 🔴: Strong indicators of compromise. Impossible travel, known malicious IP, anonymous proxy, or multiple concerning signals combined. Conditional Access policies should block access and require password reset.

The level is Entra ID's confidence assessment. High doesn't mean certain compromise. Low doesn't mean safe. It's a risk signal, not a verdict.

## 🔒 Using Sign-In Risk in Conditional Access

Sign-in risk becomes useful when Conditional Access policies are built around it:

**The standard configuration**:
- If sign-in risk is High: Block access, require password reset to clear the user risk before re-access
- If sign-in risk is Medium or Low: Require MFA to complete the sign-in (confirms the legitimate user is present)
- If sign-in risk is None: Standard access per normal policies

This creates a graduated response: suspicious but not high-confidence events get stepped up to MFA. High-confidence events get blocked entirely. Legitimate users who trigger false positives can satisfy MFA to confirm their identity.

The MFA response for medium/low risk is the design: it lets legitimate users who happen to sign in from an unusual location (traveling, new device) confirm their identity and proceed, while blocking automated attacks that can't satisfy MFA.

## ⚠️ Real-Time vs Offline Detections

Not all risk detections happen at sign-in time. Entra ID has two types:

**Real-time detections**: Evaluated during the authentication, before the token is issued. Conditional Access can act on these in the same sign-in flow. Impossible travel is a real-time detection.

**Offline detections**: Analyzed after the sign-in has already completed, using signals that require more processing time (like correlating the sign-in against threat intelligence databases). These update the risk level of a sign-in retroactively. A sign-in that was processed as "no risk" may be reclassified as medium or high risk hours later when offline analysis completes.

Offline detections don't block the specific sign-in that triggered them (it's already done), but they update the user's risk level, which affects future access decisions.

## 💡 Investigating Risky Sign-Ins

When a sign-in is flagged as risky, the Identity Protection portal shows the details: the detection type, the risk level, the IP address, the device information, and the location. The sign-in logs provide the full authentication context.

Investigation should confirm whether the sign-in was legitimate or malicious:

- Contact the user: did they sign in from an unusual location at this time?
- Review the IP: is it associated with a corporate VPN, a travel hotel, or a known threat actor?
- Check for activity after the sign-in: were files downloaded, were settings changed?

If confirmed as compromised: dismiss the risk event as compromised (increases weight for user risk), require password reset, review all activity during the session.

If confirmed as legitimate: dismiss the risk event as safe (teaches the system this pattern is normal for this user).

---

💬 **Have you investigated a risky sign-in event and found it was a genuine attack rather than a false positive?** The investigation workflow differs significantly depending on the answer. What signals in the sign-in details made the call clear?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Risk Detection](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-1-risk-detection.md) | [🏠 Contents](/README) | [Risky User →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-3-risky-user.md)
