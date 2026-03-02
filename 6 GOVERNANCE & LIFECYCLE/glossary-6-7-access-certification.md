# Access Certification
*When "Reviewed" Has to Mean Something to an Auditor*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.7 - Access Certification

---

## 🎯 TL;DR

- Access certification is the formal process of having stakeholders confirm that user access is still needed
- Failed certifications trigger automatic removal : 'recertify or lose access'
- Required for compliance frameworks (SOX, ISO 27001) that mandate periodic access reviews


The compliance auditor asked for evidence that privileged access to the financial system had been reviewed in the past 90 days. The IT team pulled together email threads, spreadsheets, and a SharePoint document that had been manually updated. The auditor looked at it for a few minutes and asked: "Who approved each individual access decision, and what evidence do you have that they actually reviewed it rather than rubber-stamped it?"

There was silence.

The evidence existed, but not in a form the auditor could evaluate. Access certification is what changes that: a formal process with documented evidence that specific people certified specific access decisions at a specific time.

## 📋 What makes certification different from review

Access review and access certification are closely related and often used interchangeably. The distinction is primarily about formality and evidence:

**Access Review** is the operational practice of periodically checking whether access is still appropriate. It can be informal, scheduled based on operational need, and its output is updated permissions.

**Access Certification** is the formal attestation process where designated certifiers sign off that access is appropriate and necessary for business operations. The output is a documented, auditable record of who certified what access, when, and for what justification. This record is what satisfies compliance requirements.

In Microsoft Entra ID Governance, access reviews produce both: they change permissions (the operational outcome) and they create an audit trail (the compliance evidence).

## 🔒 Who certifies what

Access certification campaigns define the certifier based on the type of access being certified:

**Resource owner certification** 🏢: The owner of an application or system certifies who has access to it. They're certifying: "I, as the responsible person for this system, confirm that each person on this list has appropriate business justification for their access."

**Manager certification** 👤: Each user's direct manager certifies their team members' access. They're certifying: "My direct reports have access appropriate for their roles and responsibilities."

**HR-driven certification** 📄: For compliance frameworks requiring certification that access matches job function, the human resources data (job title, department, employment type) is used to validate that access is role-appropriate.

**User self-certification** ✋: For some access types, users certify that they still need and use the access they have. Less rigorous, but useful for less sensitive resources where scale makes manager certification impractical.

## 📊 The evidence access certification produces

A completed access certification in Entra ID creates an auditable record containing:

- Which users had access at the time of certification
- Which certifier reviewed each user's access
- Whether they approved or denied
- The justification provided (if required)
- The timestamp of each decision
- Whether access was removed following a denial
- The names of certifiers who didn't respond and the fallback action applied

This record can be exported, stored for compliance retention periods, and provided to auditors as evidence of the certification activity. It answers the questions the auditor in the opening story was asking.

## 🔄 Certification frequency by access type

Different access types warrant different certification frequencies:

| Access Type | Typical Frequency |
|-------------|------------------|
| Global Administrator role | Monthly or quarterly |
| Privileged admin roles (User Admin, Security Admin) | Quarterly |
| Application access (sensitive: HR, Finance) | Quarterly or semi-annually |
| General application access | Semi-annually or annually |
| Guest/external user access | Quarterly |
| Distribution group membership | Annually |

Higher privilege, higher frequency. The rationale: more sensitive access has a higher cost if it's inappropriately held, so it warrants more frequent verification.

## ⚠️ The documentation gap

Many organizations conduct access reviews but don't retain the certification evidence in a way that satisfies auditors. Reviewing access in a spreadsheet and deleting the spreadsheet afterward means the review happened but cannot be proven.

Entra ID access reviews automatically retain the certification history in the portal and via the Microsoft Graph API. Audit logs capture each certification decision. This is the structured evidence trail that satisfies SOX, ISO 27001, SOC 2, and similar frameworks' evidence requirements.

## 💡 Linking certification to access packages

Entitlement Management access packages (covered in Glossary#6.9) can have access reviews configured as part of the package policy. Anyone who has been granted access via the package is automatically included in the periodic certification campaign. This connects the request-and-approve workflow to the ongoing certification lifecycle, creating a complete access governance loop.

---

💬 **Has your organization had an audit finding related to access certification evidence?** The gap between "we reviewed access" and "we can prove we reviewed access in the way the auditor requires" is where many compliance programs fail. What triggered the change in how your organization handles certification documentation?
✍️ TedxHarry

<!-- nav -->

---

[← Access Review](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-6-access-review.md) | [🏠 Contents](/README) | [Recertification →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-8-recertification.md)
