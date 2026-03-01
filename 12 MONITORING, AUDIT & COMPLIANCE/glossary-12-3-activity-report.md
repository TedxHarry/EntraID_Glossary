# Activity Report: The Trend View That Audit Logs and Sign-In Logs Don't Give You

**Part of Entra ID Glossary Series: Glossary#12.3 - Activity Report**

---

An IT director asked a question that audit logs and sign-in logs couldn't easily answer: "Is anyone actually using the Salesforce integration we set up eight months ago?"

The sign-in log had 40,000 events over the past 30 days. You could filter by application. But what she really wanted was: how many distinct users accessed Salesforce each week for the past quarter? Which users hadn't used it in 90 days? Is usage growing or declining?

Activity reports are the aggregate and trend view. Not individual events, but patterns across events. The answer to "what's happening across our tenant" rather than "what happened in this specific event."

## 📊 What Activity Reports Provide

Entra ID activity reports are summaries and aggregations built on top of the underlying sign-in and audit log data. They present trend data, usage statistics, and status summaries that aren't practical to derive manually from raw logs.

Key report categories:

**Usage and Insights** 📈: Application usage reports showing which applications are being used, by how many users, with what frequency. The "Azure AD Application Activity" report shows monthly active users per application, giving visibility into which integrations are actually being used versus which were set up and forgotten.

**Authentication methods usage** 🔑: What percentage of users have registered what authentication methods. How many users are capable of passwordless. How many have only password registered. Which methods are being used for actual sign-ins. This report is what drives authentication modernization programs: showing leadership the gap between "percentage of users who could go passwordless" and "percentage currently using passwordless."

**SSPR (Self-Service Password Reset) activity** 🔄: Usage of SSPR: how many password resets occurred, which authentication methods users registered for SSPR, success and failure rates. Used to evaluate SSPR adoption and identify gaps where users are still calling the help desk unnecessarily.

**Provisioning activity** ⚙️: Activity from automated provisioning (SCIM, HR-driven provisioning). How many accounts were created, updated, or disabled in connected applications during a period. Success and failure counts. Useful for validating that the provisioning pipeline is working without manually checking each application.

**Access review activity** 📋: Results of completed access reviews. How many decisions were made, by whom, with what outcome. Which reviewers are completing their reviews promptly versus which are overdue. A management-level view of governance program health.

## 🎯 Reports vs Raw Logs: When to Use Each

**Use raw sign-in logs when** 🔍: Investigating a specific user's behavior. Confirming whether a specific authentication event occurred. Troubleshooting a Conditional Access policy for a specific user. Looking at a specific time window with a specific filter.

**Use activity reports when** 📊: Understanding adoption trends. Building a business case for an authentication modernization initiative. Reporting to leadership on security posture improvements. Identifying unused application integrations. Measuring the effectiveness of an awareness campaign (did SSPR registration go up after our training?).

The reports exist because the questions they answer are different from the questions raw logs answer, and deriving trend data from raw logs at scale is impractical without significant query engineering.

## 📋 The Authentication Methods Report in Practice

The authentication methods usage report is particularly actionable. It shows:

- Total users
- Users registered for MFA (any method)
- Users registered for passwordless methods
- Users registered for SSPR
- Users registered for nothing (no additional authentication factors)

For an organization with 5,000 users, knowing that 3,200 are MFA-capable, 800 have passwordless methods, and 400 have zero secondary authentication registered is immediately actionable. The 400 are the highest-risk accounts. The 2,400 who could upgrade from MFA to passwordless are an adoption opportunity.

These numbers from the report turn "we should improve authentication security" into "here are the specific gaps and the size of each."

## ⚙️ Accessing Activity Reports

Activity reports are accessible in the Entra ID admin center under Identity > Monitoring & health > Usage & insights. Some reports are also available via the Microsoft Graph Reporting API, which enables pulling report data into custom dashboards, Power BI, or automated reporting pipelines.

The Graph Reporting API supports reports like `getAzureADApplicationSignInSummary`, `getAuthenticationMethodsUserRegistrationCount`, and others that can be scheduled and exported for regular reporting.

---

💬 **Which Entra ID activity report has been most useful for demonstrating security posture progress to leadership in your organization?** The authentication methods usage report is frequently cited for security initiatives. The application usage report is valuable for IT optimization. Which report gave you a number that changed how your organization thought about identity security?

#EntraID #ActivityReport #MonitoringAndHealth #AuthenticationMethods #MicrosoftEntra #SecurityReporting #IdentityGovernance
<!-- nav -->

---

[← Sign-In Log: The Authentication Record Your Security Team Needs to Know Cold](glossary-12-2-sign-in-log.md) | [Home](../README.md) | [Security Alert: When Entra ID Tells You Something Is Wrong →](glossary-12-4-security-alert.md)
