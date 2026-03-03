# Just-in-Time Access
*Admin Privileges Should Be Borrowed, Not Owned*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #6.13 - Just-in-Time Access

---


I asked an IT team to show me their Global Administrators. The list had 11 names.

I asked how many of them used their Global Admin privileges in a typical week. Three hands went up.

I asked why the other 8 had permanent Global Admin assignments. The answer was familiar: "In case we need them. It's easier to have it and not need it than need it and not have it."

That reasoning makes intuitive sense and is exactly backwards from a security perspective. An admin account with permanent Global Administrator access is a standing invitation: compromise the account and you get everything, forever, with no additional steps.

Just-in-time access is the architecture that removes that invitation.

## 📌 ⏱️ what just-in-time access is

Just-in-time (JIT) access means privileged access is granted for a limited time, for a specific purpose, and only when it's actually needed. Between tasks that require admin privileges, the access doesn't exist. There's nothing to compromise.

Microsoft Entra Privileged Identity Management (PIM) is the implementation of JIT access for Entra ID. With PIM:

- Admin roles are assigned as **eligible**, not permanent
- When an admin needs to use the role, they **activate** it
- Activation requires a justification and can require MFA or manager approval
- The role is active for a configured window (1 to 8 hours typically)
- At the end of the window, the activation expires and the privilege disappears

Between activations, the admin account has no elevated privileges. A compromised account has no admin access until it completes an activation, which requires additional authentication and creates an audit log entry.

## 🔄 Eligible vs active assignment

PIM introduces two assignment types for privileged roles:

**Eligible assignment** 🔵: The user can activate the role when needed. Without activation, they have no privileges from this role. This is the JIT model.

**Active assignment** 🔴: The user always has the role privileges. Traditional permanent assignment. Should be reserved for accounts where constant availability is required (break-glass accounts, service accounts that can't interactively authenticate).

The goal is to convert as many Active assignments to Eligible assignments as possible. Start with the highest privilege roles: Global Administrator, Privileged Role Administrator, Security Administrator.

## 📋 The activation experience

When an admin needs elevated access, they go to the PIM portal (`myaccess.microsoft.com` or the Entra admin center):

1. Select the eligible role they want to activate
2. Set the duration (up to the maximum configured for this role)
3. Enter the business justification ("Investigating security alert #INC-4423")
4. Complete MFA if required by the activation policy
5. If manager approval is required, wait for approval notification
6. Role activates and is available

During activation, every action the admin takes is attributable to this specific activation event in the audit logs. The justification links the privilege use to a business reason. The time limit ensures the privilege is automatically removed.

## 🔒 PIM for Azure resources

PIM isn't only for Entra ID directory roles. It also covers Azure RBAC roles: Owner, Contributor, User Access Administrator, and custom roles on Azure subscriptions and resource groups.

An engineer who needs to deploy to a production Azure subscription gets Owner access via PIM for 2 hours, makes the deployment, and the access expires. No standing Contributor on production. No accidental production changes during normal development work.

The same JIT model applies: eligible assignment, time-bound activation, justification required, audit trail created.

## ⚠️ What JIT doesn't solve

JIT access reduces the attack surface of admin accounts significantly. It doesn't eliminate risk entirely.

If an admin's account is compromised while an activation is in progress, the attacker has the active privileges for the remainder of the activation window. The window should be as short as practical for the task.

JIT also depends on admins using the activation process rather than sharing credentials or using other paths to elevated access. The process only works if the privileged roles are actually configured as eligible-only and no alternative path exists.

## 💡 Starting with PIM

The activation effort for admins is low: 2-3 minutes to activate a role, justification typing, one MFA challenge. For roles used infrequently, this is a worthwhile trade for the significant reduction in standing privilege.

Start with Global Administrator. Convert permanent assignments to eligible. Set the maximum activation time to 4 hours. Require justification. The security posture improvement is immediate and substantial.

---

💬 **What's the ratio of permanently-active admin roles to eligible PIM assignments in your organization?** The first time an organization audits this, the permanent assignment count is almost always higher than expected. What drove the move to JIT access, and what was the most common admin objection?
✍️ TedxHarry


> 🔑 **Licensing:** PIM (Just-in-Time access for Entra ID roles) requires **Entra ID P2**. Azure resource role PIM is included in Entra ID P2 as well.


### 🔧 Quick reference: PIM PowerShell

```powershell
# List all eligible role assignments (PIM)
Get-MgRoleManagementDirectoryRoleEligibilitySchedule -All |
    Select-Object PrincipalId, RoleDefinitionId, StartDateTime, EndDateTime

# Activate an eligible role (as the user)
New-MgRoleManagementDirectoryRoleAssignmentScheduleRequest -BodyParameter @{
    action = "selfActivate"
    principalId = "<your-object-id>"
    roleDefinitionId = "<role-definition-id>"
    directoryScopeId = "/"
    scheduleInfo = @{ startDateTime = (Get-Date -Format o); expiration = @{ type = "afterDuration"; duration = "PT4H" } }
    justification = "Needed for emergency break-glass account audit"
}
```

<!-- nav -->

---

[← Auto-Provision](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-12-auto-provision.md) | [🏠 Contents](/README) | [Governance →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-14-governance.md)
