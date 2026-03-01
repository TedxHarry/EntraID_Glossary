# CAE: When Access Tokens Get Revoked Mid-Session

**Part of Entra ID Glossary Series: Glossary#7.32 - CAE (Continuous Access Evaluation)**

---

A user had a valid session open in Outlook. While they were working, an admin received a report that the account had been compromised. The admin disabled the user's account in Entra ID.

Without CAE: the user's access token remained valid for its remaining lifetime, up to an hour. The compromised session would continue working for up to 60 minutes after the account was disabled.

With CAE: Outlook received a revocation signal from Entra ID within seconds of the account being disabled. The application rejected the token. The session ended. The compromised access was revoked in near real-time.

That gap between "account disabled" and "access actually stops" is what CAE is designed to close.

## ⚡ What CAE Is

Continuous Access Evaluation is a protocol that enables near-real-time enforcement of access policy changes during active sessions. It shifts the security model from "tokens expire eventually" to "tokens are revoked when conditions change."

Without CAE, the standard token lifecycle creates a security window: access tokens are issued at authentication and remain valid until they expire, typically one hour. During that window, policy changes have no effect on the active session. A user whose account is disabled continues to work in applications until their token expires.

With CAE, participating applications maintain a persistent connection with Entra ID that enables:

- Near-real-time receipt of revocation signals when critical events occur
- Immediate rejection of the current token in response to those signals
- A new authentication request to Entra ID to get a new token (or fail if access is now denied)

The result: access policy changes propagate to active sessions within seconds rather than waiting for token expiry.

## 🔔 Events That Trigger CAE Revocation

CAE responds to critical changes that should immediately affect ongoing sessions:

**User account disabled** 🚫: When an admin disables a user's account, the revocation signal propagates to active sessions. The user's session ends within seconds.

**User deleted** 🗑️: Same propagation when an account is deleted.

**Password changed** 🔑: When the user's password changes (by the user or an admin), existing sessions using the old password context are revoked.

**Risk level changed to High** 🔴: When ID Protection elevates the user's risk to High, CAE can revoke active sessions, preventing continued access during an active compromise investigation.

**Token revoked** 🎟️: When an admin explicitly revokes all refresh tokens (via PowerShell or the admin center), CAE propagates the revocation to active sessions.

**Conditional Access policy change** 📋: When a CA policy change would now deny access to a session that was previously granted, CAE enforces the new policy. If a device becomes non-compliant during an active session, the session can be revoked.

## 🔗 How CAE Works Technically

CAE is an extension to the OAuth 2.0 token flow supported by both Entra ID and participating applications:

**Long-lived tokens with real-time enforcement**: CAE-enabled applications can receive access tokens with longer lifetimes (up to 24 hours instead of 1 hour) without sacrificing security, because revocation happens in real-time rather than waiting for expiry. The tradeoff between security and offline access is improved.

**Claims challenge**: When an application receives a revocation signal, it issues a claims challenge back to the client. The client must re-authenticate to Entra ID with the new requirements. If the conditions that caused revocation (disabled account, high risk) prevent re-authentication, access is denied.

**Client-side evaluation**: CAE-enabled clients can also evaluate certain conditions locally. A Windows client that detects it has become disconnected from the managed network can enforce conditional access decisions without waiting for a server-side signal.

## 📱 Which Applications Support CAE

CAE requires support from both Entra ID (as the authorization server) and the client application. Microsoft applications support CAE natively:

- Exchange Online (Outlook, OWA)
- SharePoint Online
- Microsoft Teams
- Microsoft Graph API
- Azure Resource Manager

Third-party applications can implement CAE support using the Microsoft Identity Platform libraries (MSAL). Adoption is growing but not universal.

For applications that don't support CAE, the traditional token lifetime model still applies. Shorter token lifetimes (sign-in frequency session control in Conditional Access) can reduce the window for non-CAE applications.

## ⚙️ CAE as a Session Control

In Conditional Access, CAE is configured as a session control. You can configure:

**Strict enforcement**: Revoke sessions immediately when policy conditions change, even for events that would otherwise allow reauthentication. More disruptive but more secure.

**Standard enforcement** (default): Allow applications to reauthenticate silently if the user still meets policy requirements. The user experiences a brief pause while the token is refreshed, but not necessarily a full sign-out.

For high-security scenarios (admin accounts, sensitive data access), strict enforcement is appropriate. The brief disruption of a reauthentication is acceptable compared to the risk of an active compromised session.

---

💬 **Before you knew about CAE, did you realize there was a window between an account being disabled and access actually stopping?** The gap between "policy enforced" and "policy actually takes effect on active sessions" is surprising to many administrators. Has knowing about this gap changed how quickly you respond to account compromise incidents?

#EntraID #CAE #ContinuousAccessEvaluation #ConditionalAccess #MicrosoftEntra #ZeroTrust #IdentitySecurity
<!-- nav -->

---

[← CA Template: Microsoft's Starting Points for Conditional Access](glossary-7-31-ca-template.md) | [Home](../README.md) | [Directory Synchronization: Bridging On-Premises Identity with the Cloud →](../8%20HYBRID%20%26%20ON-PREMISES/glossary-8-1-directory-synchronization.md)
