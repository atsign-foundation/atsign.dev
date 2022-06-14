---
title: "The @platform"
SEOtitle: "The @platform (at_platform or AtPlatform)"
linkTitle: "The @platform"
weight: 1
date: 2021-06-02
content: This whitepaper will help you get a deeper understanding of the @platform
description: This whitepaper will help you get a deeper understanding of the @platform
---

<br>
<table>
  <tr>
   <td><strong>Author(s)</strong>
   </td>
   <td><a href="https://wavi.ng/@barbara">@barbara</a>,<a href="https://wavi.ng/@colin">@colin</a>,<a href="https://wavi.ng/@kevin">@kevin</a> & <a href="https://wavi.ng/@ethnic28">@ethnic28</a>
   </td>
  </tr>
  <tr>
   <td><strong>Date</strong>
   </td>
   <td>July 21, 2021
   </td>
  </tr>
</table>
<br>

# Executive Overview

## End-to-end encrypted everything

There is growing demand for real solutions that address the privacy concerns of consumers globally. The rise in popularity of applications with features like end-to-end encryption is but one example. But such solutions are difficult to build, expensive to operate and often insufficient in the degree that they actually deliver privacy.

The current status quo, in which businesses collect and consolidate consumer data, results in large databases that are tempting targets for hackers. Because of this, new privacy laws such as the [GDPR](https://gdpr.eu/what-is-gdpr/), [CCPA](https://www.acc.com/resource-library/quick-overview-understanding-california-consumer-privacy-act-ccpa), and 17 US [state legislations](https://iapp.org/resources/article/us-state-privacy-legislation-tracker/) are being implemented. Compliance with these laws is a challenge developers face today that is often treated as an afterthought,and we believe that a better approach is to use a platform that delivers “privacy by design” and assures compliance from the outset.

Thus we have created a new architecture that addresses these issues at a fundamental level, starting with a new network protocol and a modern development platform implementation that makes it easy for developers to deliver “privacy first” applications.

If you are thinking about how to deliver applications that are end-to-end encrypted, surveillance-free, and resistant to malicious hacking, read on. The @platform is designed to make it easy to do just that.

## A Simple Definition of the @platform

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 1.png" alt="@platform definition"  width="65%" ></td>

<br> Figure 1. A Simple Definition of the @platform

Atsign has created an open platform for developers who want to create applications that give people full control of their digital selves. The platform is based on the @protocol - a network protocol for the secure exchange of information only between known entities. It uses a unique identifier called an @sign that, combined with the @platform (which is based on the @protocol), allows people the freedom to share, withhold, or retract their information at will with minimal effort, and the developer no longer has to bear the cost and risk of storing and managing people’s personal data.

# Technology Overview

This document describes a software platform with the necessary technology and tools to help developers create beautiful privacy-first mobile applications that are end-to-end encrypted, surveillance-free, and resistant to malicious hacking.

It is called the @platform, and is an open source project intended to make it easy for developers to develop and deploy just such applications including the requisite supporting infrastructure at no cost.

The @platform open source project is embodied in a [public repository](https://github.com/atsign-foundation) which includes a full stack reference implementation, SDKs for application developers, useful documentation, tools, samples, and examples.

The reference implementation is licensed under the [BSD 3-Clause “New” or “Revised” License](https://choosealicense.com/licenses/bsd-3-clause/). At the time of writing, a version written in the [Dart](https://dart.dev/) language that supports the Flutter cross-platform framework has been released, with other languages and framework support expected in the future.

The technology is distributed via the [Pub package manager](https://pub.dev/publishers/atsign.org/packages) as [libraries](https://pub.dev/publishers/atsign.org/packages) for application developers, and via [dockerhub](https://hub.docker.com/u/atsigncompany) as containers for developers' infrastructure components.

# From the Perspective of an Application Developer

## The Beautiful Thing About a Protocol

There are many important and unique things that arise as a result of an architecture based on a protocol. There is ample precedence for this statement based on other successful examples (SMTP and TCP/IP come to mind). The most important things for an application developer to know about how to use the @platform are:

- Data and processing are pushed to the edge of the internet.
- Applications are based on a peer-to-peer shared data model.
- The sharing of access to private data between application instances is end-to-end encrypted only between provable known parties to prevent surveillance, leakage, or other hijacking attacks.

These things are the result of the use of the @protocol and can seem very different from the traditional client-server or API means of sharing access to data. Thus, the mental model for such a system, especially from an application developer's perspective, is worthy of discussion up front.

####

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 2.png" alt="Data shared on a device"  width="70%" ></td>

<br> 
Figure 2: Example of How to Store Shared Data on a Device

As shown above, an application developer need only use the platform SDKS to store the application data locally on the device and include an @sign to share it with; the @platform will ensure that the data gets routed to the intended destination in a safe and secure manner. This peer-to-peer model is in contrast to centralized data stores that are fraught with risk of intentional or accidental breach or exposure of private data.

## A Different Way of Thinking About Data

Certainly, there are many benefits to a decentralized data model with strict control on the part of the owner, and the @platform ensures that sharing access to private data is end-to-end encrypted, surveillance free and resistant to malicious hacking. But, there are other benefits of this architecture that may not be so obvious.

### People Own Their Data

While this is obvious for a “privacy by design” platform, there are additional features that arise from adherence to this principle.

- Data can be portable between similar applications (i.e. swap one Calendar app for another without losing your data), which gives people more choices.
- Application’s data can be shared between disparate applications (e.g. Contacts. Events, Messages) to create altogether new user experiences.
- Applications can reason over “all” their data to produce compelling new services, perhaps aided by ML algorithms (with inferences executed on the mobile device in order to preserve privacy).

### End-to-End Encryption

The @platform ensures that the owner of their data has complete control over it. This is a result of three basic things (though there are many more additional options available that are explained below):

1. Encryption happens at the edge.
2. The encryption keys are only available at the edge.
3. Data sharing is uniquely encrypted between the owner and the intended recipient.

### Data on The Edge

A person’s private data is only available “in the clear” on either the owner’s device since only they have the keys to decrypt it or from cached data that can only be decrypted on the device of the recipient it was shared with. This removes the centralized target for hackers and makes any attempt at a large-scale data breach impractical.

### P2P (peer-to-peer, person-to-person)

Also important to note is the fact that centralized, shared-tenant resources are no longer required for the sharing of access to private data. This not only saves cost, it also increases performance and security from things like denial of service attacks.

### A Kind of Polymorphism

This means of end-to-end encryption of data has a very interesting side effect in that it produces a kind of polymorphism. Since the shared data is end-to-end encrypted uniquely peer-to-peer between two parties, the answer to a query depends on who is asking, and a different response may be returned for different parties for the same query. For example:

<table>
  <tr>
   <td><strong>Query</strong>
   </td>
   <td><strong>Who’s asking</strong>
   </td>
   <td><strong>Response</strong>
   </td>
  </tr>
  <tr>
   <td rowspan="3" >location@alice
   </td>
   <td>anonymous&lt;public>
   </td>
   <td>California
   </td>
  </tr>
  <tr>
   <td>@bob
   </td>
   <td>Bay Area
   </td>
  </tr>
  <tr>
   <td>@carol
   </td>
   <td>Home &lt;address>
   </td>
  </tr>
</table>

This has already been used to create some very interesting new UX (User Experience) designs and offers many other potential use cases.

####

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 3.png" alt="Conceptual Model"  width="70%" ></td>

<br> 
Figure 3: Data Model Includes Owner Data and Cached Data from Others <br>

Enforcing data ownership is another important concept as illustrated in Figure 3. In this system, application data becomes a combination of data created by one @sign combined with data that has been shared by others. Since the shared data is encrypted uniquely for the intended recipient, it can only be accessed by them. In addition, the owner maintains control of it (i.e. updates and deletes), though it may be cached for offline use. This means the owner can literally delete their information from another person's phone.

# The @platform Architecture (Under the Covers)

For those who are interested in the nitty-gritty details, this section covers many of the architecture and design details that have been used for the development of this project.

## Functional Goals

- Provably true privacy and security.
- Support for all popular device architectures with native levels of performance.
- Robust, resilient, and scalable to internet levels.

## Technical Goals

- Dependable - designed for global scale (~100 billion people, entities, or things).
- Extensible - the platform is simple and extensible.
- Near real time - data currency ensured.
- Online/offline use is supported.

## Architectural Guidelines

- Modular, componentized design for flexibility and extensibility.

## Design Patterns And Methodologies

### Separation of Concerns

Great care has been taken when designing this architecture to apply the principles of “Separation of Concerns”. The result is a modular design that is easy to understand and maintain.

### Verbs and Verb Executors

While the SDK makes it simple and intuitive for developers to manage their data interactions, under the covers are the important use of protocol verbs. In order to ensure that verbs are handled in a consistent manner, the use of a “verb executor” repeatable pattern has been used.

### Use of Factory Classes

Across the entire project, you will find the use of factory classes to encourage ​​easy to implement, change, test, and reusable code.

### Interfaces and Implementation Classes

For the areas of software that represent modules that other developers may want to implement some other way, we have also created interface and implementation classes as a good practice of modular design.

### Sequence Diagrams for the Important Flows on the Server

###

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 4.png" alt="@platform definition"  width="65%" ></td>

<br>

##### Figure 4: Server Initialization Flow

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 5.png" alt="@platform definition"  width="65%" ></td>

<br>

##### Figure 5: Connection Request Flow

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 6.png" alt="@platform definition"  width="65%" ></td>

<br>

##### Figure 6: Wiring of a few Important Classes

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 7.png" alt="@platform definition"  width="65%" ></td>

<br>

##### Figure 7: Verb Execution Flow

## About Dart & Flutter

Dart is an object-oriented, class-based, garbage-collected language with C-style syntax. We selected it for our reference implementation for the following reasons:

- Dart is type-safe with both AOT and JIT compilers that are quick and reliable.
- Dart can compile to native code for most common HW+OS architectures.
- Flutter delivers near-native performance (approximately two times faster than JavaScript).
- Dart enforces object-oriented programming.
- Both Dart and Flutter have large open source ecosystems of contributors with many value-adding libraries released and many more being developed.
- The Pub package manager makes adoption and distribution of Dart and Flutter libraries simple.

####

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 8.png" alt="@platform definition"  width="65%" ></td>

<br>

#### Figure 8: Functional Architecture

## Application Level Components (Starting at the Top)

One of the most compelling things about Flutter is the ability to easily integrate and manage application components (called widgets) written by others into your code. Not only does the @platform take advantage of this, it also includes a number of widgets that make it easy to develop an application, access data or take advantage of services that are provided by the platform

### Widgets ([at_widgets](https://github.com/atsign-foundation/at_widgets))

The @platform currently includes the following list of widgets that are available on pub.dev as packages with the source code available on GitHub as well.

#### at_onboarding_flutter

A Flutter plugin project for onboarding any @sign in @platform apps with ease. Provides a QRscanner option and an upload key file option to authenticate.

#### at_chat_flutter

A Flutter plugin project to provide a chat feature between @signs built on the @platform to any Flutter application.

#### at_common_flutter

A Flutter package to provide common widgets used by other @platform Flutter packages.

#### at_backupkey_flutter

A Flutter plugin project for saving the backup key of any @sign that is being onboarded with @platform apps. The backup key can be used to authenticate in other @platform apps.

#### at_contacts_flutter

A Flutter plugin project to provide ease of managing contacts for an @sign using @platform.

#### At_contacts_group_flutter

A Flutter plugin project to provide group functionality with contacts using @platform.

#### at_location_flutter

A Flutter plugin project to share locations between two @signs and track them on OSM (OpenStreetMap).

#### at_events_flutter

A Flutter plugin project to manage events (time, place and attendees) using the @platform.

#### at_follows_flutter

A Flutter plugin project that provides a basic social “follows” functionality for any @sign. Provides a list of @asigns that follow you (followers) as well as the @signs that you follow (following) with the option to unfollow them.

### Libraries ([at_libraries](https://github.com/atsign-foundation/at_libraries))

In addition to the Flutter widgets listed above, there are a number of Dart libraries that provide useful functionality that can be used with the @platform as well.

#### at_persistence_spec

A Dart library containing abstract classes that defines what an implementation of the persistence layer is responsible for. This can be used to guide implementation of other persistence solutions for servers or SDKs as desired.

#### at_commons

A library of Dart and Flutter utility classes that are used across other components of the @platform.

#### at_client

A Dart library with the core, non-platform specific abstract and implementation classes that define what an atClient SDK responsibilities are.

#### at_client_mobile

A Flutter extension to the at_client library which adds support for mobile, desktop and IoT devices.

#### at_lookup

A Dart library that contains the core commands that can be used with a secondary server (scan, update, lookup, llookup, plookup, etc.). This library is also used for building command line tools.

#### at_persistence_secondary_server

A Dart library with the implementation classes for the persistence layer of the secondary server.

#### at_server_status

A Dart library that provides a means to check on the status of the @root server as well as the secondary server for any particular @sign.

#### at_utils

A Dart library that contains various utility classes such as atSign, atmetadata, configuration, and logger.

#### at_demo_data

A Dart library that contains test data, testable @sign credentials and demo environment variables that can be used for writing demo apps and testing with the local test environment.

#### at_utf7

A Dart library that provides methods to encode/decode strings to/from the UTF-7 format as defined in RFC 2152.

#### at_contact

A Dart library for managing contact data that developers can use for their applications.

#### at_base2e15

A Dart library for encoding binary data as text using a unicode string format for increased efficiency as compared to Base64 encoding. Each unicode character represents 15 bits of binary data.

#### at_server_spec

A Dart library containing abstract classes that defines what implementations of the root and secondary servers are responsible for.

# The @protocol Verb Tree

Before we look at some of the sample code, the verb tree gives you the big picture of all of the verbs and what can be executed with the @protocol. Following this is the @platform implementation that most developers will use to develop their applications.

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 9.png" alt="@platform definition"  width="65%" ></td>

<br>

#### Figure 9: The @protocol verb tree

It is worth noting that the @protocol verbs are involved in the secure exchange of information, either public or private only between two known parties. This requires such things as E2E encryption, key management, and passwordless, zero trust authentication. The SDKs are designed to take care of this complexity for the developer with the goal of making such security ubiquitous.

# The AtClientSDK ([at_client_sdk](https://github.com/atsign-foundation/at_client_sdk))

The AtClientSDK encapsulates the @protocol verbs and provides an application level abstraction that is familiar to developers.

## Setup and Configuration Methods

The AtClientSDK requires initialization and setup. For convenience, there is a preference object with default settings that is used to configure the instance.

### _&lt;setPreferences>_

_void setPreferences(AtClientPreference preference)_

The _setPreferences_ method sets the preferences such as sync strategy, storage path etc., for the AtClient instance.

### &lt;_createClient_>

_Future&lt;void> createClient(String currentAtSign, String? Namespace, AtClientPreference preference)_

The _createClient_ method is used to initialize the AtClient instance. This method accepts an @sign, non null application namespace and an AtClientPreference.

### _&lt;getClient>_

_Future&lt;AtClient?> getClient(String? currentAtSign)_

Returns a new AtClient instance. This method requires a non null @sign.

## Sync Verb Methods

The AtClientPreference model includes a parameter for how the application will handle synchronization of data to the secondary server. These can be set to one of three enumerated values.

### _&lt;SyncStrategy.IMMEDIATE>_

SyncStrategy.IMMEDIATE will synchronize changes to local keys immediately as they change to the secondary server for update and delete commands.

### _&lt;SyncStrategy.ONDEMAND>_

SyncStrategy.ONDEMAND will synchronize changes only when SyncManager.sync is invoked.

### _&lt;SyncStrategy.SCHEDULED>_

SyncStrategy.SCHEDULED will synchronize changes periodically once every time interval specified by AtClientPreference.syncIntervalMins has elapsed.

## Scan Verb Methods

The scan verb is used to retrieve all the available keys that are either public or have been specifically shared with some @sign that has been authenticated. This has been abstracted in the _getAtKeys_ method of the AtClientSDK so as to be more familiar to application developers

### &lt;_getAtKeys_>

_Future&lt;List&lt;AtKey>> getAtKeys({String? regex, String? sharedBy, String? sharedWith});_

The _getAtKeys_ method is used to execute the scan verb and retrieve a list of all the relevant keys from a secondary server. These can be filtered by applying a regular expression [_regex_], by specifying the “_sharedBy_” or “_sharedWith_” @signs.

## Update Verb Methods

The update verb is used to write entries in the secondary server as key/value pairs. This has been abstracted in the _put_ method of the AtClientSDK so as to be more familiar to application developers.

### &lt;_put_>\*\* \*\*

_Future&lt;bool> put(AtKey key, dynamic value, {bool isDedicated = false});_

The _put_ method in the AtClientSDK is used to write data into a secondary server as a key/value pair. The @sign must be authenticated to run this method.

### &lt;_putMeta_>

_Future&lt;bool> putMeta(AtKey key);_

The _putMeta_ method in the AtClientSDK is used to write metadata values for some key/value pair data on a secondary server without needing to update the value. This is done to increase efficiency. The @sign must be authenticated to run this method.

## Lookup Verb(s) Methods

The lookup verbs are used to read a value from a secondary server using a key. There are several variations of the protocol verb that the SDK uses to retrieve:

- lookup

  The lookup verb is used to lookup a value on a secondary server for another @sign’s secondary server.

- plookup

  The plookup verb is used to lookup a public value from another @sign’s secondary server if the client is authenticated. The plookup verb can only be executed on a remote secondary server.

- llookup

  The llookup verb is used to lookup a value on the local secondary server of the current @sign.

These have been abstracted in the _get_ and _getMeta_ methods in the AtClientSDK so as to be more familiar to application developers

### &lt;_get_>

_Future&lt;AtValue> get(AtKey key, {bool isDedicated = false});_

The _get_ method in the AtClientSDK is used to read the value of some key. It first attempts to read from the local persistence store, then from a remote cloud secondary server.

### &lt;_getMeta_>

_Future&lt;Metadata?> getMeta(AtKey key);_

The _getMeta_ method in the AtClientSDK is used to read the metadata of some key that has been created automatically and contains useful information about the data, such as who it was created by, when it was created or updated, the current version, etc. It first attempts to read from the local persistence store, then from a remote cloud secondary server if not found.

## Delete Verb Methods

The delete verb is used for deleting key/value pair data on a secondary server. The AtClientSDK also uses the term _delete_ for its method as well.

### &lt;_delete_>

_Future&lt;bool> delete(AtKey key, {bool isDedicated = false});_

The _delete_ method in the AtClientSDK is used to delete the key and value from @sign’s local persistence and then syncs the deletion to the cloud secondary server according to the AtClient's sync preference (e.g. immediate).

## Event Verb(s) Methods

In order to efficiently ensure data gets communicated between secondary servers, there are two verbs that are used to manage the propagation of data events.

- monitor

  The monitor verb is used to stream incoming notifications from the secondary server to @Client.

- notify

  The notify verb is used to notify another secondary server of an update or delete to some key/value pair.

### &lt;_startMonitor_>

_Future&lt;void> startMonitor(String privateKey, Function? notificationCallback, {String? regex});_

The startMonitor method in the AtClientSDK is used to create a persistent connection to a secondary server to receive notifications. Whenever a notification is created on the server, the monitor calls the specified notification’s notificationCallback function. Optionally, a regular expression can be passed to filter the notifications.

### &lt;_notify_>

_Future&lt;bool> notify(AtKey key, String value, OperationEnum operation,_

_ {MessageTypeEnum? messageType,_

_ PriorityEnum? priority,_

_ StrategyEnum? strategy,_

_ int? latestN,_

_ String? notifier,_

_ bool isDedicated = false});_

The _notify_ method in the AtClientSDK is used to propagate a change in the value for some key [AtKey] to the secondary server for the [sharedWith] @sign. Optionally, an operation can be specified and the data value and metadata can be sent along with the key as part of the notification. For rapidly changing data, the [isDedicated] parameter can be set to true to create a dedicated connection to the other secondary server.

### &lt;_notifyAll_>

_Future&lt;String> notifyAll(AtKey atKey, String value, OperationEnum operation);_

The _notifyAll_ method in the AtClientSDK is used to propagate a change in the value for some key [AtKey] to a list of [sharedWith] @signs. Optionally, an operation can be specified and the data value and metadata can be sent along with the key as part of the notification.

### &lt;_notifyList_>

_Future&lt;String> notifyList({String? fromDate, String? toDate, String? regex});_

The _notifyList_ method in the AtClientSDK returns the list of received notifications of an @sign. Optionally, notifications can be filtered by from date, to date, and regular expression.

### &lt;_notifyStatus_>

_Future&lt;String> notifyStatus(String notificationId);_

The _notifyStatus_ method in the AtClientSDK is used to check the status of a notification based on a notificationId.

## Stream Verb Methods

The @platform supports streaming connections in addition to asynchronous connections. The stream verb is used to create a direct connection between two AtClient instances that are joined together on the originator's secondary server that can be used to send an encrypted stream between two devices with @signs.

### &lt;_stream_>

_Future&lt;AtStreamResponse> stream(String sharedWith, String filePath, {String namespace});_

The _stream_ method in the AtClientSDK creates a persistent connection for encrypting and sending a file from a device [filePath] to a [sharedWith] @sign.

## File Sharing Methods

The @platform also includes a “store and forward” means of securely encrypting and sharing binary data (files) using a [filebin2](https://github.com/espebra/filebin2) service as a temporary storage mechanism.

### &lt;_uploadFile_>

_Future&lt;Map&lt;String, FileTransferObject>> uploadFile(List&lt;File> files, List&lt;String> sharedWithAtSigns);_

The _uploadFile_ method in the AtClientSDK can be used to upload a list of files to a filebin for temporary storage and then shares the file download url with [sharedWithAtSigns]. The method returns a map containing each sharedWithAtSign as the key(s) and [FileTransferObject] as the value(s) which contains the information required to download and decrypt the file.

### &lt;_downloadFile_>

_Future&lt;List&lt;File>> downloadFile(String transferId, String sharedByAtSign, {String? downloadPath});_

The _downloadFile_ method in the AtClientSDK can be used to download a list of files for a given [transferId] that has been shared by [sharedByAtSign]. Optionally, you can include a [downloadPath] to download the files.

## Config Verb Method

The config verb is used to configure block list entries in the secondary server. If an @sign is added to the block list, then connections to the secondary server will not be accepted.

## Verb Parameter Reference

required\* optional’

<table>
  <tr>
   <td><strong>Verb</strong>
   </td>
   <td><strong>Parameters</strong>
   </td>
  </tr>
  <tr>
   <td><strong>from</strong>
   </td>
   <td>atSign<strong>*</strong> - @sign you claim to be
   </td>
  </tr>
  <tr>
   <td><strong>cram</strong>
   </td>
   <td>digest<strong>*</strong> - SHA512 digest
   </td>
  </tr>
  <tr>
   <td><strong>pkam</strong>
   </td>
   <td>signature<strong>*</strong> - Signed challenge
   </td>
  </tr>
  <tr>
   <td><strong>pol</strong>
   </td>
   <td>NA
   </td>
  </tr>
  <tr>
   <td><strong>scan</strong>
   </td>
   <td>forAtSign<strong>’</strong> - Scans the keys shared by forAtSign
<p>
regex<strong>’</strong> - Regex to which the @addresses has to be matched to be returned as a result 
   </td>
  </tr>
  <tr>
   <td><strong>update</strong>
   </td>
   <td> ttl<strong>’</strong> -Time to live in milliseconds. Value for the key won't be available after the ttl’
<p>
ttb<strong>’</strong> - Time to birth in milliseconds. Value for the key will be available after the ttb’
<p>
scope<strong>’</strong>- Public vs Private
<p>
forAtSign<strong>*</strong> - For whom the value is being set 
<p>
atKey<strong>*</strong> - Name of the @address
<p>
value<strong>*</strong> - Value for the @address
   </td>
  </tr>
  <tr>
   <td><strong>lookup</strong>
   </td>
   <td>atKey<strong>*</strong> - Name of the @address
<p>
atSign<strong>*</strong> - an @sign’s namespace
   </td>
  </tr>
  <tr>
   <td><strong>llookup</strong>
   </td>
   <td>atKey<strong>* </strong>- Name of the @address
<p>
atSign<strong>*</strong> - an @sign’s namespace
   </td>
  </tr>
  <tr>
   <td><strong>plookup</strong>
   </td>
   <td>atKey<strong>*</strong> - Name of the @address
<p>
atSign<strong>*</strong> - an @sign’s namespace
   </td>
  </tr>
  <tr>
   <td><strong>delete</strong>
   </td>
   <td>atKey<strong>*</strong> - Name of the @address
   </td>
  </tr>
  <tr>
   <td><strong>stats</strong>
   </td>
   <td>statId<strong>’</strong> - Ids of the statistics to display 
   </td>
  </tr>
  <tr>
   <td><strong>config</strong>
   </td>
   <td>whatToConfig<strong>*</strong> - Thing to configure 
<p>
configValue<strong>*</strong> - Value of the thing to configure
   </td>
  </tr>
  <tr>
   <td><strong>notify</strong>
   </td>
   <td>forAtSign<strong>*</strong> - the @sign’s to notify
<p>
key<strong>*</strong> - Key to which the change has happened
<p>
change<strong>*</strong> - Change itself
   </td>
  </tr>
  <tr>
   <td><strong>monitor</strong>
   </td>
   <td>regex<strong>’</strong> - Regex that needs to be matched for the value to be monitored
   </td>
  </tr>
</table>

# Service Level Components

## Root Server ([at_root](https://github.com/atsign-foundation/at_server/tree/trunk/at_root))

The root server is responsible for storing and retrieving the addressable location of an @sign’s secondary server. The architecture is highly distributed and horizontally scalable to internet levels (~50BN endpoints). The information it contains is public and it contains no personal information whatsoever.

## Secondary Server ([at_secondary](https://github.com/atsign-foundation/at_server/tree/trunk/at_secondary))

The secondary server is an internet accessible microservice that is responsible for orchestrating the secure exchange of information between @signs and synchronizing data between the AtClient instances on an @sign owner’s various devices.

It is important to note that private data stored on a secondary server contains only data that has been encrypted on the data owner’s device and the keys are only accessible on that device. As a result, it is “provably true” that nobody else, including us, has access to private data.

## Containers

Docker is used as a standard container format and public images are published on the [Docker Hub](https://hub.docker.com/u/atsigncompany) service for finding and sharing container images.

## Container Management and Orchestration

Any container orchestration system can be used as long as it can use the Docker container standard. Both Docker Swarm and Kubernetes are used by Atsign.

## Privacy and Security

Since the architecture is one of the best “privacy by design” implementations around, people by virtue of the implementation itself have complete control of their data which is encrypted both in use and at rest. As the operator of some of the infrastructure that is deployed, we use best practices to ensure that the infrastructure is reliable and resilient to prevent denial of service attacks.

## Supported Platforms

Dart, the underlying programming language that the @platform is coded in, can be compiled into native binaries for ARM32, ARM64, and AMD64 on Windows, OSX, and Linux operating systems and with the use of the Flutter framework, IOS and Android.

Dart can also be compiled to JavaScript Web but with some limitations.

####

<td align="center"><img src="/docs/Resources/Whitepapers/images/Fig 10.png" alt="@platform definition"  width="65%" ></td>

<br>

Figure 10: (Diagram from [Dart overview](https://dart.dev/overview))

# Summary

This white paper has outlined the intent, architecture and implementation of the @platform that developers can use to create “privacy first” applications with advanced security features built into every exchange of data.

Our intention is that this will herald a new generation of applications that are end-to-end encrypted, surveillance-free, and resistant to malicious hacking. Please join our rapidly growing community and build something, contribute to the open source project, or just give us your feedback.

This is important for all of us.
