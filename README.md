# Microsoft Entra ID Glossary

A comprehensive glossary of Microsoft Entra ID (formerly Azure Active Directory) concepts, organized into 13 topic areas. Each entry is written as an approachable, experience-driven article — not just a definition.

**189 terms across 13 sections.**

---

## Table of Contents

- [Section 1: FOUNDATIONAL CONCEPTS](#section-1-foundational-concepts)
- [Section 2: CORE IDENTITY CONCEPTS](#section-2-core-identity-concepts)
- [Section 3: AUTHENTICATION](#section-3-authentication)
- [Section 4: TOKENS & AUTHORIZATION](#section-4-tokens-authorization)
- [Section 5: DEVICES & COMPLIANCE](#section-5-devices-compliance)
- [Section 6: GOVERNANCE & LIFECYCLE](#section-6-governance-lifecycle)
- [Section 7: SECURITY & RISK MANAGEMENT](#section-7-security-risk-management)
- [Section 8: HYBRID & ON-PREMISES](#section-8-hybrid-on-premises)
- [Section 9: INTEGRATION & EXTERNAL IDENTITIES](#section-9-integration-external-identities)
- [Section 10: WORKLOAD IDENTITIES & MANAGED IDENTITIES](#section-10-workload-identities-managed-identities)
- [Section 11: TOKENS & TECHNICAL DETAILS](#section-11-tokens-technical-details)
- [Section 12: MONITORING, AUDIT & COMPLIANCE](#section-12-monitoring-audit-compliance)
- [Section 13: ADVANCED FEATURES & CONCEPTS](#section-13-advanced-features-concepts)

---

## Section 1: FOUNDATIONAL CONCEPTS

1. [What Is Microsoft Entra ID? The Foundation of Modern Identity](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-1-microsoft-entra-id.md)
2. [The Microsoft Entra Product Family: Why There's More Than Just Entra ID](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-2-microsoft-entra-product-family.md)
3. [What Is a Tenant? (And Why Getting This Wrong Causes Real Problems)](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-3-tenant.md)
4. [Cloud-Based Identity: What It Actually Means When the Servers Aren't Yours](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-4-cloud-based-identity.md)
5. [Active Directory Isn't Dead. Here's Why That Matters.](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-5-active-directory.md)
6. [Hybrid Identity: Living in Two Worlds at Once](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-6-hybrid-identity.md)

## Section 2: CORE IDENTITY CONCEPTS

1. [Identity: The Word Everyone Uses and Almost Nobody Defines](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-1-identity.md)
2. [The User Object: What's Actually Inside (And Why It Matters More Than You Think)](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-2-user-identity-object.md)
3. [Service Principal: The Most Misunderstood Object in Entra ID](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-3-service-principal.md)
4. [Groups in Entra ID: The Access Management Tool You Should Be Using More](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-4-group.md)
5. [Enterprise Applications: What the Portal Is Actually Showing You](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-5-enterprise-application.md)
6. [Directory Roles: Why "Just Give Them Global Admin" Is the Worst Habit in Entra ID](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-6-directory-role.md)
7. [Access Control: What It Actually Means When Everything Is Everywhere](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-7-access-control.md)
8. [API Permissions in Entra ID: Reading What You're Actually Granting](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-8-permission.md)
9. ["Role": One Word, Three Completely Different Things in Entra ID](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-9-role-identity-role.md)
10. [Delegation: Giving People Just Enough Access — No More](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-10-delegation.md)
11. [Admin Roles: The Keys to Your Tenant and Why You Need Far Fewer of Them](2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-11-admin-role.md)

## Section 3: AUTHENTICATION

1. [Authentication: The Question Behind Every Sign-In](3%29%20AUTHENTICATION/glossary-3-1-authentication.md)
2. [What Actually Happens When You Click "Sign In"](3%29%20AUTHENTICATION/glossary-3-2-sign-in.md)
3. [Authentication Methods: Not All Proof Is Created Equal](3%29%20AUTHENTICATION/glossary-3-3-authentication-method.md)
4. [Multi-Factor Authentication: Why 99.9% Attack Prevention Still Has an Asterisk](3%29%20AUTHENTICATION/glossary-3-4-mfa.md)
5. [Passwordless Authentication: Fixing the Right Problem](3%29%20AUTHENTICATION/glossary-3-5-passwordless-authentication.md)
6. [FIDO2: Why a Small USB Stick Can Eliminate Phishing from Your Attack Surface](3%29%20AUTHENTICATION/glossary-3-6-fido2.md)
7. [Windows Hello for Business: It's Not Just a PIN](3%29%20AUTHENTICATION/glossary-3-7-windows-hello.md)
8. [Microsoft Authenticator: More Than a Code Generator](3%29%20AUTHENTICATION/glossary-3-8-microsoft-authenticator.md)

## Section 4: TOKENS & AUTHORIZATION

1. [The Authorization Code: Why Sign-In Takes Two Steps Instead of One](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-1-authorization-code.md)
2. [The Authorization Endpoint: Reading What That Long URL Is Actually Saying](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-2-authorization-endpoint.md)
3. [The Token Endpoint: The Server-Side Half Nobody Talks About](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-3-token-endpoint.md)
4. [The Authorization Server: What Entra ID Is Actually Doing Behind the Scenes](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-4-authorization-server.md)
5. [Access Tokens: What's Actually Inside That Long String](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-5-access-token.md)
6. [The ID Token: Proof of Who Signed In (Not a Key to the API)](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-6-id-token.md)
7. [Refresh Tokens: What "Keep Me Signed In" Is Actually Doing](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-7-refresh-token.md)
8. [Bearer Tokens: The Name That Tells You Everything About the Risk](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-8-bearer-token.md)
9. [Token Lifetime: The Trade-Off Between Security and Not Annoying Your Users](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-9-token-lifetime.md)
10. [Token Revocation: Why "I Disabled Their Account" Isn't Always Enough](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-10-token-revocation.md)
11. [Scope: The Permission on the Label vs the Permission You Actually Need](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-11-scope.md)
12. [Audience: The Token Knows Who It Was Meant For](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-12-audience.md)
13. [Authorization Grant: Four Ways to Get a Token (and When to Use Each)](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-13-authorization-grant.md)
14. [Actor: The Application in the Token, and Why It Matters](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-14-actor.md)
15. [Subject: Whose Data Is This, Really?](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-15-subject.md)
16. [OAuth 2.0: The Protocol That Solved a Problem We Didn't Realize Was a Problem](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-16-oauth2.md)
17. [OpenID Connect: The Layer OAuth Was Missing](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-17-oidc.md)
18. [SAML: The Protocol That Refuses to Die (and Sometimes Shouldn't)](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-18-saml.md)
19. [Token Security: Treating Every Token Like the Key It Is](4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-19-token-security.md)

## Section 5: DEVICES & COMPLIANCE

1. [Device Compliance: When the Device Has to Earn Its Access](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-1-device-compliance.md)
2. [Device Identity: When the Device Itself Has to Prove Who It Is](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-2-device-identity.md)
3. [Device Registration: Three Ways to Join a Device to Entra ID (They're Not the Same)](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-3-device-registration.md)
4. [Device Enrollment: The Difference Between Knowing a Device Exists and Managing It](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-4-device-enrollment.md)
5. [Intune: What the Device Management Piece of Microsoft's Puzzle Actually Does](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-5-intune.md)
6. [Mobile Device Management: The Trade-Off Between Control and Trust](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-6-mobile-device-management.md)
7. [Endpoint Manager: One Console, All Your Devices](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-7-endpoint-manager.md)
8. [Device Trust: Not All Devices Are Equally Trustworthy (And Entra ID Knows It)](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-8-device-trust.md)
9. [Hybrid Entra Joined: The Device That Lives in Both Worlds](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-9-hybrid-device.md)
10. [App Protection Policy: Managing the Data, Not the Device](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-10-app-protection-policy.md)
11. [Device State: The Real-Time Health Signal That Drives Access Decisions](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-11-device-state.md)
12. [Managed Device: Enrolled Isn't the Same as Secure](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-12-managed-device.md)
13. [Compliant Device: The Security Baseline That Has to Be Earned Continuously](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-13-compliant-device.md)
14. [Non-Compliant Device: What Happens When the Device Fails Its Security Check](5%20DEVICES%20%26%20COMPLIANCE/glossary-5-14-non-compliant-device.md)

## Section 6: GOVERNANCE & LIFECYCLE

1. [User Provisioning: Accounts That Create Themselves (When It's Done Right)](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-1-user-provisioning.md)
2. [User Onboarding: The First Day Experience Is an Identity Problem](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-2-user-onboarding.md)
3. [User Offboarding: The Day Someone Leaves Is the Day Access Has to Stop](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-3-user-offboarding.md)
4. [Deprovisioning: Disabling the Entra ID Account Is Not Enough](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-4-deprovisioning.md)
5. [Lifecycle Management: Identity Automation for the Entire Employee Journey](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-5-lifecycle-management.md)
6. [Access Review: The Audit That Finds What Accumulates Over Time](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-6-access-review.md)
7. [Access Certification: When "Reviewed" Has to Mean Something to an Auditor](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-7-access-certification.md)
8. [Recertification: Access That Was Right Then Might Not Be Right Now](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-8-recertification.md)
9. [Entitlement Management: Self-Service Access Without the Security Compromise](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-9-entitlement-management.md)
10. [Access Request: The User's Side of the Access Conversation](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-10-access-request.md)
11. [Approval Workflow: Who Decides, in What Order, and What Happens If They Don't](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-11-approval-workflow.md)
12. [Auto-Provision: When Access Appears Without Anyone Creating It](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-12-auto-provision.md)
13. [Just-in-Time Access: Admin Privileges Should Be Borrowed, Not Owned](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-13-just-in-time-access.md)
14. [Governance: The System That Keeps Access from Running Away from You](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-14-governance.md)
15. [Certification Campaign: Access Review at Scale, on a Schedule](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-15-certification-campaign.md)
16. [Bulk User Operations: When You Need to Change 500 Accounts at Once](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-16-bulk-user-operations.md)
17. [User Attributes: The Properties That Drive Everything Else](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-17-user-attributes.md)
18. [Source of Authority: Which System Gets to Say Who You Are](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-18-source-of-authority.md)
19. [Identity Verification: Confirming the Person Behind the Account](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-19-identity-verification.md)
20. [Emergency Access: The Account You Hope You Never Need](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-20-emergency-access.md)
21. [Shared Accounts: Why "We All Use the Same Login" Is a Security Problem](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-21-shared-accounts.md)
22. [Account Lockout: How Entra ID Stops Password Guessing Without Locking Out Real Users](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-22-account-lockout.md)
23. [Password Reset: Giving Users the Key to Their Own Lock](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-23-password-reset.md)
24. [Risky User: When the Account Itself Is Flagged, Not Just One Sign-In](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-7-3-risky-user.md)
25. [ID Protection: Entra ID's Automated Threat Response System](6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-7-4-id-protection.md)

## Section 7: SECURITY & RISK MANAGEMENT

1. [Risk Detection: How Entra ID Knows Something Looks Wrong](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-1-risk-detection.md)
2. [Risky Sign-In: When the Authentication Looks Suspicious](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-2-risky-sign-in.md)
3. [Anomaly Detection: How Entra ID Learns What Normal Looks Like](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-5-anomaly-detection.md)
4. [Leaked Credentials: When Your Password Shows Up on the Dark Web](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-6-leaked-credentials.md)
5. [Threat Intelligence: Why Entra ID Knows an IP Is Bad Before You Do](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-7-threat-intelligence.md)
6. [Conditional Access: The Policy Engine That Makes "Never Trust, Always Verify" Real](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-8-conditional-access.md)
7. [CA Policy: Building the If-Then Logic of Access Control](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-9-ca-policy.md)
8. [Zero Trust: The Security Model That Stopped Trusting Your Network](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-10-zero-trust.md)
9. [Assignment: Who and What Your Conditional Access Policy Actually Covers](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-11-assignment.md)
10. [Condition: The Signals That Make Conditional Access Contextual](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-12-condition.md)
11. [Grant Control: The Access Decision in Conditional Access](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-13-grant-control.md)
12. [Block Access: The Hardest Grant Control to Get Right](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-14-block-access.md)
13. [Require MFA: The Grant Control That Changed Identity Security](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-15-require-mfa.md)
14. [Require Device Compliance: The Grant Control That Stops Token Theft](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-16-require-device-compliance.md)
15. [Require Authentication Strength: Not All MFA Is Equal](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-17-require-authentication-strength.md)
16. [Report-Only Mode: How to Test a Policy Without Breaking Production](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-18-report-only-mode.md)
17. [Location: Using Where You Sign In to Shape What You Can Access](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-19-location.md)
18. [Trusted Location: Teaching Conditional Access What "Safe" Looks Like](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-20-trusted-location.md)
19. [IP Address Range: The Building Block of Location-Based Access Control](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-21-ip-address-range.md)
20. [Legacy Authentication: The Open Door That MFA Can't Close](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-22-legacy-authentication.md)
21. [Session Control: Governing What Happens After Access Is Granted](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-23-session-control.md)
22. [Terms of Use: Making Consent Part of the Access Flow](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-24-terms-of-use.md)
23. [Authentication Strength: Why Some MFA Is Stronger Than Others](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-25-authentication-strength.md)
24. [Authentication Methods: Choosing the Right Mix for Your Security Posture](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-26-authentication-methods-security.md)
25. [SSPR Security: When Self-Service Password Reset Becomes an Attack Vector](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-27-sspr-security.md)
26. [Insider Risk: When the Threat Already Has a Badge](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-28-insider-risk.md)
27. [User Risk Level: Understanding the Number Behind the Flag](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-29-user-risk-level.md)
28. [Sign-In Risk Level: Reading the Signals in a Single Authentication](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-30-sign-in-risk-level.md)
29. [CA Template: Microsoft's Starting Points for Conditional Access](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-31-ca-template.md)
30. [CAE: When Access Tokens Get Revoked Mid-Session](7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-32-cae.md)

## Section 8: HYBRID & ON-PREMISES

1. [Directory Synchronization: Bridging On-Premises Identity with the Cloud](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-1-directory-synchronization.md)
2. [Entra Connect: The Engine Behind Hybrid Identity](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-2-entra-connect.md)
3. [Cloud Sync: The Lighter Path to Hybrid Identity](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-3-cloud-sync.md)
4. [Password Hash Sync: How On-Premises Passwords Work in the Cloud](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-4-password-hash-sync.md)
5. [Pass-Through Authentication: Validating Cloud Sign-Ins Against On-Premises AD](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-5-pass-through-auth.md)
6. [Federation: When Entra ID Trusts Another Identity Provider for Authentication](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-6-federation.md)
7. [Domain Services: Active Directory Without the Domain Controllers](8%20HYBRID%20%26%20ON-PREMISES/glossary-8-7-domain-services.md)

## Section 9: INTEGRATION & EXTERNAL IDENTITIES

1. [App Integration: Connecting Applications to Entra ID for Authentication](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-1-app-integration.md)
2. [Cloud Application: SaaS in Your Tenant's Security Perimeter](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-2-cloud-application.md)
3. [Federated Application: When an App Trusts Entra ID to Prove Who You Are](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-3-federated-application.md)
4. [Application Proxy: Publishing On-Premises Apps Without VPN](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-4-application-proxy.md)
5. [OAuth 2.0 in App Integration: How Modern Applications Request Access](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-5-oauth2-app-integration.md)
6. [OIDC in App Integration: Building Modern Authentication the Right Way](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-6-oidc-app-integration.md)
7. [SAML in App Integration: The Enterprise Protocol That Refuses to Retire](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-7-saml-app-integration.md)
8. [SCIM: The Standard That Automates User Provisioning Across Applications](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-8-scim.md)
9. [B2B Collaboration: Giving External Partners Access Without Managing Their Identity](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-9-b2b-collaboration.md)
10. [B2C: Identity Management for Your Customers, Not Your Employees](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-10-b2c.md)
11. [CIAM: Identity Management Designed for Customers, Not Employees](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-11-ciam.md)
12. [External User: Managing Access for People Who Don't Work for You](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-12-external-user.md)
13. [External Identity: The Broader Category Behind Every Non-Employee](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-13-external-identity.md)
14. [Entra External ID: Microsoft's Unified Platform for Non-Employee Identities](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-14-entra-external-id.md)
15. [Workforce Tenant: The Corporate Identity Foundation Behind Every Employee Account](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-15-workforce-tenant.md)
16. [External Tenant: The Entra ID Tenant Type Built for Your Customers](9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-16-external-tenant.md)

## Section 10: WORKLOAD IDENTITIES & MANAGED IDENTITIES

1. [Workload Identity: When the Thing Connecting to Your Systems Isn't a Person](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-1-workload-identity.md)
2. [Managed Identity: Credentials That Azure Manages So You Don't Have To](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-2-managed-identity.md)
3. [System-Assigned Managed Identity: One Resource, One Identity, One Lifecycle](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-3-system-assigned-managed-identity.md)
4. [User-Assigned Managed Identity: One Identity Shared Across Many Resources](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-4-user-assigned-managed-identity.md)
5. [Workload Federation: Authenticating to Azure Without Storing Azure Credentials](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-5-workload-federation.md)
6. [Federated Identity Credential: The Trust Configuration That Makes Keyless Auth Work](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-6-federated-identity-credential.md)
7. [Instance Metadata Service: The Local Endpoint That Gives Azure Resources Their Identity](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-7-imds.md)
8. [Principal ID: The Identifier You Use When Giving a Managed Identity Permission](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-8-principal-id.md)
9. [Azure Resource Manager: The Management Plane Where Managed Identity Permissions Live](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-9-azure-resource-manager.md)
10. [CAE for Workloads: Real-Time Token Revocation for Non-Human Identities](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-10-cae-for-workloads.md)
11. [Long-Lived Tokens: Why 24-Hour Workload Tokens Are Safer Than You'd Think](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-11-llts.md)
12. [Conditional Access for Workloads: Security Policies That Apply to Applications, Not Just People](10%20WORKLOAD%20IDENTITIES%20%26%20MANAGED%20IDENTITIES/glossary-10-12-ca-for-workloads.md)

## Section 11: TOKENS & TECHNICAL DETAILS

1. [Authorization Code Flow: The OAuth Dance That Powers Most Modern Web App Sign-Ins](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-1-authorization-code-flow.md)
2. [Authorization Endpoint: What's Actually in That Sign-In URL](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-2-authorization-endpoint-deep-dive.md)
3. [Token Endpoint: Where Codes and Credentials Become Tokens](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-3-token-endpoint-deep-dive.md)
4. [Authorization Server: What Entra ID Is Actually Doing When It Issues a Token](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-4-authorization-server-deep-dive.md)
5. [Authorization Grant: Matching the Right OAuth Flow to the Right Scenario](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-5-authorization-grant-deep-dive.md)
6. [Actor: When an Application Acts as the Middle Layer Between User and API](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-6-actor-deep-dive.md)
7. [Subject: The User Identifier in Tokens That Isn't What You'd Expect](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-7-subject-deep-dive.md)
8. [Bearer Token: Why "Whoever Has It Can Use It" Is Both the Point and the Risk](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-8-bearer-token-deep-dive.md)
9. [Token Lifetime: The Configuration Behind How Long Your Tokens Last](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-9-token-lifetime-deep-dive.md)
10. [Token Revocation: Why "Revoke All Tokens" Doesn't Mean Instant Lockout](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-10-token-revocation-deep-dive.md)
11. [Audience: The Token Claim That Prevents One API's Token From Working on Another](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-11-audience-deep-dive.md)
12. [Scope: Defining and Validating What Applications Are Allowed to Do With Your API](11%20TOKENS%20%26%20TECHNICAL%20DETAILS/glossary-11-12-scope-deep-dive.md)

## Section 12: MONITORING, AUDIT & COMPLIANCE

1. [Audit Log: The Record of Every Identity Operation in Your Tenant](12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-1-audit-log.md)
2. [Sign-In Log: The Authentication Record Your Security Team Needs to Know Cold](12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-2-sign-in-log.md)
3. [Activity Report: The Trend View That Audit Logs and Sign-In Logs Don't Give You](12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-3-activity-report.md)
4. [Security Alert: When Entra ID Tells You Something Is Wrong](12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-4-security-alert.md)
5. [Compliance: How Entra ID Controls Map to the Regulations Your Auditors Ask About](12%20MONITORING%2C%20AUDIT%20%26%20COMPLIANCE/glossary-12-5-compliance.md)

## Section 13: ADVANCED FEATURES & CONCEPTS

1. [Attribute-Based Access Control: Access Decisions That Go Beyond Role Membership](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-1-abac.md)
2. [Cloud-Based Sync (Advanced): Complex Synchronization Scenarios Beyond the Basics](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-2-cloud-sync-advanced.md)
3. [Continuous Authorization: Shifting From "You Were Trusted" to "You Are Trusted Right Now"](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-3-continuous-authorization.md)
4. [Identity Correlations: Matching the Same Person Across Different Systems](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-4-identity-correlations.md)
5. [Passwordless Authentication (Advanced): Deployment Reality Beyond the Demo](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-5-passwordless-auth-advanced.md)
6. [Real-Time Remediation: Automated Immediate Response to Identity Risks](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-6-real-time-remediation.md)
7. [UPN: The Sign-In Name That Looks Like an Email But Isn't Always One](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-7-upn.md)
8. [OID: The Stable GUID That Should Be Your Application's User Key](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-8-oid.md)
9. [Global Secure Access: Microsoft's Zero Trust Network Access Layer](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-9-global-secure-access.md)
10. [Service Account: The Legacy Pattern That Managed Identity Is Replacing](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-10-service-account.md)
11. [Sync Agent: The On-Premises Software That Bridges Your Directory to the Cloud](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-11-sync-agent.md)
12. [Custom Role: Administrative Permissions That Fit What Your Team Actually Needs](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-12-custom-role.md)
13. [Administrative Unit: Scoped Administration Without Multiple Tenants](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-13-admin-unit.md)
14. [Consent Framework: How Applications Get Permission to Access Your Data](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-14-consent-framework.md)
15. [Consent Experience: What Users See When an App Asks for Permission](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-15-consent-experience.md)
16. [Enterprise Application (Advanced): Governing the Applications in Your Tenant Beyond Basic Integration](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-16-enterprise-application-advanced.md)
17. [Cross-Tenant Access: Controlling How Your Tenant Interacts With Other Entra ID Tenants](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-17-cross-tenant-access.md)
18. [Tenant Restrictions: Controlling Which Microsoft Tenants Your Users Can Access](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-18-tenant-restrictions.md)
19. [CA Optimization Agent: Automated Recommendations for Conditional Access Policy Gaps](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-19-ca-optimization-agent.md)
20. [Policy Evaluation: Understanding How Conditional Access Decisions Are Made](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-20-policy-evaluation.md)
21. [Microsoft Graph API: Programmatic Access to Everything in Your Entra ID Tenant](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-21-graph-api.md)
22. [Microsoft Authenticator Advanced: Beyond Basic MFA to Modern Authentication](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-22-microsoft-authenticator-advanced.md)
23. [Microsoft Entra Suite: The Consolidated Identity and Network Access Platform](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-23-microsoft-entra-suite.md)
24. [Advanced Scenarios: Where Entra ID Capabilities Combine to Solve Complex Problems](13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-24-advanced-scenarios.md)

---

## About This Glossary

Each article in this glossary series goes beyond dictionary definitions. The entries are written from hands-on experience and explain not just what each term means, but why it matters, how it behaves in practice, and where things commonly go wrong.

**Topics covered:**
- Core identity and authentication fundamentals
- Tokens, OAuth 2.0, OIDC, and SAML
- Conditional Access policies and Zero Trust
- Device compliance and management
- Identity governance, lifecycle management, and PIM
- Hybrid identity and on-premises synchronization
- External identities, B2B, and B2C
- Workload identities and managed identities
- Advanced features and real-world multi-feature scenarios

---

*Part of the Entra ID Glossary Series — start at [Glossary #1.1: Microsoft Entra ID](1%20FOUNDATIONAL%20CONCEPTS/glossary-1-1-microsoft-entra-id.md)*
