# IP Address Range
*The Building Block of Location-Based Access Control*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #7.21 - IP Address Range

---

## 🎯 TL;DR

- IP address ranges in Named Locations use CIDR notation (e.g., 192.168.1.0/24) to define network ranges
- Single IPs are /32; IPv6 ranges are also supported
- Keep Named Locations updated : stale IP ranges can create security gaps or block legitimate users


An organization asked me to help them understand why some users were still being prompted for MFA despite a policy that should have excluded their office. We opened the Named Location definition and found it: the IP range was entered as `10.0.0.0/8`. The office used `192.168.1.0/24`. The admin who set it up had used a private address range from memory instead of checking what the actual office IP was.

The policy was correctly designed. The IP range was wrong. Users at the office appeared to come from outside the trusted location because the trusted location didn't contain their actual IP.

IP Address Range is the foundational data that location-based Conditional Access is built on. Getting it wrong silently breaks location policies in ways that are hard to diagnose.

## 📡 What IP address range is in Entra ID

An IP Address Range is a CIDR-notated set of IP addresses defined in a Named Location in Entra ID. Conditional Access policies use Named Locations as conditions, and Named Locations are built from IP address ranges.

CIDR notation (Classless Inter-Domain Routing) expresses a range of IP addresses as a base address plus a prefix length. Examples:

- `203.0.113.0/24`: All 256 addresses from 203.0.113.0 to 203.0.113.255
- `198.51.100.10/32`: Exactly one IP address (the /32 means a single host)
- `192.0.2.0/22`: 1,024 addresses across four class C blocks

Entra ID supports both IPv4 and IPv6 CIDR ranges in Named Location definitions.

## 🏗️ How IP ranges are used in practice

**Corporate office definition** 🏢: Your ISP assigns a fixed IP or range to your office. That range goes into a Named Location. Conditional Access policies use that Named Location to identify office traffic.

Finding your office's external IP: the external (public) IP address that your office traffic appears to come from is often different from the internal private IP addresses on your LAN. External traffic to Microsoft's servers comes from your ISP-assigned public IP range, not from your 192.168.x.x or 10.x.x.x internal ranges. Use a public IP lookup service from a device on the office network to confirm the actual external IP.

**VPN egress** 🔒: Corporate VPN solutions use fixed IP addresses for egress (the IP that traffic appears to come from when it exits the VPN). These IPs go into a Named Location so VPN users get the same trusted treatment as office users.

**Multiple offices** 🌍: Each office location has its own external IP range. Define one Named Location per location or combine them into a single Named Location with multiple CIDR ranges. Keeping them separate makes it easier to identify which office a sign-in came from. Combining them simplifies policy management.

**Cloud infrastructure** ☁️: Azure services have published IP range documents that list the IP addresses for each service and region. If your organization's Azure workloads make authentication requests, those IPs may need to be in a Named Location depending on how service authentication is configured.

## ⚙️ Technical considerations

**CIDR accuracy** 🎯: An IP range that's too broad includes IPs that don't belong to you. An IP range that's too narrow misses some of your traffic. The right range is exactly what your ISP has allocated to your organization. Check with your network team or ISP if you're unsure.

**Static vs dynamic IPs** 📊: Corporate offices and VPN infrastructure typically use static (fixed) IP addresses. Residential internet connections use dynamic IPs that change periodically. You can only put static ranges in Named Locations. Dynamic home IPs can't be reliably included.

**IPv6 readiness** 🔢: Some networks and ISPs are transitioning to IPv6. If your infrastructure uses IPv6 addresses, include them in your Named Location definitions alongside IPv4 ranges. Sign-ins from IPv6 addresses that aren't in any Named Location are treated as coming from an unknown location.

**Maximum ranges per Named Location** 📋: Entra ID supports up to 2,000 IP ranges per Named Location. Organizations with large distributed networks may need multiple Named Locations.

## 🔍 Verifying your IP range definitions

Before marking a Named Location as trusted or building policies around it, verify that the IP ranges actually match your traffic:

**Sign-in log verification** 📋: In the Entra admin center sign-in logs, filter by a known office user and look at the IP address reported for a recent sign-in. That IP should fall within your Named Location range. If it doesn't, the range is wrong.

**IP range calculators** 🧮: CIDR notation isn't always intuitive. Use an IP range calculator to confirm that a given CIDR block covers the IPs you intend to include. `10.0.0.0/24` is 256 addresses. `10.0.0.0/8` is over 16 million.

**Network team input** 🤝: For large organizations, the network team maintains authoritative records of external IP allocations. Confirm ranges with them rather than guessing.

## ⚠️ Common IP range mistakes

**Private vs public IP confusion** 🔀: Private IP ranges (10.x.x.x, 172.16-31.x.x, 192.168.x.x) are internal addresses. They never appear as the source IP for traffic that reaches Microsoft's servers. Only public (external) IPs belong in Named Locations.

**Too broad ranges** 📡: Defining a /8 (16 million addresses) when your office uses a /29 (8 addresses) marks millions of IPs you don't control as "trusted."

**Outdated ranges** 📅: IP allocations change when ISPs reconfigure, organizations move offices, or VPN providers update their infrastructure. Named Location definitions need periodic review. A trusted location pointing to an IP range that now belongs to someone else is a security gap.

---

💬 **Have you ever discovered that a Named Location's IP range was misconfigured and causing policies to behave unexpectedly?** The private IP vs public IP confusion is by far the most common mistake. What was the sign-in log investigation that revealed the mismatch in your environment?
✍️ TedxHarry

<!-- nav -->

---

[← Trusted Location](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-20-trusted-location.md) | [🏠 Contents](/README) | [Legacy Authentication →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-22-legacy-authentication.md)
