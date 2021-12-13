---
title: "The @platform persistence keystore guide"
SEOtitle: "The @platform (AtPlatform or at_platform) persistence keystore guide"
linkTitle: "Persistence Keystore Guide"
weight: 4
description: How to use the @platform encrypted key/value store
content : How to use the @platform encrypted key/value store

---


### Application data storage

Data for your application is the combination of the device owner’s data with data that has been shared by others. 
An @sign owner's data is...
- Stored in the the @sign owner's device’s (local) @persistence keystore 
- Accessed by others via their internet addressable, always-on, secure, cloud (remote) @server
- Backed up in their secure cloud (remote) @server
- Synchronized between their cloud (remote) @server and any other devices that belong to the owner
- Secured by secret keys which are only stored on the @sign owner's device’s keychain

Note: The @sign owner's cloud (remote) @server does not hold the owner’s secret key, which is required to make changes to the data. The local @server on the owner’s device must initialize any data changes.

Data that others have shared with an @sign owner is...
- Accessed directly from their secure cloud (remote) @server with full privacy controls so it is always up to date
- Cached on the @sign owner's device’s local keystore if permitted
- Removed from the @sign owner's device’s local keystore automatically according to the permissions set by the owner of the data
- Updated upon change automatically using the notification verb



#### How application data is stored and retrieved

As mentioned above, data is stored encrypted as a key/value pair. The @Client SDK supports a familiar set of methods to store and retrieve data from an @persistence keystore. You should always keep in mind that the @protocol includes strict privacy controls applied to all data in an @persistence keystore.

#### Application Access

#### Apps can reason over all of my data in my @persistence keystore

One super interesting side effect of giving people control of their data and storing it all in one place is that any application that they can choose to reason over any data that they are allowed to access in order to create altogether new user experiences. 

For example, their certified messaging application may contain a thread where a group of people are discussing which movie to go see on Wednesday night. If permitted, this information can also be presented as an event in their certified calendar application as well as a group in their certified contacts application.


#### Access within an application namespace

Applications that only rely on data within its own namespace can also store data in the @persistence keystore if certified as @protocol compliant. If the data being stored rightfully belongs to the person creating it (which is the case most of the time), then they will have control of how it is used and shared with other entities and applications. 

#### Use a separate @persistence keystore for your application (certification not required)

If you would like to store application data, you are free to use the @persistence keystore for your persistence if you want to. You may want to get your application certified anyways to advertise that it is privacy compliant and have it included in our list of certified apps. 



#### Authentication only, no need to use the @persistence keystore (certification not required)

If your application does not require data persistence on behalf of the person using it; for example, if you just want to make sure that your application is licensed to the person using it, then you do not need to get it certified. You may want to get your application certified anyways to advertise that it is privacy compliant and have it included in our list of certified apps. 


For more information about getting your application certified, please see the [Certification](/dev_tools/certification) page.
