# ID Protection: Entra ID's Automated Threat Response System

**Part of Entra ID Glossary Series: Glossary#7.4 - ID Protection**

---

A security analyst joined a company that had 12,000 users and one person managing identity security part-time. Before he'd found a way to review sign-in logs manually at scale, he enabled ID Protection and connected it to Conditional Access.

Two weeks later, ID Protection had automatically blocked 47 high-risk sign-in attempts, flagged 3 accounts with leaked credentials from external breach databases, and generated 12 medium-risk events that his investigation confirmed were legitimate users traveling internationally.

He hadn't reviewed a single event in real time. The automated response handled everything. When he came in each morning, the dashboard showed him what had happened and what remained for investigation. The signal-to-noise ratio was manageable because the automated policies had already acted on the clear-cut cases.

## 🛡️ What ID Protection Is

Microsoft Entra ID Protection is the risk detection and response engine built into Entra ID. It's not a separate product you install. It's a capability that activates when you have the right licensing (Entra ID P2 required for the full feature set; P1 has limited access).

ID Protection does three things:

**Detects risk** 🔍: Evaluates every sign-in and continuously monitors user accounts for indicators of compromise. The detection uses machine learning, behavioral baselines, and Microsoft's global threat intelligence from processing billions of authentications daily.

**Provides investigation tools** 📊: Surfaces detected risks through the Identity Protection dashboard with enough context to determine whether an event represents genuine compromise or a false positive.

**Enables automated response** 🤖: Integrates with Conditional Access so that detected risk triggers automatic policy enforcement, without requiring a human to review every event before acting.

The combination is what makes it operationally viable. Detection alone produces a log that requires staff to act on. Detection plus automated response means the clear-cut cases are handled immediately while investigation resources focus on the ambiguous ones.

## 🔍 The Detection Engine

ID Protection generates two types of risk events:

**Sign-in risk detections** target specific authentication events. Impossible travel, unfamiliar sign-in properties, malicious IP addresses, anonymous proxies, token anomalies. These are assessed in real time during the sign-in, and Conditional Access can act on the result before the token is issued.

**User risk detections** target accounts. Leaked credentials found in breach databases, anomalous post-sign-in activity, suspicious behavior patterns that suggest the account itself is compromised. These persist across sessions until remediated.

Both types carry a confidence level (Low, Medium, High) based on the strength of the signals. The confidence level is what Conditional Access policies key off of when deciding how to respond.

Real-time detections can block a specific sign-in. Offline detections (analyzed after the fact, requiring more processing time) update the risk level retroactively and affect future access decisions.

## 📊 The Investigation Dashboard

The Identity Protection portal in the Entra admin center provides three key views:

**Risky sign-ins** 📋: All sign-in events flagged with a risk level, with details on the detection type, IP address, device, location, and the user's sign-in history for context. Sortable by risk level, user, date, or detection type.

**Risky users** 👤: All accounts currently carrying a user risk level, with the detection types driving the risk and the timeline of how the risk accumulated. The user risk level persists until dismissed or remediated.

**Risk detections** 🎯: The underlying detection events that drive sign-in and user risk, with the full details of what signal triggered each detection.

For each event, the dashboard provides investigation data and remediation options: confirm as compromised (adds weight to future risk signals), dismiss as safe (teaches the system this pattern is normal), or reset the user's password.

## 🔒 Connecting ID Protection to Conditional Access

ID Protection generates the risk signals. Conditional Access is what acts on them. The connection is through risk-based Conditional Access policies:

**Sign-in risk policy** 🚦: Condition set to "Sign-in risk is High/Medium/Low." Grant controls specify the response: block access, require MFA, require compliant device.

**User risk policy** 🚦: Condition set to "User risk is High/Medium/Low." Grant controls specify the response: require password change, require MFA, block access.

The recommended baseline configuration:
- Sign-in risk High: Block access
- Sign-in risk Medium: Require MFA
- User risk High: Require password change
- User risk Medium: Require MFA

This creates a fully automated response loop. Detection fires, Conditional Access responds, the user either satisfies the challenge or is blocked. No analyst needs to be in the loop for the high-confidence cases.

## ⚙️ Licensing and Capabilities

The full ID Protection feature set requires Entra ID P2 licensing. Key P2-only capabilities:

- Risky users report with full detection details
- User risk Conditional Access policies
- Risky sign-ins report with full detection details
- The ability to confirm or dismiss risk events
- Vulnerability and risk summary reports

Entra ID P1 provides some sign-in risk signals and sign-in logs but lacks the full user risk capabilities and investigation tools.

Without any Entra ID P2, organizations are effectively flying blind on identity risk. They have sign-in logs but no automated risk scoring or response capability.

## 💡 False Positive Management

Not every risk detection is genuine compromise. Legitimate users trigger false positives regularly: international travel flagged as impossible travel, VPN use flagged as anonymous IP, bulk project work flagged as anomalous activity.

The investigation workflow is designed for this. When you confirm a detection as a false positive and dismiss it as safe, the system learns. That user's travel patterns, VPN usage, or work habits become part of their behavioral baseline. Future similar events generate lower risk scores or don't trigger at all.

False positive rate drops over time as the system builds accurate baselines. New users and new behaviors generate more noise. Established patterns generate less.

---

💬 **When you first enabled ID Protection, what was the ratio of genuine attacks to false positives in the first month?** The initial calibration period is always noisier than steady state. What detection type generated the most false positives in your environment, and how long did it take to tune down?

#EntraID #IDProtection #IdentityProtection #RiskDetection #MicrosoftEntra #ConditionalAccess #ZeroTrust
<!-- nav -->

---

[← Risky User: When the Account Itself Is Flagged, Not Just One Sign-In](glossary-7-3-risky-user.md) | [Home](../README.md) | [Anomaly Detection: How Entra ID Learns What Normal Looks Like →](../7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-5-anomaly-detection.md)
