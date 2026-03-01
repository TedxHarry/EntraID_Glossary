# Audience (Deep Dive)
*The Token Claim That Prevents One API's Token From Working on Another*

**Part of Entra ID Glossary Series: Glossary#11.11 - Audience (Deep Dive)**

---

A developer was building two APIs: a billing API and a reporting API, both protected by Entra ID. During testing, they noticed something: a token acquired for the billing API could also be used to call the reporting API. Both APIs had the same application ID as their intended audience.

Both APIs had forgotten to validate the audience claim.

An attacker who compromises a low-privilege token for any API in the tenant could potentially use it against any other API that skips audience validation. Audience validation is what prevents this. It's not a suggestion; it's the core of the resource server security model.

## 🎯 What the Audience Claim Is

The audience (`aud`) claim in a JWT access token identifies the intended recipient of the token. Only the service or API the token was issued for should accept it.

In Entra ID, the audience is expressed as the Application ID URI of the resource application. When you register an API in Entra ID, you define its Application ID URI (something like `api://my-api` or `https://api.contoso.com`). When a client requests a token for your API, Entra ID issues a token with that URI in the `aud` claim.

The resource API's first validation step: does the `aud` claim in this token match my own Application ID URI? If not, reject the token. If the billing API's URI is `api://billing` and a token arrives with `aud: api://reporting`, the billing API should reject it. The token wasn't issued for this API.

## 🔒 Why Audience Validation Matters

**Token confusion attacks** 🎭: An attacker acquires a legitimate token for a low-privilege API (perhaps through a public client application), then uses it against a different API that skips audience validation. Without audience validation, the second API trusts the token's other claims (user identity, scopes) without checking whether the token was intended for it.

**Scope misapplication** 🔑: Tokens carry scope claims representing permissions granted by the user or admin. These scopes are meaningful only within the context of the API they were defined in. A `User.Read` scope granted for Microsoft Graph has no authority over a custom API. But if the custom API doesn't validate the audience and just checks whether a scope named `User.Read` is present, a Microsoft Graph token could satisfy that check.

**Defense in depth** 🛡️: Audience validation is one layer in the API security model. Even if other validation steps have issues, correct audience validation limits token usability to the intended service.

## ⚙️ Configuring Your API's Audience

When registering an API application in Entra ID, the Application ID URI is set in the app registration's Expose an API section. This is the value that becomes the audience for tokens issued for that API.

Common patterns:
- `api://{client-id}` (the default, using the app registration's GUID)
- `https://api.contoso.com` (for APIs with a domain-based identifier)
- `api://my-api-name` (for descriptive, human-readable identifiers)

This URI must be globally unique within Entra ID. The default `api://{client-id}` is guaranteed unique because it uses the GUID. Custom URIs must be verified against a domain your tenant owns.

## 📋 Audience in Practice: Middleware Validation

Most API frameworks validate tokens through middleware or libraries that handle JWT validation. The audience is a required configuration parameter:

**ASP.NET Core with Microsoft.Identity.Web**:
```csharp
services.AddMicrosoftIdentityWebApiAuthentication(configuration,
    "AzureAd");
```
The `ClientId` or `Audience` setting in configuration is what the middleware validates against the `aud` claim. If not set correctly, all tokens pass or all tokens fail.

**Node.js with passport-azure-ad**: The `audience` parameter in BearerStrategy options must match the Application ID URI. Omitting it or setting it to `null` disables audience validation.

When integrating third-party middleware or writing custom JWT validation, audience validation must be explicitly configured. Libraries often don't enforce it by default; they require the developer to specify the expected audience.

## 🌐 Multi-Audience Tokens

Microsoft Graph tokens have `aud: https://graph.microsoft.com`. Tokens for Azure Resource Manager have `aud: https://management.azure.com`. These are fixed audience values for Microsoft's own services.

For custom APIs, you control the audience through the Application ID URI. A single audience per token is the standard model. There are mechanisms for multi-audience tokens (the v1.0 token endpoint handles audiences differently than v2.0), but for new applications using the v2.0 endpoint, one API per token is the clean implementation.

## ⚠️ The Dangerous Default

Some libraries and tutorials omit audience validation for simplicity in example code. That example code then gets used in production. Regularly audit your resource APIs' JWT validation configuration to confirm audience validation is active and set to the correct value.

The test: acquire a token for a different API and try to use it against your API. If it succeeds, audience validation isn't working.

---

💬 **Have you ever audited your organization's APIs for correct audience validation, and what did you find?** The token confusion vulnerability is more common than it should be, especially in APIs built by teams without OAuth expertise. What's the validation test your team runs to confirm a new API is correctly rejecting tokens not intended for it?
<!-- nav -->

---

[← Token Revocation (Deep Dive)](glossary-11-10-token-revocation-deep-dive.md) | [Home](../README.md) | [Scope (Deep Dive) →](glossary-11-12-scope-deep-dive.md)
