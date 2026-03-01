# Global Secure Access
*Microsoft's Zero Trust Network Access Layer*

**Part of Entra ID Glossary Series: Glossary#13.9 - Global Secure Access**

---

A company had 4,000 remote employees. They connected to internal applications through a VPN. The VPN terminated at a central hub, routed all traffic through the corporate network, and provided access to everything on the internal network once connected.

The security problem: VPN grants network-level access. Once a user connected, their device was effectively inside the perimeter. An attacker with compromised credentials could reach anything on the internal network, not just the specific application they claimed to need.

The identity problem: VPN authentication was separate from Entra ID. Users authenticated to the VPN with one set of credentials, then authenticated to Entra ID for cloud applications separately. Two authentication events, two points of control, no unified policy.

Global Secure Access is Microsoft's answer to both problems.

## 🌐 What Global Secure Access Is

Microsoft Entra Global Secure Access is Microsoft's Security Service Edge (SSE) solution, providing network-level access control integrated with Entra ID identity. It's the convergence of network security and identity security into a unified policy model.

Global Secure Access has two components with distinct purposes:

**Microsoft Entra Internet Access** 🌍: A Secure Web Gateway (SWG) for internet-bound traffic. Routes users' internet traffic through Microsoft's network, applying web content filtering, threat protection, and Conditional Access policies to internet access. Think: cloud proxy that knows who the user is because it's integrated with Entra ID identity.

**Microsoft Entra Private Access** 🔒: A Zero Trust Network Access (ZTNA) solution replacing traditional VPN for access to private applications. Instead of granting network-level access to everything on the corporate network, Private Access grants application-level access to specific applications, with each access decision evaluated by Conditional Access.

## 🔑 Private Access: ZTNA vs VPN

The fundamental difference between ZTNA and traditional VPN is the scope of access granted:

**Traditional VPN** 🔧: Authenticates the user and device, then establishes a tunnel to the corporate network. Once tunneled, the device has network-level access to resources on that network segment. Access control happens at the network layer.

**ZTNA (Private Access)** 🔐: Authenticates the user and device, evaluates Conditional Access policy per application, and grants access to the specific application requested. The device doesn't get network-level access to anything else. Each application is individually protected. Conditional Access policy applies at the application level.

For a compromised device scenario: with VPN, the compromised device has network access. With Private Access, the compromised device fails the device compliance check in the per-application Conditional Access policy and is denied access to each application individually.

## 🏗️ The Global Secure Access Client

The Global Secure Access client is a lightweight agent installed on Windows, macOS, iOS, and Android devices. It routes the appropriate traffic to Microsoft's network:

For Private Access: traffic to private application connectors is routed through the GSA infrastructure to the application, without exposing the underlying network. The user's device connects to the application, not to the corporate network.

For Internet Access: internet-bound traffic is routed through Microsoft's SWG for filtering and policy application.

The client is registered with Entra ID, making it possible for the Conditional Access engine to know which traffic is coming through the GSA client. This enables "compliant network" as a Conditional Access condition: traffic coming through an authenticated, managed GSA client is from a known, controlled access path.

## 🔐 Compliant Network Conditional Access

One of the most significant integrations between Global Secure Access and Entra ID Conditional Access is the "compliant network" location condition.

Traditional IP-based location conditions in CA rely on knowing which IP ranges are "trusted" (corporate network, VPN exit nodes). With remote work and cloud resources, IP ranges are less reliable as a trust indicator.

The compliant network condition uses the GSA client as a trust signal: the user is authenticating through a managed, identity-aware access path. This is a stronger signal than an IP range. You know the traffic came through a device that authenticated to GSA and passed the GSA client policy.

Microsoft 365 services can require the compliant network condition, meaning that direct-to-internet traffic to Microsoft 365 that doesn't go through GSA is blocked. All Microsoft 365 access flows through GSA, giving the organization visibility and control over all Microsoft 365 traffic regardless of location.

## 📊 Where This Fits the Entra ID Picture

Global Secure Access extends Entra ID's identity-driven access control from application authentication into network access. The same Conditional Access policies, the same device compliance signals, the same risk-based controls that govern application sign-ins now also govern network-level access to private applications and internet traffic.

For organizations using the full Entra ID stack, GSA is the layer that closes the gap between "we control identity for application access" and "we control the entire access path, not just the authentication event."

---

💬 **Is your organization evaluating or using Global Secure Access or a competing ZTNA solution to replace legacy VPN, and what's driving the timeline?** The VPN replacement conversation is happening in most organizations, pushed by remote work patterns and the inadequacy of network-perimeter security models. What would have to be true about GSA for your organization to commit to it over alternatives?
<!-- nav -->

---

[← OID (Object ID)](glossary-13-8-oid.md) | [Home](../README.md) | [Service Account →](glossary-13-10-service-account.md)
