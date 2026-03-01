# User Attributes: The Properties That Drive Everything Else

**Part of Entra ID Glossary Series: Glossary#6.17 - User Attributes**

---

A dynamic group was supposed to automatically include all members of the Engineering department. Six engineers were in the group. Two were missing.

The dynamic membership rule was correct: `(user.department -eq "Engineering")`. The query was right. But those two users had been onboarded before the HR integration was fully configured, and their department attribute in Entra ID was blank. The rule couldn't match what wasn't there.

User attributes are the properties stored on the user object. They look like background data. But they drive group memberships, Conditional Access decisions, provisioning scope filters, access review routing, and lifecycle workflow triggers. When attributes are wrong or missing, everything built on top of them behaves unexpectedly.

## 📋 The Core User Attributes

Every Entra ID user object has a standard set of attributes defined by the Microsoft Graph user schema:

**Identity attributes** 🆔
- `userPrincipalName` (UPN): The sign-in identifier. `name@domain.com` format. Must be unique in the tenant.
- `displayName`: The full name shown in the directory and applications.
- `givenName` / `surname`: First and last name separately.
- `mail`: The primary email address. May differ from UPN.
- `mailNickname`: The alias used for the email address before the @ symbol.

**Organizational attributes** 🏢
- `department`: The department or organizational unit. Used heavily in dynamic group rules and provisioning filters.
- `jobTitle`: The user's role. Used in provisioning, sometimes in Conditional Access.
- `companyName`: Organization name. Important in multi-organization tenants.
- `manager`: A reference to another user object (not a string). Points to the user's manager, used for approval routing in PIM and entitlement management.
- `employeeId`: HR system identifier. Used to correlate the Entra ID account with the HR record.
- `employeeType`: Employee, contractor, vendor. Useful for dynamic group rules that should include/exclude contractors.

**Contact attributes** 📞
- `mobilePhone`: Used for SMS MFA.
- `businessPhones`: Work phone numbers.
- `officeLocation`: Physical office or building.
- `usageLocation`: Two-letter country code. Required before licenses can be assigned.

**Account state attributes** 🔒
- `accountEnabled`: Whether the account is enabled or disabled.
- `createdDateTime`: When the account was created.
- `lastSignInDateTime`: When the user last signed in (read-only, system-populated).

## 🔄 How Attributes Drive Dynamic Groups

Dynamic Entra ID groups use attributes as membership criteria. Instead of manually adding users, the group membership rule evaluates every user's attributes and includes those that match.

Common dynamic group rules:

```
# All full-time employees in Engineering
(user.department -eq "Engineering") and (user.employeeType -eq "Employee")

# All contractors
(user.employeeType -eq "Contractor") and (user.accountEnabled -eq true)

# All users in a specific country
(user.usageLocation -eq "GB")

# All users whose job title contains "Manager"
(user.jobTitle -contains "Manager")
```

When an attribute changes on a user (promoted from Engineer to Engineering Manager, transferred from Engineering to Product), the dynamic group memberships update automatically. The right access follows the person without manual group management.

## ⚙️ Custom Security Attributes and Extension Attributes

Beyond the standard schema, Entra ID supports:

**Extension attributes** (`extensionAttribute1` through `extensionAttribute15`): Legacy attributes originally from Exchange Online. Limited to strings, no validation, but widely used in hybrid environments where on-premises AD synchronizes values to these fields.

**Custom security attributes**: The modern alternative. Admins define custom attribute sets with specific value types and allowed values. These can be used in access controls, dynamic group rules, and attribute-based access control (ABAC) scenarios.

## ⚠️ Attribute Quality as a Governance Foundation

Every governance control that uses attributes to route decisions depends on those attributes being accurate. The engineering dynamic group failure in the opening story is a mild version. Worse cases:

- Approval workflows routing to the wrong manager because the manager attribute points to a former manager who left
- PIM activation reviews going to the wrong email because UPN changed but wasn't updated in PIM configuration
- Provisioning creating accounts in the wrong system because department attribute is inconsistent

Attribute quality is an infrastructure concern, not a cosmetic one. Regular audits of key attributes (department, manager, employeeType, usageLocation) against the authoritative HR system prevent these failures.

## 💡 HR as the Attribute Authority

For organizations with HR integration, the HR system should be the source of truth for organizational attributes. Inbound provisioning from Workday or SuccessFactors keeps department, manager, jobTitle, and employeeType synchronized automatically. When these change in HR, Entra ID attributes update within the provisioning cycle.

Manual attribute maintenance in Entra ID is error-prone at scale. Automating the connection to HR removes the dependency on IT keeping up with every hire, transfer, and title change.

---

💬 **Have you traced a governance or provisioning failure back to a missing or inaccurate user attribute?** The "dynamic group didn't include the right people" failure mode almost always comes down to attribute data quality. What was the attribute, and what was the impact of the mismatch?
<!-- nav -->

---

[← Bulk User Operations: When You Need to Change 500 Accounts at Once](glossary-6-16-bulk-user-operations.md) | [Home](../README.md) | [Source of Authority: Which System Gets to Say Who You Are →](glossary-6-18-source-of-authority.md)
