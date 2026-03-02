# Anomaly Detection
*How Entra ID Learns What Normal Looks Like*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #7.5 - Anomaly Detection

---

## 🎯 TL;DR

- Anomaly detection compares current behavior to historical baseline and flags deviations as risks
- Examples: token issued in one country, used in another (impossible travel); volume anomalies in Graph calls
- Machine learning continuously refines the baseline : detection accuracy improves over time per-tenant


A financial analyst had worked at the same company for six years. She signed in from the same office, on the same laptop, using the same browser, at roughly the same times every day. Her pattern was deeply established.

One Friday afternoon, her account downloaded 4,200 files from SharePoint in 22 minutes. She was in a client meeting at the time. She hadn't touched her computer.

Entra ID's anomaly detection flagged the activity. The Conditional Access policy for high user risk triggered, and the account was blocked for further access pending investigation. The attacker, who had compromised the account through a phishing link the analyst had clicked two weeks earlier, had finally made their move. The detection caught them mid-exfiltration.

## 🔍 What anomaly detection is

Anomaly detection in Entra ID ID Protection is the process of identifying behaviors that deviate significantly from an established baseline for a user or account. It's not rule-based in the traditional sense.

Traditional security rules look like: "alert if more than 100 file downloads in an hour." These rules are static. They treat every user the same. They miss attacks that stay below the threshold. They generate false positives for users whose legitimate work regularly crosses the line.

Anomaly detection works differently. It establishes what's normal for each individual user over time, then flags deviations from that baseline. The analyst who downloads 4,200 files on a Friday afternoon when her baseline shows she downloads an average of 30 files per day on Fridays is flagged. The data engineer who downloads 10,000 files every Tuesday as part of their normal pipeline run is not.

## 🧠 How baselines are built

The baseline for each user is built from their historical behavior across multiple dimensions:

**Sign-in patterns** 📍: What locations does this user typically sign in from? What devices? What time of day? What browser? These patterns build the "normal" fingerprint for each account.

**Application usage** 📱: What applications does this user access? How often? What data volumes are typical for each application?

**Administrative actions** ⚙️: For accounts with elevated permissions, what administrative operations are typical? Frequency, scope, and targets of administrative actions all form part of the baseline.

**Data interaction patterns** 📂: Volume and types of data accessed, shared, downloaded, or sent externally.

The baseline isn't static. It updates as behavior evolves. A user who transitions to a data-intensive role will see their baseline shift over time. A user who starts regularly traveling for work will have international sign-in locations incorporated into their normal pattern.

## 🚨 What triggers anomaly detection

Anomaly detection generates risk events when behavior deviates significantly from the established baseline:

**Anomalous user activity** 🔴: Bulk operations inconsistent with the user's history. Mass file downloads, mass email sends to external recipients, unusual administrative actions outside the user's normal pattern. This is classified as a user risk detection because it reflects the account's behavior after authentication, not the authentication itself.

**Unfamiliar sign-in properties** 🔴: Sign-in from a device, browser, or location the user hasn't used before. The system evaluates novelty relative to the user's specific history, not against a generic threshold.

**Atypical travel** 🟡: Sign-in timing and locations that are unusual for this user but don't reach the threshold for impossible travel.

The anomaly detection signals feed into the overall risk scoring system. A single anomalous behavior might generate a low or medium risk signal. Multiple anomalies in combination can push the aggregate to high.

## ⚠️ The false positive challenge

Anomaly detection generates false positives. This is unavoidable. Legitimate users do unusual things. They travel to new countries. They work on a borrowed laptop when their regular device fails. They run a one-time data export for an audit. They start a new project that requires accessing systems they've never touched before.

The key is making false positives manageable, not eliminating them:

**Graduated response**: Low and medium risk anomalies prompt for MFA rather than blocking. The legitimate user confirms their identity and proceeds. The attacker who doesn't have MFA access is blocked. This design handles most false positives without user disruption.

**Investigation and dismissal**: When a false positive is investigated and dismissed as safe, the system learns. The user's baseline incorporates the behavior. Similar future events generate lower risk scores.

**Pre-registration for known anomalies**: Named Locations in Conditional Access let organizations register IP ranges (office locations, VPN endpoints, cloud egress points) as trusted. Traffic from these ranges is treated as familiar even if the specific IP is new.

## 💡 The operational trade-off

Anomaly detection is about sensitivity vs specificity. High sensitivity catches more attacks but generates more false positives. High specificity reduces false positives but misses more attacks.

The right balance depends on the account. For standard user accounts, a moderate sensitivity that prompts MFA for anomalies strikes the right balance. For privileged accounts with access to sensitive systems, higher sensitivity and stricter response policies are appropriate. Missing an attack on a Global Administrator is more costly than an occasional extra MFA prompt.

The analyst's 4,200-file download was caught because her baseline was clear and the deviation was extreme. Not every attack will be this obvious. Tuning the baseline through false positive feedback over time is what separates effective anomaly detection from noise.

---

💬 **Has anomaly detection in Entra ID caught something in your environment that traditional threshold-based rules would have missed?** The bulk file download scenario is common, but some of the more subtle behavioral detections are genuinely impressive. What was the anomaly that made you trust the system?
✍️ TedxHarry


> 🔑 **Licensing:** Anomaly detection signals are generated by Identity Protection : requires **Entra ID P2**.

<!-- nav -->

---

[← ID Protection](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-4-id-protection.md) | [🏠 Contents](/README) | [Leaked Credentials →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-6-leaked-credentials.md)
