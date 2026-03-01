# Access Request: The User's Side of the Access Conversation

**Part of Entra ID Glossary Series: Glossary#6.10 - Access Request**

---

A developer needed read access to the production logs for a service she'd been assigned to debug. She knew the resource existed. She didn't know who owned it, which team managed the Entra ID group controlling access, or how to submit the right request to the right person.

She spent 45 minutes sending emails and Teams messages before someone pointed her to the correct process. The access itself was granted in 10 minutes once she reached the right approver.

The bottleneck wasn't the approval. It was the request: not knowing where to go, who to ask, or how to ask.

Access request is the process users follow to formally request access to resources they don't currently have. Getting this right is as much about user experience as it is about governance.

## 📬 What an Access Request Is

An access request is a formal expression of need: "I need access to this resource, for this reason, for this long." It initiates an approval and provisioning workflow and creates an auditable record of why access was granted.

Access requests exist because not all access should be available to everyone automatically. Resources with sensitive data, privileged capabilities, or compliance implications require a human decision before access is granted. The request-and-approve model is how that decision gets made systematically.

Without a formal request process, access is granted informally: "Can you just add me to the group?" "Can you ask the SharePoint admin to give me access?" These ad-hoc requests bypass the approval record and make audit evidence impossible to produce.

## 🖥️ The My Access Portal

In Microsoft Entra ID Governance, users submit access requests through the My Access portal at `myaccess.microsoft.com`. This portal shows:

- **Available access packages**: Resources the user is eligible to request, based on their user attributes and the package policies configured for their population
- **My access**: Access they currently have, with expiration dates and renewal options
- **My requests**: History of requests they've submitted, with current status

The user browses available packages, selects what they need, writes a business justification, and submits. They receive a confirmation. Approvers receive notifications. Status updates arrive by email as the request moves through the workflow.

## 📋 What Makes a Good Access Request Process

**Discoverability** 🔍: Users can only request access they know exists. Access packages need descriptive names and descriptions that match how users think about their work, not how IT thinks about the resources. "Finance Team SharePoint and Distribution List" is more discoverable than "FIN-SP-DIST-ACCESS-GRP."

**Business justification** 📝: Requiring a justification improves request quality and gives approvers context. A justification of "need for my project" is weak. "Auditing Q3 vendor invoices for the procurement review" gives the approver enough context to approve confidently or ask a follow-up question.

**Appropriate scope** 🎯: Access packages that bundle too many resources into one request make approvers uncomfortable approving the whole thing when they'd be fine with part of it. Packages scoped to a coherent business use case (rather than "everything this team uses") have higher approval rates and better security properties.

**Clear expiration** ⏱️: Requests for time-limited access (a project, a contract engagement, a temporary coverage role) should specify an end date. This prevents indefinite access accumulation and removes the need for a later review to clean up.

## 🔄 What Happens After the Request

After submission:

1. Approvers receive email notifications with the request details and justification
2. Each approver stage has a configured response window (typically 14 days)
3. Approvers approve, deny, or request more information
4. If all approval stages pass, access is granted automatically
5. The user receives a confirmation with the access details
6. If the package has an expiration, the access has an end date set automatically

If an approver doesn't respond within the configured window, the policy's timeout behavior applies: the request can be automatically approved, automatically denied, or escalated to an alternate approver.

## ⚠️ Requests That Fall Outside Packages

Not every access need fits into a pre-configured package. When a user needs something not available through My Access, they still need a path to request it. The options:

- IT ticket for manual processing (the traditional route)
- Self-service group joining if the group allows self-service membership
- Requesting a new access package be created (admin workflow)

The goal isn't to eliminate all IT involvement in access requests. It's to automate the common cases so IT capacity goes to the unusual cases that genuinely need judgment.

---

💬 **How do users in your organization currently request access to resources they don't have?** The mix of "send IT a ticket," "ask your manager to add you to the group," and "message the resource owner on Teams" is the standard starting point for most organizations. What's been the biggest driver toward a more structured request process?

#EntraID #AccessRequest #EntitlementManagement #IdentityGovernance #MicrosoftEntra #MyAccess #SelfServiceIT
