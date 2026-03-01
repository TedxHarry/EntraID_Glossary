# Service Principal
*The Most Misunderstood Object in Entra ID*

**Part of Entra ID Glossary Series: Glossary#2.3 - Service Principal**

---

Of all the concepts I explain to people learning Entra ID, service principals generate the most confused looks. Not because the idea is actually complicated — once you have the right mental model, it clicks quickly. The problem is that most explanations start in the wrong place.

Let me start in the right place.

## The Question That Always Comes First

"I registered an app in Entra ID. Now I see it in App Registrations. But I also see something in Enterprise Applications with the same name. What's the difference? Did I create two things?"

Yes. You created two things. Deliberately. And they serve different purposes.

Here's the mental model that makes this make sense.

## Think About a Franchise

McDonald's has one master recipe for a Big Mac. One formula, documented centrally, owned by corporate headquarters. But there are 40,000 McDonald's locations around the world, and each one makes that Big Mac. The recipe is the same everywhere — but the restaurant is local, operating in a specific city, with its own staff, its own cash register, its own local health inspection records.

An **App Registration** is the master recipe. It's the global definition of your application: what it's called, what permissions it needs, what redirect URIs it uses, what certificates it has. One App Registration, owned in one tenant — the tenant where the developer registered the app.

A **Service Principal** is the local restaurant. When your app is used in a tenant — either your own tenant or someone else's — Entra ID creates a service principal in that tenant. The service principal is the local instance of the app's identity. It's where the tenant-specific configuration lives: which users can access the app, what permissions have been granted in this tenant, whether admin consent has been given.

One App Registration. Potentially many service principals — one per tenant the app appears in.

## The Three Types of Service Principals

Not all service principals come from app registrations you created. Entra ID creates them in three scenarios:

**Type 1: Application service principals.** Created when an app is registered or when a multi-tenant app is added to a tenant. This is the "app instance" kind — the one that represents your registered application.

**Type 2: Managed identity service principals.** When you enable a managed identity on an Azure resource (a VM, a Function App, an App Service), Entra ID creates a service principal for it. You don't manage the credentials — Azure does. The service principal is how you grant that managed identity access to other resources.

**Type 3: Legacy service principals.** Some older Microsoft services and third-party apps created service principal-like objects that don't have a corresponding app registration in the traditional sense. You'll encounter these when auditing older tenants. Don't worry about these too much as a beginner — just know they exist.

## What a Service Principal Actually Controls

In your tenant, the service principal for an application is where the real governance happens. Several things live on the service principal rather than the app registration:

**Permission grants.** When an admin clicks "Grant admin consent" for an app, that consent is recorded on the service principal in their tenant. The app registration might say "I need User.Read.All" — but whether that permission has been granted in your tenant is tracked on the service principal.

**User assignment.** You can configure an app so that only specific users or groups can access it (user assignment required = yes). The list of who's assigned is stored on the service principal.

**Sign-in configuration.** Properties like whether the app is enabled, what the sign-in audience is, and SAML configuration for SSO are configured at the service principal level in your tenant.

**Conditional Access targeting.** When you write a Conditional Access policy that targets a specific application, you're targeting the service principal in your tenant.

## Why This Matters in Real Troubleshooting

The app registration / service principal split causes confusion when things go wrong. Here's a scenario I've seen several times:

Developer registers an app. Configures API permissions in the app registration — looks fine. But users are getting "unauthorized" errors when the app tries to call Microsoft Graph. The app registration shows the permissions listed correctly.

The problem: the permissions in the app registration are a *request*. Whether they're actually granted depends on the service principal in the tenant — specifically, whether admin consent was given there. The app registration and the service principal are separate. Both have to be right.

Finding service principals is straightforward: in the Entra admin center, go to Enterprise Applications and search by the application's display name or the Object ID. You can also use Microsoft Graph or PowerShell (`Get-MgServicePrincipal`) to query them directly, which gives you much richer detail than the portal UI. 🔧

---

**Related Terms:**
- Glossary#2.1 - Identity (service principals are a type of identity)
- Glossary#2.5 - Enterprise Application (the portal view of an app's service principal)
- Glossary#10.2 - Managed Identity (a type of service principal managed by Azure)

---

**Your experience:** Has the app registration vs. service principal distinction tripped you up before? The "I configured permissions but the app still doesn't work" problem is one of the most common Entra ID support scenarios. Drop your troubleshooting story below.
<!-- nav -->

---

[← User (Identity Object)](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-2-user-identity-object.md) | [🏠 Contents](/README) | [Group →](/2%20CORE%20IDENTITY%20CONCEPTS/glossary-2-4-group.md)
