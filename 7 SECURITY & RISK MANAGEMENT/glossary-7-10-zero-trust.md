# Zero Trust
*The Security Model That Stopped Trusting Your Network*

**Part of Entra ID Glossary Series: Glossary#7.10 - Zero Trust**

---

The breach happened inside the perimeter. An attacker had gotten a foothold through a phishing email, established persistence on one endpoint, and spent three months moving laterally through a network that treated all internal traffic as trusted.

When the forensics team reconstructed the timeline, they found the attacker had used legitimate credentials, accessed legitimate systems through legitimate paths, and done it all from inside the network that the firewall was protecting. The perimeter model had assumed everything inside was safe. The attacker had exploited that assumption.

Zero Trust is the answer to exactly this scenario. Not a product. Not a feature. A different assumption about what "secure" means.

## 🏗️ The Principle

Zero Trust starts from three core principles, stated plainly:

**Verify explicitly** ✅: Don't assume trust based on network location. Authenticate and authorize every request using all available signals: identity, location, device health, service, workload, data classification, and anomalies.

**Use least privilege access** 🔑: Limit user access with just-in-time and just-enough-access, risk-based adaptive policies, and data protection. Users should only have access to what they need for the task at hand.

**Assume breach** 🚨: Design systems as if the attacker is already inside. Minimize blast radius, segment access, encrypt everything, use analytics to detect anomalies, and drive to improvement through verification.

The perimeter model's failure was the first principle. It authenticated users at the perimeter and then trusted them implicitly for everything inside. Zero Trust removes that implicit trust entirely.

## 🌐 Why the Perimeter Model Broke Down

The perimeter model made sense when:
- All users worked in the office
- All data lived in on-premises data centers
- All access happened through corporate-controlled endpoints
- The network edge was a real boundary that could be defended

None of those things are true anymore:
- Users work from home, hotels, airports, client sites
- Data lives in cloud services, SaaS applications, personal devices, partner systems
- Endpoints include personal phones, unmanaged devices, BYOD laptops
- The "network" is a mix of corporate LAN, home broadband, mobile data, and VPN

When the perimeter dissolves, the assumption that "inside the network = safe" becomes dangerous. The attacker doesn't need to breach the firewall. They need to compromise one endpoint, steal one set of credentials, or get one user to click one phishing link. Then they're "inside."

## 🔒 Identity as the New Control Plane

In a Zero Trust architecture, identity replaces the network as the primary trust boundary. Instead of asking "is this traffic coming from inside our network?", the system asks "is this identity verified, authorized, and accessing resources in a manner consistent with policy?"

This shifts where security controls live:

**Authentication is continuous, not one-time** 🔄: Verified at sign-in and re-evaluated throughout the session based on risk signals. Continuous Access Evaluation (CAE) revokes tokens in near-real-time when conditions change.

**Authorization is contextual** 📋: Access decisions consider the full context of each request. The device's health status. The user's current risk level. The sensitivity of the resource being accessed. The authentication method used.

**Least privilege is enforced, not assumed** 🛡️: Users have access to the specific resources their role requires, granted for the duration they need it, reviewed and recertified regularly.

## 🔧 How Entra ID Implements Zero Trust

Entra ID is the identity plane of a Zero Trust architecture. Its components map directly to Zero Trust principles:

**Conditional Access** implements "verify explicitly" by evaluating every access request against conditions before granting access. Device compliance, sign-in risk, user risk, location, authentication strength.

**ID Protection** provides the risk signals that make contextual verification possible. Real-time detection of compromised credentials, suspicious behavior, and threat intelligence.

**PIM (Privileged Identity Management)** implements "use least privilege" by requiring just-in-time elevation for privileged roles. Administrators don't hold standing access to high-privilege roles. They activate time-bound access when needed.

**Access Reviews** implement ongoing verification that access assignments remain appropriate. Not just verifying identity at access time, but verifying that the access itself is still justified.

**Managed Identities and workload identities** remove human credentials from service-to-service authentication, eliminating a credential theft vector entirely.

## ⚠️ What Zero Trust Isn't

Zero Trust is not:
- A product you can buy and install
- A setting you can enable in a portal
- Something you achieve and complete
- Synonymous with MFA (MFA is one control, not the model)
- About trusting nothing (it's about verifying before trusting)

It's a maturity journey. Every organization implementing Zero Trust is somewhere on a continuum between "implicit trust everywhere" and "explicit verification for everything." Progress is incremental. The goal isn't perfect Zero Trust. It's continuous improvement toward more explicit, contextual verification.

The attacker in the opening scenario succeeded because the organization had implicit trust everywhere. Implementing device compliance for high-value resources, risk-based access for sensitive data, and least privilege for administrative actions wouldn't have caught the initial phishing. But it would have dramatically limited the lateral movement that made the breach catastrophic.

---

💬 **Where is your organization on the Zero Trust maturity journey?** Most organizations have MFA deployed. Fewer have device compliance enforced. Even fewer have risk-based access and JIT privilege. What's the next control you're working to implement, and what's the blocker?
<!-- nav -->

---

[← CA Policy](glossary-7-9-ca-policy.md) | [Home](../README.md) | [Assignment →](glossary-7-11-assignment.md)
