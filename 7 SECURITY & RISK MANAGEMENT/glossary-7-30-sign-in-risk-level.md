# Sign-In Risk Level
*Reading the Signals in a Single Authentication*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #7.30 - Sign-In Risk Level

---


Two sign-in events. Same user account. Same credentials. Different risk levels.

Monday morning, 8:47am. Corporate office IP. Windows device. Chrome browser. The same combination the user has used 400 times in the past year. Sign-in risk: None. Access granted, no additional requirements.

Monday afternoon, 3:12pm. IP address in a country the user has never authenticated from. Android device. First time this browser identifier has been seen for this account. Sign-in from a residential IP with no commercial affiliation. Sign-in risk: High. Conditional Access blocks access. The user's legitimate session from the morning is unaffected.

The second sign-in was a credential stuffing attack. The attacker had the password. Sign-in risk assessment stopped them.

## 📊 What sign-in risk level is

Sign-in risk level is the classification assigned by Entra ID ID Protection to a specific authentication event, representing the system's real-time confidence that this particular sign-in is not coming from the legitimate account owner.

It's evaluated per sign-in, not per account. Each authentication attempt gets its own risk assessment. The same user can have a no-risk sign-in followed immediately by a high-risk sign-in if the circumstances change dramatically between them.

The evaluation happens during the authentication process, before the token is issued. Conditional Access can act on the result in the same sign-in flow: step up to MFA, block access, or allow through depending on the level and the policy.

## 🔢 The three levels

**Low** 🟡: Something looks slightly unusual but there's low confidence it represents a threat. Examples: the user is signing in from a device type they don't typically use, but from a familiar location. Or the IP has weak threat signals. Policies typically prompt for MFA to confirm identity.

**Medium** 🟠: More concerning signals in combination. An unusual device from an unfamiliar location, or moderate threat intelligence against the IP. Policies typically require MFA.

**High** 🔴: Strong confidence that this sign-in does not represent the legitimate user. Examples: impossible travel (the user signed in from London 20 minutes ago, this sign-in is from Singapore), malicious IP address, anonymous proxy, multiple high-confidence signals in combination. Policies should block and require password reset.

**None**: Normal sign-in, no unusual signals detected. Standard access policies apply.

## 🔍 What signals drive sign-in risk

Sign-in risk is assembled from multiple detection types evaluated simultaneously:

**Impossible travel** 🌍: The geographic distance between this sign-in and the previous successful sign-in, divided by the time between them, exceeds physically possible travel speed. High confidence indicator of credential theft.

**Unfamiliar sign-in properties** 🖥️: The device, browser, IP subnet, or location is new relative to this user's historical sign-in profile. The system learns normal for each user. Deviation from normal contributes to risk.

**Malicious IP address** 🔴: The IP has been associated with attack activity in Microsoft's threat intelligence data. Includes botnet infrastructure, command-and-control networks, and confirmed attacker-operated hosting.

**Anonymous IP address** 🕵️: Tor exit node or commercial VPN/proxy service that obscures the real IP. May be legitimate privacy use. May be an attacker masking their location.

**Token issuer anomaly** 🎟️: Abnormal characteristics in the token issuance process suggesting potential token manipulation.

**Password spray** 💧: Sign-in pattern consistent with a password spray attack: many failed attempts across multiple accounts from the same IP, then a successful attempt.

## 🔀 ⏱️ real-time vs offline

Not all sign-in risk detections happen instantly:

**Real-time detections** ⚡: Evaluated and available during the authentication. Impossible travel, unfamiliar sign-in properties, malicious IP, anonymous IP. Conditional Access acts on these in the same sign-in flow. The user is blocked or stepped up before the token is issued.

**Offline detections** 🕐: Analyzed after authentication completes, using signals that require additional processing time (correlating against threat intelligence databases, analyzing patterns across multiple sign-ins). These update the risk level of a completed sign-in retroactively. A sign-in processed as "Low risk" may be reclassified as "High" hours later.

Offline detections don't block the specific sign-in (it's already done). They update the user's risk score, which affects future sign-ins and may trigger alerts.

## 🔒 Using sign-in risk in conditional access

The standard configuration:

- High sign-in risk → Block access (or require password reset if combined with user risk)
- Medium sign-in risk → Require MFA
- Low sign-in risk → Require MFA (optional, depends on risk tolerance)
- No sign-in risk → Standard policies apply

The Medium + Require MFA design is intentional: it allows legitimate users who happen to sign in from an unusual location (traveling, new device) to confirm their identity and proceed. The MFA challenge stops automated attacks that don't have MFA access. Legitimate users who are actually traveling satisfy MFA and continue working.

High risk gets blocked rather than stepped up because at High confidence, a step-up challenge creates an opportunity for the attacker to attempt social engineering the user into approving MFA.

---

💬 **What's the most interesting high-risk sign-in you've investigated?** The impossible travel detections are often the clearest: the timeline makes it obvious an account is being used from two places simultaneously. But some of the malicious IP detections tell a more complex story about the infrastructure attackers are using. What did the investigation reveal?
✍️ TedxHarry

<!-- nav -->

---

[← User Risk Level](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-29-user-risk-level.md) | [🏠 Contents](/README) | [CA Template →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-31-ca-template.md)
