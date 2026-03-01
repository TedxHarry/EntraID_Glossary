# Policy Evaluation
*Understanding How Conditional Access Decisions Are Made*

📚 **Part of Entra ID Glossary Series: Glossary#13.20 - Policy Evaluation**

---

A user called the helpdesk because they couldn't access Salesforce from their laptop. They could access everything else. The helpdesk agent couldn't reproduce the issue from their own workstation. An administrator spent 40 minutes reviewing the 37 active Conditional Access policies trying to figure out which one was blocking access and why.

The answer was in the sign-in log the whole time, in the Conditional Access tab of the sign-in event. It showed exactly which policies had been evaluated, which applied, and what each one required. The user's laptop was compliant, but the Salesforce enterprise application had a policy requiring phishing-resistant MFA that the user had never been prompted to register.

CA policy evaluation tools exist precisely to answer questions like this without guessing.

## 🔍 How Conditional Access Evaluation Works

When a user attempts to authenticate and access a resource, the Conditional Access evaluation engine checks every active policy in the tenant to determine which ones apply to this specific sign-in. Policies are evaluated simultaneously, not sequentially. All applicable policies must be satisfied for access to be granted.

The evaluation engine applies this logic:

**Condition matching** 🎯: For each policy, the engine checks whether the sign-in satisfies the conditions (user, application, platform, location, client app, device state, risk levels). If any condition doesn't match, the policy doesn't apply to this sign-in. No condition match means no policy evaluation for that sign-in.

**Grant control assessment** ✅: For policies where all conditions match, the engine checks what grant controls are required (MFA, compliant device, hybrid joined, approved app, app protection policy) and whether the current sign-in satisfies them.

**Session control application** 📱: For policies that are satisfied, session controls (sign-in frequency, persistent browser session, app-enforced restrictions) are applied to the resulting session.

**Conflict resolution** ⚠️: When multiple applicable policies have conflicting controls, the most restrictive result wins. If one policy grants access with MFA and another policy blocks access, block takes precedence. Among grant controls, all required controls must be satisfied.

## 🔧 The What If Tool

The What If tool is a policy simulation capability in the Conditional Access blade that lets administrators answer: "If this user tried to sign in to this application from this location on this device, which policies would apply and what would happen?"

You specify:

**User** 👤: Specific user account, or a guest user type.

**Application** 📱: The specific application or the authentication endpoint being targeted.

**IP address** 🌐: Simulates signing in from a specific network location. Useful for testing named location conditions.

**Device platform** 💻: Windows, macOS, iOS, Android, Linux. Tests platform-based CA conditions.

**Client app** 🔗: Browser, mobile app, desktop client. Tests client app conditions.

**Device state** ✅: Whether the simulated device is compliant or hybrid joined.

**Sign-in risk level** ⚠️: High, medium, low, none. Tests risk-based CA policy behavior.

The What If result shows every policy evaluated, whether each policy matched (and why or why not), and the combined outcome. It answers definitively which policies would block access, which would grant with controls, and which wouldn't apply.

## 📊 Report-Only Mode

Report-only mode lets you deploy a CA policy in a non-enforcing state. The policy is evaluated for every sign-in in scope, but it doesn't block or grant based on its controls. Instead, the evaluation result (would have blocked, would have required MFA, would have required compliant device) is logged to the sign-in log.

This is how you safely answer the question: "If I turn on this policy, what will actually break?"

A policy in report-only mode for a week accumulates real data: how many sign-ins matched its conditions, how many users would have been required to do something different, which specific users would have been blocked. That data lets you make decisions about scope adjustments before enforcement creates disruption.

Report-only mode is especially valuable for new policies targeting large user populations, policies with device compliance conditions (where device enrollment rates may be lower than expected), and risk-based policies where you want to observe what would trigger before you commit to enforcement behavior.

## 📋 Sign-In Log CA Details

Every sign-in event in the Entra ID sign-in log includes a Conditional Access tab showing the evaluation results for that specific sign-in. For each policy evaluated:

**Status**: Not applied (conditions didn't match), Success (applied and satisfied), Failure (applied but requirements not met).

**Grant controls**: Which controls the policy required and whether they were satisfied.

**Session controls**: Which session controls the policy applied.

This is the diagnostic tool for real-world CA issues. When a user calls saying they can't access something, find their sign-in event, open the CA tab, and you'll see exactly which policy blocked them and which specific control they didn't satisfy. The troubleshooting time drops from 40 minutes of policy review to a 2-minute log investigation.

## 🏗️ CA Insights and Reporting

The Conditional Access Insights and Reporting workbook aggregates sign-in log CA data across all users and shows it at the policy level:

**Policy coverage** 📊: How many sign-ins matched each policy versus how many sign-ins occurred that the policy didn't apply to. Policies with low match rates relative to total sign-in volume may have scoping issues.

**Outcome distribution** 📈: For each policy, how many sign-ins resulted in Success, Failure, or Not Applied. High failure rates on a policy often indicate a condition that's misconfigured or a user population that wasn't expected to be in scope.

**User impact** 👥: Which specific users are most frequently affected by each policy. Useful for identifying users who are repeatedly failing a specific control (and may need remediation like device enrollment or MFA registration) versus users who are genuinely blocked from access they need.

---

💬 **When you troubleshoot a CA-related access issue, do you go to the sign-in log CA tab first, or do you still find yourself manually reviewing individual policies?** The sign-in log CA details exist specifically to eliminate policy review as the diagnostic approach, but awareness of the tool is uneven across teams. What's the most complex CA evaluation scenario your team has had to untangle?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← CA Optimization Agent](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-19-ca-optimization-agent.md) | [🏠 Contents](/README) | [Microsoft Graph API →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-21-graph-api.md)
