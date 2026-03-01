# Hybrid Device
*The Device That Lives in Both Worlds*

📚 **Part of Entra ID Glossary Series: Glossary#5.9 - Hybrid Device**

---

An organization with 8,000 Windows desktops asked me how long their cloud migration would take. They wanted all devices eventually cloud-managed, no on-premises dependencies. I told them the device migration alone would be 18 to 24 months, minimum.

The reason wasn't technical complexity in the join process itself. It was the on-premises dependencies those devices had: legacy applications that required Kerberos, file shares that only worked from the domain, line-of-business software that authentication against the local domain controller. Until those were resolved or replaced, they needed devices that could authenticate both ways.

That's what Hybrid Entra Joined devices are for: organizations that need both.

## 🔗 What Hybrid Entra Joined Means

A Hybrid Entra Joined device is registered with two identity systems simultaneously:

- **On-premises Active Directory**: Traditional domain membership. The device can obtain Kerberos tickets and authenticate to on-premises resources.
- **Microsoft Entra ID**: Cloud device identity. The device can authenticate to cloud services and satisfy device-based Conditional Access policies.

The device has an identity in both directories. On-premises domain controller sees it as a member computer. Entra ID sees it as a joined device. Users on that device get SSO to both on-premises and cloud resources.

## ⚙️ How Hybrid Join Is Set Up

Hybrid join requires Entra Connect (or Cloud Sync in newer configurations) to synchronize device objects from on-premises AD to Entra ID.

The technical flow:
1. Device is domain-joined to on-premises Active Directory (standard domain join)
2. An automatic registration process runs on the device (via scheduled task or Group Policy)
3. The device registers with Entra ID and a device object is created
4. Entra Connect syncs the device object from on-premises AD to Entra ID
5. Entra ID issues a Primary Refresh Token (PRT) for the device

When this works, `dsregcmd /status` on the device shows both `DomainJoined: YES` and `AzureAdJoined: YES`.

When it doesn't work (and hybrid join has more failure modes than Entra Join), `dsregcmd /status` is the first diagnostic tool. The error codes it returns point to whether the failure is in the registration process, the Entra Connect sync, or the token issuance.

## 🔐 The Primary Refresh Token

The PRT is the mechanism that makes SSO work on Hybrid Entra Joined (and Entra Joined) Windows devices. It's a special long-lived token issued to the device that represents both the device's identity and the signed-in user's identity.

When a user opens a browser or an app that uses modern authentication, the device presents the PRT to Entra ID and silently gets an access token. No interactive sign-in prompt. The SSO experience comes from this token, not from a browser cookie.

If the PRT is missing or expired, users get prompted to sign in to apps that should be SSO-seamless. The most common cause: the automatic registration process failed and the device never got a PRT in the first place.

## ⚠️ Common Hybrid Join Problems

**Inconsistent registration state**: Some devices in a batch are hybrid joined, others aren't, even with identical configuration. Usually caused by the automatic registration process failing silently on some machines. The fix: check scheduled task status (`Task Scheduler > Microsoft > Windows > Workplace Join`).

**"JoinType: Unknown"**: The device is domain-joined but the Entra ID registration hasn't completed. Either Entra Connect hasn't synced the device yet (up to 30-minute lag), or the registration scheduled task hasn't run.

**Certificate issues**: Hybrid join uses a device certificate. If the enterprise certificate authority isn't configured correctly for auto-enrollment, devices can't obtain the certificate needed for registration.

**Firewall blocking registration endpoints**: The registration process calls Entra ID endpoints. Proxy configurations or firewall rules blocking `login.microsoftonline.com` or `device.login.microsoftonline.com` silently break the registration.

## 💡 Hybrid Join as a Transitional State

Most modern guidance treats Hybrid Entra Joined as a transitional state rather than a long-term target. The end goal for most organizations is Entra Joined: cloud-only management, no on-premises domain dependency.

Getting there requires eliminating on-premises dependencies app by app. Once those are gone, new devices get Entra Joined. Existing devices get migrated as they're replaced. The fleet transitions over a refresh cycle.

---

💬 **Is your organization running hybrid joined devices as a permanent state or as a transitional step toward cloud-only?** The on-premises dependencies that force hybrid join are often the same ones driving the broader cloud migration timeline. Which legacy apps or services have been the hardest to move away from?
> ✍️ *Written by **TedxHarry***

<!-- nav -->

---

[← Device Trust](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-8-device-trust.md) | [🏠 Contents](/README) | [App Protection Policy →](/5%20DEVICES%20%26%20COMPLIANCE/glossary-5-10-app-protection-policy.md)
