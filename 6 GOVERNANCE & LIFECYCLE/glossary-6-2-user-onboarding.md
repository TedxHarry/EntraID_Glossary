# User Onboarding
*The First Day Experience Is an Identity Problem*

📚 **Part of Entra ID Glossary Series: Glossary#6.2 - User Onboarding**

---

I asked a group of IT professionals at a conference to raise their hands if a new employee had ever started and couldn't do meaningful work on their first day because they didn't have the right access.

Every hand went up.

Then I asked how many of them had a documented, automated onboarding process. About a third kept their hands up. For the other two-thirds, onboarding was a mix of tickets, tribal knowledge, and hoping the right people had been looped in.

User onboarding is fundamentally an identity problem. Getting someone's access right from day one requires getting their identity right first.

## 🧩 What Onboarding Actually Involves

Onboarding isn't a single action. It's a sequence of identity and access operations that have to happen in the right order:

**1. Identity creation** 🆔: The user object is created in Entra ID (manually by IT, or automatically from an HR system via inbound provisioning). This is the foundation everything else depends on.

**2. License assignment** 📄: Microsoft 365 licenses, Entra ID P1/P2 licenses, and any other subscription-based services need to be assigned before the user can access the corresponding services.

**3. Group membership** 👥: Adding the user to the right Entra ID groups determines which applications they can access, which Conditional Access policies apply, which Intune profiles they receive, and which email distribution lists include them.

**4. Application access** 📱: For apps using provisioning, group membership triggers automatic account creation. For apps not using provisioning, manual accounts need to be created in each system.

**5. MFA registration** 🔐: The user needs to register their authentication methods (phone number, authenticator app, FIDO2 key) before they can satisfy MFA requirements. If they can't register on day one, they may be blocked from apps that require MFA.

**6. Device setup** 💻: The device the user works from needs to be enrolled in Intune (or already be enrolled via Autopilot), join Entra ID, and pass compliance checks before device-based Conditional Access policies allow access.

## 🔄 The Automation Gap

The difference between a smooth first day and a frustrating one is how many of these steps happen automatically versus requiring human action.

**Best case (fully automated)**:
- HR creates the employee record in Workday
- Inbound provisioning creates the Entra ID account automatically
- License group assignment triggers license provisioning
- Department or role group membership triggers app provisioning to all required applications
- Autopilot handles device enrollment with no IT intervention
- User registers MFA from their smartphone before day one via a temporary access pass

**Common reality (partially manual)**:
- IT creates the Entra ID account manually from an HR ticket (delay if ticket arrives late)
- IT assigns licenses manually
- Someone sends an email to the helpdesk to create the Salesforce account (a 2-3 day queue)
- The user arrives to find their laptop isn't ready
- They try to register MFA but their phone number wasn't entered during account creation

## ♻️ ⏰ Lifecycle Workflows: Automating the Sequence

Microsoft Entra Lifecycle Workflows allow organizations to define automated task sequences triggered by identity events. For onboarding, a "Joiner" workflow can:

- Trigger when a new user is created (or when their hire date approaches)
- Automatically generate a Temporary Access Pass for MFA registration
- Send a welcome email with access instructions
- Add the user to appropriate groups
- Trigger manager notifications

The workflow runs at a defined time before the hire date (often 2 or 3 days prior) so that by the user's actual start date, most access is already in place.

## 💡 The Manager's Role

One of the most reliable inputs for onboarding automation is the manager attribute on the user object. If the new hire's manager is set correctly, workflows can:

- Notify the manager to approve access requests
- Apply the same base group memberships the manager's team has
- Route device shipment to the manager's office location

Manager-driven onboarding reduces IT involvement in access decisions and puts those decisions with the person who actually knows what the new hire needs.

---

💬 **What's the single biggest friction point in your organization's current onboarding process?** The gap between "user created in Entra ID" and "user can do their job" is where most first-day frustration lives. Whether it's MFA registration, device provisioning, or app access, the bottleneck is usually the same for months until someone fixes it.
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← User Provisioning](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-1-user-provisioning.md) | [🏠 Contents](/README) | [User Offboarding →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-3-user-offboarding.md)
