# Password Reset: Giving Users the Key to Their Own Lock

**Part of Entra ID Glossary Series: Glossary#6.23 - Password Reset**

---

A help desk manager calculated that password resets accounted for 34% of their total monthly ticket volume. Each reset took an average of 8 minutes of staff time: 4 minutes to verify the caller's identity, 2 minutes to perform the reset, 2 minutes to document.

At 600 resets per month, that was 80 hours of help desk time. Monthly. On password resets.

She enabled Self-Service Password Reset. One month later, 71% of resets were user-initiated, handle time dropped from 8 minutes to 0 for those cases, and the help desk recovered 56 hours per month for work that required actual judgment.

## 🔄 What SSPR Is

Self-Service Password Reset (SSPR) allows users to reset their own passwords or unlock their own accounts without contacting IT. When a user is locked out or forgets their password, they navigate to the SSPR page (`aka.ms/sspr`), verify their identity using pre-registered authentication methods, and set a new password.

SSPR in Entra ID supports:

**Password reset** 🔑: For users who've forgotten their password. They verify their identity, enter a new password that meets complexity requirements.

**Account unlock** 🔓: For users who are locked out (Smart Lockout). They verify their identity and unlock the account without changing the password.

**Password change** 🔄: For signed-in users who want to change their known password to a new one. Requires the current password.

## 🔐 SSPR Authentication Methods

To use SSPR, users must pre-register authentication methods that can verify their identity without the password. Entra ID supports:

- 📱 **Microsoft Authenticator app** (push notification or code)
- 📲 **SMS to registered mobile phone**
- 📞 **Voice call to registered phone**
- 📧 **Email to alternate email address** (not the corporate email)
- 🔑 **FIDO2 security key**
- ❓ **Security questions** (least recommended, knowledge-based, weakest option)

Organizations configure which methods are allowed and how many a user must complete for SSPR. Requiring 2 methods is the standard for accounts with access to sensitive resources. Requiring 1 method is acceptable for lower-risk environments.

The most reliable combination: Microsoft Authenticator (primary) plus a backup phone number. Users who lose access to their phone need at least two methods registered so they're not completely locked out.

## ⚙️ SSPR Registration

SSPR only works if users have pre-registered their authentication methods. The common failure mode: users need SSPR when they're locked out, but they never registered methods because they've never been locked out before.

**Registration campaigns** force users to register. When enabled, Entra ID interrupts users during sign-in and prompts them to register SSPR methods. Users can skip for up to a configured number of days (typically 14), after which registration is required to complete sign-in.

**Combined registration** (the current default): Users register for both MFA and SSPR simultaneously in the same workflow. Registering the Authenticator app for MFA automatically satisfies SSPR registration for that method. One registration, both purposes.

## 🏢 SSPR in Hybrid Environments

For organizations with on-premises Active Directory synchronized to Entra ID, SSPR has an extra consideration: the password needs to change in both places.

**Password writeback** is the feature that handles this. When a user resets their password via Entra ID SSPR, password writeback pushes the new password back to on-premises AD simultaneously. The user's password is consistent in both environments without any additional steps.

Password writeback requires Entra Connect (or Cloud Sync) with the writeback feature enabled and the right permissions configured in on-premises AD. Without writeback, Entra ID SSPR only resets the cloud password. On-premises authentication continues to use the old password.

## ⚠️ What SSPR Doesn't Handle

SSPR allows users to reset their own passwords. It doesn't handle:

- Users who've never registered authentication methods (they need admin-initiated reset)
- Accounts in specific admin roles that require elevated reset procedures for security reasons
- Accounts where the authentication methods themselves are compromised (if the attacker has the phone and the email, SSPR gives them the password)

For privileged accounts, admin-initiated password resets with identity verification (not SSPR) should be the policy.

## 💡 The Admin Override Path

When SSPR isn't available (no registered methods, admin account), administrators can reset user passwords from the Entra admin center or via PowerShell:

```powershell
Update-MgUserPassword -UserId "user@contoso.com" `
  -PasswordProfile @{ ForceChangePasswordNextSignIn = $true; Password = "TempP@ssw0rd!" }
```

Forcing a password change on next sign-in ensures the temporary password is immediately replaced by something the admin doesn't know.

---

💬 **What percentage of your organization's help desk tickets are password resets?** The answer before SSPR is almost always higher than expected. After SSPR adoption, the residual cases are almost always users who never registered. What drove your organization to invest in SSPR adoption?
<!-- nav -->

---

[← Account Lockout: How Entra ID Stops Password Guessing Without Locking Out Real Users](glossary-6-22-account-lockout.md) | [Home](../README.md) | [Risk Detection: How Entra ID Knows Something Looks Wrong →](../7%20SECURITY%20%26%20RISK%20MANAGEMENT/glossary-7-1-risk-detection.md)
