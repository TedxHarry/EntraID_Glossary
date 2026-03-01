# User Offboarding
*The Day Someone Leaves Is the Day Access Has to Stop*

**Part of Entra ID Glossary Series: Glossary#6.3 - User Offboarding**

---

A security audit found 47 active accounts belonging to employees who had left in the previous 12 months. Not suspended. Not disabled. Active, with valid passwords, valid MFA registrations, and in some cases valid access tokens still within their window.

One of those accounts had been used to log in to the company's SharePoint six weeks after the person's last day. The access log showed document downloads. Nobody had noticed because the account still looked like any other active employee account.

Offboarding is where identity programs fail most visibly and most consequentially.

## ⚡ The First 15 Minutes

When an employee leaves under any circumstances, access revocation should begin immediately. The sequence matters:

**Disable the Entra ID account** 🔴: This is the single most important action. A disabled account cannot complete new authentications. Do this first. Every minute of delay is a minute of residual access risk.

**Revoke all sign-in sessions** 🔴: Disabling the account prevents new sign-ins but doesn't invalidate existing access tokens. Revoking sessions (`Revoke-MgUserSignInSession`) invalidates all refresh tokens, forcing re-authentication on the next token refresh. For CAE-capable services (Exchange, SharePoint, Teams), access stops in seconds.

**Reset the password** 🔒: Belt-and-suspenders. If the account was disabled correctly, this matters less. But if there's any chance stored credentials could be used before the disable takes effect globally, a password reset closes that path.

**Trigger device wipe** 📱: If the user had corporate-owned devices enrolled in Intune, trigger a selective wipe (for personal devices with corporate data) or full wipe (for corporate-owned devices) via Intune.

## 📋 The Full Offboarding Checklist

Beyond the immediate actions, thorough offboarding covers:

**Identity layer** 🆔
- ✅ Account disabled in Entra ID
- ✅ Sign-in sessions revoked
- ✅ Password reset
- ✅ MFA methods removed (prevents reactivation without admin)
- ✅ Active PIM role activations deactivated
- ✅ Break-glass or shared account credentials changed if the user knew them

**Access layer** 🔑
- ✅ All Entra ID group memberships removed or account removed from all assignable groups
- ✅ Application role assignments revoked
- ✅ Direct application account deprovisioning for non-SSO apps (Salesforce, GitHub org, AWS IAM user, etc.)
- ✅ Shared mailbox and resource calendar access revoked

**Device layer** 💻
- ✅ Corporate devices wiped or reassigned
- ✅ Device objects disabled in Entra ID

**Data layer** 📁
- ✅ OneDrive access redirected to manager or designated data owner (30-day window before deletion)
- ✅ Email forwarding configured if needed for business continuity
- ✅ Microsoft 365 group ownerships transferred

## 🔄 Automated vs Manual Offboarding

The 47 abandoned accounts in the audit were the result of manual offboarding: IT received a ticket when someone left, manually disabled the account, and manually removed some access. The manual steps that weren't completed left the gaps.

Automated offboarding changes the model:
- HR marks the employee as terminated in the HR system
- Inbound provisioning detects the change and automatically disables the Entra ID account
- A Leaver lifecycle workflow triggers: session revocation, group membership removal, manager notification, data access transfer
- Downstream app provisioning removes accounts in connected applications

With automation, offboarding is complete and consistent regardless of whether IT received a timely ticket. The HR action is the trigger, not a human remembering to create a ticket.

## ⚠️ The Non-Obvious Access Points

The obvious access points get covered. It's the non-obvious ones that linger:

- 🔴 **Personal access tokens** (GitHub, Azure DevOps): These are separate from Entra ID authentication and don't get revoked by account disable
- 🔴 **Service accounts**: If the employee created a service account that runs automated processes, that account survives
- 🔴 **Shared credentials**: If the employee knew a shared password (for a vendor portal, for example), that credential is still valid
- 🔴 **OAuth consents**: Apps the employee authorized continue to have tokens until those tokens expire, though disabling the account prevents new token issuance

The sign-in logs and audit logs from the week before departure are the right place to look for any access patterns that indicate non-obvious ongoing access.

---

💬 **Has your organization discovered active accounts belonging to departed employees during a security review?** It's one of the most common audit findings in identity programs, and the gap is almost always a manual offboarding process with no enforcement. What triggered your organization to address it?
<!-- nav -->

---

[← User Onboarding](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-2-user-onboarding.md) | [🏠 Contents](/README) | [Deprovisioning →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-4-deprovisioning.md)
