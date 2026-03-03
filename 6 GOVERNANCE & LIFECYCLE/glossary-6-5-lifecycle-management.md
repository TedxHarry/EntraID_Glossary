# Lifecycle Management
*Identity Automation for the Entire Employee Journey*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #6.5 - Lifecycle Management

---


A CISO told me her organization spent roughly 3 hours of IT staff time per new hire on access setup, and another 2 hours per departure on access removal. With 400 hires and departures per year, that was 2,000 hours of manual identity work annually.

She also told me they'd had two security incidents in the past 18 months where a former employee had accessed systems after their departure. Both traced back to steps that were missed in the manual offboarding process.

The problem wasn't people failing to do their jobs. It was asking people to execute a complex multi-step process consistently, under time pressure, for hundreds of events per year. Lifecycle management is what happens when you replace that dependency with automation.

## 🔄 The joiner-mover-leaver model

Identity lifecycle management organizes the events an employee goes through into three categories:

**Joiner** 🟢: A new person enters the organization. Account creation, license assignment, group membership, application provisioning, device enrollment, MFA registration, access to role-appropriate resources. All of this needs to happen before day one.

**Mover** 🔵: An existing person changes roles, departments, locations, or employment type. Access that fit their old role needs to be removed. Access appropriate for their new role needs to be added. Groups, app assignments, and permissions all need to be reconciled.

**Leaver** 🔴: A person leaves the organization. All access must be revoked: account disabled, sessions invalidated, app accounts deprovisioned, devices wiped, data transferred to appropriate owners.

The Mover event is the one organizations most often handle inconsistently. Joiners get attention because the new hire experience is visible. Leavers get attention because security incidents happen when they're missed. Movers accumulate access over time (getting new access for each new role without removing old access) and become over-privileged over years.

## ⚙️ Microsoft entra lifecycle workflows

Entra ID's Lifecycle Workflows feature lets organizations define automated task sequences that trigger on identity events. These are pre-built automatable steps, configured in the Entra admin center, that run against user accounts meeting defined criteria.

**Built-in tasks available**:
- Generate Temporary Access Pass (for pre-day-one MFA registration)
- Send welcome email to new hire
- Send email to user's manager
- Add user to groups
- Assign licenses
- Disable user account
- Delete user account
- Remove all group memberships
- Revoke all sign-in sessions

**Triggers available**:
- Days before employment start date (Joiner: prepare 2 days before hire date)
- Employment start date
- Days after employment end date (Leaver: cleanup 1 day after departure)
- Employee type or department change (Mover: triggers when attributes change)

A Joiner workflow might run 2 days before hire date, generate a Temporary Access Pass, email it to the new hire with setup instructions, add them to department groups, and notify their manager. All automated, triggered by the hire date attribute on the user object.

## 🔗 HR system integration

The most mature lifecycle management implementations start with the HR system as the source of truth.

**Inbound provisioning** from HR (Workday, SuccessFactors, BambooHR) to Entra ID means:
- New hire in Workday → Entra ID account created automatically
- Termination in Workday → Entra ID account disabled automatically
- Department transfer in Workday → Entra ID attributes updated automatically

When HR drives Entra ID, and Entra ID drives app provisioning, the entire Joiner-Mover-Leaver cycle becomes HR-triggered. IT doesn't need to receive a ticket, create an account, or remember to run an offboarding checklist. The HR event is the trigger for everything downstream.

## ⚠️ What still needs human judgment

Automation handles the routine lifecycle events well. It doesn't replace judgment for:

- Access that's role-appropriate but not automatically assigned by group membership
- Exceptions where a specific person needs broader access than their role group provides
- Leaver scenarios where transferred data ownership needs a human decision
- Mover scenarios where the new role requires access the automation doesn't know about

The goal isn't to remove humans from access decisions. It's to remove humans from the routine, repeatable execution steps so they can focus on the decisions that actually need judgment.

---

💬 **Has your organization automated any part of the Joiner-Mover-Leaver cycle, and what was the first process you tackled?** The decision about where to start often comes down to where the most pain is: missed offboardings that create security risk, or slow onboarding that creates first-day frustration. Which drove your first automation investment?
✍️ TedxHarry


> 🔑 **Licensing:** Lifecycle Workflows require **Entra ID Governance** or **Entra ID P2**. Basic lifecycle (create/disable users) is available in Entra ID Free.

<!-- nav -->

---

[← Deprovisioning](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-4-deprovisioning.md) | [🏠 Contents](/README) | [Access Review →](/6%20GOVERNANCE%20%26%20LIFECYCLE/glossary-6-6-access-review.md)
