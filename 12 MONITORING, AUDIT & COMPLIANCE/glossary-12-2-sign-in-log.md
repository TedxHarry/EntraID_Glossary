# Sign-In Log
*The Authentication Record Your Security Team Needs to Know Cold*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #12.2 - Sign-In Log

---


A SOC analyst got an alert: possible account compromise for a senior finance executive. The analyst opened the Entra ID sign-in logs for that account.

In the last 24 hours: 47 successful sign-ins. 23 from Seattle, WA. 24 from Kuala Lumpur, Malaysia. The sign-ins alternated between locations at intervals that made physical travel impossible.

That's not a sign-in pattern. That's an account being used by two different people in different hemispheres simultaneously. The executive's credentials had been compromised. The sign-in log made this visible in about 90 seconds.

## 🔐 What sign-in logs capture

Every authentication event in Entra ID generates a sign-in log entry. The sign-in log is the authentication record: who signed in, when, from where, using what, to access what, and whether it succeeded.

Fields available in each sign-in event:

**Identity** 👤: User principal name, user display name, user ID (object ID). For service principal sign-ins: the application name and service principal object ID.

**Application** 📱: Which application the user was authenticating to. Application display name and app ID. The client application (the thing the user signed in from) and the resource application (the thing being accessed).

**Location** 📍: IP address, city, state, country. For some IPs, additional context about whether the IP is associated with a known hosting provider, anonymous proxy, or Tor exit node.

**Device** 💻: Device ID, device display name, operating system. Browser and browser version for web sign-ins.

**Authentication details** 🔑: Authentication method used (password, Microsoft Authenticator push, FIDO2 key, Windows Hello, certificate). Whether MFA was completed. Authentication strength satisfied.

**Conditional Access** 🔐: Which CA policies were evaluated. Whether each policy applied and what the result was (grant, block, not applied). This is the diagnostic field for CA troubleshooting.

**Risk** ⚠️: User risk level at the time of sign-in. Sign-in risk level. Risk detail (what triggered the risk score).

**Result** ✅: Success or failure. For failures: the error code and description. Interrupted (required MFA that wasn't completed) vs blocked (Conditional Access blocked the sign-in).

## 📊 Three types of sign-in logs

Entra ID separates sign-in activity into three log streams:

**Interactive user sign-ins** 👤: Sign-ins where the user provided credentials or completed MFA. The most familiar type. Browser-based, MSAL interactive flows, Windows Hello authentication.

**Non-interactive user sign-ins** 🔄: Silent token refresh. When MSAL silently acquires a new access token using a refresh token, this appears as a non-interactive sign-in. These can be extremely high volume for active users. Filtering these out is often necessary when looking for initial authentication events.

**Service principal sign-ins** 🤖: Authentications by applications and service principals, not users. CI/CD pipelines, background services, automation. Separate from user sign-ins for clarity.

Separating these three streams prevents the non-interactive refresh token events from burying the interactive sign-ins that are most relevant for security investigations.

## 🔍 What security teams look for

**Impossible travel** ✈️: Sign-ins from locations geographically impossible to reach in the elapsed time. Entra ID ID Protection detects this automatically, but direct log review confirms it.

**Unfamiliar sign-in properties** 🌐: First-time use of a particular browser, OS, location, or ASN. New patterns in an established account's history.

**Failed then succeeded MFA** 📱: Multiple failed MFA attempts followed by a success can indicate a real-time phishing (adversary-in-the-middle) attack where the attacker is forwarding MFA prompts in real time.

**Legacy authentication** 📧: Sign-ins using legacy protocols (IMAP, POP, SMTP AUTH). These don't support MFA. If your CA policy is blocking legacy auth but legacy auth sign-ins still appear, something is misconfigured.

**Unusual application access** 🔑: A user suddenly accessing applications they've never accessed before, especially administrative interfaces or sensitive data stores.

## 📌 ⏰ retention and export

Same retention as audit logs: 7 days for free tier, 30 days for P1/P2. Export to Log Analytics, Storage, or Event Hub via Diagnostic Settings. The same retention gap applies: compliance requirements often exceed 30 days.

Sign-in logs in Log Analytics integrate with Microsoft Sentinel for alert rules, anomaly detection, and SOAR automation. A sign-in from a risky IP that triggers an ID Protection alert can automatically create an incident in Sentinel, which triggers a Teams notification to the SOC team.

---

💬 **How quickly can your SOC team access and query Entra ID sign-in logs during an active incident, and is the 30-day retention window sufficient?** Sign-in log investigation is often the first step in an identity incident response. The difference between logs in a Log Analytics workspace (queryable in seconds) versus portal-only (limited filter options, slower) can make a real difference in response time. What's your team's current sign-in log access setup?
✍️ TedxHarry


### 🔧 Quick reference: PowerShell : sign-in logs

```powershell
# Get failed sign-ins for a specific user
Get-MgAuditLogSignIn -Filter "userPrincipalName eq 'user@contoso.com' and status/errorCode ne 0" -Top 50 |
    Select-Object CreatedDateTime, AppDisplayName, Status, ConditionalAccessStatus

# Find sign-ins where MFA was not satisfied
Get-MgAuditLogSignIn -Filter "authenticationRequirement eq 'multiFactorAuthentication' and status/errorCode ne 0" -Top 100
```

<!-- nav -->

---

[← Audit Log](/12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-1-audit-log.md) | [🏠 Contents](/README) | [Activity Report →](/12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-3-activity-report.md)
