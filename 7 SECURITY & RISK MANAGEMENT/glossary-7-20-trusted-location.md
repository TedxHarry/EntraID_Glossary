# Trusted Location
*Teaching Conditional Access What "Safe" Looks Like*

**Part of Entra ID Glossary Series: Glossary#7.20 - Trusted Location**

---

A Conditional Access policy required MFA for all users. The CISO wanted the security. The operations team wanted office workers to not be prompted every single morning. The argument went on for three weeks.

The resolution took five minutes: create a Named Location for the corporate office IP range, mark it as trusted, exclude it from the MFA requirement. Users at the office had the same MFA-free sign-in experience they'd always had. Users everywhere else were now required.

Both teams got what they wanted. The security improved, the user experience didn't degrade, and the policy was actually enforced rather than being ignored because it was too painful.

Trusted Locations are how you make Conditional Access policies practical.

## 🔒 What a Trusted Location Is

A Trusted Location is a Named Location in Entra ID that has been explicitly marked as trusted. The "trusted" designation has two effects:

**Effect on Conditional Access policies** 🎯: Policies can include or exclude Trusted Locations by name. A policy can say "exclude all trusted locations" from an MFA requirement, effectively exempting sign-ins from those IP ranges from the policy's grant control.

**Effect on risk scoring** 📊: ID Protection considers sign-ins from trusted locations lower risk than sign-ins from unknown or untrusted locations. A sign-in from a Trusted Location contributes fewer risk signals to the sign-in risk score. This means users signing in from trusted locations are less likely to trigger risk-based policies.

The designation is a signal to the system: "we have verified that this IP range belongs to us and represents a controlled environment."

## 🏗️ Creating a Trusted Location

In Entra admin center, under Security > Conditional Access > Named Locations:

1. Create a new **IP ranges location**
2. Enter the IPv4 or IPv6 CIDR ranges for the location
3. Check the **"Mark as trusted location"** checkbox
4. Save

The trust mark is binary: a Named Location is either trusted or not. You can have multiple Trusted Locations (one for each office, one for each VPN egress point, one for partner network IPs).

Country-based Named Locations cannot be marked as trusted. Trust designation applies only to IP-range-based Named Locations.

## 🎯 What to Define as Trusted

Trusted Locations should represent IP ranges where your organization has meaningful control or verification:

**Corporate offices** 🏢: Fixed IP ranges assigned to your office network infrastructure. Sign-ins from these IPs originate from devices connected to your managed network.

**VPN egress points** 🔒: If your organization uses a corporate VPN, the IP addresses that VPN traffic exits from. Users connecting through the VPN are using corporate infrastructure. Including VPN egress IPs allows VPN users to receive the same trusted treatment as office users.

**Cloud infrastructure egress** ☁️: If your Azure-hosted services or managed infrastructure use fixed outbound IPs, these may warrant trusted designation for service-to-service scenarios.

**Partner network IPs** 🤝: In some scenarios, long-term partner networks with well-defined IP ranges may be added as trusted for specific applications or user populations.

## ⚠️ What Not to Trust

The trusted designation is a security claim. Marking an IP range as trusted tells Conditional Access and ID Protection: "we vouch for traffic from here." Be careful about what you vouch for:

**Dynamic/residential IP ranges** 🏠: Home internet connections don't have fixed IPs. You can't define a trusted range for "all my employees' home connections" because those IPs change. Attempting to use residential IP ranges as Trusted Locations generally doesn't work and creates unpredictable behavior.

**Overly broad cloud provider ranges** ☁️: Marking an entire AWS, Azure, or GCP region's IP range as trusted because your infrastructure lives there also marks every other customer's infrastructure in that region as trusted. Don't trust IP ranges you don't exclusively control.

**Shared office buildings** 🏗️: If your office shares an IP range with other tenants in a shared building (co-working spaces, shared office buildings), the "trusted" traffic from that range includes anyone in the building who can access that network. Evaluate the real-world access control before trusting a shared network.

## 🔄 Trusted Location and MFA Frequency

Session controls in Conditional Access include sign-in frequency: how often users must re-authenticate. Trusted Locations interact with this control.

A common pattern: require MFA re-authentication every 8 hours for sign-ins outside trusted locations, but allow persistent sessions for sign-ins from trusted locations. This balances security (regular re-authentication for remote/travel scenarios) with user experience (infrequent re-authentication at the office).

## 💡 The Trust Verification Problem

Trusted Locations are IP-range-based. They trust the IP address, not the user. Anyone on a network whose IP is in your Trusted Location range gets trusted treatment.

This creates a risk: a guest in your office connected to the guest wifi shares the building's IP range. If the guest wifi and corporate wifi use the same outbound IP (which is common in smaller offices), a visitor's unauthenticated laptop signs in to their own account from what appears to Conditional Access as your corporate office network.

This is why Trusted Locations work best as one layer in a defense-in-depth architecture, not as a standalone security boundary. MFA exemptions from trusted locations are reasonable for user experience. Removing device compliance requirements from trusted locations is riskier.

---

💬 **How many Named Locations do you have defined as trusted in your tenant?** The difference between a clean, intentionally scoped set of trusted locations and an organically grown list of 40 IP ranges nobody can explain is significant. How often do you review and audit your trusted location definitions?
<!-- nav -->

---

[← Location](glossary-7-19-location.md) | [Home](../README.md) | [IP Address Range →](glossary-7-21-ip-address-range.md)
