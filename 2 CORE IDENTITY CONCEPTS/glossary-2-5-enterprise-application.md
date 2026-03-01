# Enterprise Applications: What the Portal Is Actually Showing You

**Part of Entra ID Glossary Series: Glossary#2.5 - Enterprise Application**

---

Here's a conversation I've had more times than I can count:

"I went to add an app to Entra ID. I registered it under App Registrations. But then someone told me I also needed to go to Enterprise Applications. And now I see the same app in both places, but they look totally different. What am I actually looking at? Are these the same thing?"

Yes and no. And understanding why is one of the more useful clarity moments in learning Entra ID.

## Enterprise Applications: The Tenant's View of an App

In the last article (Glossary#2.3), we covered service principals — the local instance of an application in your tenant. Enterprise Applications is simply the portal's name for the same thing, presented through a different lens.

When you open Enterprise Applications in the Entra admin center, you're looking at service principal objects in your tenant, organized and surfaced through a management-focused interface. The emphasis is on: who can use this app, what has it been granted, what's the SSO configuration, is it provisioning users?

When you open App Registrations, you're looking at the application object — the global definition of the app, focused on developer configuration: redirect URIs, certificates, API permissions requested, token configuration.

Same underlying app. Two different views, each surfacing different properties for different audiences.

The reason both exist in the portal: App Registrations is for developers configuring *what the app is*. Enterprise Applications is for admins configuring *how the app behaves in their tenant*.

## Three Ways an App Ends Up in Enterprise Applications

Not every app in your Enterprise Applications list was registered by your team.

**Gallery apps** come from Microsoft's application gallery — a library of thousands of pre-integrated SaaS applications. When you add Salesforce, Workday, ServiceNow, or any of the 3,000+ apps in the gallery, Entra ID creates a service principal in your tenant using a pre-configured template. The SSO configuration, attribute mappings, and provisioning schemas are partly pre-built. You configure the tenant-specific details on top.

**Non-gallery apps** are applications you integrate manually — your own custom apps, or third-party apps not in the gallery. You register them (or they're registered elsewhere and you're configuring their service principal in your tenant). Everything is configured from scratch.

**Microsoft's own apps** also appear as service principals. Microsoft Graph, the Microsoft Graph Command Line Tools, Microsoft Teams, Office 365 SharePoint Online — these all have service principals in your tenant. This is normal. They're how Microsoft's own services authenticate and access resources in your organization.

The third category surprises a lot of beginners. If you go to Enterprise Applications and filter for "All Applications," you'll see service principals for dozens of Microsoft services you probably didn't explicitly add. They were created automatically when you enabled various Microsoft 365 services.

## What You Actually Configure in Enterprise Applications

Four main areas drive most of the admin work here:

**Properties** — basic settings like whether the app is enabled, whether it's visible to users in My Apps, and whether user assignment is required. "User assignment required" is a critical toggle: when set to yes, only users and groups explicitly assigned to the app can sign in. When set to no, any user in your tenant can sign in (assuming they have credentials and Conditional Access allows it). Default for gallery apps is typically "no" — which means unless you change it, any employee can access the app the moment you add it to your tenant.

**Users and Groups** — who's been assigned to this application. If user assignment is required (see above), only what's listed here can access the app. This is where you implement app-level access control: this group gets access, that group doesn't.

**Single Sign-On** — the SSO configuration for the app. SAML SSO settings (entity IDs, ACS URLs, attribute claims) are configured here. For OIDC/OAuth2 apps, you'll mostly configure this in App Registrations instead. The portal guides you to the right place.

**Provisioning** — if the app supports SCIM provisioning, you configure it here. This is where you connect Entra ID to an app's user management API so that when you create a user in Entra ID (or add them to a group), an account is automatically created in the app. And when they leave, the account is disabled automatically. This is the real-time version of not having to manually create 2,000 Salesforce accounts.

## A Real Example: Setting Up SSO for a Gallery App

Let me walk through what this looks like in practice for a typical gallery app integration.

You add Salesforce from the gallery. Entra ID creates a service principal. You then:

1. Go to **Single Sign-On**, select SAML, download the Entra ID SAML metadata or copy the certificate and login URLs
2. Give those URLs to the Salesforce admin, who pastes them into Salesforce's SSO configuration
3. Come back to Entra ID, configure the claims mapping — what attributes Entra ID sends to Salesforce and what format they're in
4. Go to **Users and Groups**, assign the groups whose members should have Salesforce access
5. Test with a pilot user
6. Roll out

That's it. Once working, users click Salesforce in My Apps or their browser bookmark, they're authenticated automatically through Entra ID, and they land in Salesforce without typing a password. That's SSO. Enterprise Applications is where you built it. 🔌

---

**Related Terms:**
- Glossary#2.3 - Service Principal (what Enterprise Applications is actually displaying)
- Glossary#9.1 - App Integration (the broader concept of connecting apps to Entra ID)
- Glossary#6.1 - User Provisioning (the automated account creation feature configured in Enterprise Apps)

---

**What apps are you integrating?** Whether it's a standard gallery app or a custom internal tool, the first SSO integration is always memorable. What was yours, and did it go smoothly or were there some surprises along the way?

#EntraID #EnterpriseApplications #SingleSignOn #SSO #IdentityManagement #MicrosoftEntra #CloudSecurity
