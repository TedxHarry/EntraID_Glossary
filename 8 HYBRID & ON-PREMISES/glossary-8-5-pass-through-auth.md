# Pass-Through Auth
*Validating Cloud Sign-Ins Against On-Premises AD*

**Part of Entra ID Glossary Series: Glossary#8.5 - Pass-Through Auth**

---

A financial services firm had a regulatory requirement: user passwords must not be stored outside their on-premises infrastructure. Even in hashed form. Even transformed. No representation of a credential could exist in the cloud.

Password Hash Sync was off the table. Federation (ADFS) was expensive to maintain and they wanted to simplify. Pass-Through Authentication gave them a middle path: users sign in to Microsoft 365 with their on-premises credentials, Entra ID validates the sign-in against on-premises AD in real time, and no password representation ever leaves their infrastructure.

## 🔄 What Pass-Through Authentication Is

Pass-Through Authentication (PTA) is an Entra ID authentication method for hybrid users where password validation is delegated to on-premises Active Directory via agents running in the on-premises environment, rather than validated against Entra ID directly.

The flow when a user signs in:

1. User submits username and password to Entra ID
2. Entra ID queues an encrypted validation request
3. An on-premises PTA agent picks up the request from the queue
4. The agent validates the credentials against the local domain controller
5. The domain controller responds with success or failure
6. The agent passes the response back to Entra ID
7. Entra ID issues the access token (or rejects the sign-in)

The password is submitted to Entra ID but is immediately encrypted and forwarded. Entra ID itself never validates the password against a stored hash. The actual validation happens in the customer's on-premises environment.

## 🏗️ The PTA Agent Infrastructure

PTA requires at least one agent running on-premises. Microsoft recommends multiple agents for resilience:

**Agent installation**: PTA agents are lightweight Windows services installable on Windows Server machines in the on-premises environment. They establish outbound connections to Entra ID using HTTPS on port 443. No inbound ports are required.

**Agent communication**: Agents register with Entra ID and maintain a persistent connection through which they receive validation requests. The communication is outbound-only from the on-premises side, which means no inbound firewall rules are needed and no DMZ configuration is required.

**Multi-agent resilience**: With multiple agents, if one agent or server is unavailable, requests are distributed to other available agents. Two agents minimum, three or more for comfortable redundancy. Agents can run on existing infrastructure alongside other services.

**Agent updates**: PTA agents update automatically. Manual intervention isn't typically required for version maintenance.

## ⚖️ PTA vs Password Hash Sync: The Trade-offs

**Security posture** 🔐:
- PTA: No password representation in the cloud. Satisfies strict data sovereignty requirements. On-premises AD is the definitive authority for every sign-in.
- PHS: Password hash representation in cloud, but transformed in a way that prevents recovery. Enables leaked credentials detection.

**Resilience** 💪:
- PTA: If on-premises AD is unavailable (or PTA agents are all down), cloud authentication fails. Users cannot sign in to Microsoft 365 during an on-premises outage.
- PHS: Cloud authentication is independent of on-premises infrastructure. Microsoft 365 stays available during on-premises outages.

**Security features** 🛡️:
- PTA: Smart Lockout still applies at the Entra ID level. ID Protection risk signals still apply to sign-ins.
- PHS: Additionally enables leaked credentials detection because the hash representation exists in Entra ID for comparison against breach data.

**Operational complexity** ⚙️:
- PTA: Requires maintaining PTA agent infrastructure. Agent servers need monitoring.
- PHS: No additional agent infrastructure beyond Entra Connect/Cloud Sync.

## ⚠️ The Resilience Problem

The most significant operational consideration with PTA is the dependency on on-premises infrastructure for every cloud authentication.

An AD outage that would normally affect only on-premises resources now also affects Microsoft 365 sign-ins. An on-premises network outage. A domain controller failure where PTA agents can't reach a DC. All of these scenarios prevent users from signing in to cloud services.

Organizations with PTA deployed should:
- Deploy multiple PTA agents across different servers for agent resilience
- Have PTA agents on servers that can still reach domain controllers during most failure scenarios
- Consider Password Hash Sync as a fallback authentication method (PTA and PHS can be configured together; if PTA validation fails for infrastructure reasons, PHS can serve as backup)

## 🔒 What PTA Validates

PTA validates the password and some account state attributes:

**What's checked on-premises**:
- Password correctness
- Account locked (AD lockout policy applies)
- Account disabled in AD
- Password expired
- Account restricted by logon hours

**What's NOT checked on-premises**:
- Entra ID-specific controls (Conditional Access, Smart Lockout at the Entra ID level) still apply before and after the on-premises validation
- Entra ID risk assessments still run for every sign-in

The combination means both on-premises AD policy and Entra ID policy apply to every sign-in through PTA.

---

💬 **What drove your organization's decision to use Pass-Through Authentication instead of Password Hash Sync?** The regulatory requirement around passwords not leaving on-premises is the most common answer. But the resilience trade-off is often discovered later during an on-premises incident. How did you architect for that resilience?
<!-- nav -->

---

[← Password Hash Sync](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-4-password-hash-sync.md) | [🏠 Contents](/README) | [Federation →](/8%20HYBRID%20%26%20ON-PREMISES/glossary-8-6-federation.md)
