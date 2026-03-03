# LLTs (Long Lived Tokens)
*Why 24-Hour Workload Tokens Are Safer Than You'd Think*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #10.11 - LLTs (Long Lived Tokens)

---


The instinct when thinking about token security is: shorter is safer. A one-hour token that's compromised has a one-hour blast radius. A 24-hour token that's compromised has a 24-hour blast radius. Shorter lifetimes mean shorter windows of exposure.

That instinct is correct in isolation. But it misses something: every token acquisition is also an authentication event, and authentication events are attack surfaces. An application that re-authenticates once per hour has 24 authentication events per day. An application that re-authenticates once per day with a long-lived token has one.

Long-lived tokens flip the tradeoff: extend the valid window, reduce the authentication surface, and rely on Continuous Access Evaluation to revoke the token in near-real-time when something goes wrong.

## 🔑 What long-lived tokens are

Long-Lived Tokens (LLTs) are access tokens issued with extended validity periods, up to 24 hours, specifically for workload identities when CAE is supported by both the client and the resource provider.

Standard access tokens for workloads typically expire in one hour. LLTs extend this to cover an entire working day, or a full day of automated processing, without requiring the workload to re-authenticate. The extended lifetime is only issued when the resource provider supports CAE, because CAE provides the near-real-time revocation capability that makes the longer window manageable.

LLTs aren't a separate token type in the technical sense. They're standard JWT access tokens with a later expiry time (`exp` claim). What makes them "long-lived" is the combination of the extended lifetime and the CAE-based revocation mechanism that enforces policies despite the longer window.

## ⚙️ The tradeoff explained

Standard token lifecycle without CAE:

Token issued with 1-hour expiry. Workload uses token until it expires. If permissions are revoked at the 30-minute mark, the workload continues to have valid access for another 30 minutes. The maximum exposure window for a revoked permission is the token's remaining lifetime, up to one hour.

Long-lived token with CAE:

Token issued with 24-hour expiry. Workload uses token. If permissions are revoked, the resource provider is notified by Entra ID via the CAE mechanism. The resource provider rejects the token in near-real-time. The workload tries to get a new token. The new token request fails because the permission is revoked.

The exposure window after revocation isn't 24 hours; it's the CAE notification latency, which is measured in seconds to minutes, not hours.

This is why LLTs, counterintuitively, can offer better security posture than short-lived tokens in a CAE-capable environment: the revocation is near-real-time regardless of the token's remaining lifetime, and the reduced authentication frequency shrinks the attack surface at the authentication layer.

## 📊 Authentication overhead reduction

For workloads making frequent calls to Microsoft Graph, Azure Storage, or other CAE-capable services, reducing authentication frequency from once per hour to once per day has measurable operational benefits.

Every token acquisition request is an outbound call to Entra ID's token endpoint. For a workload that processes thousands of items per day and makes one token acquisition per hour, that's 24 token requests per day instead of one. At scale across hundreds of service principals, the authentication overhead adds up.

LLTs are also meaningful for workloads that have cold-start scenarios: applications that spin up quickly, make a burst of API calls, then idle. With one-hour tokens, a workload that runs for 20 minutes, idles for 50, then runs again needs to re-authenticate. With a 24-hour LLT, the same token serves across multiple execution windows throughout the day.

## 🔒 What llts don't change

LLTs don't change the fundamental security model for scenarios where CAE isn't supported. If the resource a workload calls doesn't support CAE, tokens for that resource remain at standard lifetimes. The extended lifetime only applies where the CAE enforcement mechanism exists to back it up.

LLTs also don't change the requirement for secure token storage. A long-lived token that's extracted from memory or stolen from a credential cache is still a valid credential for up to 24 hours. The same protections that apply to short-lived tokens (secure token cache, in-memory handling, no persistence to disk) apply to LLTs.

The security improvement from LLTs comes from the combination of reduced authentication surface and near-real-time CAE revocation. Without both elements, a 24-hour token would be a straightforward security regression.

---

💬 **Has your team measured the authentication overhead from frequent token acquisitions in high-volume workloads?** The shift from hourly to daily token acquisition sounds small, but for workloads making thousands of API calls per day, it can be meaningful. What Azure services are your workloads authenticating to most frequently, and are they CAE-capable?
✍️ TedxHarry

<!-- nav -->

---

[← CAE for Workloads](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-10-cae-for-workloads.md) | [🏠 Contents](/README) | [Conditional Access for Workloads →](/10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-12-ca-for-workloads.md)
