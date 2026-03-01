# OAuth 2.0 in App Integration: How Modern Applications Request Access

**Part of Entra ID Glossary Series: Glossary#9.5 - OAuth 2.0 (App Integration Focus)**

---

A developer on my team built an internal tool that needed to read from SharePoint. His first attempt was straightforward: store a service account's username and password in the application's configuration file, use them to authenticate against SharePoint.

That approach worked. It also meant hardcoded credentials in a config file, credentials that would stop working when the service account's password changed, no audit trail for what the application accessed, and a shared secret that was now in version control history.

The OAuth 2.0 approach replaced all of that: register the application in Entra ID, grant it specific Microsoft Graph permissions (Files.Read.All scoped to the specific SharePoint sites), use a certificate instead of a password for the application to authenticate, and let Entra ID issue access tokens that SharePoint validates. No credentials in config files. Automatic token refresh. Precise audit trail in the sign-in logs.

## 🔌 OAuth 2.0 in the Application Context

At the protocol level (covered in Phase 4), OAuth 2.0 defines how authorization happens. In the application integration context, it's the practical mechanism through which applications registered in Entra ID authenticate themselves and request access to protected resources.

Every integrated application that makes API calls or accesses Microsoft resources uses OAuth 2.0 to get access tokens. The specific OAuth 2.0 flow it uses depends on what kind of application it is and whether a user is involved.

## 🔐 The Two Application Identity Models

**Delegated access (on behalf of a user)** 👤: The application acts on behalf of a signed-in user. The access token represents the user's identity and permissions. The application can only do what the user themselves is allowed to do. Used by applications where a human is present and interacting: web apps, mobile apps, desktop apps.

Example: A project management web app that reads the signed-in user's SharePoint files. The app requests a delegated token for Files.Read. The token allows reading the files that the specific user has access to. Another user signing in would get a different token with access to their files.

**Application access (no user present)** 🤖: The application acts with its own identity, not on behalf of any user. The access token represents the application's identity. The application's permissions determine what it can access. Used by background services, scheduled jobs, daemons, and automation.

Example: A nightly reporting job that reads from SharePoint to generate reports. No user is signed in. The application authenticates directly with Entra ID using a certificate or client secret, receives an app-only token, and accesses the data it's been granted permission to access.

## 📋 Application Registration: The OAuth 2.0 Starting Point

Before any OAuth 2.0 flow can happen, the application must be registered in Entra ID. The App Registration creates:

**Application ID (Client ID)** 🏷️: The unique identifier for the application. Included in OAuth 2.0 requests so Entra ID knows which application is requesting access.

**Redirect URIs** 🔄: The URLs where Entra ID sends the authorization code after user authentication. Must exactly match what the application uses. Security measure: prevents authorization codes from being sent to attacker-controlled URLs.

**Authentication credentials** 🔑: How the application proves its identity when requesting tokens. Two options:
- Client secret: A generated password. Convenient but has rotation requirements and exposure risk.
- Certificate: A public key uploaded to Entra ID. The application uses the private key to sign token requests. No shared secret. More complex to configure but more secure.

**API permissions** 📋: The specific permissions the application needs. Requesting Mail.Read and Files.Read.All requests those specific scopes. Users or admins consent to grant those permissions.

## 🎯 The Client Credentials Flow (App-Only)

The OAuth 2.0 flow for application access without a user:

1. Application sends a POST request to Entra ID's token endpoint
2. Request includes: client_id, client_assertion (signed with certificate) or client_secret, scope, and grant_type=client_credentials
3. Entra ID validates the application's identity (certificate or secret)
4. Entra ID verifies the application has the requested permissions (admin-consented)
5. Entra ID returns an access token
6. Application uses the access token in API calls

This flow has no user interaction, no redirect, no consent prompt. It's a direct machine-to-machine authentication. The token represents the application, not a user.

## ⚠️ Application Permissions vs Delegated Permissions

The distinction matters significantly for security:

**Delegated permissions** 👤: The application requests access on behalf of a specific user. The effective permission is the intersection of what the application is allowed AND what the user is allowed. If the user can only read their own files, the application can only read that user's files even if it has broad delegated permissions.

**Application permissions** 🤖: The application has its own permissions granted by an administrator. These permissions apply regardless of which user (if any) is involved. An application with Mail.ReadAll application permission can read all mailboxes in the organization. This is powerful and requires careful scoping.

Application permissions require admin consent (a tenant admin explicitly grants them). Delegated permissions can sometimes be consented by individual users depending on configuration. Over-provisioning application permissions is a significant security risk: a compromised application with Mail.ReadAll can exfiltrate all organizational email.

---

💬 **What's the most over-permissioned application registration you've found in your tenant?** Application permissions that were granted broadly during development and never scoped down are common. Mail.ReadAll granted when only one mailbox needed to be read. Directory.ReadWrite.All when only a few attributes needed updating. What was the permission scope that prompted a least-privilege review?

#EntraID #OAuth2 #AppIntegration #MicrosoftEntra #APIPermissions #ApplicationSecurity #IdentityDev
