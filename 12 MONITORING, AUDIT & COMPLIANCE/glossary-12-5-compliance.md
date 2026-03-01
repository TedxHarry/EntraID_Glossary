# Compliance
*How Entra ID Controls Map to the Regulations Your Auditors Ask About*

**Part of Entra ID Glossary Series: Glossary#12.5 - Compliance**

---

An auditor preparing for an SOC 2 Type II assessment asked for evidence of access controls, least privilege, user access reviews, and administrative activity monitoring. The security team produced 14 pieces of evidence from Entra ID.

The auditor's response: "This is the most organized identity evidence package we've seen."

Not because the controls were complex. Because the team knew which Entra ID feature corresponded to which control requirement and could produce the evidence efficiently. That mapping is what compliance in the context of Entra ID means in practice.

## 🏛️ What Compliance Means Here

Compliance in the Entra ID context is about demonstrating that your organization's identity controls meet the requirements of applicable regulatory frameworks and security standards. The regulations differ: GDPR (privacy), HIPAA (healthcare data), SOX (financial reporting), PCI DSS (payment card), ISO 27001 (information security management), SOC 2 (service organization controls). But the underlying Entra ID controls that satisfy them overlap significantly.

Entra ID isn't a compliance product by itself. It's an identity platform with controls that can be configured, documented, and evidenced to satisfy control requirements across multiple frameworks.

## 📋 Core Control Areas and Their Entra ID Evidence

**Access control and least privilege** 🔑: Who has access to what, and is it the minimum necessary? Entra ID evidence: role assignments (PIM-managed, time-limited for privileged roles), access packages with defined policies and expiry, Conditional Access policies enforcing device and authentication requirements. Auditor artifact: current role assignment export, PIM activation log, access package catalog.

**Multi-factor authentication** 📱: Are users required to use more than one authentication factor? Entra ID evidence: MFA registration status from the authentication methods usage report, Conditional Access policies requiring MFA, Sign-in logs confirming MFA completion. Auditor artifact: authentication methods report, CA policy screenshots, MFA-required sign-in sample.

**User access reviews** 📋: Are access rights periodically reviewed and inappropriate access removed? Entra ID evidence: Access review configurations (quarterly reviews, auto-removal for non-responsive reviewers), completed access review results showing decisions made. Auditor artifact: access review history, reviewer completion rates, removal actions taken.

**Privileged access governance** 🔐: Are administrative accounts subject to additional controls? Entra ID evidence: PIM configuration for Global Administrator and other privileged roles, activation approval requirements, time-limited role assignments, PIM audit log showing activations and justifications. Auditor artifact: PIM role settings export, recent activation log.

**Audit trail** 📊: Is there a record of who did what in the identity system? Entra ID evidence: Audit logs exported to Log Analytics or Storage, retention configuration showing retention meets requirements, sample audit events for key operation types. Auditor artifact: audit log export, retention documentation.

**Account provisioning and deprovisioning** 🔄: Are user accounts promptly created when employees join and disabled when they leave? Entra ID evidence: Lifecycle Workflows configuration showing automated disable on termination date from HR system, audit log entries confirming accounts were disabled on the expected dates. Auditor artifact: lifecycle workflow configuration, termination event audit log sample.

## 🔒 GDPR-Specific Controls

GDPR adds privacy-specific requirements beyond general access control:

**Data subject access requests** 👤: The ability to export all personal data held about a specific individual. Microsoft 365 compliance tooling integrates with Entra ID to support this. The user's Entra ID attributes (name, email, department, etc.) are part of the export.

**Right to erasure** 🗑️: The ability to delete a user's personal data. Deleting a user account in Entra ID begins the process, though complete erasure of backed-up and logged data requires more deliberate lifecycle management.

**Consent management** 📋: For external/customer identities (in External Tenant scenarios), recording consent for data processing at registration. External tenant sign-up flows can include consent capture as part of the user flow.

**Data residency** 🌐: Where is identity data stored? Microsoft publishes data residency documentation per service and geography. Organizations with EU data residency requirements configure Entra ID to provision in EU regions.

## 📊 Microsoft Compliance Manager

Microsoft Purview Compliance Manager provides a structured mapping between Microsoft cloud controls (including Entra ID) and compliance framework requirements. It shows which Entra ID features address which control requirements in frameworks like NIST 800-53, ISO 27001, SOC 2, and others.

Using Compliance Manager, an organization can see: "The SOC 2 CC6.1 control (logical access security) is addressed by these Microsoft controls: MFA policy, Conditional Access, PIM, access reviews." It provides a structured starting point for building the evidence package.

The Compliance Manager score isn't a guarantee of compliance; it's a tool for identifying which controls are configured and which have gaps. External auditor judgment still determines whether the controls satisfy the requirement.

---

💬 **Which regulatory framework puts the most compliance pressure on your Entra ID configuration, and which control area requires the most ongoing effort to evidence?** Access reviews are the most commonly cited ongoing compliance effort. But organizations in regulated industries often find data residency and audit log retention more challenging. What's the compliance requirement that most drives your identity security investment?
<!-- nav -->

---

[← Security Alert](glossary-12-4-security-alert.md) | [Home](../README.md) | [Attribute-Based Access Control (ABAC) →](../13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-1-abac.md)
