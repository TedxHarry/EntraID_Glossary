# Application Proxy
*Publishing On-Premises Apps Without VPN*

> **Difficulty:** 🔴 Advanced

📚 Part of Entra ID Glossary Series #9.4 - Application Proxy

---

## 🎯 TL;DR

- Application Proxy publishes on-premises web apps to the internet without opening firewall ports
- Outbound-only connector agents in the DMZ handle traffic : no inbound firewall rules needed
- Users authenticate via Entra ID first; only authenticated sessions reach the internal application


A company had 12 on-premises web applications. Legacy internal tools, a home-grown expense system, a facilities management portal. All running on on-premises web servers. None of them had been modified in years.

Remote workers needed access to these applications. The IT solution for the past decade was VPN: connect to the VPN, access the internal network, reach the applications.

VPN created its own problems: performance, licensing costs, the help desk burden of VPN troubleshooting, and full network access for anyone with VPN credentials. An employee who needed the expense system got VPN access to the entire corporate network.

Application Proxy published all 12 applications externally with Entra ID authentication, no VPN required. Each application got its own external URL. Users signed in with corporate credentials. Access was scoped to the specific application, not the network. The VPN was still there for users who needed broader network access, but most employees never needed it for application access anymore.

## 🌐 What application proxy is

Microsoft Entra Application Proxy is a feature that securely publishes on-premises web applications to external users without requiring those users to connect to the corporate VPN or have direct network access to the on-premises environment.

It works through outbound connections from on-premises Application Proxy connectors to Microsoft's cloud service. The connector establishes and maintains outbound HTTPS connections. When an external user accesses the published application URL, the request flows through Microsoft's network to the connector, which forwards it to the internal application.

The on-premises application doesn't need any firewall changes. No inbound ports need to be opened. The application doesn't know it's being accessed externally; from its perspective, requests come from the connector on the internal network.

## 🏗️ The architecture

**External URL** 🌐: Each application gets an external URL in the format `appname.msappproxy.net` or a custom domain. This is the URL users navigate to from outside the network.

**Application Proxy connector** 🔌: A lightweight Windows service installed on a server in the on-premises environment. The connector registers with Entra ID and establishes persistent outbound connections. One or more connectors per connector group, with multiple connectors for redundancy.

**Connector groups** 📦: Connectors can be organized into groups for different networks, application segments, or geographic locations. Different published applications can be assigned to different connector groups.

**Authentication flow** 🔐:
1. User navigates to the external URL
2. Entra ID handles authentication (Entra ID sign-in page, MFA if required by Conditional Access)
3. After successful authentication, Entra ID sends the request to the connector via the Microsoft cloud service
4. Connector forwards the request to the on-premises application
5. Application responds; response flows back through connector to user

Authentication happens at Entra ID before the user reaches the application. Conditional Access policies apply. Only authenticated, policy-compliant users reach the on-premises application.

## 🔐 SSO options for published applications

Application Proxy supports multiple SSO mechanisms to provide seamless sign-in to applications that expect credentials:

**Integrated Windows Authentication (IWA)** 🪟: For on-premises applications that use Windows authentication. The connector uses Kerberos Constrained Delegation to obtain a Kerberos ticket on behalf of the authenticated user and present it to the application. The user signs in with Entra ID; the application receives a Kerberos token. Transparent to the user.

**Header-based authentication** 📋: For applications that authenticate by reading user information from HTTP headers. The connector injects the authenticated user's claims into specific HTTP headers that the application expects.

**SAML** 🔄: For on-premises applications that support SAML SSO. Entra ID acts as the identity provider.

**Password vaulting** 🔑: For applications with username/password fields that don't support modern auth. Entra ID stores and auto-fills credentials.

## 🛡️ Security benefits vs VPN

**Least privilege access** 🎯: VPN gives network access. Application Proxy gives application access. Users who need the expense system get access to the expense system URL, not the corporate network.

**Conditional Access enforcement** 🚦: Application Proxy published applications are Entra ID-integrated applications. Conditional Access applies. Require MFA, require compliant device, or block access from risky locations, all enforced before the user reaches the application.

**No lateral movement risk from application compromise** 🔒: If the published application is compromised, the attacker has access to that application. They don't have the network-level access a VPN connection would provide.

**Sign-in visibility** 👀: All access attempts appear in Entra ID sign-in logs. Who accessed the application, from where, at what time, with what policy result.

## ⚠️ Limitations and considerations

**Web applications only** 🌐: Application Proxy publishes HTTP/HTTPS web applications. It doesn't support non-web protocols (RDP, SSH, thick client applications that aren't web-based).

**Application compatibility** 🔧: Applications with hardcoded internal URLs, absolute redirect URIs, or cookies scoped to internal hostnames may have issues when published externally. Testing is important before deployment.

**Connector placement** 🏢: Connectors must be network-adjacent to the applications they publish. A connector can't reach an application it doesn't have network access to.

---

💬 **Have you used Application Proxy to eliminate VPN requirements for specific applications?** The "we replaced VPN for most users with Application Proxy" outcome is compelling, but the application compatibility testing is where the work is. What was the application that required the most troubleshooting to publish correctly?
✍️ TedxHarry

<!-- nav -->

---

[← Federated Application](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-3-federated-application.md) | [🏠 Contents](/README) | [OAuth 2.0 (App Integration Focus) →](/9%20INTEGRATION%20%26%20EXTERNAL%20IDENTITIES/glossary-9-5-oauth2-app-integration.md)
