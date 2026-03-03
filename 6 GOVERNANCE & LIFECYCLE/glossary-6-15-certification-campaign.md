# Certification Campaign
*Access Review at Scale, on a Schedule*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.15 - Certification Campaign

---


A compliance team needed to certify that all 1,800 users with access to the company's financial applications had appropriate business justification for that access. Quarterly. Starting this quarter.

The manual approach would have taken weeks: pulling reports from each application, distributing spreadsheets to 40 managers, chasing responses, consolidating results, applying the changes, producing evidence. And then doing it again in 90 days.

They ran it as a certification campaign in Entra ID Governance. The campaign started, ran for 14 days, managers received notifications, made decisions in the portal, and the results were automatically applied. The evidence was in the portal, exportable for the auditor.

The campaign that would have taken weeks of manual work took 2 hours to configure and ran itself.

## 🏁 What a certification campaign is

A certification campaign is a time-bounded, organized effort to review and certify access for a defined scope of users, applications, or resources. The word "campaign" carries its meaning precisely: a coordinated effort, with a defined start and end, clear objectives, and a structured process for achieving them.

In Microsoft Entra ID Governance, a campaign is an instance of an access review (or a collection of related access reviews) running simultaneously across a defined population. It has:

- **A defined scope**: Which users, which resources, which access types are being certified
- **Designated reviewers**: Who certifies each access decision
- **A defined window**: Start date, end date, response deadline
- **Automated outcomes**: What happens to access when decisions are made or when reviewers don't respond
- **Audit evidence**: A complete record of every decision, by whom, when, with what justification

## 📋 Campaign types

**Entitlement campaign** 🔵: Certifying access granted through Entitlement Management access packages. The campaign asks holders: do you still need this access? Or asks managers: does your team member still need this?

**Group membership campaign** 🔵: Certifying that members of specific groups (especially privileged or sensitive groups) still need that group membership.

**Application role campaign** 🔵: Certifying that users assigned specific roles in enterprise applications still have appropriate business justification.

**Privileged role campaign** 🔵: Certifying Entra ID directory role assignments. Who has User Administrator? Who has Security Administrator? Do they still need it? These typically run monthly or quarterly.

**Guest access campaign** 🔵: Certifying external user access. Guest accounts accumulate over time as vendors and contractors are invited and their engagements end without formal offboarding. Guest campaigns typically find the highest percentage of stale access.

## ⚙️ Configuring a campaign

A campaign in Entra ID Governance is a configured access review with specific settings:

**Scope definition**: Which resources and which users. Can be filtered by group, application, or user attributes.

**Reviewer assignment**: Managers (automatically identified from the manager attribute), resource owners, specific named reviewers, or self-review by the users themselves.

**Duration**: How long reviewers have to respond. Common: 14 days for quarterly campaigns, 30 days for annual reviews.

**Reminder settings**: Email reminders to reviewers who haven't responded at day 7 and day 12 of a 14-day campaign.

**Fallback behavior**: If a reviewer doesn't respond by the deadline: auto-approve (access continues), auto-deny (access is removed), or escalate to an alternate reviewer.

**Auto-apply**: Whether approved/denied decisions are automatically applied when the campaign closes, or held for manual review before applying.

## 📊 Reading campaign results

At close, a campaign produces a results report: how many access decisions were made, how many approved, how many denied, how many had no response (and what happened). This report is the compliance evidence: it shows that a structured review occurred, who reviewed, and what was decided.

For audit purposes, the report answers:
- Was the review conducted during the required period?
- Who had access at review time?
- Who certified each access assignment?
- What was the outcome for inappropriate access?

## 💡 Campaign timing matters

Running a certification campaign in the third week of December (when half the organization is on leave) produces poor response rates and meaningless results. Running it immediately after a major product launch produces the same. Campaign timing should account for organizational rhythms.

Quarter-end, fiscal year transitions, and immediately after large organizational changes (mergers, reorganizations) are generally poor campaign windows. Mid-quarter, during normal operational periods, produces the most engaged reviewers and the most meaningful results.

---

💬 **Has your organization run an access certification campaign and found the response rate from reviewers lower than expected?** The gap between sending campaign notifications and receiving meaningful decisions is where most campaigns struggle. What changes improved engagement with your reviewers?
✍️ TedxHarry

<!-- nav -->

---

[← Governance](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-14-governance.md) | [🏠 Contents](/README) | [Bulk User Operations →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-16-bulk-user-operations.md)
