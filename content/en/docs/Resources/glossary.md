---
title: "The @platform Glossary of Terms"
SEOtitle: "The @platform (at_platform or AtPlatform) Glossary of Terms"
linkTitle: "@Glossary"
content : Definitions of terms and acryonms often used with the @platform
weight: 2
description: Definitions of terms and acryonms often used with the @platform
---

#### @platform :
 The @platform is an open development platform for developers who want to create applications that give people full control of their digital selves. The platform is based on the @protocol - a network protocol for the secure exchange of information only between known entities. It uses a unique identifier called an @sign that, combined with the @platform (which is based on the @protocol), allows people the freedom to share, withhold, or retract their information at will with minimal effort, and the developer no longer has to bear the cost and risk of storing and managing people’s personal data.     
#### @protocol :
The @protocol is the underlying network protocol used by the @platform.The @protocol's objective is to provide end-to-end encrypted data transfer between two known @signs, but also provides access to publicly available data that is cryptographically signed by the creating @sign.
#### @sign
Each participant in the @protocol has a unique identifier known as an @sign. @sign’s are centrally registered and the rest of the infrastructure is fully distributed.Every @sign has a unique secondary server microservice that is accessible on the Internet via a unique Fully Qualified Domain Name (FQDN) and TCP/IP port number and Secure Sockets Layer (SSL) certificate.
#### root server :
The root servers are the only centralized part of the @protocol and are centralized to provide a single namespace and a globally dependable platform. No data beyond the @sign and responding authoritative secondary server is held on the root servers. This information is considered public, and no authentication is required to look up the secondary server for a particular @sign.
#### secondary server :
Secondary servers provide the second tier of the @protocol architecture, and are responsible for answering lookups for specific @signs. Secondary servers are generally deployed as microservices running on orchestrators such as Docker Swarm or Kubernetes, but can also run as standalone executables. Secondary servers have to be uniquely Internet addressable through use of an FQDN & Port pair that can be translated via DNS to a unique IP & Port.

<!-->
##### CRAM (Challenge-Response Authentication Mechanism) key

##### PKAM (Public Key Authentication Method) logic

##### @protocol verbs/methods

##### AtKey

##### virtual environment

##### at_hello_world

##### at_chats (application)

##### at_cookbook (application)

##### @mosphere

##### server_demo_service

##### clientSDK
