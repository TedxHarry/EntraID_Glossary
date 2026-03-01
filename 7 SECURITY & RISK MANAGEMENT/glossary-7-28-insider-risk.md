# Insider Risk
*When the Threat Already Has a Badge*

> **Difficulty:** 🔴 Advanced

📚 **Part of Entra ID Glossary Series: Glossary#7.28 - Insider Risk**

---

## 🎯 TL;DR

- Insider risk signals from Microsoft Purview can feed into Adaptive Protection in Entra ID
- Adaptive Protection automatically applies stricter CA policies to users with elevated insider risk scores
- Requires both Microsoft Purview Insider Risk Management and Entra ID P2 + the integration enabled


A software engineer at a technology company gave notice. Two weeks later, on her last day, she downloaded 14,000 files from SharePoint. Source code, customer data, internal architecture documents. She had legitimate access to all of it. Her credentials were valid. Her actions didn't trigger any fraud detection.

She joined a competitor two weeks after that.

The investigation that followed took months and cost more in legal fees than the data was worth to recover. The detection had failed because the tools were designed for external attackers, not for someone whose access was legitimate.

Insider risk is the security problem that technical access controls alone can't solve.

## 👤 What Insider Risk Is

Insider risk refers to security threats that originate from within the organization: current employees, contractors, partners, or former employees whose access hasn't been fully revoked. Unlike external attacks that require credential theft or network intrusion, insider risk scenarios involve actors who already have legitimate access.

The challenge is that insider risk behaviors often look identical to legitimate work activities:

- An employee downloading files before leaving looks the same as an employee downloading files to work from home
- An employee accessing systems outside their normal scope looks the same as an employee covering for a colleague
- An employee communicating with external parties looks the same as normal business development

Traditional security controls are designed to detect unauthorized access. Insider risk involves authorized access being used in unauthorized ways.

## 🔍 Types of Insider Risk

**Malicious insiders** 🔴: Employees who intentionally misuse their access for personal gain, retaliation, or to benefit a competitor. Data exfiltration before resignation is the most common pattern. Financial fraud, IP theft, and sabotage are others.

**Negligent insiders** 🟡: Employees who cause security incidents through carelessness rather than malice. Sending sensitive data to personal email for convenience, using unsecured storage, misconfiguring settings that expose data. The intent isn't harmful but the outcome is.

**Compromised insiders** 🟠: Employees whose credentials or devices have been compromised by external actors. The threat technically originates externally but manifests with insider-level access. This is the intersection of external threat and insider risk.

## 🔒 Microsoft Purview Insider Risk Management

Microsoft Purview Insider Risk Management is the dedicated product for detecting and investigating insider risk scenarios. It integrates with Entra ID and Microsoft 365 to analyze behavioral signals across the environment.

The system works by building behavioral profiles and detecting anomalies:

**Departure indicators** 📅: HR data can be fed in (resignation dates, termination events). The system elevates monitoring for users approaching departure dates, as the risk of intentional data exfiltration is highest in the notice period.

**Data handling signals** 📁: Bulk file downloads, uploads to personal storage (OneDrive personal, Dropbox, Google Drive), email sends with large attachments to external addresses, printing sensitive documents.

**Access pattern changes** 🔀: Accessing resources or systems outside the user's normal pattern, accessing data outside their role scope, accessing systems at unusual hours.

**Communication signals** 💬: Language patterns in email and Teams messages that indicate disgruntlement, job searching, or discussion of sensitive topics with external parties. (This signal requires careful consideration of privacy and legal requirements in each jurisdiction.)

## 🔗 Insider Risk and Conditional Access

Insider risk signals can feed into Conditional Access policies through Microsoft's integration between Purview and Entra ID. When a user's insider risk score crosses a threshold, Conditional Access can respond:

**Elevated monitoring**: Route the user's sessions through Microsoft Defender for Cloud Apps for real-time monitoring without restricting access.

**Step-up authentication**: Require additional verification for accessing sensitive resources when a user's insider risk level is elevated.

**Access restriction**: For confirmed high-risk scenarios, limit access to specific resource types or apply read-only session controls while investigation proceeds.

**Account suspension**: In extreme cases, disable the account pending investigation. This is a significant action requiring human review and confirmation.

## ⚠️ The Privacy and Legal Complexity

Insider risk monitoring raises legitimate privacy and legal concerns that external threat monitoring doesn't. Monitoring employee communications and file access at this level may be:

- Subject to works council or union agreement requirements in some countries
- Regulated by employment law regarding monitoring disclosure
- Subject to GDPR and similar privacy laws regarding the processing of employee personal data
- Dependent on clear acceptable use policies that employees have acknowledged

Before deploying insider risk monitoring, involve legal counsel, HR, and employee representatives where required. The technical capability exists. Whether and how to deploy it is a legal and organizational decision.

## 💡 The Human Process Requirement

Technology alone doesn't resolve insider risk cases. A high insider risk score is a flag for human investigation, not an automated verdict.

False positives are common: legitimate data migrations, authorized project work, covering for a colleague's responsibilities. Investigation requires context that the system can detect but not interpret.

Organizations deploying insider risk capabilities need a defined investigation process: who reviews alerts, what evidence is required to escalate, who makes access decisions, how cases are documented, when legal or HR involvement is triggered.

---

💬 **Has your organization implemented any form of insider risk monitoring?** The conversation about deploying it is often more complex than the technical setup because of privacy, legal, and cultural considerations. What was the hardest part of getting agreement to monitor insider risk signals?
> ✍️ *Written by **TedxHarry***


> 🔑 **Licensing:** Adaptive Protection (Insider Risk + CA integration) requires **Microsoft Purview Insider Risk Management** + **Entra ID P2**.

<!-- nav -->

---

[← SSPR (Security Focus)](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-27-sspr-security.md) | [🏠 Contents](/README) | [User Risk Level →](/7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-29-user-risk-level.md)
