# CA Policy
*Building the If-Then Logic of Access Control*

**Part of Entra ID Glossary Series: Glossary#7.9 - CA Policy**

---

An organization had Conditional Access deployed. Their policy was: require MFA for all users, all apps.

It was one policy. It covered everything. It was also wrong.

The policy required MFA for service accounts that authenticate machine-to-machine with no user present. Service accounts can't satisfy MFA. The workaround was excluding service accounts from the policy. The exclusion list grew. Eventually the exclusion list had 47 entries, including several accounts whose purpose nobody remembered. The policy's coverage had quietly eroded over two years.

Good CA policy design isn't about having one policy that covers everything. It's about having a set of policies that cover everything correctly, with the right controls for the right scenarios.

## 📋 What a CA Policy Is

A Conditional Access policy is a discrete rule that evaluates specific access requests and enforces specific controls when those requests match. A tenant can have many CA policies. Each one is evaluated independently. A sign-in is evaluated against every active policy. The most restrictive matching policy wins.

Every policy has the same components:

**Name** 🏷️: What this policy does. Make it descriptive. "Require MFA - All Users - All Apps" is clear. "Policy 7" is not.

**State** 🔄: On, Off, or Report-Only. Off means the policy is disabled. Report-Only means it evaluates but doesn't enforce.

**Assignments** 👥: The scope of who and what this policy covers.

**Conditions** 📊: Additional signals that refine when the policy fires.

**Grant controls** 🔑: What the policy enforces when it fires.

**Session controls** 🔒: Additional constraints on granted sessions.

## 👥 Assignments: Defining Scope

Assignments define who the policy applies to and what it applies to. A policy with misconfigured assignments either covers too much or too little.

**Users and groups**: Include or exclude specific users, groups, directory roles. Workload identities (service accounts, managed identities) are configured separately. The common error is including all users and then building an exclusion list. Exclusion lists grow, they're rarely reviewed, and they become the path of least resistance for bypassing policies. Include specifically where possible rather than excluding broadly.

**Cloud apps and actions**: Which applications does this policy cover? All cloud apps, or specific ones. Targeting specific apps lets you apply appropriate controls for the sensitivity level of each app. High-value apps get strict controls. Less sensitive apps get lighter touch.

**Target resources**: Newer policies can target specific resource types beyond just apps.

The combination of user assignment and app assignment defines the exact scenarios this policy evaluates. A policy targeting "all users" and "Microsoft 365" only fires when a user in scope tries to access Microsoft 365. Sign-ins to other apps are evaluated against other policies.

## 📊 Conditions: Refining When the Policy Fires

Conditions narrow or broaden when a policy applies within its assignment scope:

**Sign-in risk** 🔴: Only fire this policy when the sign-in risk level is High, Medium, or Low. Used to build risk-responsive policies.

**User risk** 👤: Only fire this policy when the user's risk level is High, Medium, or Low.

**Device platforms** 📱: Only apply to Windows, macOS, iOS, Android. Useful when different device types need different controls.

**Locations** 📍: Only apply when sign-in comes from specific Named Locations, or apply everywhere except specific Named Locations. Used for IP-based trust or geographic blocking.

**Client apps** 💻: Only apply to browser access, or mobile app access, or legacy protocols (Exchange ActiveSync). Critical for blocking legacy authentication, which can't satisfy MFA.

**Authentication strength**: Only apply when the authentication method used meets or doesn't meet a specified strength level.

Conditions are AND logic by default within a policy. A policy with both a location condition and a platform condition only fires when both conditions are met simultaneously.

## 🔑 Grant Controls: The Access Decision

When a policy fires (assignments match, conditions evaluate), the grant control determines the outcome:

**Block access** 🚫: The request is denied. No way through.

**Grant access** ✅: Access is allowed, with or without additional requirements. Additional requirements (MFA, compliant device, domain join) are specified as part of the grant.

When multiple requirements are specified: "Require all selected controls" means every requirement must be satisfied. "Require one of the selected controls" means satisfying any one is sufficient.

The order of specificity matters for user experience. Requiring MFA alone is less disruptive than requiring MFA plus a compliant device. Set controls that match the sensitivity of the resource.

## 🔒 Session Controls: Constraints After Access

Session controls apply after access is granted:

**Sign-in frequency**: How often must the user re-authenticate. Override the default token lifetime for specific apps.

**Persistent browser session**: Whether the "stay signed in" option is available.

**Continuous Access Evaluation**: Whether the session token respects near-real-time revocation signals.

**App-enforced restrictions**: For supported apps like Exchange Online and SharePoint, apply in-app restrictions based on the session context. Unmanaged devices might get read-only access while managed devices get full access.

**MCAS (Microsoft Defender for Cloud Apps) session policies**: Route the session through MCAS for monitoring or control.

## ⚙️ Policy Evaluation Order

All enabled policies are evaluated for every sign-in. If two policies both match a sign-in, both are applied. If one requires MFA and another requires a compliant device, the user must satisfy both. There's no priority order between policies; the union of all matching policies applies.

This is why exclusions need careful design. An exclusion from one policy doesn't exempt the user from other matching policies.

---

💬 **What's the trickiest CA policy interaction you've debugged?** The "why is this user being asked for MFA when they shouldn't be" investigation almost always comes down to an unexpected policy match. What was the policy that surprised you?
<!-- nav -->

---

[← Conditional Access](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-8-conditional-access.md) | [🏠 Contents](/README) | [Zero Trust →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-10-zero-trust.md)
