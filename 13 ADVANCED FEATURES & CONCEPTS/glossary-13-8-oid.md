# OID: The Stable GUID That Should Be Your Application's User Key

**Part of Entra ID Glossary Series: Glossary#13.8 - OID (Object ID)**

---

An application stored user records keyed on UPN. For three years it worked. Then the organization went through a merger-driven rebranding. Everyone's email domain changed from `oldco.com` to `newco.com`. UPNs changed to match.

The application broke for every single user. Their UPN in Entra ID was now `user@newco.com`. The application's database still had records under `user@oldco.com`. The application couldn't find anyone.

The fix was a database migration: update every user record's key from the old UPN to the new UPN. Two weeks of engineering work for a naming convention change.

If the application had used the Object ID instead, none of this would have happened. The Object ID didn't change. It never does.

## 🔷 What the Object ID Is

The Object ID (OID) is the globally unique identifier assigned to every object in Entra ID at the time of creation. It's a GUID: 32 hexadecimal characters in the format `xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx`.

Every type of directory object has one: users, groups, applications, service principals, managed identities, administrative units, role definitions, role assignments. The OID is the permanent, immutable identifier for that object within its tenant.

The OID appears in Entra ID tokens as the `oid` claim. It's what Entra ID uses internally to reference objects. It's what Graph API calls reference when you do `GET /users/{oid}`. It's what PIM uses for role assignment targeting. It's the foundation identifier in the Entra ID data model.

## 🔑 OID vs Other User Identifiers

Several identifiers are associated with a user object, each with different characteristics:

**OID (Object ID)** 🔵: Immutable GUID. Never changes. Unique within the tenant. The same user in two different tenants has different OIDs. The correct identifier for persistent application records.

**UPN (User Principal Name)** 📝: Mutable. Can change when email naming conventions change, after mergers, or for legitimate name changes. The sign-in identifier, not a storage key.

**Email address** 📧: Mutable, and may differ from UPN. A user can have multiple email aliases. Not appropriate as a unique key.

**sub (Subject claim)** 🎯: Pairwise pseudonymous. Stable within one application's tokens for one user, but different for the same user across different applications. Not suitable as a cross-application user key.

**employeeId** 🏢: Sourced from HR system. Stable within the organization's HR system, but not universally present in Entra ID, and can change in some organizational contexts.

**SID (Security Identifier)** 🔐: The on-premises Active Directory identifier. Synchronized to Entra ID as the `onPremisesSecurityIdentifier` attribute. Stable for hybrid users but absent for cloud-only users.

For application development, the guidance is consistent: use `oid` + `tid` (tenant ID) as the composite key for user records in multi-tenant applications, or `oid` alone for single-tenant applications. This survives UPN changes, email changes, display name changes, and any other mutable attribute updates.

## 📋 OID in Tokens and API Responses

In access tokens and ID tokens from the v2.0 endpoint, the Object ID appears as the `oid` claim. It's present in tokens issued for both user sign-ins and client credentials flows (where it identifies the service principal):

```json
{
  "oid": "a1b2c3d4-e5f6-7890-abcd-ef1234567890",
  "tid": "tenant-guid-here",
  "sub": "different-value-per-application",
  "upn": "user@contoso.com"
}
```

The `oid` is the same across all applications the user signs into within the same tenant. The `sub` differs per application. This is why `oid` is the right persistent key and `sub` is not.

In Microsoft Graph API responses, the `id` field of a user object is the OID. `GET /users/me` returns the current user's object where `"id"` is the OID.

## 🔍 Finding an Object's OID

**In the Entra ID portal** 📱: Navigate to any user, group, application, or service principal. The Overview page shows the Object ID prominently.

**Via Graph API** 🔷: `GET https://graph.microsoft.com/v1.0/users/{upn}` returns the user object where `id` is the OID. You can then store the OID and use it for subsequent lookups.

**Via Azure CLI** 💻: `az ad user show --id user@contoso.com --query id` returns the OID.

**In application logs** 📋: The `oid` claim in the JWT access token. Decode the token (base64, middle section) to see it directly.

## ⚠️ Cross-Tenant OID Uniqueness

OIDs are unique within a tenant, not across all of Entra ID. Two different Entra ID tenants could theoretically have objects with the same OID (extremely unlikely given GUID generation, but architecturally possible). For multi-tenant applications that accept users from any tenant, the stable user key is the combination of `oid` and `tid`, not `oid` alone.

---

💬 **Does your organization's internal application development standard specify which user identifier to use for persistent user records?** The UPN-as-key antipattern causes real migration pain when it eventually breaks. Do your application teams default to OID, or does the choice get made ad hoc per project?

#EntraID #ObjectID #OID #OAuth2 #TokenClaims #MicrosoftEntra #AppDevelopment
