# Microsoft Authenticator: More Than a Code Generator

**Part of Entra ID Glossary Series: Glossary#3.8 - Microsoft Authenticator**

---

When I ask IT admins how their users authenticate, the answer is usually some version of: "They use the Authenticator app, you know, for the six-digit codes."

Fair enough. That's how most people use it. But the Microsoft Authenticator app has three distinct authentication modes, meaningful anti-phishing features that have been fighting real attacks, and a passwordless capability that eliminates the password from the sign-in flow entirely.

The six-digit codes are maybe 30% of what this app can do.

## 📱 The Three Authentication Modes

**Mode 1: TOTP codes (Time-Based One-Time Passwords)**
The classic mode. The app generates a 6-digit code that rotates every 30 seconds based on a shared secret and the current time. The user types the code during sign-in. This works offline, requires no network connection on the phone, and is compatible with almost every MFA-capable service, not just Microsoft.

Limitation: TOTP codes are phishable. A real-time phishing site can capture the code and relay it to the legitimate site within the 30-second window. Better than password alone, but not phishing-resistant.

**Mode 2: Push notifications (Approval requests)**
The app receives a push notification asking "Did you just sign in?" The user taps Approve or Deny. No code typing required, faster user experience, and Entra ID logs which device approved the request.

This mode has evolved significantly in response to MFA fatigue attacks. Modern push notifications in Authenticator include:

- 🔢 **Number matching:** The sign-in screen shows a number. The app shows three numbers. The user must select the matching one. A flood of approval requests still arrives in a fatigue attack, but each one requires the user to actively identify the correct number from the sign-in page they're looking at. If they're not actually signing in, there's no number to match.

- 📍 **Additional context:** The notification shows the application being accessed and the geographic location of the sign-in. "Microsoft Outlook from Kyiv, Ukraine" is much harder to accidentally approve than a generic "Sign in?" prompt.

**Mode 3: Passwordless phone sign-in**
The user registers their phone for passwordless sign-in. During authentication, they enter only their username. No password field appears. The app sends a push notification with number matching to approve. The credential is bound to the specific registered device.

This mode satisfies MFA requirements automatically because it combines something you have (the registered phone) with something you know or are (the biometric or PIN used to unlock the phone and approve the notification).

## ⚙️ Registration and Setup

Users register the Authenticator app through the Security Info page at `mysignins.microsoft.com`. The process:

1. Download Microsoft Authenticator on iOS or Android
2. Go to Security Info, click Add sign-in method, select Authenticator app
3. Scan the QR code shown on screen
4. Complete a test notification to verify the connection

Registration takes under two minutes. The tricky part isn't the technology, it's making sure users do it before they're locked out of something and need it urgently.

💡 Enable the **MFA registration campaign** in Entra ID (under Protection > Authentication Methods > Registration campaign). It nudges users who haven't registered through a gentle prompt during sign-in, allowing a configurable number of skips before making it mandatory. This removes the "we told them to do it but many didn't" problem.

## 🛡️ Number Matching: Why It Matters

Before number matching became default, push notification MFA had a real Achilles heel. An attacker with stolen credentials could spam approval requests to a user's phone at 2 AM, and enough users would tap approve just to stop the notifications. This wasn't theoretical: the Uber breach in 2022 succeeded in part through this exact technique.

Microsoft made number matching mandatory for Authenticator push notifications starting in May 2023. It's now on by default and can't be disabled through normal policy.

The practical effect: MFA fatigue attacks against Authenticator push notifications became dramatically less effective overnight. The attacker can still spam notifications. The user can still receive them. But approving one requires actively typing a number that only appears on a screen the user is currently looking at during a legitimate sign-in.

## 🔄 Authenticator vs FIDO2 vs Windows Hello

These three aren't competitors. They occupy different parts of the authentication landscape.

| Scenario | Best Option |
|---|---|
| Admin accounts, highest assurance | FIDO2 hardware key |
| Managed Windows laptop users | Windows Hello for Business |
| Mobile-first users, personal or unmanaged devices | Authenticator passwordless |
| Fallback/backup method | Authenticator push with number matching |
| Offline environments | Authenticator TOTP codes |

The Authenticator app is particularly valuable as a universally deployable option. FIDO2 keys require hardware procurement. Windows Hello for Business requires managed Windows devices. Authenticator works on any iOS or Android device a user already carries.

For organizations early in their authentication journey, "Authenticator with push notifications and number matching enabled" is an achievable and meaningful security improvement for the entire user population, not just those with specific hardware or device types. 🔐

---

💬 **How many of your users have the Authenticator app registered and actually use it for sign-in?** And have you enabled number matching and additional context if you're using push notifications? The difference in attack resistance between plain push and number-matched push is significant.

#EntraID #MicrosoftAuthenticator #MFA #CloudSecurity #Passwordless #MicrosoftEntra #IdentityProtection
