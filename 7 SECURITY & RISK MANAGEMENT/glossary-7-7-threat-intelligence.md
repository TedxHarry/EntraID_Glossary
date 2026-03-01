# Threat Intelligence: Why Entra ID Knows an IP Is Bad Before You Do

**Part of Entra ID Glossary Series: Glossary#7.7 - Threat Intelligence**

---

An IP address showed up in a sign-in log. The security team had never seen it before. There was no obvious reason to flag it. It was registered to a hosting provider in Germany. The sign-in had used correct credentials. MFA was satisfied.

But Entra ID had blocked the sign-in as high risk. The reason: the IP address had been used in attacks against 47 other organizations in Microsoft's tenant ecosystem over the previous 72 hours. Microsoft's threat intelligence had already classified it as malicious. The organization's team couldn't have known. They had no visibility into those other 47 organizations.

Their sign-in logs would have shown a successful authentication. Microsoft's logs showed an IP with a confirmed attack history trying it again.

## 🌐 What Threat Intelligence Is in Entra ID

Threat intelligence in Entra ID ID Protection is the feed of external indicators that inform risk assessments. It's the data about known malicious infrastructure, attack campaigns, and compromised credential sets that Microsoft aggregates across its global footprint.

When Entra ID evaluates a sign-in, it doesn't only look at your organization's data. It incorporates intelligence about:

- IP addresses and ranges associated with attack activity
- IP addresses used by known botnets, command-and-control infrastructure, and anonymization services
- Credential sets found in breach databases matching your tenant's accounts
- Attack patterns and techniques currently active in the threat landscape

This external intelligence is what makes risk detection useful. Any single organization sees a tiny slice of the attack traffic targeting Microsoft's identity platform. Microsoft sees all of it.

## 📊 The Scale Advantage

Entra ID processes billions of authentications per day across millions of organizations worldwide. This scale creates an intelligence feedback loop that no individual organization can replicate:

When an IP address is used in an attack against one organization and the attack is detected, that IP is flagged in the threat intelligence system. The next time that same IP attempts a sign-in against any other organization in the ecosystem, the risk score already reflects the known malicious history. The second organization benefits from the first organization's detection without any direct sharing of their data.

This is the material security advantage of a cloud-based identity platform over on-premises alternatives. An on-premises Active Directory deployment has visibility into what happens against your domain. It has no visibility into attacks against anyone else's infrastructure.

## 🔍 How Threat Intelligence Feeds into Risk Detection

The threat intelligence layer contributes to several specific risk detections:

**Malicious IP address** 🔴: Sign-in from an IP that Microsoft's threat intelligence has classified as actively malicious. Associated with attack campaigns, botnet infrastructure, or confirmed attacker-controlled hosting. This is a high-confidence signal and generates a high risk score.

**Anonymous IP address** 🟡: Sign-in from Tor exit nodes or other anonymous proxy services. Could be legitimate privacy use. Could be an attacker masking their location. The threat intelligence can sometimes differentiate between high-confidence anonymization infrastructure and potentially legitimate VPN services, which affects the risk level assigned.

**Atypical travel + IP reputation** 🟡: When unusual travel is combined with an IP that has some threat signals, even if not confirmed malicious, the combined score is higher than either signal alone.

**Leaked credentials** 🔴: The breach database monitoring described in the previous article. This is threat intelligence applied to credential data rather than network infrastructure.

## 🔒 Named Locations vs Threat Intelligence

Organizations can configure Named Locations in Conditional Access: IP ranges and countries that are explicitly trusted or explicitly blocked. Named Locations are organization-defined policy decisions.

Threat intelligence is different. It's Microsoft's continuously updated assessment of infrastructure across the entire ecosystem. An IP that falls within a Named Location your organization has marked as trusted but that Microsoft's threat intelligence has flagged as malicious will still generate a risk signal. The risk assessment considers both.

The combination is intentional: Named Locations handle what your organization knows about your own network topology. Threat intelligence handles what Microsoft knows about the broader attack ecosystem that your organization can't see.

## ⚠️ What Threat Intelligence Doesn't Tell You

Threat intelligence signals are probabilistic, not deterministic. A malicious IP flag means "this IP has been associated with attack activity." It doesn't mean "the user signing in from this IP is an attacker."

Legitimate scenarios can generate IP reputation hits:

**Corporate VPNs with shared egress**: If your organization uses a VPN service whose exit IPs have been used by other customers for malicious purposes, your users' traffic may show risk signals even though they're legitimate.

**Cloud provider IPs**: Some cloud provider IP ranges are associated with both legitimate automated testing and attack infrastructure. An IP in these ranges may carry risk signals even for benign traffic.

**Geographic restrictions**: Blocking sign-ins from countries where your organization has no presence is a legitimate policy, but it's implemented via Named Locations (country blocking), not threat intelligence.

The response to threat intelligence signals should be calibrated investigation, not automatic assumption of compromise. The risk level indicates confidence, not certainty.

## 💡 The Intelligence Gap for Novel Attacks

Threat intelligence is reactive by nature. It's built from observed attack behavior. New infrastructure, new techniques, and new attack campaigns that haven't been seen yet won't appear in threat intelligence feeds until they're detected.

This is why threat intelligence works alongside behavioral analysis and anomaly detection rather than replacing them. Known-bad infrastructure is caught by threat intelligence. Novel attacker behavior on unknown infrastructure gets caught by behavioral analysis. Neither is sufficient alone.

---

💬 **Have you ever investigated a sign-in that was flagged for malicious IP and traced the IP back to infrastructure you recognized as legitimate, like a shared VPN exit node or a cloud provider range?** The false positive scenarios from IP reputation are specific and predictable once you've seen them. What was your approach to resolving it without weakening the detection for genuine threats?
<!-- nav -->

---

[← Leaked Credentials: When Your Password Shows Up on the Dark Web](glossary-7-6-leaked-credentials.md) | [Home](../README.md) | [Conditional Access: The Policy Engine That Makes "Never Trust, Always Verify" Real →](glossary-7-8-conditional-access.md)
