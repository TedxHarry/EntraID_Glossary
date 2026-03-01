# Audience
*The Token Knows Who It Was Meant For*

> **Difficulty:** 🔴 Advanced

📚 **Part of Entra ID Glossary Series: Glossary#4.12 - Audience**

---

## 🎯 TL;DR

- The audience (`aud` claim) in a token specifies which API the token is valid for
- Tokens for Microsoft Graph have `aud: https://graph.microsoft.com`; your API should validate its own audience
- Accepting tokens with the wrong audience is a critical security vulnerability


A team had built two internal APIs. Both used Entra ID for authentication. During a security review, a developer noticed something: a token acquired for API A, when passed to API B, was sometimes accepted.

The investigation started with one question: were these APIs validating the audience claim?

They weren't. Tokens issued for one service were being accepted by another. The boundary that audience validation creates simply didn't exist.

## 🎯 What the Audience Claim Is

Every access token contains an `aud` (audience) claim. Its value identifies who the token was issued for: specifically, which resource server is meant to consume it.

A token issued for Microsoft Graph has `aud: https://graph.microsoft.com`. A token issued for your custom API has `aud` set to that API's application ID URI, something like `api://your-api-client-id`. An ID token (for the application itself, not an API) has `aud` set to the client application's ID.

The resource server consuming the token must validate that the `aud` claim matches its own identifier. If it doesn't match, the token must be rejected. Not logged and allowed through. Rejected.

## 🔒 Why Audience Validation Matters

Access tokens are bearer tokens. Whoever holds one can present it. If APIs don't validate audience, a token issued for one service can be used against any other service that accepts tokens from the same issuer.

This creates a cross-service escalation path. If an attacker obtains a token your app legitimately acquired for a low-sensitivity API, and your higher-sensitivity APIs don't check audience, that same token might work against them too.

In the scenario from the security review: API B was less sensitive than API A. The developers assumed that was fine because attackers couldn't get tokens for API A without appropriate permissions. What they'd missed: any valid token from the issuer could potentially work against both, because neither was checking who it was actually meant for.

Entra ID does its part correctly. It issues tokens with specific, appropriate audience values and signs them. The validation responsibility then falls entirely on the API consuming the token.

## 📋 What Correct Audience Validation Looks Like

For a custom API built on ASP.NET Core using `Microsoft.Identity.Web`:

```csharp
builder.Services.AddAuthentication(JwtBearerDefaults.AuthenticationScheme)
    .AddMicrosoftIdentityWebApi(builder.Configuration.GetSection("AzureAd"));
```

With the right configuration (audience set to your API's application ID URI in appsettings.json), the library validates the `aud` claim automatically on every request. The audience value in configuration must match exactly what Entra ID puts in the token.

For APIs in other languages and frameworks, MSAL and standard OpenID Connect libraries handle this as part of token validation. The key is ensuring the expected audience value is explicitly configured, not left as a wildcard or empty.

## ⚠️ The Dangerous Pattern to Avoid

The dangerous configuration is: "accept any valid token from this issuer."

That's signature validation, not audience validation. Signature validation confirms the token was legitimately issued by Entra ID. Audience validation confirms it was issued for you specifically.

An API that validates signatures but not audience is like a nightclub that checks whether an ID is genuine but doesn't check whether the person is old enough. The check exists. It just doesn't check the right thing.

## 🔍 Multi-Audience Scenarios

Some APIs legitimately need to accept tokens with different audience values, for example during a migration where an API has a new application ID but must still accept tokens issued for the old one, or when the same API serves multiple environments.

In these cases, the validation should check against an explicit allowlist of expected audience values. Not skip validation. Not accept any audience. An explicit list of the values that are legitimately valid for this specific API.

## 💡 Testing Your Audience Validation

If you're reviewing an existing API, three checks matter:

- 🔍 Does the validation middleware have an explicit audience configured?
- 🔍 Is that audience value the API's application ID URI (not the client app's ID)?
- 🔍 Have you tested with a token issued for a different audience and confirmed you get a 401?

That last test is the one most teams skip. Testing the happy path confirms the API accepts valid tokens. Testing with a valid-but-wrong-audience token confirms it actually enforces the boundary. Both tests are necessary.

---

💬 **Have you built or reviewed an API and found the audience validation was missing or misconfigured?** It's a subtle check that's easy to skip when you're focused on getting the happy path working. What does your team's API security review checklist cover?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Scope](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-11-scope.md) | [🏠 Contents](/README) | [Authorization Grant →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-13-authorization-grant.md)
