# Risk Detection: How Entra ID Knows Something Looks Wrong

**Part of Entra ID Glossary Series: Glossary#7.1 - Risk Detection**

---

A user signed in from Chicago at 9am. Two hours later, a sign-in attempt came from Singapore. No flight covers that distance in two hours. Nobody is in both places simultaneously.

Entra ID ID Protection flagged this automatically: impossible travel. Risk detection level: High. The Conditional Access policy for high sign-in risk triggered: block access, require password reset.

The user in Chicago never lost access. The sign-in from Singapore was blocked. The investigation confirmed it was a credential stuffing attempt using credentials from a previous data breach. The whole sequence, from detection to block, took seconds.

## 🔍 What Risk Detection Is

Risk detection is the automated process by which Microsoft Entra ID Protection identifies sign-in events and user accounts that show indicators of compromise or suspicious behavior. It's not rule-based in the traditional sense. It combines machine learning, Microsoft's global threat intelligence, and behavioral analysis to identify anomalies.

When Entra ID detects a risk, it creates a risk event that is attached to either the specific sign-in (sign-in risk) or the user account (user risk). These events become inputs to Conditional Access policies and to the Identity Protection dashboard for investigation.

## 📋 The Detection Categories

**Sign-in risk detections** apply to a specific authentication event:

🔴 **Impossible travel**: Sign-in from two locations with a time gap that doesn't allow for the physical travel between them. High confidence indicator of credential theft.

🔴 **Unfamiliar sign-in properties**: Sign-in from a device, browser, or location that the user has never used before. The system learns what "normal" looks like for each user and flags deviations.

🔴 **Malicious IP address**: Sign-in from an IP address known to Microsoft's threat intelligence as associated with attack activity, botnets, or anonymization services.

🟡 **Anonymous IP address**: Sign-in from a Tor exit node or other anonymous proxy service. Could be legitimate privacy use, could be an attacker masking their location.

🟡 **Atypical travel**: Similar to impossible travel but with longer time windows or lower confidence. Flagged as medium risk.

🔴 **Token issuer anomaly**: Abnormalities in the token issuance process that indicate potential token replay or token manipulation attacks.

**User risk detections** apply to the account itself, not a specific sign-in:

🔴 **Leaked credentials**: Microsoft's threat intelligence scans dark web forums, paste sites, and breach databases. When a username/password combination matching an Entra ID account is found in breach data, the account is flagged as high user risk.

🔴 **Anomalous user activity**: Patterns of activity after sign-in that are inconsistent with the user's historical behavior. Bulk file downloads, mass email sends, unusual administrative actions.

🟡 **Suspicious browser**: Sign-in from a browser that appears to be automated or that exhibits characteristics of an attack tool.

## 🌐 The Intelligence Behind It

Risk detection quality comes from the scale of Microsoft's visibility. Entra ID processes billions of authentications daily across millions of organizations worldwide. Patterns that are invisible at an individual organization's scale are clear at this scale.

When an IP address is used in an attack against one organization, that signal becomes part of the threat intelligence that protects every other organization. When a set of credentials appears in a breach database, every organization whose user has those credentials benefits from the detection.

Individual organizations couldn't build this. The shared intelligence model is a material security advantage of a cloud-based identity platform.

## 🔒 Risk Detections and Conditional Access

Risk detections are only valuable if they trigger something. The integration with Conditional Access is what gives them teeth:

- Sign-in risk level "High" → block access + require password reset before continuing
- Sign-in risk level "Medium" → require MFA to proceed
- User risk level "High" → require password change + MFA, or block until admin review

These policies mean detected risks are handled automatically, in real time, without requiring a security analyst to review and respond to each event manually. The high-risk sign-in from Singapore is blocked in milliseconds, not after a 2-hour alert triage cycle.

## 💡 Investigation Workflow

When a risk detection occurs, the Identity Protection dashboard provides investigation tools:

- The specific detection type and the signals that triggered it
- The sign-in details (IP, location, device, browser)
- The user's recent sign-in history for context
- Suggested remediation actions

For confirmed attacks, remediation actions include: confirm sign-in as compromised (adds weight to user risk), require password reset, block the user. For false positives: dismiss the risk event (signals that this pattern should not be risk-flagged for this user in future).

---

💬 **Has Entra ID ID Protection detected a genuine attack on an account in your organization?** The impossible travel detection is often the first one that makes people realize the scale of credential attacks happening in the background. What was the first risk detection that caught something real?

#EntraID #RiskDetection #IDProtection #ThreatIntelligence #MicrosoftEntra #IdentitySecurity #ZeroTrust
