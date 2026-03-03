# CA Optimization Agent
*Automated Recommendations for Conditional Access Policy Gaps*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #13.19 - CA Optimization Agent

---


A security team finished an 18-month project to deploy Conditional Access across the organization. Forty-three policies. Multiple rounds of testing in report-only mode. They felt good about where they'd landed.

Then an Entra ID recommendation appeared: 847 users in the tenant had no Conditional Access policy requiring MFA. Not because the policies were wrong, but because those users had been onboarded through a provisioning flow that assigned them to groups not covered by any existing policy scope.

The CA Optimization Agent found a gap the team didn't know existed.

## 🔍 What the CA optimization agent is

The CA Optimization Agent is part of the Entra Recommendations engine, which continuously analyzes your tenant configuration and surfaces actionable findings to improve your security posture. The CA-specific recommendations focus on Conditional Access coverage gaps and configuration improvements.

Unlike a general security score that gives you a number, Entra Recommendations give you specific findings: this many users are affected, here's the specific gap, here's what to do about it. The CA Optimization Agent is one component of that broader recommendation engine, focused specifically on Conditional Access policy coverage and configuration quality.

You'll find it in the Entra admin center under **Identity > Overview > Recommendations**, or directly within the Conditional Access blade under **Insights and Reporting**.

## 📋 Categories of CA optimization recommendations

**MFA coverage gaps** 🔐: Users who have no CA policy applying to them that requires MFA. The recommendation surfaces the specific count of affected users and breaks down why they're uncovered. Common root causes are dynamic group membership exclusions, service accounts in scope of user-facing policies, or new users provisioned after groups were last reviewed.

**Legacy authentication not blocked** 🚫: Clients that don't support modern authentication (basic auth, legacy mail protocols) bypass Conditional Access entirely. A policy with a client apps condition blocking legacy authentication clients should exist. The recommendation flags tenants where this policy is missing or has gaps in scope.

**Privileged role coverage** 👑: Users holding privileged roles (Global Administrator, Privileged Role Administrator, Security Administrator) who aren't covered by policies requiring compliant devices or phishing-resistant MFA. The recommendation surfaces privileged users whose authentication requirements are weaker than the role's risk profile warrants.

**Sign-in risk coverage** ⚠️: Whether risk-based CA policies exist and whether they cover the affected user population. Users outside the scope of sign-in risk policies don't have automated responses to risky authentication events.

**Session control gaps** 📱: Recommendations for applications handling sensitive data where session controls (app-enforced restrictions, sign-in frequency limits) would reduce exposure from persistent sessions on unmanaged devices.

## ⚙️ How recommendations surface and update

The Entra Recommendations engine runs continuously in the background, re-evaluating tenant state against the recommendation criteria. Recommendations appear when the finding criteria are met and disappear when the issue is resolved or marked as dismissed.

Each recommendation includes:

**Impact assessment** 📊: How many users are affected, and a classification of the recommendation's security impact level (high, medium, low). The CA optimization recommendations related to MFA gaps on large user populations are typically classified as high impact.

**Remediation guidance** 🔧: Step-by-step instructions for resolving the finding, usually linking directly to the CA policy creation workflow with pre-populated settings relevant to the specific gap.

**Affected user details** 👥: The specific user accounts or groups affected by the gap. For MFA coverage gaps, you can see which users are uncovered and why, which helps diagnose whether the issue is in group membership, policy scope, or exclusion lists.

**Status tracking** 📈: Recommendations have status states: Active (unresolved), Completed (resolved), Dismissed (acknowledged but intentionally not resolved), Postponed (deferred with a future review date).

## 🎯 Using recommendations effectively

The CA Optimization Agent surfaces findings but doesn't automatically remediate them. The remediation workflow requires administrative review and explicit action.

**Validate before acting** ✅: The affected user count in a recommendation doesn't always mean all those users need the recommended control immediately. Some may be service accounts that should be excluded. Others may be in licensing tiers without certain feature access. Verify the affected population before deploying new policies.

**Report-only first** 🔍: When a recommendation leads to creating a new CA policy, deploy it in report-only mode first. The sign-in log shows which sign-ins would have been affected. A week of report-only observation catches edge cases before enforcement creates business disruption.

**Dismiss with documentation** 📝: Some recommendations don't apply to your environment. Dismissing a recommendation requires selecting a reason (planned, not applicable, accepted risk). The dismissal reason and the identity of who dismissed it are captured in the audit log. That audit trail matters for compliance reviews when auditors ask why a security recommendation wasn't implemented.

**Periodic review cadence** 📅: Recommendations change as your tenant changes. New user populations, new application deployments, and policy modifications can open new gaps or resolve existing findings. A monthly review of the Recommendations blade keeps the CA posture current rather than letting gaps accumulate unnoticed.

## 🔗 Relationship to CA insights and reporting

The CA Optimization Agent surfaces gaps before they become incidents. The CA Insights and Reporting workbook (in the Conditional Access blade) shows what's actually happening: how many sign-ins each policy matched, how many were granted or blocked, and which users are being affected by which policies.

These two tools work together. Recommendations tell you what should change. Insights show you what the current policies are actually doing. Both are necessary for a complete view of your CA posture.

---

💬 **Have you had a CA Optimization recommendation surface a gap that your team hadn't noticed, and how did you verify whether the finding was a genuine risk or an expected configuration?** The most common pattern is MFA coverage gaps appearing after user provisioning changes add users to groups that weren't in the original CA policy scope. What's been your most unexpected CA recommendation finding?
✍️ TedxHarry

<!-- nav -->

---

[← Tenant Restrictions](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-18-tenant-restrictions.md) | [🏠 Contents](/README) | [Policy Evaluation →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-20-policy-evaluation.md)
