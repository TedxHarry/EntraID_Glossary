# Device State: The Real-Time Health Signal That Drives Access Decisions

**Part of Entra ID Glossary Series: Glossary#5.11 - Device State**

---

A user called saying she could access Teams without any issues but was getting blocked from SharePoint. Same device. Same location. Same time.

The answer was in the Conditional Access policies: Teams had a policy requiring MFA. SharePoint had a policy requiring a compliant device. She'd satisfied the MFA requirement. But her device had fallen out of compliance the previous day when a Windows update failed to install, and the grace period had expired.

Two apps, two policies, two different access outcomes, all because her device's compliance state had changed without her knowing.

## 📊 What Device State Is

Device state is the combination of signals Entra ID has about a device at any given moment. It's not a single value but a collection of properties that Conditional Access evaluates together:

**Registration state** 🏷️: Is the device known to Entra ID? What join type (Registered, Entra Joined, Hybrid Joined)?

**Compliance state** ✅❌: Has the device passed its Intune compliance policy checks? This is the most dynamic piece, evaluated on a schedule by Intune.

**Enabled state** 🔓🔒: Is the device object enabled in Entra ID? Disabled device objects cannot authenticate.

**Device risk** ⚠️: If Microsoft Defender for Endpoint is integrated, the device risk level (Clean, Low, Medium, High) appears as a signal. A device with active malware gets a High risk signal.

**Last activity** 📅: When the device last authenticated or checked in. Stale devices haven't been seen recently.

## 🔄 How State Changes Over Time

Device state isn't static. It changes constantly based on what happens to the device and to the policies evaluating it.

**Compliance state changes** happen when:
- The device checks in with Intune (typically every 8 hours for Windows)
- A compliance policy is created or modified
- The user's device health changes (Defender disabled, update failed, encryption turned off)
- The compliance policy grace period expires after a violation is detected

**Device risk changes** happen when:
- Defender for Endpoint detects or clears a threat
- Microsoft threat intelligence identifies the device in breach data
- A vulnerability is detected that Defender flags as active risk

**Enabled state changes** happen when:
- An admin explicitly disables the device object (lost/stolen device response)
- An admin enables a previously disabled device object

## 🔒 Conditional Access Reads Device State

Conditional Access policies evaluate device state at every authentication attempt, not just at initial sign-in. This is the key property that makes device state meaningful as a security signal.

When the user in the opening example tried to access SharePoint, Conditional Access evaluated:
- User identity: authenticated ✅
- MFA: not required by this policy, not evaluated
- Device compliance: checked Intune's last reported compliance state for this device
- Result: non-compliant, access blocked ❌

The compliance check used the most recent state Intune had reported. If Intune had checked in 6 hours ago and found the device compliant, that would still be the state Conditional Access saw. If Intune had checked in 2 hours ago and found the Windows update failed, that failure state was what Conditional Access saw.

## ⏱️ State Evaluation Timing Matters

The 8-hour default Intune check-in interval means there's always a lag between a device changing state and Conditional Access acting on that change. A device that becomes non-compliant at 9am might not be blocked until Intune's next check-in at 5pm, depending on when the last check-in occurred.

For critical compliance changes, admins can force a sync from the Intune admin center or from the Intune Company Portal app on the device. This triggers an immediate compliance evaluation and updates the state in Entra ID.

CAE (Continuous Access Evaluation) improves this for supported services: when a device is disabled or a policy change is pushed, CAE-capable services like Exchange Online and SharePoint receive real-time notifications and can immediately re-evaluate access without waiting for token expiry.

## 💡 Troubleshooting Device State Issues

When a user is blocked and device state is suspected:

1. Check `dsregcmd /status` on the device to confirm registration state
2. Check the Intune admin center for the device's compliance state and the specific policies it's failing
3. Check whether the device object is enabled in Entra ID
4. Force a device sync from Intune Company Portal and wait for compliance to re-evaluate
5. Check Conditional Access sign-in logs in Entra ID to see exactly which policy blocked access and what device state it evaluated

The sign-in logs are often the fastest path to a diagnosis. They show exactly what the policy evaluated and what the outcome was.

---

💬 **Have you troubleshot a "one app works, another doesn't" situation and traced it back to different Conditional Access policies with different device state requirements?** It's a common support scenario that's easy to misdiagnose without looking at both the policy configuration and the actual device state at the time of the blocked sign-in. What's your go-to diagnostic approach?

#EntraID #DeviceState #DeviceCompliance #ConditionalAccess #Intune #MicrosoftEntra #ZeroTrust
