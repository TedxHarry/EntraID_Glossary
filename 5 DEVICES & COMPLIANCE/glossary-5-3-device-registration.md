# Device Registration
*Three Ways to Join a Device to Entra ID (They're Not the Same)*

> **Difficulty:** 🟡 Intermediate

📚 Part of Entra ID Glossary Series #5.3 - Device Registration

---


An admin asked me why a Conditional Access policy was blocking a user's device. The policy required "Hybrid Entra Joined" devices, and the device showed "Entra Registered" in the portal. The admin thought registered and joined were the same thing with different labels.

They're not. They represent different relationships between the device and Entra ID, with different security properties, different use cases, and different levels of corporate control.

## 🗺️ The three registration types

**Entra Registered** (formerly Azure AD Registered) is the lightest touch. The device is personal: the employee's own phone or laptop, or a shared device. The user registers their own account on the device to get access to work resources. The organization doesn't own or fully manage the device.

What this gives you: Entra ID knows the device exists. The user can access apps that allow registered devices. Single sign-on works on the device for apps in scope.

What this doesn't give you: The organization doesn't control the device configuration. Compliance policies aren't typically enforced. Conditional Access policies requiring "joined" devices will not be satisfied.

**Entra Joined** (formerly Azure AD Joined) is for cloud-first corporate devices. The device is owned by the organization, joined directly to Entra ID, and Entra ID is the authority. No on-premises Active Directory is required or involved.

What this gives you: Full organizational control through Intune. SSO to cloud resources. Conditional Access policies requiring "joined" devices are satisfied. Windows Hello for Business is available. Users sign in with their work account.

What this doesn't give you: Native access to on-premises resources that require Kerberos (like on-premises file shares or legacy applications). You can work around this with Cloud Kerberos Trust or VPN, but it requires additional configuration.

**Hybrid Entra Joined** is for organizations running both on-premises Active Directory and Entra ID. The device is domain-joined to on-premises AD and simultaneously registered with Entra ID. It has an identity in both systems.

What this gives you: Access to both on-premises resources (via Kerberos from domain membership) and cloud resources (via the Entra ID device identity). Single sign-on works across both environments. Satisfies the most restrictive device-based Conditional Access policies.

What this doesn't give you: Simplicity. Hybrid join requires Entra Connect synchronization, careful configuration, and troubleshooting skills for when the sync breaks or devices get into an inconsistent state.

## 🔄 Which to use

| Scenario | Right Choice |
|----------|-------------|
| Employee's personal device for email access | Entra Registered |
| New cloud-first corporate laptop | Entra Joined |
| Existing corporate Windows PCs already domain-joined | Hybrid Entra Joined |
| Organization migrating gradually from on-premises | Hybrid Entra Joined during transition, Entra Joined as target |
| Organization fully cloud, no on-premises AD | Entra Joined |

## 🔐 Registration vs enrollment

Registration (any of the three types above) creates a device identity in Entra ID. It does not automatically enroll the device in Intune for full management.

Enrollment in Intune is a separate step that enables compliance policy evaluation, configuration profiles, app deployment, and remote management. An Entra Joined device that isn't enrolled in Intune won't report compliance state. Conditional Access policies requiring "compliant device" will block it.

For corporate devices, both registration/join AND Intune enrollment are typically required. For personal devices using the Entra Registered model, Intune enrollment is optional and often replaced by app protection policies that manage the application rather than the device.

## ⚠️ The hybrid join troubleshooting reality

Hybrid join is the most powerful option and the most complex to maintain. The `dsregcmd /status` command on a Windows device shows its current registration state and is the first diagnostic step when something looks wrong:

```
AzureAdJoined: YES
DomainJoined: YES
```

Both YES means hybrid joined. If AzureAdJoined is NO but DomainJoined is YES, the device is domain-joined but not yet registered with Entra ID, which means the Entra Connect sync hasn't processed it, or the automatic registration process failed.

---

💬 **Has your organization gone through a device registration migration, moving from Hybrid Entra Joined toward Entra Joined as you reduced on-premises dependencies?** The transition involves more than just joining devices differently. What were the on-premises dependencies that took the longest to resolve?
✍️ TedxHarry

<!-- nav -->

---

[← Device Identity](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-2-device-identity.md) | [🏠 Contents](/README) | [Device Enrollment →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-4-device-enrollment.md)
