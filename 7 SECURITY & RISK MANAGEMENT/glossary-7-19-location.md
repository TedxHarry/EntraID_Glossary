# Location
*Using Where You Sign In to Shape What You Can Access*

**Part of Entra ID Glossary Series: Glossary#7.19 - Location**

---

A company's security team noticed an unusual pattern in their sign-in logs. Authentication attempts from IP addresses in countries where they had no employees, no offices, no partners, no operations. Hundreds of attempts per day. Most failing on password. A few succeeding.

The ones that succeeded were using credentials from a breach of a consumer site. The users had reused passwords. The attackers were trying them systematically from data centers abroad.

The fix was a Location condition in Conditional Access: block sign-ins from countries the organization had no presence in. Implementation took 15 minutes. The attack surface dropped by 60% overnight.

## 📍 What Location Is in Conditional Access

Location is a condition in Conditional Access policies that evaluates where the sign-in is coming from. It's based on the IP address of the authentication request, mapped to one of two signals:

**IP address ranges** 🌐: Specific IPv4 or IPv6 address ranges that the organization has defined as Named Locations. A sign-in from an IP within a defined range matches that Named Location.

**Country/region** 🗺️: The country determined by the geographic location of the IP address. Microsoft resolves IP addresses to countries using geographic IP databases.

Location conditions can be used to include or exclude sign-ins from specific Named Locations or countries. This lets you build policies that respond differently to sign-ins from trusted vs untrusted locations.

## 🗂️ Named Locations: The Building Blocks

Named Locations are the pre-defined location objects that Conditional Access policies reference. They're created in Entra admin center under Security > Conditional Access > Named Locations.

Two types:

**IP ranges Named Location** 📡: One or more IPv4 or IPv6 CIDR ranges. Examples: your corporate office IP range, your VPN egress IP addresses, your cloud infrastructure IP range, your partner network IPs. Can be marked as "trusted" to give them additional trust signals in risk assessments.

**Countries Named Location** 🌍: A list of countries. Used for geographic blocking or geographic allowlisting. "All countries except [list]" or "[list of countries] only" are both common patterns.

## 🎯 Common Location-Based Policy Patterns

**Country blocking** 🚫: A policy targeting all users and all apps, with a location condition for countries where the organization has no presence, and a grant control of Block access. Reduces attack surface from automated credential stuffing attacks that use infrastructure in specific geographic regions.

The important design consideration: mark countries where business travel is expected as exceptions, or pair with a step-up MFA requirement rather than a full block for countries where employees might travel.

**Trusted location MFA exemption** ✅: A policy requiring MFA for all users and all apps, with a location exclusion for the corporate office IP range. Users at the office on the corporate network are excluded from MFA. Users everywhere else are required.

This pattern reduces MFA friction for office-based workers while maintaining MFA for remote and hybrid access. The trade-off: if an attacker gets on the corporate network, MFA isn't protecting those resources.

**VPN IP trust** 🔒: Mark VPN egress IPs as Named Locations. Apply MFA exemptions or reduced requirements for users coming through the VPN. The VPN connection provides some implicit verification that the user has VPN credentials and is connecting through corporate infrastructure.

**Hybrid work: require MFA outside the office** 🏠: Location condition excluding "Corporate Office" Named Location + Require MFA grant. Clean experience at the office, stepped up for home/remote.

## ⚠️ Location Signal Limitations

Location in Conditional Access is based on IP addresses. IP addresses are not perfect location signals:

**VPNs and proxies** 🔀: A user connecting through a consumer VPN will appear to come from the VPN provider's exit IP, which may be in a different country than the user's actual location. Your location block for Country X blocks your users who happen to be tunneling through Country X.

**IPv6** 🔢: IPv6 adoption is increasing. Ensure Named Location definitions include IPv6 ranges where relevant.

**Shared infrastructure** 🏢: Cloud provider IP ranges and large hosting provider ranges are used by both legitimate traffic and attackers. An IP in an AWS region may be a legitimate user on a remote work connection or an attacker's rented server.

**Dynamic IPs** 📡: Home internet connections often have dynamic IP addresses. A trusted location based on a home IP range needs to accommodate DHCP changes.

**Geographic IP accuracy** 🗺️: Country-level IP geolocation is generally accurate but not perfect. IP blocks are bought, sold, and reassigned. An IP registered to one country may be in active use from another.

These limitations mean location conditions should be considered a risk signal and access simplification tool, not a precise security boundary. Don't use location alone as the sole defense for sensitive resources.

## 💡 Location and Risk Signals Interact

Entra ID ID Protection considers sign-in location when evaluating risk. Sign-ins from unfamiliar locations contribute to sign-in risk scores. A Named Location that's marked as trusted carries lower inherent risk.

This interaction creates a compounding effect: sign-ins from trusted corporate locations get both the Conditional Access location exemption and lower risk scores from ID Protection. Sign-ins from unknown locations get both higher scrutiny from Conditional Access conditions and higher risk scores from ID Protection.

---

💬 **Have you implemented country-based location blocking in Conditional Access?** The before and after comparison in sign-in logs is often striking: hundreds of failed authentication attempts from blocked countries that simply stop appearing after the policy goes live. What countries were generating the most attack traffic before you blocked them?
<!-- nav -->

---

[← Report-Only Mode](glossary-7-18-report-only-mode.md) | [Home](../README.md) | [Trusted Location →](glossary-7-20-trusted-location.md)
