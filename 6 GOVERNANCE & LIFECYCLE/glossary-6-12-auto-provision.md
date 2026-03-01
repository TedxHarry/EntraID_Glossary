# Auto-Provision: When Access Appears Without Anyone Creating It

**Part of Entra ID Glossary Series: Glossary#6.12 - Auto-Provision**

---

An HR coordinator asked me how a new hire on her team had a fully configured Workday account ready on their first day, including the right reporting structure and org chart position, when she hadn't submitted any ticket to have it created.

The answer: their Workday account was provisioned automatically when their Entra ID account was created and they were added to the HR team group. The provisioning connection had been configured months earlier. When the conditions were met, the account appeared.

That's auto-provision working as it should: access that exists when you need it, without anyone having to do anything to create it.

## ⚙️ What Auto-Provisioning Is

Auto-provisioning (automatic provisioning) is the process where user accounts in connected applications are created, updated, or disabled automatically in response to changes in Entra ID, without manual intervention from IT or application administrators.

When auto-provisioning is configured between Entra ID and an application:

- Adding a user to a provisioning scope → account created in the app
- Updating user attributes in Entra ID → account attributes updated in the app
- Removing a user from scope or disabling their account → account disabled/deleted in the app

The provisioning runs on a schedule (every 40 minutes by default) and on-demand when triggered manually. It doesn't wait for a ticket. It doesn't depend on anyone remembering.

## 🔄 The Trigger-Action Model

Auto-provisioning is fundamentally trigger-action: a change happens in Entra ID, and that change triggers a provisioning action in the target application.

**Common triggers**:
- User assigned to the application directly in Entra ID
- User added to a group that is in scope for provisioning to the application
- User's department attribute changes to match a provisioning filter rule
- New user created (if all users are in scope)
- User account disabled in Entra ID

**Resulting actions in the target application**:
- CREATE: New account created with mapped attributes
- UPDATE: Existing account attributes updated to match current Entra ID values
- DISABLE: Account deactivated (soft delete)
- DELETE: Account permanently removed (hard delete, if configured)

Which action occurs depends on what changed in Entra ID and how the provisioning is configured.

## 📋 Attribute Mapping

Auto-provisioning moves more than just the user's existence to the target application. Attribute mapping configuration defines which Entra ID attribute values map to which fields in the target application.

A typical mapping for a SaaS application:

| Entra ID Attribute | Target App Field |
|-------------------|-----------------|
| userPrincipalName | Username |
| displayName | Full Name |
| mail | Email |
| department | Department |
| jobTitle | Job Title |
| manager.mail | Manager Email |

Attributes can be mapped directly, transformed (convert to uppercase, extract a substring), or computed from expressions combining multiple source values.

Getting attribute mapping right is the primary configuration work in setting up auto-provisioning. The defaults usually cover the basics, but custom attributes, format differences, and app-specific required fields need manual mapping attention.

## 🔧 Provisioning Scope

Not every user necessarily gets provisioned to every application. Provisioning scope defines which users are included:

**All users**: Every user in Entra ID is provisioned to the application. Appropriate for organization-wide tools.

**Assigned users only**: Only users specifically assigned to the application in Entra ID are provisioned. The most common model for role-specific applications.

**Scoping filters**: Rules based on attribute values. Example: only provision users whose department is "Engineering" or whose jobTitle contains "Developer." Useful when group membership isn't the right signal but an attribute is.

## ⚠️ What Breaks When Provisioning Is Misconfigured

The most common auto-provisioning issue: an attribute that's required by the target application isn't populated in Entra ID for all users. Provisioning fails for those users, silently or with an error in the provisioning logs that nobody checks.

The provisioning logs in the Entra admin center show every provisioning operation: what was attempted, what was sent, what the application returned. For troubleshooting provisioning failures, the logs are the starting point. A user whose app account wasn't created will have a corresponding failure entry in the logs with the specific error.

## 💡 Testing Before Enabling

Entra ID provisioning has an "on-demand provisioning" feature: you can select a specific user and trigger provisioning for them alone, seeing exactly what would be sent and what the application would return. This allows testing the configuration against a real account before enabling provisioning for the entire scope.

Testing one user before enabling broad provisioning catches attribute mapping errors, app-side validation failures, and permission issues before they affect hundreds of accounts.

---

💬 **Which application in your environment generates the most manual provisioning work today that could be automated?** The combination of "frequently onboards new users" and "has a SCIM endpoint or gallery connector available" is the sweet spot for first automation projects. What's stopping the first connection from being made?
<!-- nav -->

---

[← Approval Workflow: Who Decides, in What Order, and What Happens If They Don't](glossary-6-11-approval-workflow.md) | [Home](../README.md) | [Just-in-Time Access: Admin Privileges Should Be Borrowed, Not Owned →](glossary-6-13-just-in-time-access.md)
