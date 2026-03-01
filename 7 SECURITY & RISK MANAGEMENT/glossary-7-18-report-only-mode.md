# Report-Only Mode
*How to Test a Policy Without Breaking Production*

**Part of Entra ID Glossary Series: Glossary#7.18 - Report-Only Mode**

---

An organization wanted to block legacy authentication across the tenant. One engineer created the policy, set it to enabled, and pushed it live without testing. By the end of business, the helpdesk had 34 tickets. Three printers that authenticated via SMTP were offline. One business-critical ERP integration using basic auth was failing. A conference room display system couldn't connect to Exchange.

None of these devices showed up in any inventory. Nobody knew they were using legacy auth. The policy found them by breaking them.

Report-Only mode exists so you can find those devices without breaking them.

## 📊 What Report-Only Mode Does

Report-Only mode is a Conditional Access policy state that evaluates the policy against every sign-in in its scope but does not enforce the policy. It logs what it would have done without actually doing it.

A policy in Report-Only mode:

- Evaluates every sign-in against its assignments and conditions
- Determines what the outcome would be (grant, block, require MFA, etc.)
- Records that outcome in the sign-in logs with a "report-only" result
- Does NOT actually block access or require anything from users

Users don't see any change. They don't get prompted. They don't get blocked. Their sign-ins proceed normally. Behind the scenes, the policy is watching every sign-in and recording what it would have done if it were live.

## 🔍 Where to See Report-Only Results

The results appear in two places:

**Sign-In Logs** 📋: Each sign-in log entry has a "Conditional Access" section. Policies in Report-Only mode appear here with their result. You can filter by policy name to see all sign-ins the policy evaluated and what it would have done.

**CA Insights Workbook** 📊: In the Entra admin center under Monitor > Workbooks, the Conditional Access Insights workbook aggregates report-only results. It shows the number of sign-ins that would have been affected, broken down by result (would have granted, would have required MFA, would have blocked).

For a legacy auth block policy, this view shows you exactly how many sign-ins used legacy protocols in the last 30 days, which applications, which users, and what the outcome would have been.

## 🏗️ The Standard Deployment Workflow

Report-Only mode is the right first step for every new Conditional Access policy. The workflow:

**Phase 1: Report-Only** 📝 (2-4 weeks)
- Create the policy in Report-Only mode
- Let it run for at least 2 weeks to capture the full range of sign-in patterns (including weekly and monthly processes)
- Review the results regularly

**Phase 2: Analyze** 🔎
- Who would be blocked that shouldn't be?
- What service accounts are in scope that can't satisfy the grant control?
- What legacy applications are using old protocols?
- Are emergency access accounts excluded?
- What's the false positive rate?

**Phase 3: Adjust** 🔧
- Fix assignment scope if it's too broad or too narrow
- Add exclusions for service accounts that need separate handling
- Update named locations if they're misconfigured
- Verify emergency access account exclusions

**Phase 4: Enforce** ✅
- Switch the policy from Report-Only to On
- Monitor the sign-in logs for unexpected blocks in the first week
- Have a rollback plan ready (switching back to Report-Only or Off)

## ⚙️ The Three Policy States

Conditional Access policies have three states:

**On** ✅: The policy is active and enforced. Every matching sign-in is evaluated and the grant control is applied.

**Report-Only** 📊: The policy evaluates but doesn't enforce. Results are logged for analysis.

**Off** ❌: The policy is disabled. It doesn't evaluate anything. Useful for pausing a policy without deleting it.

Switching between states is instant and doesn't require creating a new policy. You can go from Report-Only to On, from On back to Report-Only, or from On to Off without losing the policy configuration.

## ⚠️ What Report-Only Doesn't Catch

Report-Only mode is excellent for understanding coverage and identifying unexpected scope. It has one significant limitation: it tests what would happen based on current sign-in behavior. It doesn't predict future behavior.

The legacy auth scenario is a good example. If an application only uses legacy auth quarterly for a report export process, and the report-only period happens to not include a quarter-end, that application won't show up in the report-only logs. It'll show up as a helpdesk ticket after enforcement.

To mitigate this: run report-only for at least a full business cycle that includes any monthly, quarterly, or irregular processes. 30 days is a reasonable minimum. 60 days captures more edge cases.

## 💡 The "What If" Tool for Targeted Testing

Report-Only mode captures results from real sign-ins. The "What If" tool in Conditional Access provides targeted hypothetical testing: specify a specific user, app, conditions, and see which policies would fire and what they'd do.

What If is useful for testing specific scenarios: "what happens to this service account when it tries to access this app?" Report-Only is better for understanding the broad population impact over time.

Use both: What If for pre-deployment spot checking, Report-Only for observing real behavior over time before enforcement.

---

💬 **What's the most surprising thing you discovered by running a policy in Report-Only mode before enforcement?** The legacy auth scenarios that appear are often genuinely unexpected. Printers, conference room displays, old integrations, monitoring tools. What did report-only reveal in your environment that would have caused an outage if you'd enforced immediately?
<!-- nav -->

---

[← Require Authentication Strength](glossary-7-17-require-authentication-strength.md) | [Home](../README.md) | [Location →](glossary-7-19-location.md)
