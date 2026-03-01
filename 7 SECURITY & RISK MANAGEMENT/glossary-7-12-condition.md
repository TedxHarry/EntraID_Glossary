# Condition
*The Signals That Make Conditional Access Contextual*

**Part of Entra ID Glossary Series: Glossary#7.12 - Condition**

---

Two sign-ins. Same user. Same application. Same credentials.

First sign-in: 9am, corporate office, managed Windows laptop, compliant device, familiar location. Result: granted, no additional prompts.

Second sign-in: 11pm, unrecognized location, personal Android phone, no device management, anonymous IP, MFA hasn't been used for 18 days. Result: required MFA, required password change, session limited to read-only.

The difference wasn't the identity. It was the conditions. Conditions are what make Conditional Access context-aware rather than just authentication-aware.

## 📊 What Conditions Are

Conditions are additional signals evaluated by a Conditional Access policy after the assignment scope matches. They narrow or broaden when a policy fires and what it responds to.

Without conditions, a policy fires for every matching user and app, every time. With conditions, the policy only fires when specific additional circumstances are present. Or it fires with different grant controls depending on which conditions are true.

Conditions are the mechanism that lets Conditional Access policies respond to the "circumstances of this access request" rather than just "is this the right user?"

## 🔍 The Condition Types

**Sign-in risk** 🔴: The risk level assigned by Entra ID ID Protection to the specific sign-in event. High, medium, low, or no risk. Requires Entra ID P2 licensing.

Use this condition to build policies that respond differently to risky vs clean sign-ins. "If sign-in risk is high, block access" and "if sign-in risk is medium, require MFA" can be two separate policies targeting the same apps and users, each firing on different risk levels.

**User risk** 👤: The risk level of the user account itself, separate from any specific sign-in. High user risk often means credentials were found in breach data or anomalous activity was detected. Requires Entra ID P2.

**Device platforms** 📱: Windows, macOS, iOS, Android, Linux, Windows Phone. Use this to apply different controls to different device types. Require compliant device for Windows and macOS. Require app protection policy for iOS and Android. Block access from platforms you don't support.

**Locations** 📍: Named Locations defined in the Entra admin center. IP address ranges or countries. Use locations to exclude trusted network ranges (corporate offices, VPN egress points) from MFA requirements. Or use them to block access from countries where your organization has no presence.

**Client apps** 💻: What application type is being used for authentication. Browser (modern auth). Mobile apps and desktop clients (using MSAL/modern auth). Exchange ActiveSync. Other clients (legacy auth protocols: basic auth, NTLM, older protocols that can't satisfy MFA).

The client apps condition is critical for legacy authentication blocking. Legacy auth clients can't satisfy MFA, so attackers actively seek out accounts accessible via legacy protocols. A policy that blocks "other clients" (legacy auth) eliminates this attack vector entirely.

**Authentication strength** 🔐: What authentication method was used. A policy can require that access to highly sensitive resources uses phishing-resistant MFA (FIDO2, certificate-based auth) rather than just any MFA (SMS OTP, voice call). This differentiates between "the user authenticated with something" and "the user authenticated with something that can't be phished."

**Filter for devices** 🖥️: Device-attribute-based filtering beyond just platform type. Target policies at specific device extension attributes, device trust types (Entra Registered, Entra Joined, Hybrid Entra Joined, Entra Compliant), or other device properties.

## ⚙️ How Conditions Combine

Conditions within a single policy use AND logic. A policy with both a location condition and a device platform condition only fires when the sign-in matches both: the specified location AND the specified platform.

This lets you build precise policies. "Require MFA when signing in from outside trusted locations on iOS or Android devices" combines a location condition (not a named trusted location) and a platform condition (iOS or Android).

For OR logic across conditions, you need separate policies. "Apply this control when sign-in risk is high OR when user risk is high" requires two policies: one with a sign-in risk condition, one with a user risk condition, both with the same grant control.

## 🎯 Common Condition Patterns

**Legacy auth block** 🚫: Client apps condition targeting "Other clients" + Grant: Block access. No additional conditions needed. Block all legacy authentication unconditionally.

**Location-based MFA exemption** ✅: Location condition excluding "Corporate trusted locations" + Grant: Require MFA. The policy fires everywhere except the trusted locations. Users at the office get through without MFA. Users elsewhere are required.

**Risk-responsive access** 🔴: Sign-in risk condition set to High + Grant: Block access. Separate policy with sign-in risk set to Medium + Grant: Require MFA. The policies respond to different risk levels with different responses.

**Phishing-resistant auth for sensitive apps** 🔐: Authentication strength condition requiring phishing-resistant methods + Applied to specific high-value apps. Standard MFA is acceptable everywhere else. Sensitive apps require stronger methods.

**Device-specific controls** 📱: Device platform condition for iOS and Android + Grant: Require approved app. Ensures mobile access to corporate data happens through managed apps with app protection policies, not through any browser.

## ⚠️ The Unintended Interaction

Conditions interact with assignments in non-obvious ways. A condition that fires for one group of users may not fire for another, even within the same policy scope.

Testing condition behavior with the What If tool before enforcement is essential. The scenarios that need testing aren't just the happy path. Test the edge cases: a user on a VPN whose IP is in a trusted location but who is accessing from a blocked country. A device that meets platform conditions but fails device filter conditions. A sign-in that uses a client app type that wasn't considered.

---

💬 **Which condition type has generated the most unexpected behavior in your environment?** The client apps condition and legacy auth blocking tends to surface applications that teams didn't know were using basic auth. What was the legacy auth offender that surprised your team when you started blocking it?
<!-- nav -->

---

[← Assignment](glossary-7-11-assignment.md) | [Home](../README.md) | [Grant Control →](glossary-7-13-grant-control.md)
