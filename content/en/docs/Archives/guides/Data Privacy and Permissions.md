---
title: "The @platform data privacy & permissions guide"
SEOtitle: "The @platform (at_platform or AtPlatform) data privacy & permissions guide"
linkTitle: "Data Privacy & Permissions Guide"
weight: 3
content : The @platform data privacy and principles which assure that people always have control over their data
description: The @platform data privacy and principles which assure that people always have control over their data

---


### Application Access to Data

There are three basic types of application data access:
1. Storing and retrieving data for your application
2. Accessing data shared by others
3. Accessing and reasoning over data stored by other applications


#### Storing and retrieving data for your application

If your application needs to store data, you can use the @SDK to manage data securely and easily in the @persistence keystore. This SDK provides the following capabilities:
- Data is stored in an encrypted keystore locally for your application
- Data access is in-memory and super-fast
- Offline access with the device is supported
- Data is synchronized and backed up to a cloud @server automatically
- Data is synchronized across all the person’s devices automatically
- Privacy is hardcoded: The owner of the data controls all access to it

Note: the cloud @server does not have access to the secret private key. This prevents bad actors from accessing or modifying private data not meant for them.

##### Creating, updating and deleting data with your application
Data operations that involve writing data to the @persistence keystore can only be done with the approval of the owner. Access to this data is cryptographically controlled. This is managed for your application by the @SDK and is remarkably easy. The types of access that can be set for each data record include:
- public: data that can be read by anyone without need for authentication
- shared: data that the owner has explicitly granted the right to some entity to read it after proving they are who they claim to be
- private: data that is only accessible to the owner (requires authentication)  
- hidden: publicly readable data that is not listed in a scan of the keystore.

Naturally, the owner of an @persistence keystore has access to any and all data that is contained therein. After being authorized, your application can read the data that it needs from the keystore as well. Applications that prefer to rely on data within its own namespace can also store read data from the @persistence keystore with approval of the owner. As always, all data stored is owned and controlled by the owner of the @persistence keystore.

For more information on how your application can create, update, or delete data, see the [@Persistence Keystore Guide](https://pub.dev/packages/at_persistence_spec) and the [@Protocol Verbs](https://atsign.dev/docs/functional_architecture/verbs).

#### Accessing data shared by others

Applications typically are a combination of an owner's data and data that has been shared with them by others. This is a new feature and is what we’re referring to when we talk about P2P (Peer-to-Peer) applications.

For example, messaging applications available today involve a combination of data (messages) from various people but have no way to ensure that each individual message belongs to its creator. With the @protocol, messages that I create and share with other people are owned by me and likewise, messages that others create and share with me are owned by them. The messaging application is thus responsible for interleaving and presenting these messages while simultaneously maintaining privacy controls for the owner of the data (i.e. I own my messages to you and you own your messages to me).

While this may seem confusing and difficult at first, the @Client SDK and the Flutter UI Component libraries make it very simple to implement. This results in surveillance-free, privacy-compliant applications that are simple, cost-effective, and efficient, with better performance than backend server-based applications of the past.

The @Client SDK provides the following capabilities that help to integrate data shared by others in your application:
- Public data shared by others can be looked up
- The notification verb alerts your application when new data shared by others is available 
- The monitor verb creates a persistent connection for real-time interactions
- Data can be scanned for and read directly from another persons @persistence keystore
- Shared data is cached for fast, reliable access to shared data with all privacy related parameters managed for you by the @Client SDK

For more information on how your application can create, update, or delete data, see the [@Persistence Keystore Guide](Persistence Keystore Guide) and the [@Protocol Verbs](https://atsign.dev/docs/functional_architecture/verbs).

#### Accessing and reasoning over data stored by other applications

One super interesting side effect of giving people control of their data and storing it all in one place is that any application that they authorize can reason over any data that they are allowed to access. Applications that are certified as @protocol compliant (@pps) can provide amazing new experiences because they have the ability to access and reason over all data stored in an @persistence keystore.

For example, a certified messaging app may contain a thread where a group of people are discussing which movie to go see on Wednesday night. If permitted, this information can also be presented as an event in their certified calendar application and similarly presented as a group in their certified contacts application.


### Advanced Options

#### Create a separate @persistence keystore for your application (certification not required)

If you would like to store application data, you are free to use the @persistence keystore for your persistence if you want to. You may want to get your application certified anyways to advertise that it is privacy compliant and have it included in our list of certified apps. 


#### Authentication only, without the @persistence keystore (certification not required)

If your application does not require data persistence on behalf of the person using it; for example, if you just want to make sure that your application is licensed to the person using it, then you do not need to get it certified. You may want to get your application certified anyways to advertise that it is privacy compliant and have it included in our list of certified apps. 


For more information about getting your application certified, see the [Certification page](https://atsign.dev/dev_tools/certification/).
