---
title: "Services provided by the @platform"
SEOtitle: "Services provided by the  @platform (at_platform or AtPlatform)"
linkTitle: "Architecture"
content: Important services provided by the @platform
description: Important services provided by the @platform
parent: /Functional_Architecture/
weight: 1
---

### Data Caching & Encryption

Data that others have shared with an @sign owner is cached on the @sign owner's device’s local keystore if permitted.

[Learn more](https://atsigncompany.medium.com/data-encryption-caching-with-the-protocol-debe9efc0f49)

### Notification

Notification is a mechanism which enables an @sign to share data with another @sign. The data shared is end to end encrypted. @sign owner can query the status of the notification.

[Learn more](https://blog.atsign.dev/part-1-the-notify-verb-cko97bv8f00l5gws13umb0nvz)

### Onboarding

The onboarding process is responsible for creating the authenticating keys for a new @sign or retrieving the authenticating keys of an existing @sign from the keys file provided by the @sign owner. It also synchronizes the data between mobile apps and the cloud secondary server.

[Learn more](https://pub.dev/packages/at_onboarding_flutter)

### Peer-to-Peer Streams

Streams enable transferring of files between the @sign's through a secure and dedicated socket between sender and receiver. The files can be a text documents, images, audio-video files etc. The stream transfers are end to end encrypted.

[Learn more](https://blog.atsign.dev/the-stream-verb-protocol-ckmwi28is01aqd2s184bien2q)

### Persistence

The persistence defines the interfaces on how the data in @protocol is stored.

[Learn more](https://pub.dev/packages/at_persistence_spec)

### Synchronization

Synchronization is a process to keep the data in mobile apps and @sign server identical.

[Learn more](https://atsigncompany.medium.com/the-protocol-synchronization-77b00ca5341b)
