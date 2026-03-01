# Microsoft Graph API: Programmatic Access to Everything in Your Entra ID Tenant

**Part of Entra ID Glossary Series: Glossary#13.21 - Microsoft Graph API**

---

An operations team was manually processing new hire requests every Monday morning. HR sent a spreadsheet. The team created user accounts, assigned licenses, added users to the right groups, and set up mailboxes. For 30 new hires, that was three hours of work. For 150 new hires at the end of a hiring surge, it was the entire morning.

A developer spent two days writing a script using Microsoft Graph API. The script read new hire data from the HR system, created user objects in Entra ID, assigned licenses, added users to department groups, and sent a confirmation email. Monday morning processing time: four minutes.

Microsoft Graph API is what makes Entra ID programmable.

## 🔗 What Microsoft Graph API Is

Microsoft Graph is a single REST API endpoint (`https://graph.microsoft.com`) that provides access to data and functionality across Microsoft 365 services, including the entire Entra ID directory. Users, groups, applications, service principals, devices, sign-in logs, audit logs, Conditional Access policies, directory roles, and more are all accessible through Graph endpoints.

The same data you see in the Entra admin center is available through Graph. The admin center itself is built on Graph. Every object you create, update, or delete through the admin UI is creating, updating, or deleting through the same API your scripts and applications use.

## 📋 Key Identity Endpoints for Entra ID Operations

**Users** 👤: `GET /users` retrieves all users. `GET /users/{id}` retrieves a specific user by object ID or UPN. `POST /users` creates a new user. `PATCH /users/{id}` updates attributes. `DELETE /users/{id}` deletes the user. The full user object includes every attribute available in Entra ID: displayName, userPrincipalName, jobTitle, department, accountEnabled, and all extension attributes.

**Groups** 👥: `GET /groups/{id}/members` retrieves group members. `POST /groups/{id}/members/$ref` adds a member. Managing dynamic groups via API requires updating the `membershipRule` property, which is the same filter expression shown in the dynamic group UI.

**Application registrations and service principals** 🔧: `GET /applications` lists app registrations. `GET /servicePrincipals` lists enterprise applications (service principals). Creating an app registration via API creates the application object in the home tenant; a service principal object in the same tenant is created separately.

**Conditional Access policies** 🔐: `GET /identity/conditionalAccess/policies` retrieves all CA policies with their full configuration in JSON. Creating and modifying CA policies via API uses the same object structure. Infrastructure-as-code CA policy management (storing policies in version control, deploying via pipeline) uses these endpoints.

**Directory roles and assignments** 🎯: `GET /directoryRoles` lists active roles. `GET /roleManagement/directory/roleAssignments` lists all role assignments. Managing PIM-based role assignments uses `roleManagement/directory/roleEligibilityScheduleRequests`.

## 🔑 Authentication for Graph API Calls

Microsoft Graph API requires a valid OAuth 2.0 token. Two permission models:

**Delegated permissions** 👤: The application acts on behalf of a signed-in user. The effective permissions are the intersection of what the user can do and what the application is permitted to do. If the user can read only their own profile, the application with `User.Read` gets only their profile, not all users.

**Application permissions** 🤖: The application acts as itself, without a user context. Uses the client credentials flow to obtain a token. Common for background jobs, automation scripts, and scheduled tasks that run without a user signing in. Application permissions for Graph tend to be broad: `User.ReadWrite.All` gives the application write access to all users in the tenant.

The distinction matters for governance: application permissions with high-privilege Graph scopes (especially `Directory.ReadWrite.All`, `RoleManagement.ReadWrite.Directory`, or `Mail.ReadWrite.All`) are significant attack surface if the service principal is compromised.

## 🔧 Graph Explorer and the SDK

**Graph Explorer** (developer.microsoft.com/graph/graph-explorer) is a browser-based tool for exploring Graph endpoints interactively. Sign in with your Entra ID account, select sample queries, modify them, and run them against your tenant. It shows the request URL, the required permissions, and the full JSON response. The right tool for learning Graph before writing code.

**Microsoft Graph SDK** 📦: Available for C#, Java, Python, JavaScript/TypeScript, Go, PHP, and PowerShell. The SDK handles authentication token acquisition, automatic retry on throttling, and type-safe deserialization of Graph objects. For production code, the SDK reduces boilerplate significantly versus raw HTTP calls.

**Microsoft Graph PowerShell** 💻: The `Microsoft.Graph` PowerShell module provides cmdlets wrapping Graph endpoints. `Get-MgUser`, `New-MgUser`, `Update-MgUser` for user management; `Get-MgGroup` for groups; `Get-MgIdentityConditionalAccessPolicy` for CA policies. The module replaced the older AzureAD and MSOnline modules, both of which are deprecated.

## ⚠️ Throttling and Bulk Operations

Graph API has throttling limits. High-volume operations (creating 5,000 users, bulk group membership updates) hit throttle limits and receive `429 Too Many Requests` responses. The correct approach: implement exponential backoff on 429 responses, use batch requests (up to 20 requests in a single batch call), and use delta queries for incremental sync rather than full retrieval on each run.

The `$batch` endpoint allows sending 20 Graph requests in a single HTTP call, dramatically reducing the time and throttle exposure for bulk operations.

---

💬 **What Graph API operations does your team rely on for Entra ID automation, and have you migrated from the deprecated AzureAD and MSOnline PowerShell modules to the Microsoft Graph PowerShell module?** The migration from legacy modules to Graph PowerShell is one of those projects that's easy to defer until it becomes urgent. What was the most valuable automation your team built on Graph, and what would break if you lost API access to Entra ID?

#EntraID #MicrosoftGraph #GraphAPI #PowerShell #IdentityAutomation #MicrosoftEntra #DirectoryManagement
<!-- nav -->

---

[← Policy Evaluation: Understanding How Conditional Access Decisions Are Made](glossary-13-20-policy-evaluation.md) | [Home](../README.md) | [Microsoft Authenticator Advanced: Beyond Basic MFA to Modern Authentication →](glossary-13-22-microsoft-authenticator-advanced.md)
