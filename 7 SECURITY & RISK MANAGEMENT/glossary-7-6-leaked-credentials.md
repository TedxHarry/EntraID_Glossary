# Leaked Credentials
*When Your Password Shows Up on the Dark Web*

**Part of Entra ID Glossary Series: Glossary#7.6 - Leaked Credentials**

---

The breach happened at an online retailer. 42 million username/password combinations were exposed. The retailer wasn't a Microsoft customer. They had nothing to do with Entra ID.

But 312 of the exposed email addresses were corporate accounts from a company running Entra ID. The users had signed up for the retailer's loyalty program years ago using their work email addresses. Many of them had used the same password for both the retailer account and their corporate account.

Microsoft's threat intelligence found the breach database within 48 hours of it being published. The 312 accounts were flagged as high user risk. Conditional Access required password resets before any of those accounts could be used again.

No corporate accounts were compromised. The credential stuffing attack that the threat actor planned for the following week found locked doors at every account they tried.

## 🔑 What Leaked Credentials Means

Leaked credentials is a specific risk detection type in Entra ID ID Protection. It triggers when Microsoft's threat intelligence finds a username/password combination that matches an Entra ID account in external breach data.

The detection has nothing to do with a breach of Microsoft's systems or your organization's systems. It means credentials matching your organization's accounts have appeared somewhere else, in data from breached third-party services, dark web marketplaces, paste sites, or criminal forums.

The trigger is finding the specific password hash or plaintext credential that matches what's currently in use for an Entra ID account. Not just the username. The actual credential pair that would work against your tenant.

## 🌐 How Microsoft Finds Leaked Credentials

Microsoft operates a large-scale threat intelligence operation that continuously monitors sources where stolen credentials appear:

**Breach databases** 🗄️: When major services are breached, the stolen data often circulates through criminal communities. Microsoft's intelligence operation acquires and analyzes this data to identify Entra ID accounts at risk.

**Dark web forums** 🕵️: Criminal marketplaces where stolen credentials are bought and sold. Credential sets are often listed with enough information to identify which service they came from and whether the accounts are still active.

**Paste sites** 📋: Public and semi-public sites where breach data is shared. Attackers sometimes publish partial breach data to advertise the quality of a larger dataset for sale.

**Credential stuffing infrastructure** 🤖: In some cases, Microsoft can identify credential stuffing campaigns in progress and extract the credential lists being used against other Microsoft-adjacent services.

The matching process compares the harvested credentials against Entra ID account credentials. When a match is confirmed, the detection fires.

## 📊 What Happens When Detection Fires

A leaked credentials detection generates a **High** user risk event on the affected account. The detection type in the Identity Protection portal shows as "Leaked credentials."

The response depends on your Conditional Access policies:

**With a user risk policy in place**: The next time the user attempts to sign in, they hit the high user risk condition. If the policy requires a password change for high user risk, they're prompted to set a new password before access is granted. This clears the compromised credential before an attacker can use it.

**Without a user risk policy**: The detection appears in the Identity Protection dashboard. An admin can see the flagged account. But nothing happens automatically. The account continues to function with the leaked password until a human acts on it.

The second scenario is why the policy matters more than the detection.

## ⚠️ The Credential Reuse Problem

Leaked credentials detections are almost always a credential reuse problem. The user signed up for a third-party service using their work email address and the same password they use for work. The third-party service got breached. Now the work account is at risk.

This is structurally unavoidable without organization-wide controls:

- Users reuse passwords. It's human behavior. Telling them not to doesn't stop it.
- Third-party services get breached. No organization can control the security of every service their users interact with.
- Work email addresses are used for personal accounts. This is often a policy violation, but enforcing it is difficult.

The realistic response is assuming credential reuse happens and building detection and response around it. The leaked credentials detection plus a mandatory password reset policy handles the scenario even when it occurs.

## 🔧 Reducing Exposure

Several controls reduce the impact of leaked credential events:

**Passwordless authentication** 🔑: If users authenticate with FIDO2 security keys or Windows Hello, there's no password to leak. A breach of a third-party service exposes the email address but no credential that would work against the Entra ID account.

**MFA as minimum** 📱: Even without passwordless, requiring MFA means a leaked password alone isn't enough. An attacker needs the password and the MFA factor. This doesn't prevent the leaked credentials detection from firing, but it prevents the attacker from using the leaked credential without the second factor.

**Password Protection** 🛡️: Entra ID Password Protection blocks commonly used and compromised passwords. Users can't set passwords that appear in known breach lists, which reduces the risk of the leaked password being one that was already in a breach database.

**SSPR with strong methods** 🔄: When the leaked credentials detection triggers a mandatory password reset, the new password is set by the user through SSPR using strong authentication methods. The compromised credential is replaced before damage occurs.

---

💬 **Have you had a leaked credentials detection fire in your tenant where the source was a completely unrelated third-party breach?** The credential reuse chain from a retail or gaming site to a corporate account is surprisingly common. How did you handle communicating it to the affected users without them feeling blamed for something that wasn't entirely their fault?
<!-- nav -->

---

[← Anomaly Detection](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-5-anomaly-detection.md) | [🏠 Contents](/README) | [Threat Intelligence →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-7-threat-intelligence.md)
