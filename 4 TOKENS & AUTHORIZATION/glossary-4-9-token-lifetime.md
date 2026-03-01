# Token Lifetime
*The Trade-Off Between Security and Not Annoying Your Users*

📚 **Part of Entra ID Glossary Series: Glossary#4.9 - Token Lifetime**

---

A security team I worked with wanted access tokens to expire every 15 minutes. Their reasoning was solid: shorter lifetime, less time for a stolen token to be useful. Hard to argue with.

The developers on the same project had a different view. Their app made API calls frequently. Every 15 minutes, every active user would get a silent token refresh in the background. At 5,000 concurrent users, that's thousands of simultaneous token requests every quarter hour. The token endpoint becomes a bottleneck. And if a refresh fails silently, the user gets kicked out mid-task.

Both teams were right. Token lifetime is a genuine trade-off, not a setting you just make as small as possible. Understanding the defaults, the levers, and the modern approach (CAE) helps you find a configuration that works for both security and users.

## 🎫 ⏱️ The Default Token Lifetimes

Entra ID ships with these defaults:

**Access tokens:** 60 minutes (3,600 seconds). This is the token you present to APIs. It's a JWT with a hard expiry embedded in the `exp` claim. Once expired, it's rejected by resource servers. There is no way to extend an expired access token; the application must get a new one.

**ID tokens:** Also 60 minutes. Same mechanism, same expiry model.

**Refresh tokens:** Up to 90 days of inactivity. As long as the refresh token is used at least once within the 90-day window, it stays valid. Each use resets the clock. Some flows and some policies apply a hard maximum lifetime on top of this.

**Session tokens (browser cookies):** The persistent session cookie that keeps users signed in across browser sessions defaults to 90 days when "Keep me signed in" is selected, less if the user doesn't select it or if Conditional Access sign-in frequency is configured.

## 🔧 Configurable Token Lifetime Policies

Before Conditional Access got sign-in frequency controls, there was a Token Lifetime Policy: a configurable object you could assign to service principals to override default lifetimes per application.

Today, Microsoft recommends against using Token Lifetime Policies for access and ID tokens. Instead:

- 🎛️ **Sign-in frequency in Conditional Access:** Controls how often users must re-authenticate interactively. This is the right lever for controlling session duration. You can scope it per application, per user group, per location, or per device compliance state.

- 🔐 **Persistent browser session:** A Conditional Access setting that controls whether the persistent session cookie ("keep me signed in") is issued at all.

Token Lifetime Policies still work for refresh tokens and session tokens for specific scenarios, but the Conditional Access approach is more flexible and consistent.

## ⚡ CAE: The Modern Solution to the Lifetime Trade-Off

Continuous Access Evaluation (CAE) changes the economics of token lifetime in a meaningful way.

The problem with long-lived tokens has always been: if something changes (user disabled, risk detected, device non-compliant), the access token remains valid until it naturally expires. With a 60-minute lifetime, that's up to 60 minutes of continued access after the account should have been blocked.

CAE solves this by enabling near-real-time token revocation for supported services. When Entra ID detects a revocation event (user disabled, password changed, location policy violated), it pushes a notification to capable resource servers (Exchange Online, SharePoint, Teams, Microsoft Graph). Those services start rejecting the existing access token immediately, not at expiry.

Because CAE provides real-time enforcement, Entra ID can safely issue longer-lived access tokens (up to 24 hours) to CAE-capable services. The service will revoke them promptly if needed, so the long lifetime doesn't create the exposure it otherwise would.

The practical result: users get longer sessions with fewer interruptions. Security teams get near-real-time enforcement of policy changes. The 15-minute vs 60-minute debate becomes less relevant when the token can be revoked in seconds if circumstances change.

## 💡 What to Configure in Practice

**For most standard applications:**
Leave access token lifetime at the default 60 minutes. Use Conditional Access sign-in frequency to set how often interactive re-authentication is required (daily for lower-risk apps, every 8 hours for higher-risk ones).

**For privileged access scenarios:**
Use Conditional Access sign-in frequency to require re-authentication every 1-4 hours. Combine with PIM activation windows so admin access is time-limited at the role level too.

**For applications supporting CAE:**
Tokens can extend to 24 hours safely. The main Microsoft 365 services already support CAE. Custom applications can implement CAE support using the CAE client capabilities flag.

**Don't try to achieve security through very short lifetimes alone.** Fifteen-minute tokens that aren't backed by real-time revocation still leave a 15-minute window. CAE with 24-hour tokens leaves a near-zero window on supported services.

---

💬 **Has token lifetime configuration caused friction in your environment?** Users complaining about sign-out frequency, developers complaining about token refresh load, or security teams pushing for shorter lifetimes than is practical? What compromise did you land on?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Bearer Token](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-8-bearer-token.md) | [🏠 Contents](/README) | [Token Revocation →](/4%20TOKENS%20%26%20AUTHORIZATION/glossary-4-10-token-revocation.md)
