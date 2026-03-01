# SSPR (Security Focus)
*When Self-Service Password Reset Becomes an Attack Vector*

**Part of Entra ID Glossary Series: Glossary#7.27 - SSPR (Security Focus)**

---

An attacker had a target's email address and some publicly available personal information. They went to the organization's SSPR portal. The SSPR was configured to require security questions as the verification method. The questions: mother's maiden name, first pet, elementary school.

All three answers were findable in 15 minutes on the target's social media profiles and a genealogy website.

The attacker reset the password. They were in.

The organization had deployed SSPR to reduce help desk burden. They hadn't thought about the security implications of the authentication methods they chose for the SSPR flow. Self-service password reset is only as secure as the methods used to verify identity during the reset.

## 🔐 SSPR as an Authentication Security Surface

Self-Service Password Reset (SSPR) is a user-facing authentication flow that allows users to reset their own passwords by verifying their identity through pre-registered methods. The security analysis of SSPR is distinct from the operational benefits discussed in the governance context.

SSPR creates a path to account access that bypasses the normal authentication flow. That's the point: locked-out users can regain access. But any path that leads to account access is a path an attacker will try to exploit.

The security questions from the opening scenario illustrate the core problem: SSPR is only as strong as its verification methods. If the verification methods are weak, SSPR becomes a privileged attack surface.

## 🚨 SSPR Attack Vectors

**Knowledge-based answer guessing** 🔍: Security questions are the weakest SSPR verification method. Answers are often predictable (pet names, schools, maiden names) and findable through social media, public records, or social engineering. An attacker who knows the target's email address can attempt SSPR with guessed answers.

**Phone number hijacking** 📱: If SMS is the SSPR verification method, SIM swapping the user's phone number gives the attacker the reset code. The attacker calls the carrier, impersonates the user, and transfers the number.

**Email-based reset attack** 📧: If the SSPR alternate email method uses a personal email account that the attacker has also compromised (credential reuse is common), the email reset code goes directly to the attacker.

**Social engineering of registration** 🗣️: If SSPR registration is self-service without strong verification, an attacker who briefly has access to an account can register their own phone number or email as the SSPR verification method. Future SSPR attempts then go to the attacker.

**SSPR portal enumeration** 🔎: SSPR portals can leak whether an account exists by showing different error messages for known vs unknown usernames. This helps attackers build target lists.

## 🔒 Securing the SSPR Flow

**Method selection** 📱: Microsoft Authenticator push notification and FIDO2 keys are the strongest SSPR verification methods. Require them as primary methods for any account with elevated access. SMS should be a backup method only, not the primary. Security questions should be disabled.

**Number of methods required** 🔢: Requiring two methods to complete SSPR significantly raises the bar. An attacker who has compromised one method (guessed the security question, SIM swapped the phone) still needs a second. For privileged accounts, requiring two strong methods (Authenticator + alternate email, or Authenticator + phone) provides meaningful defense in depth.

**Restricting SSPR for privileged accounts** 🚫: Global Administrators and other high-privilege role members cannot use SSPR by default in Entra ID. This is intentional and correct. Privileged account password resets should go through admin-initiated processes with identity verification, not self-service flows. Confirm this restriction is in place and not accidentally removed.

**Monitoring SSPR activity** 👀: SSPR usage is logged in the Entra audit logs. Monitor for SSPR attempts on accounts with elevated permissions, SSPR activity at unusual hours, and repeated SSPR failures (indicating guessing attempts). Alert on SSPR completion for admin accounts.

**Registration protection** 🛡️: Require strong authentication (MFA) before users can register or change SSPR authentication methods. If an attacker briefly accesses an account, they shouldn't be able to register their own contact methods without completing MFA first. This is configured in Security Info registration Conditional Access policies.

## ⚙️ Security Info Registration Policies

A critical but often missed SSPR security control: protect the registration of authentication methods themselves.

In Conditional Access, there's a user action called "Register security information." Applying a Conditional Access policy to this action requires that users complete MFA (or another requirement) before they can register or change their authentication methods.

Without this policy: an attacker who gets access to an account (even temporarily) can register their own phone number, authenticator app, or alternate email as the SSPR method. Future SSPR attempts then go to the attacker.

With this policy: changing authentication method registration requires completing the current MFA setup first. If the attacker doesn't have the MFA, they can't change the registered methods.

## 💡 The Privileged Account Carve-Out

The zero-trust principle for privileged accounts: no self-service recovery. Any path that allows a privileged account to be recovered without admin verification is an attack surface that doesn't need to exist.

For admin accounts: disable SSPR, require admin-initiated password reset with identity verification, and enforce phishing-resistant MFA as the primary authentication method. The inconvenience of calling the helpdesk for a password reset is acceptable for accounts that can manage the entire tenant.

---

💬 **Have you ever audited the SSPR verification methods that your users have registered and found methods that shouldn't be there?** The security questions that were set up during initial deployment and never changed, or the personal email address that's been the alternate recovery contact for five years, are common findings. What was the SSPR security gap that prompted a policy change?
<!-- nav -->

---

[← Authentication Methods (Security Focus)](glossary-7-26-authentication-methods-security.md) | [Home](../README.md) | [Insider Risk →](glossary-7-28-insider-risk.md)
