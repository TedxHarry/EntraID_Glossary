# Sign-In
*What Actually Happens When You Click "Sign In"*

**Part of Entra ID Glossary Series: Glossary#3.2 - Sign-In**

---

Most people click "Sign In" and think about it for roughly zero seconds. You type your email, type your password, maybe approve a phone notification, and you're in. The whole thing takes three seconds.

Those three seconds contain a remarkable amount of work.

Understanding what Entra ID actually does during a sign-in changes how you troubleshoot, how you design policies, and how you explain problems to users when something goes wrong. So let's slow it down.

## 🔄 The Sign-In Flow, Step by Step

**Step 1: Discovery**
You enter your email address on the sign-in page. Entra ID takes the domain part (everything after the @) and determines where to send you for authentication. For a managed domain (password hashes in Entra ID), you stay on the Microsoft sign-in page. For a federated domain (on-premises AD FS or a third-party identity provider), you get redirected to that system.

This step trips up hybrid environments where the UPN domain in Entra ID doesn't match what users expect to type. Wrong domain, wrong place.

**Step 2: Credential Collection**
Entra ID presents an authentication prompt appropriate for what it knows about you. If your organization has configured Windows Hello for Business, you might see a biometric prompt. If you've registered the Microsoft Authenticator for passwordless, you might see a number matching prompt. If nothing fancy is configured, you see a password field.

**Step 3: Risk Evaluation**
Before even checking your credentials, Entra ID is already collecting signals:

- 📍 Where is this sign-in coming from? Known IP, new country, impossible travel location?
- 💻 What device is being used? Registered? Compliant? Entra ID joined?
- 🕐 What time is it? Usual sign-in hours or 3 AM on a Saturday?
- 📊 Does this look like the user's normal behavior pattern?

These signals feed into Identity Protection's real-time risk engine and into Conditional Access policy evaluation.

**Step 4: Conditional Access Evaluation**
Every Conditional Access policy in your tenant gets evaluated against this sign-in. Policies that don't match (wrong user, wrong app, wrong conditions) are skipped. Policies that match apply their grant controls: require MFA, require compliant device, block access, or pass through.

If MFA is required, the authentication flow pauses here, sends the user a challenge (push notification, TOTP code, etc.), and waits for a response. If the user satisfies MFA, the flow continues. If they don't or can't, access is denied.

**Step 5: Token Issuance**
Authentication succeeded and Conditional Access said yes. Entra ID now issues tokens: an ID token (proving who the user is), an access token (granting access to the specific resource), and potentially a refresh token (for future silent re-authentication without a full sign-in).

The tokens contain claims about the user: their Object ID, display name, group memberships, assigned roles, authentication method used, and more. The receiving application reads these claims to make authorization decisions.

**Step 6: Access**
The application receives the token, validates it (checking that it was issued by your Entra ID tenant, that it hasn't expired, that it's for the right audience), and grants access accordingly.

Total elapsed time for all six steps: typically under two seconds.

## 📋 Sign-In Logs: Your Best Troubleshooting Tool

Every sign-in generates a log entry in Entra ID. Every single one. Successful or failed, interactive or non-interactive, human or application. These logs are your first stop for any authentication problem.

The sign-in log entry tells you:

- ✅ Whether authentication succeeded or failed
- ❌ The specific error code if it failed
- 🔒 Which Conditional Access policies applied and what they required
- 📱 What authentication method was used
- 📍 Where the sign-in came from (IP, location, device)
- ⚡ The risk level detected

I've resolved authentication issues in minutes that other teams spent hours on, simply because I went to the sign-in logs first instead of guessing. The log tells you exactly what happened and at which step. "Authentication failed because the user didn't satisfy MFA" is a completely different problem than "authentication failed because the account was disabled" or "authentication failed because Conditional Access blocked legacy auth."

Go to the Entra admin center, find Identity > Monitoring > Sign-in logs. Filter by the user's UPN and the approximate time of the issue. Read what it says. Most of the answer is right there.

## 🚪 Interactive vs Non-Interactive Sign-Ins

Two categories you'll see in the logs, and they matter for understanding what you're looking at.

**Interactive sign-ins** involve a human. There's a browser, a prompt, a credential entry, possibly an MFA response. The user is present and participating.

**Non-interactive sign-ins** are background authentications with no human involvement. An app using a refresh token to silently get a new access token. A service authenticating with a certificate. These generate log entries too, and can generate a lot of them. Filter accordingly when you're troubleshooting a human sign-in issue.

---

💬 **Have you ever solved a sign-in issue by reading the logs directly?** What did they reveal that wasn't obvious from the user's description? Sign-in logs have a way of telling a very different story than "it just doesn't work."
<!-- nav -->

---

[← Authentication](glossary-3-1-authentication.md) | [Home](../README.md) | [Authentication Method →](glossary-3-3-authentication-method.md)
