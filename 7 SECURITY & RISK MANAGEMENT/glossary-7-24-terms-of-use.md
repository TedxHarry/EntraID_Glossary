# Terms of Use
*Making Consent Part of the Access Flow*

**Part of Entra ID Glossary Series: Glossary#7.24 - Terms of Use**

---

A healthcare organization had an acceptable use policy. It was a PDF on the intranet. New employees were supposed to read it during onboarding. Most didn't. When a nurse used a personal device to access patient records in a way that violated the policy, the organization had no evidence the nurse had ever agreed to the policy. The compliance investigation was complicated.

They added a Terms of Use to their Conditional Access policy for the records application. Every user, on every device, was required to review and accept the terms before accessing patient data. Acceptance was recorded with a timestamp and the user's identity in Entra ID.

The next policy question came with documented, timestamped proof of acceptance from every user.

## 📋 What Terms of Use Is in Conditional Access

Terms of Use is a grant control in Conditional Access that requires users to review and explicitly accept a document before access is granted to a resource. The acceptance is recorded in Entra ID with the user identity, timestamp, and the specific ToU document version they accepted.

The ToU document is a PDF uploaded to Entra ID. It can be any document: acceptable use policy, data handling requirements, compliance statements, guest access agreements, third-party data sharing notices.

When a Conditional Access policy with a Terms of Use requirement fires, users see a page displaying the document with an "Accept" and "Decline" button. If they accept, access is granted (assuming other grant controls are satisfied). If they decline, access is denied.

## 🏗️ How Terms of Use Works Technically

**Document setup** 📄: In Entra admin center, under Protection > Terms of Use, upload a PDF of your document. Configure the display name, language, and acceptance settings.

**Policy integration** 🔒: In a Conditional Access policy, add the ToU as a grant control. It can be combined with other grant controls (require MFA AND require ToU) or used alone.

**User experience** 👤: On first access after the policy is enabled, users see the ToU page. They review the document, scroll through it (optionally enforced), and click Accept or Decline. Accepted once, they don't see it again until re-acceptance is required.

**Re-acceptance** 🔄: ToU can be configured to require re-acceptance on a schedule (annually, on document update, etc.). When re-acceptance is triggered, users see the ToU page again on their next sign-in.

## 🎯 Where Terms of Use Is Appropriate

**Regulated data access** 🏥: Healthcare (HIPAA), financial services, legal work. Users handling regulated data should explicitly acknowledge the data handling requirements and applicable regulations.

**External and guest users** 🌍: Partners and guests accessing your resources should acknowledge what they're allowed to do with that access. Guest ToU often covers confidentiality, data use restrictions, and security requirements.

**High-value applications** 💼: Applications with sensitive data, intellectual property, or significant privacy implications. Making users explicitly acknowledge the sensitivity raises awareness and creates compliance documentation.

**Regulatory and compliance requirements** ⚖️: Some frameworks and regulators require documented evidence of user acknowledgment of policies. ToU provides a verifiable audit trail: who accepted, when, and which version.

**Acceptable use for all employees** 👥: Some organizations require annual re-acceptance of the general acceptable use policy as a Conditional Access condition. Every user must acknowledge the policy annually to maintain access.

## 📊 The Audit Trail Value

The most underappreciated feature of Conditional Access Terms of Use is the audit trail. Every acceptance is logged in Entra ID:

- User identity (UPN and Object ID)
- Timestamp of acceptance
- IP address of the sign-in
- Device information
- Which ToU document and version was accepted

This data is available through the Entra admin center (under Protection > Terms of Use > select the ToU > View Audit Log) and through Azure Monitor / Log Analytics for more sophisticated reporting.

For compliance purposes, this is proof of acceptance that's tied directly to the user's authenticated identity, not a PDF form or checkbox in a training system that could have been completed by anyone.

## ⚙️ Configuration Options

**Per-device acceptance** 💻: Users can be required to accept the ToU on each device they use, rather than once per user. Useful for organizations that want explicit acceptance tied to each device access.

**Multi-language support** 🌍: ToU documents can have versions in multiple languages. Entra ID shows the user the version matching their browser language preference, falling back to the default if their language isn't available.

**Expiration** 📅: Set a date after which acceptance expires and re-acceptance is required. Annual expiration is common for compliance purposes.

**Require expanded view** 📜: Optionally require users to scroll through the entire document before the Accept button is available. Reduces rubber-stamping.

## ⚠️ What Terms of Use Doesn't Do

ToU records that a user accepted a document. It doesn't verify that they read or understood it. A user who clicks Accept without reading has still "accepted" for audit purposes.

ToU also doesn't provide a legal guarantee that the acceptance is binding in all jurisdictions. The legal status of electronic acceptance of terms varies by location and context. For high-stakes legal agreements, work with legal counsel rather than relying solely on Conditional Access ToU.

---

💬 **Have you used Terms of Use as a Conditional Access grant control for compliance or audit purposes?** The timestamp-and-identity audit trail it provides is often better evidence of policy acceptance than the traditional "sign here" onboarding document approach. What drove your organization to add ToU to your access policies?
<!-- nav -->

---

[← Session Control](glossary-7-23-session-control.md) | [Home](../README.md) | [Authentication Strength →](glossary-7-25-authentication-strength.md)
