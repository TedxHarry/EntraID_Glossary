# Block Access
*The Hardest Grant Control to Get Right*

**Part of Entra ID Glossary Series: Glossary#7.14 - Block Access**

---

An administrator wanted to stop sign-ins from countries where their organization had no business presence. Reasonable policy. They created a Conditional Access policy targeting All users, All cloud apps, with a location condition for the countries they wanted to block, and a grant control of Block access.

They tested it. It worked. They set it to enforcement mode.

Fifteen minutes later, the helpdesk had 23 tickets. Remote employees who were traveling. The CTO, who was in Singapore for a conference. A developer who'd relocated temporarily to Spain but hadn't told IT. A vendor who was on-site with a client in Germany.

The policy was right in principle. The scope was wrong. Block access is the most powerful grant control. It's also the one that does the most damage when misconfigured.

## 🚫 What Block Access Does

Block access is a Conditional Access grant control that denies the access request entirely. No bypass. No step-up option. No way through for the user to present additional verification.

When a policy with block access fires:
- The user sees a generic error message indicating access is blocked
- No MFA prompt is offered
- The user cannot do anything from that session to resolve it
- Only an administrator can address a block access situation

This is intentional. Block access is designed for scenarios where there's no legitimate reason to allow access under these conditions, regardless of what the user can present. It's not "step up to MFA." It's "you may not proceed."

## 🎯 When Block Access Is the Right Control

Block access is appropriate when the conditions it fires on represent scenarios where no legitimate user should ever be accessing this resource:

**Legacy authentication protocols** 🔌: Clients using basic auth, NTLM, or other legacy protocols can't satisfy MFA. Block them. There's no legitimate reason for modern cloud resources to be accessed via legacy auth. Any user trying to access via legacy protocols is either using very old software (which should be updated) or an attacker trying to bypass MFA.

**Countries with no business presence** 🌍: If your organization has no employees, partners, or operations in specific countries, sign-ins from those countries have no legitimate source. Blocking them reduces attack surface. The important design detail: the location condition should target "Selected locations" (the countries to block) with careful thought about VPN egress points and traveler scenarios.

**Specific risky platforms you don't support** 📱: If your organization explicitly doesn't support Linux or Windows Phone, you can block those platforms. Be sure the support decision is firm before the policy is.

**High-risk sign-ins to sensitive resources** 🔴: A sign-in risk of high on the most sensitive systems (admin portals, financial systems, HR data) warrants a block rather than a step-up prompt. The attacker who has compromised credentials won't satisfy MFA either, but high-risk sign-ins to admin systems are the most dangerous scenario, and a step-up prompt gives the attacker a chance to social-engineer the user.

**Guest access to specific resources** 🚫: If external users should never access certain applications regardless of how they're invited, block access for guest identities to those specific apps.

## ⚠️ When Block Access Goes Wrong

Block access errors share a pattern: they fire on conditions that include legitimate users who have no way to resolve the block themselves.

**The traveling employee problem**: Location-based block policies need to account for business travel. Options include a named location exclusion list for commonly visited countries, an emergency access process for travelers, or using more granular conditions combined with step-up rather than block.

**The VPN exit problem**: If users connect through a VPN that exits in a country on your block list, every user on that VPN is blocked. Know where your VPN exits before deploying location-based blocks.

**The overly broad app scope**: A block policy targeting "All cloud apps" blocks everything, including the sign-in portal, password reset, MFA registration. If users are blocked before they can register MFA methods, they're stuck in a loop. Always exclude MFA registration user actions from block policies.

**The forgotten service account**: A block policy for legacy auth that catches a service account authenticating via basic auth. The service account breaks silently and nobody notices for three days until the process that depends on it fails visibly.

## 🔧 Block Access Policy Design

The discipline required for block access policies is more rigorous than for step-up policies. Because the impact of a misconfigured block is immediate and the user has no self-service resolution path:

**Start in report-only mode** 📊: Always. For block policies specifically, report-only reveals the blast radius before enforcement. Review the sign-ins that would have been blocked and validate that none of them are legitimate.

**Narrow the scope precisely** 🎯: Overly broad block policies are more dangerous than overly broad MFA policies. An extra MFA prompt is annoying. An extra block is a production outage.

**Exclude emergency access accounts** 🔴: Break-glass accounts must never be caught by block policies. They exist for scenarios where everything else is wrong. A block policy that catches break-glass accounts is a global admin lockout waiting to happen.

**Document the intent** 📋: Block access policies should have a documented owner, a documented purpose, and a documented review schedule. "Why is this user blocked and who can unblock them?" should have a clear answer that doesn't require forensic investigation of the policy configuration.

**Pair with an unblock process** 🔑: What's the process when a legitimate user is blocked? Who do they contact? What information do they need to provide? How quickly can the block be resolved? Block access without an unblock process creates support escalations that surface at the worst possible times.

## 💡 Block vs Require MFA: The Decision

The choice between block and require MFA is about whether any legitimate user should be able to access this resource under these conditions:

- If yes, even rarely: require MFA (let them prove themselves)
- If absolutely not, ever: block access

Most scenarios are the former. Block access is reserved for scenarios where the condition itself (legacy protocol, unsupported country, specific platform) eliminates any legitimate use case entirely.

---

💬 **Have you deployed a block access policy that caused an unexpected outage?** The legacy auth block catching a service account or the location block catching a traveling executive are both classic block-access war stories. What was the post-mortem lesson?
<!-- nav -->

---

[← Grant Control](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-13-grant-control.md) | [🏠 Contents](/README) | [Require MFA →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-15-require-mfa.md)
