# Actor: The Application in the Token, and Why It Matters

**Part of Entra ID Glossary Series: Glossary#4.14 - Actor**

---

A user called to say emails were being sent from her account without her knowledge. The sign-in logs showed nothing suspicious. Her password hadn't changed. No alerts had fired.

When I looked at the token details in the audit logs for those email sends, the picture was clear: a third-party app she'd authorized months earlier. The app had `Mail.Send` delegated permission. She'd consented during an initial setup. The emails were technically authorized. But she'd forgotten she'd done it, and the app had been sending marketing emails on her behalf ever since.

The actor claim in the token identified the responsible party immediately. Without it, the investigation would have taken much longer.

## 🎭 What "Actor" Means in OAuth

In OAuth 2.0, the actor is the application making the request. When a user authenticates and an application gets a delegated token, there are two parties encoded in that token:

- The **subject** (`sub`/`oid`): the user whose resources are being accessed
- The **actor**: the application doing the accessing

In Entra ID access tokens, these actor-related claims appear on every delegated token:

**`appid`** (v1.0 tokens) / **`azp`** (v2.0 tokens): The client ID of the application that requested the token. This is the actor. This is which application is making the API calls.

**`appidacr`** / **`azpacr`**: How the application authenticated. `0` means public client, no secret. `1` means client secret. `2` means certificate. Higher values indicate stronger application authentication. A `0` here means anyone who can run the app code can request tokens with it.

## 🔍 Why Audit Logs Use Actor

When a user's calendar is read, files downloaded, or email sent, the audit log entry includes two identities: the subject (whose resource was affected) and the actor (which application made the call).

This combination answers the question: "did the user do this directly, or did an application do it on their behalf?"

In the email investigation: audit logs showed the user as subject and the third-party app as actor. Both pieces of information were necessary. The user's identity confirmed whose mailbox was involved. The actor confirmed it wasn't the user sitting at a keyboard; it was an application calling the Graph API.

For security investigations, the actor claim is often the first thing to check when something looks wrong. Users can be compromised, but they can also be falsely accused of actions taken by an application they long since forgot they authorized.

## 🔗 Actor in the On-Behalf-Of Flow

The On-Behalf-Of (OBO) flow adds explicit actor semantics. In OBO:

1. A user authenticates to API A
2. API A needs to call API B's endpoint to fulfill the request
3. API A exchanges the user's token for a new token to call API B
4. The resulting token shows: subject is the original user, actor is API A

This creates an auditable chain. API B can verify not just that the user has permission, but that the intermediate service (the actor) was legitimately authorized to participate in the request. Each hop in a service-to-service call chain can be traced.

## 📋 Reading Actor Information in Practice

For anyone reviewing tokens or audit logs, the actor information is in these places:

| Location | Field | What It Shows |
|----------|-------|---------------|
| Access token (v2.0) | `azp` | Client ID of the requesting app |
| Access token (v2.0) | `azpacr` | How the app authenticated |
| Entra audit logs | Initiated by | Application name and ID |
| Sign-in logs | Client application | The app that initiated sign-in |

When investigating unexpected access, the first check is always: what was the actor? Which application made this call? Was that application authorized to do so? Did the user actually consent to that permission?

## ⚠️ Application-Only Tokens

For daemon applications using client credentials (no user), there is no separate subject and actor. The application is both. The `oid` in the token belongs to the service principal. The actor and the subject are the same entity.

APIs that accept both delegated and application tokens need to handle this distinction. The presence of a `scp` claim confirms a user is in context. The presence of a `roles` claim (and absence of `scp`) confirms it's an application acting alone.

---

💬 **Have you investigated suspicious activity and found it was an authorized application doing something the user had forgotten they'd consented to?** It's one of the more common sources of unexpected access events. How does your organization track which apps users have granted permission to?

#EntraID #OAuth2 #Actor #AppSecurity #AuditLogs #MicrosoftEntra #CloudSecurity
