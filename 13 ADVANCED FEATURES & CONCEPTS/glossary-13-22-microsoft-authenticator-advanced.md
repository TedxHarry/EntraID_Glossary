# Microsoft Authenticator Advanced
*Beyond Basic MFA to Modern Authentication*

**Part of Entra ID Glossary Series: Glossary#13.22 - Microsoft Authenticator Advanced**

---

A security team deployed push notification MFA across 8,000 users. Three months later, an incident investigation revealed that a user had approved 11 fraudulent MFA push requests in a single week. The attacker had the user's password and sent rapid-fire push requests at 6am when the user was half asleep. The user kept tapping "Approve" to make the notifications stop.

The authentication method was technically MFA. It provided essentially zero protection against a determined attacker with a credential.

Number matching, additional context, and passkey support in Microsoft Authenticator exist because push notifications without them have a well-documented weakness.

## 📱 Number Matching: Closing the MFA Fatigue Gap

Number matching is a defense against MFA fatigue attacks (also called push bombing). Without number matching, a push notification says "Approve sign-in?" The user taps Approve without knowing anything about the sign-in attempt.

With number matching enabled, the authentication flow shows a two-digit number on the sign-in screen. The Authenticator push notification says "Enter the number shown on your sign-in screen." The user must look at both screens and type the matching number. An attacker sending fraudulent push requests gets no matching number. The user receives a push with no context and is prompted to enter a number they don't have.

Microsoft enabled number matching by default across all tenants in 2023. Disabling it requires explicit configuration and is not recommended. It's one of the highest-impact low-effort security improvements in Microsoft's authentication stack.

## 📍 Additional Context: Showing Users What They're Approving

Additional context in Authenticator push notifications shows two pieces of information the user didn't previously see:

**Application name** 📱: Which application is requesting authentication. "Sign in to Salesforce" is more meaningful than "Sign in." If the user isn't trying to access Salesforce, the notification is suspicious.

**Geographic location** 🌍: The approximate location derived from the sign-in IP address. "Sign in from Seattle, WA" helps users identify when a sign-in request is coming from an unexpected location.

Combined with number matching, additional context gives users enough information to make an informed approve-or-deny decision rather than reflexively approving a generic notification. Both number matching and additional context are configured in the Authentication Methods policy in the Entra admin center.

## 🔐 Passkey Support in Authenticator

Microsoft Authenticator supports passkeys stored in the Authenticator app itself. This makes the phone a phishing-resistant FIDO2 authenticator without requiring a separate hardware security key.

A passkey in Authenticator uses the phone's biometric authentication (fingerprint, face) to protect a device-bound private key. The sign-in flow: enter username, tap a notification on the phone, biometrically verify identity on the phone, sign-in completes. No password. No OTP code. No network-exposed credential.

Passkeys in Authenticator satisfy the phishing-resistant MFA requirement in Conditional Access authentication strength policies. They're bound to the phone and can't be exported or phished through fake websites. They work for both standard MFA and passwordless sign-in workflows.

Enabling passkeys in Authenticator requires configuring the Microsoft Authenticator authentication method policy to allow passkey authentication and enabling the Authentication methods policy for FIDO2. Users register the passkey from myprofile.microsoft.com or through an admin-initiated Temporary Access Pass bootstrap.

## 📲 Authenticator Lite

Authenticator Lite embeds push notification MFA capabilities directly into the Outlook mobile app. Users who have Outlook on their phone can use it for MFA approval without installing a separate Authenticator app.

For organizations with adoption resistance to installing security apps, Authenticator Lite reduces friction while maintaining push notification MFA. It supports number matching and additional context. It doesn't support passkeys or passwordless phone sign-in, which require the full Authenticator app.

Authenticator Lite is enabled in the Authentication Methods policy for the Microsoft Authenticator method. It's enabled by default for users who have the Authenticator method enabled and have Outlook installed.

## 🔑 Passwordless Phone Sign-In

Passwordless phone sign-in removes the password from the authentication flow entirely. The flow: enter username, receive a notification on the phone, tap the notification, biometrically verify or enter the phone PIN, authentication completes. No password prompt.

The credential is device-bound to the phone. Even if someone has the user's username, they can't authenticate without physical access to the registered phone. This eliminates password-based attacks (credential stuffing, phishing for passwords) from the attack surface.

Passwordless phone sign-in requires the Authenticator app to be registered as an authentication method, the user to have completed registration, and the passwordless phone sign-in configuration enabled in the Authentication Methods policy. It doesn't satisfy phishing-resistant MFA requirements (that requires passkeys or FIDO2 hardware keys), but it provides significantly stronger security than password-plus-OTP.

## ⚙️ Authentication Methods Policy

All Authenticator features are configured in the Entra admin center under **Protection > Authentication Methods > Microsoft Authenticator**. The policy lets you enable the method for all users or specific groups, configure number matching and additional context display modes (enabled, disabled, or Microsoft managed), and enable passkey and passwordless features.

The Microsoft Managed setting lets Microsoft's defaults evolve as security recommendations change, without requiring manual policy updates for each improvement.

---

💬 **Has your organization enabled number matching and additional context for Authenticator push notifications, and have you seen a measurable reduction in MFA fatigue attack attempts since enabling them?** The gap between "we have MFA" and "we have MFA that's actually resistant to the attacks people use against MFA" is where many organizations find themselves after an incident. What authentication method changes has your team made after seeing the limits of basic push MFA?
<!-- nav -->

---

[← Microsoft Graph API](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-21-graph-api.md) | [🏠 Contents](/README) | [Microsoft Entra Suite →](/13%20ADVANCED%20FEATURES%20%26%20CONCEPTS/glossary-13-23-microsoft-entra-suite.md)
