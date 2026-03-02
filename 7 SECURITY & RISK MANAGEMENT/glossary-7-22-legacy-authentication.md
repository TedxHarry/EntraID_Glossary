# Legacy Authentication
*The Open Door That MFA Can't Close*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #7.22 - Legacy Authentication

---

## 🎯 TL;DR

- Legacy authentication protocols (SMTP AUTH, POP3, IMAP, older Office clients) can't satisfy MFA
- Blocking legacy auth is one of the highest-impact, lowest-disruption security improvements you can make
- Create a CA policy: Block access for All Users where Client App = Legacy authentication clients


An organization had MFA deployed. 100% of users had MFA registered. The Conditional Access policy requiring MFA had been running for six months. They felt protected.

A penetration tester's report was a surprise. One finding read: "Successfully authenticated as user@contoso.com via IMAP using only username and password. MFA was not challenged."

The organization had MFA. Their email server still accepted IMAP connections. IMAP is a legacy protocol. It doesn't support MFA. The attacker bypassed six months of MFA deployment in two minutes by connecting to a protocol that predates MFA by three decades.

## 🔌 What legacy authentication is

Legacy authentication refers to authentication protocols that don't support modern authentication mechanisms like MFA or OAuth 2.0. These protocols were designed in an era when username and password was the only authentication model. They authenticate by transmitting credentials directly, with no mechanism to challenge for a second factor.

The main legacy protocols in Microsoft 365 environments:

**SMTP AUTH** 📧: Basic SMTP authentication. Used by printers, scanners, legacy applications, and some email clients to send mail directly through Exchange Online.

**POP3** 📬: Post Office Protocol. Older email protocol used to download email. Sends credentials in plaintext or simple encrypted form.

**IMAP** 📨: Internet Message Access Protocol. Another older email access protocol. Widely supported by email clients. Cannot challenge for MFA.

**Exchange ActiveSync (EAS)** 📱: Mobile email sync protocol. The older version of EAS doesn't support modern authentication. Newer EAS versions do, but many older mobile clients use the legacy version.

**Exchange Web Services (EWS)** 🔄: Older Exchange API. Used by some third-party calendar, mail, and productivity tools.

**Autodiscover v1** 🔍: Protocol some email clients use to automatically configure their Exchange settings.

**MAPI over HTTP (older versions)** 🖥️: Used by older Outlook clients.

## 🚨 Why legacy auth is a security problem

The problem is simple: these protocols only accept a username and password. There's no mechanism to prompt for a second factor. When an attacker has a valid username and password, legacy auth protocols give them access regardless of MFA policies.

This makes legacy authentication the primary attack vector for credential stuffing. Automated attack tools explicitly target legacy protocols because they bypass MFA. The flow is:

1. Attacker obtains leaked credentials from a breach database
2. Attacker tests credentials via IMAP, POP3, or SMTP AUTH
3. Credentials work. MFA is never challenged.
4. Attacker has email access and often uses it to request password resets for other services.

Microsoft's telemetry consistently shows that over 90% of password spray attacks use legacy authentication protocols. This isn't because attackers prefer legacy protocols for aesthetic reasons. It's because legacy protocols work even when MFA is deployed.

## 🔒 Blocking legacy authentication with conditional access

The fix is a Conditional Access policy that blocks legacy authentication protocols:

**Assignments** 👥: All users (and consider all guests/external users too)

**Conditions - Client apps** 💻: Select "Other clients" (this targets legacy authentication protocols specifically). Optionally also include "Exchange ActiveSync clients" if you want to block EAS-based connections.

**Grant control** 🚫: Block access

This policy blocks any sign-in attempt that uses a legacy auth protocol. The sign-in fails at the authentication level. The attacker's credential stuffing tool gets a block response instead of a successful authentication.

## ⚙️ What breaks when you block legacy auth

This is the hard part. Legacy authentication is used by legitimate things too:

**Printers and multifunction devices** 🖨️: Many printers use SMTP AUTH to send scanned documents via email. Blocking legacy auth breaks scan-to-email for these devices.

**Line-of-business applications** 💼: Applications built 5-10+ years ago often authenticate to Exchange or SharePoint using legacy protocols. ERP systems, CRM systems, monitoring tools, and custom-built internal apps are common offenders.

**Older mobile email clients** 📱: Email apps that haven't been updated may use IMAP/POP3 rather than the modern Exchange protocols.

**Monitoring and alerting systems** 🔔: Systems that send email alerts sometimes use SMTP AUTH to send through Exchange Online.

The Report-Only mode workflow is essential before blocking legacy auth. Two to four weeks in report-only reveals exactly what would break.

## 🔧 Handling legitimate legacy auth usage

For legitimate services that genuinely need legacy auth:

**Printers** 🖨️: Most modern printers support OAuth or can be configured to use an SMTP relay service that doesn't require Exchange authentication. Replace SMTP AUTH with a proper relay.

**Applications** 💻: Update the application to use modern authentication (OAuth 2.0). If the application is a vendor product, this is a vendor conversation. If it's internal, it's a development project.

**Monitoring tools** 🔔: Switch to a service account with a registered managed identity or configure the monitoring tool to use modern auth if it supports it.

For cases where the work to migrate can't happen immediately, create a specific exclusion group with a documented review date. The exclusion list should shrink over time, not grow.

---

💬 **What was the legacy auth offender that surprised you most when you started blocking it?** The printer scenario is almost universal. But the business-critical ERP system that nobody knew was using IMAP to send monthly reports is the one that causes the most painful conversation. What did your legacy auth block surface in your environment?
✍️ TedxHarry


### 🔧 Quick reference: block legacy auth

```powershell
# Create a CA policy to block legacy authentication
$params = @{
    displayName = "Block Legacy Authentication"
    state = "enabledForReportingButNotEnforced"  # Start in Report-Only!
    conditions = @{
        users = @{ includeUsers = @("All") }
        applications = @{ includeApplications = @("All") }
        clientAppTypes = @("exchangeActiveSync", "other")
    }
    grantControls = @{ operator = "OR"; builtInControls = @("block") }
}
New-MgIdentityConditionalAccessPolicy -BodyParameter $params
```

<!-- nav -->

---

[← IP Address Range](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-21-ip-address-range.md) | [🏠 Contents](/README) | [Session Control →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-23-session-control.md)
