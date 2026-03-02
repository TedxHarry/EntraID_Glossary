# Bulk User Operations
*When You Need to Change 500 Accounts at Once*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.16 - Bulk User Operations

---

## 🎯 TL;DR

- Bulk operations create, update, or delete multiple users at once via CSV upload or PowerShell/Graph API
- CSV bulk upload supports up to 40,000 users; PowerShell/Graph supports larger batches
- Always test bulk operations on a small group first : mistakes affect many users simultaneously


A company acquired a smaller firm. 340 new employees needed Entra ID accounts, licenses, and initial group memberships created before the integration date. Doing this one at a time through the Entra admin portal would have taken two days of solid clicking.

The IT team exported the HR data as a CSV, transformed it into the required format, and ran a bulk import. 340 accounts, created in 20 minutes. The remaining time was spent verifying the results and troubleshooting the 4 accounts that had data issues.

Bulk user operations exist because identity administration at scale requires handling multiple objects simultaneously, not one at a time.

## 📋 What bulk operations cover

Entra ID supports bulk operations across the main administrative tasks:

**Bulk create** ➕: Upload a CSV file with user account details. Entra ID creates all accounts in the file, returning a results file showing which succeeded and which failed with error details.

**Bulk invite** 📧: Invite multiple external guest users simultaneously. Upload a CSV with email addresses and optional personal messages. Entra ID sends invitations to all addresses in the file.

**Bulk delete** ❌: Delete multiple user accounts from a CSV of user principal names or object IDs. Deleted accounts go to the recycle bin (recoverable for 30 days) unless permanently deleted.

**Bulk restore** 🔄: Restore multiple recently deleted user accounts from a CSV. Useful when a bulk delete goes wrong or when accounts need to be recovered after an offboarding batch.

**Bulk license assignment** 📄: Assign or remove licenses for multiple users simultaneously. This is often done through group-based licensing rather than individual bulk operations, but direct bulk assignment is available.

## 🔧 The CSV format

Bulk create via CSV requires specific column headers and formatting. The required fields:

```
Name [displayName] Required
User name [userPrincipalName] Required
Initial password Required
Block sign in (Yes/No) Required
```

Optional fields include department, job title, usage location, manager, phone numbers, and addresses. The usage location field is required for license assignment and must be a valid two-letter country code (US, GB, DE, etc.).

The most common bulk create failure: invalid characters in the UPN, missing required fields, or usage location codes that don't match Entra ID's accepted values.

## ⚡ PowerShell and graph API for scale

The portal CSV approach works for hundreds of accounts. For thousands of accounts, or for operations that need to run regularly (weekly new hire batches from HR), PowerShell or the Microsoft Graph API is more appropriate.

**PowerShell with the Microsoft Graph module**:

```powershell
# Create multiple users from an array
$users | ForEach-Object {
    New-MgUser -DisplayName $_.Name `
               -UserPrincipalName $_.UPN `
               -PasswordProfile @{ Password = $_.TempPassword } `
               -AccountEnabled $true `
               -UsageLocation "US"
}
```

**Graph API batch requests**: The Graph API supports batch requests that combine up to 20 individual operations into a single HTTP call. For large-scale user creation, batching reduces the API call overhead significantly.

## ⚠️ What to verify before and after

Before running a bulk operation, especially bulk delete or bulk attribute update:

- ✅ Validate the CSV in a test environment or against a non-production tenant if possible
- ✅ Confirm the scope is exactly what you intend (one extra column in the CSV can include accounts that shouldn't be included)
- ✅ For bulk delete: confirm the list has been reviewed and is accurate (deleted accounts are recoverable for 30 days, but permanent deletion is not)

After running:
- ✅ Download and review the results file - it shows success/failure for each row
- ✅ Spot-check a sample of the affected accounts
- ✅ Confirm downstream effects (provisioning, group membership, license assignment) if the operation triggers them

## 💡 Group-Based licensing vs bulk license assignment

For ongoing license management, group-based licensing is more maintainable than bulk operations. Users added to a licensed group automatically receive the assigned licenses. Users removed from the group lose them.

Bulk license assignment is appropriate for initial migrations, one-time events, or scenarios where group-based licensing isn't the right model. For day-to-day operations, group-based licensing removes the need for recurring bulk operations.

---

💬 **What's the largest bulk user operation you've run, and what validation process did you use before executing it?** The combination of "this affects hundreds of accounts" and "if I get the CSV wrong" creates a specific kind of pre-execution anxiety. What's your checklist?
✍️ TedxHarry

<!-- nav -->

---

[← Certification Campaign](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-15-certification-campaign.md) | [🏠 Contents](/README) | [User Attributes →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-17-user-attributes.md)
