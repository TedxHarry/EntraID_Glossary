# Recertification
*Access That Was Right Then Might Not Be Right Now*

**Part of Entra ID Glossary Series: Glossary#6.8 - Recertification**

---

A team lead certified her team's access to the HR system in January. Twelve members, all approved. Appropriate at the time.

By July, three of those people had changed roles. One had moved to a completely different department. The access they'd been certified for in January still matched the jobs they had in January. It didn't match the jobs they had now.

Without a July recertification, the access would continue indefinitely. The January certification, accurate when it was done, had become stale. Recertification is the mechanism that prevents certifications from becoming out of date.

## 🔄 What Recertification Is

Recertification is the periodic re-execution of an access certification for access that was previously certified. It's not a one-time event but a recurring checkpoint that verifies access remains appropriate over time.

The key word: re. The first certification establishes that access is appropriate at a point in time. Recertification confirms it's still appropriate after time has passed, roles have changed, and business needs have evolved.

In Microsoft Entra ID Governance, recertification is built into the access review configuration. When you create an access review, you set a recurrence:

- Monthly (for the most sensitive access: privileged admin roles)
- Quarterly (for sensitive application access, privileged groups)
- Semi-annually (for general application access, team groups)
- Annually (for low-sensitivity distribution lists, read-only resources)

Each recurrence launches a new review instance. Reviewers receive notifications, evaluate current access, and certify or deny. The cycle repeats.

## ⏱️ Why Recurrence Frequency Matters

Access drift is real and happens continuously. People change roles. Projects end. Contractors finish their engagements. Reorganizations shift reporting structures. Each change creates an opportunity for access to become misaligned with actual need.

A quarterly recertification of privileged admin roles means no admin has excess privilege for more than 3 months before a review surfaces it. An annual recertification means privilege can sit misaligned for up to 12 months before being caught.

For compliance frameworks (SOX, ISO 27001, SOC 2), recertification frequency requirements are often explicitly defined. SOX-relevant access is commonly required to be certified quarterly. Meeting those requirements means configuring appropriate recurrence intervals and retaining the evidence.

## 📋 Recertification vs Initial Certification

Initial certification and recertification look identical from a reviewer's perspective. Both involve evaluating a list of users and approving or denying their access. The difference is context:

**Initial certification**: Establishes the baseline. Reviewers may be seeing this access list for the first time. The review often surfaces obvious problems: people who shouldn't have access, accounts that look unfamiliar.

**Recertification**: Verifies continued appropriateness. Reviewers should know who's on the list from last time. The value is in catching what changed since the last review: new additions that look wrong, people who moved roles and retained old access, accounts whose business justification has expired.

Reviewers doing recertification well ask a different question than initial certification. Not just "should these people have access?" but "since last time, has anything changed that should affect this list?"

## 🔧 Continuous vs Periodic Recertification

Periodic recertification (quarterly, annually) catches access drift on a schedule. The alternative is event-driven recertification: triggering a review when a specific event occurs rather than on a calendar.

Event-driven triggers in Entra ID Governance:
- User changes manager (manager-certified access should be re-reviewed by the new manager)
- User changes department (department-based access may no longer be appropriate)
- User changes job title (role-based access should be validated against new role)
- Access package policy changes (existing holders may no longer meet new conditions)

The most robust approach combines both: periodic recertification as the baseline, with event-driven reviews for significant identity changes that shouldn't wait for the next scheduled cycle.

## ⚠️ The Recertification Fatigue Problem

Over-recertifying is as much a risk as under-certifying. If reviewers receive access reviews every 30 days for low-sensitivity resources, they will click through them without engaging. Review quality degrades. Rubber-stamp certification defeats the entire purpose.

Calibrate frequency to sensitivity and risk. Privileged access: frequent. General application access: less frequent. Low-sensitivity distribution lists: annual or not at all. The goal is meaningful reviews, not maximum reviews.

---

💬 **What recertification frequency does your organization use for privileged admin roles?** The gap between "we certified this 11 months ago" and "we recertify this quarterly" is the difference between access governance as an annual checkbox and access governance as an operational control. What drove your current schedule?
<!-- nav -->

---

[← Access Certification](glossary-6-7-access-certification.md) | [Home](../README.md) | [Entitlement Management →](glossary-6-9-entitlement-management.md)
