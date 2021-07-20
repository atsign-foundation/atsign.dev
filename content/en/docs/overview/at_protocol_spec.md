---
title: "Specification"
SEOtitle: "AtProtocol (at_protocol or @protocol) Specification"
linkTitle: "Specification"
weight: 1
description: >
  The @protocol specification repository contains the specification document as well as other supporting documentation. 
---

# The @protocol Specification
<br>
<table>
  <tr>
   <td>
   <strong>Subject</strong>
   </td>
   <td>@protocol specification
   </td>
  </tr>
  <tr>
   <td><strong>Author(s)</strong>
   </td>
   <td>Colin Constable, Kevin Nickels, Jagannadh Vanghuri
   </td>
  </tr>
  <tr>
   <td><strong>Revision</strong>
   </td>
   <td>v0.1.0 (draft)
   </td>
  </tr>
  <tr>
   <td><strong>Date</strong>
   </td>
   <td>July 5, 2021
   </td>
  </tr>
</table>
<br>

## Root Server
A Root Server should provide a lookup of where a Secondary Server for an @sign is running. This is similar to a DNS server.

When asking a Root Server for the lookup of a particular @sign the Root Server should respond with a null if the name does not exist and if the name exists the DNS name or address of the @server and the IP port number for that @sign should be returned.

**Response:** 

```<host>:<port>```

The Root Server only has one verb - `@exit` and all other inputs are considered to be lookup requests.

## Secondary Server
A Secondary Server is where an @sign user's personal data should be stored. One interacts with a secondary using the verbs exposed by the protocol.

A Secondary Server should have 4 major sub components:
1. Key Store
2. Commit Log
3. Access Log
4. Notification Log

Verbs described in the document should be used to create, update, delete and retrieve information from the above sub components.

### 1. Key Store

Key store is a place where user data in a Secondary Server should be saved as key and value pairs. Apart from the value, an @sign user should be able to add certain metadata for a key. 
    
#### **Key**

A key in the @protocol can be formed by using any alphanumeric and special characters (UTF-8) excluding "@", ":" and a white space (" "). A key in a secondary can be any of the following 5 types:

1. Public Key

    - A public key is a key which can be looked up by any @sign user.

    - A public key should be part of the <em><span style="text-decoration:underline;">scan</span></em> verb result.

    - Format of the public key should be **public:<identifier>:<@sign>**.

    **Example:**    

    ```public:location@alice```

    > The owner of the secondary should be allowed to update or delete the value of a public key.


2. Private Key
        
    - A private key is a key which cannot be looked up any @sign user other than the one created it.
    
    - A private key should not be returned in a <em><span style="text-decoration:underline;">scan</span></em> verb result.
    
    - Format of the private key should be <strong>privatekey:<identifier>:<@sign></strong>.

    **Example:**    

    ```privatekey:pk1@alice```

    > The owner of the secondary should be allowed to update or delete the value of a private key.


3. User key
    - A user key can only be looked up by an @sign user with whom the data has been shared.
    - A user key should be part of the <em><span style="text-decoration:underline;">scan</span></em> verb result only for the user who created it and the specific user it has been shared with.
    - Format of the key shared with someone else should be <strong><Shared with @sign>:<identifier>:<Created by @sign></strong>

    **Example:**    

    ```@bob:phone@alice```
    
    > Note: Above Key should be part of scan verb result for only @alice and @bob 

    > The owner of the secondary should be allowed to update or delete the value of a user key.


4. Internal Key

    - Internal keys start with an underscore(_) and are not displayed in scan results. Internal keys can be looked up only by the owner of the secondary


5. Cached Key

    - A cached key is a key that was originally created by another @sign user but is now cached on the Secondary Server of another user's @sign as he/she was given permission to cache it. 

    <!-- - A user should be able to enable/disable caching of someone else's key by virtue of the "enableKeyCaching" config parameter. <TO DO: Kevin, Colin - We need to discuss. We don't have this yet -->

    - A cached key should be listed in the <em><span style="text-decoration:underline;">scan</span></em> verb result for the @sign user who cached it.

    - Format of the key shared with someone else should be <strong>cached:<Shared with @sign>:<identifier>:<Created by @sign></strong>

    **Example:**    

    ```cached:@bob:phone@alice```

    > The user who has cached the key should not be allowed to update the cached key.

    > An @sign user who has created and shared the key should be allowed to update a cached key, and if the "autoNotify" config parameters is set to true, the updated value should be notified (please refer to the `notify` verb) and the cached key updated with the new value.

    > If the user who originally shared the keys set the CCD (Cascade delete) to true, the cached key will be deleted when the original key is deleted.

#### **Value**

Text or binary values can be saved in a Secondary Server. The size of the value saved in a secondary is bound by the config parameter "maxBufferSize".
<!-- <TO DO: Kevin, Colin - We need to discuss. Do we need this.> -->

> A user should be made aware of this limitation by using the `stats` verb.

<!-- <TODO: Ex: @stats:10 should return the max size permitted by a secondary as a single value in bytes> -->

> If a binary value is being saved on a Secondary Server, the "isBinary" attribute on the metadata should be set to true by the convention.

1. Reference Value

    A Secondary Server should support referencing another key's value.
    
    A reference value should be in the format "atsign://<key>".

    For example, 'phone@bob(key)' is 1234 (value). Now another key called altPhone@bob can refer to phone@bob by referencing it as altPhone@bob = atsign://phone@bob.

    When the user does a lookup on the key that contains a reference, the Secondary Server should return a fully resolved value.

    <!-- <TO DO: Caching referenced keys is tricky. We have not yet implemented this yet.> -->

2. Metadata

    Metadata of a key should describe the following properties of the value being inserted. 

    <table>
    <tr>
    <td>
    <strong>Meta Attribute</strong>
    </td>
    <td><strong>Auto create?</strong>
    </td>
    <td><strong>Description</strong>
    </td>
    </tr>
    <tr>
    <td>createdOn
    </td>
    <td>Yes
    </td>
    <td>Date and time when the key has been created.
    </td>
    </tr>
    <tr>
    <td>createdBy
    </td>
    <td>Yes
    </td>
    <td>@sign that has created the key
    </td>
    </tr>
    <tr>
    <td>updatedOn
    </td>
    <td>Yes
    </td>
    <td>Date and time when the key has been last updated.
    </td>
    </tr>
    <tr>
    <td>sharedWith
    </td>
    <td>No
    </td>
    <td>@sign of the user with whom the key has been shared. Can be null if not shared with anyone.
    </td>
    </tr>
    <tr>
    <td>ttl
    </td>
    <td>No
    </td>
    <td>Time to live in milliseconds. 
    </td>
    </tr>
    <tr>
    <td>expiresOn
    </td>
    <td>Yes
    </td>
    <td>A Date and Time derived from the ttl (now + ttl). A Key should be auto deleted once it expires.
    </td>
    </tr>
    <tr>
    <td>ttb
    </td>
    <td>No
    </td>
    <td>Time to birth in milliseconds.
    </td>
    </tr>
    <tr>
    <td>availableFrom
    </td>
    <td>Yes
    </td>
    <td>A Date and Time derived from the ttl (now + ttl). A Key should be only available after availableFrom.
    </td>
    </tr>
    <tr>
    <td>isCached
    </td>
    <td>No
    </td>
    <td>True if the key can be cached by another @sign user.
    </td>
    </tr>
    <tr>
    <td>ttr
    </td>
    <td>No
    </td>
    <td>Time in milliseconds after which the cached key needs to be refreshed. Ttr of -1 indicates that the key can be cached forever.
    </td>
    </tr>
    <tr>
    <td>refreshAt
    </td>
    <td>No
    </td>
    <td>A Date and Time derived from the ttr. The time at which the key gets refreshed.
    </td>
    </tr>
    <tr>
    <td>ccd
    </td>
    <td>No
    </td>
    <td>Indicates if a cached key needs to be deleted when the @sign user who has originally shared it deletes it.
    </td>
    </tr>
    <tr>
    <td>isBinary
    </td>
    <td>No
    </td>
    <td>True if the value is a binary value.
    </td>
    </tr>
    <tr>
    <td>isEncrypted
    </td>
    <td>No
    </td>
    <td>True if the value is encrypted
    </td>
    </tr>
    </table>


### 2. Commit Log

A Secondary Server should record any create, update and delete operations in a commit log. The Commit Log should record these operations with a unique commit id so that users of the secondary can lookup operations that happened on or after a given commit id.

A Secondary Server should provide a way to compact the Commit Log based on time and size.

### 3. Access Log

A Secondary Server should record the following user actions: user login, user authentication and lookup. The Access Log should record these operations so that users of the secondary can retrieve various statistics such as the most visited @sign or most visited keys.

A Secondary Server should provide a way to compact the Access Log based on time and size.

### 4. Notification Log

A Secondary Server should record any notifications that have been received and sent. Please check the `notify` verb specification for details on how a notification should be sent.

A Secondary Server should provide a way to compact the Notification Log based on time and size.

## Standard Keys
A Secondary Server should have the following standard keys:

<table>
  <tr>
   <td>
<strong>Key</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>public:publickey@<atsign>
   </td>
   <td>Public key used by other atsigns for encryption.
   </td>
  </tr>
  <tr>
   <td>public:signing_publickey@<atsign>
   </td>
   <td>Public key used on a pol handler to verify a signed challenge
   </td>
  </tr>
  <tr>
   <td><atsign>@signing_privatekey@<atsign>
   </td>
   <td>Private key used to sign a challenge on a pol request
   </td>
  </tr>
  <tr>
   <td><atsign>:shared_key@<atsign>
   </td>
   <td>Symmetric key used to encrypt/decrypt self atsign data
   </td>
  </tr>
</table>

## Configuration Parameters
A Secondary Server should honor the following configuration parameters.

<!-- <TO DO: Ideally these parameters should be set using some verb so that the user can control them. config verb can be extended to accomplish the same. Config verb also has the list option, so we can set/reset/list the configuration using the same> -->

<table>
  <tr>
   <td>
   <strong>Key</strong>
   </td>
   <td><strong>Valid Values</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td><strong>autoNotify</strong>
   </td>
   <td>true/false
   </td>
   <td>If set to true, a Secondary Server should automatically notify another @sign user when a key has been shared with him/her. Please refer to the <em><span style="text-decoration:underline;">notify </span></em>verb spec for details.
   </td>
  </tr>
  <tr>
   <td><strong>bufferLimit </strong>
   </td>
   <td>Number of bytes
   </td>
   <td>Maximum size of a value for a key that can be transferred to a Secondary Server
   </td>
  </tr>
  <tr>
   <td><strong>inbound_max_limit</strong>
   </td>
   <td>An Integer
   </td>
   <td>Maximum number of inbound connections that a Secondary Server can accept
   </td>
  </tr>
  <tr>
   <td><strong>outbound_max_limit</strong>
   </td>
   <td>An Integer
   </td>
   <td>Maximum number of outbound connections that a secondary can make to another Secondary Server
   </td>
  </tr>
  <tr>
   <td><strong>inbound_idle_time_millis</strong>
   </td>
   <td>Time in milliseconds
   </td>
   <td>Maximum time the inbound connection can be active
   </td>
  </tr>
  <tr>
   <td><strong>outbound_idle_time_millis</strong>
   </td>
   <td>Time in milliseconds
   </td>
   <td>Maximum time the outbound connection can be active.
   </td>
  </tr>
</table>

## Block List
A user of the Secondary Server should be able to decide who is allowed to connect to a Secondary Server. The `config` verb should be used to configure this. Once added, a Secondary Server should honor the list at the time of accepting new connections from an @sign user using the `from` verb.

<!-- ## Life Cycle -->

<!-- <TO DO: TBD: What I want to write is, A User of the secondary should be able to control pausing and resuming of a Secondary Server> -->

## Verbs

### The `from` verb

**Synopsis:**

The `from` verb is used to tell a secondary whom you claim to be.

Following regex represents the syntax of the `from` verb:

**Example:**

```r'^from:(?<@sign>@?[^@\s]+$)' ```

**Response:**

If the user who is trying to connect is the owner of the Secondary Server, then the `from` verb should respond with the following response.

```key:<sessionId@sign:uuid>```

If the user who is trying to connect is not the owner of the Secondary Server, then the `from` verb should respond with the following response.

```proof:<sessionid>@<@sign>:<UUID>```

If the user is not allowed to connect to the Secondary Server, then it should respond back with the following error and close the connection to the server.

```error:AT0013-Connection Exception```

**Description:**

The `from` verb is used to tell the Secondary Server what @sign you claim to be. With the `from` verb, one can connect to one's own Secondary Server or someone else's Secondary Server. In both cases, the Secondary Server responds back with a challenge to prove that you are who you claim to be. This is part of the authentication mechanism of the @protocol. 

This authentication mechanism varies based on whether you are connecting to your own secondary (cram) or someone else's secondary (pol).

**OPTIONS:**

```<@sign>``` 
Required: Yes
Description: @sign with which you are connecting to a Secondary Server.

### The `cram` verb

**Synopsis:**

The `cram` verb is used to boostrap authenticate one's own self as an owner of a Secondary Server. It is 
intended to be used once until a set of PKI keys are cut on the owner's mobile device and from then on 
we use the `pkam` verb.

The following regex represents the syntax of the `cram` verb:

```r'^cram:(?<digest>.+$)'```

**Response:**

If the user gets the challenge right, the prompt should change to the @sign of the user.

```<@sign>@```

If the user gets the cram authentication wrong, then it should respond back with the following error and close the connection to the server.

```error:AT0401-Client authentication failed```

**Description:**

The `cram` verb follows the `from` verb. As an owner of the Secondary Server, you should be able to take the challenge thrown by the `from` verb and encrypt using the shared key that the server has been bound with. Upon receiving the `cram` verb along with the digest, the server decrypts the digest using the shared key and matches it with the challenge. If they are the same, then the secondary lets you connect to the Secondary Server and changes the prompt to your @sign.

**OPTIONS:**

```<digest> ```
Required: Yes
Description: Encrypted challenge

### The `pol` verb

**Synopsis:**

The `pol` verb is part of the `pkam` process to authenticate oneself while connecting to someone else's Secondary Server. The term
'pol' means 'proof of life' as it provides a near realtime assurance that the requestor is who it claims to be.

Following regex represents the syntax of the `pol` verb:

```r'^pol$'```

**Response:**

If the user gets the challenge right the prompt should change to the @sign of the user.

```<@sign>@```

If the user gets the cram authentication wrong then it should respond back with the following error and close the connection to the server.

```error:AT0401-Client authentication failed```

**Description:**

The `pol` verb follows the `from` verb. 'pol' indicates another secondary that the user who is trying to connect is ready to authenticate himself. For example, if @bob is trying to connect to @alice, @bob would take the key and value from the proof response of the verb and create a public key and value which then can be looked up by @alice. After @alice looks up @bob's secondary @alices secondary should change the prompt to @bob.

**OPTIONS:**

NA

### The `update` verb

**Synopsis:**

The `update` verb is used to insert key/value pairs into a Key Store. An update can only be run by the owner of a Secondary Server on his/her own Secondary Server.

Following regex represents the syntax of the `update` verb:

```r'^update:(?:ttl:(?<ttl>\d+):)?(?:ttb:(?<ttb>\d+):)?(?:ttr:(?<ttr>(-?)\d+):)?(ccd:(?<ccd>true|false):)?((?:public:)|(@(?<for@sign>[^@:\s]-):))?(?<atKey>[^:@]((?!:{2})[^@])+)(?:@(?<@sign>[^@\s]-))? (?<value>.+$)'```

**Response:**

The Secondary Server should return the commit id from Commit Log if the update is successful.

```data:<CommitId>```

If the user provides the invalid update command, then it should respond with the following error and close the connection to the server

```error:AT0003-Invalid Syntax```

**Description:**

The `update` verb should be used to perform create/update operations on the Secondary Server. The `update` verb requires the owner of the secondary to authenticate himself/herself to the Secondary Server using `from` and `cram` verbs.

If a key has been created for another @sign user, the Secondary Server should honor "autoNotify" configuration parameter.

**OPTIONS:**

`<ttl>` 
Required: No
Description: Time to live in milliseconds

`<ttb>` 
Required: No
Description: Time to birth in milliseconds

`<ttr>` 
Required: No
Description: Time to refresh in milliseconds. 
> -1 is a valid value which indicates that the user with whom the key has been shared can keep it forever and the value for this key won't change forever.

`<ccd>` 
Required: No
Description: A value of "true" indicates that the cached key needs to be deleted when the @sign user who has originally shared it deletes it.

`<for@sign>`
Required: Yes (Not required when the key is a public key)
Description: @sign of the user with whom the key has been shared

`<@sign>`
Required: Yes 
Description: @sign of the owner

`<value>`
Required: Yes
Description: Value for the key

### The `update:meta` verb

**Synopsis:**

The `update:meta` verb should be used to update the metadata of a key @sign user without having to send or save the value again.

Following is the regex for the `update:meta` verb

```^update:meta:((?:public:)|((?<forAtSign>@?[^@\s]-):))?(?<atKey>((?!:{2})[^@])+)@(?<atSign>[^@:\s]-)(:ttl:(?<ttl>\d+))?(:ttb:(?<ttb>\d+))?(:ttr:(?<ttr>\d+))?(:ccd:(?<ccd>true|false))?(:isBinary:(?<isBinary>true|false))?(:isEncrypted:(?<isEncrypted>true|false))?$```

**Response:**

The Secondary Server should return the commit id from Commit Log if the update is successful.

```data:<CommitId>```

If the user provides the invalid update meta command, then it should respond with the following error and close the connection to the server


```error:AT0003-Invalid Syntax```

**Description:**

The `update:meta` verb should be used to perform create/update operations on the Secondary Server. The `update:meta` verb requires the owner of the secondary to authenticate himself/herself to the Secondary Server using `from` and `cram` verbs.

The Secondary Server should allow creation of keys with null values. If a key has been created for another @sign user, the Secondary Server should honor "autoNotify" configuration parameter.

**OPTIONS:**

`<ttl>` 
Required: No
Description: Time to live in milliseconds

`<ttb> `
Required: No
Description: Time to birth in milliseconds

`<ttr> `
Required: No
Description: Time to refresh in milliseconds. 
> -1 is a valid value which indicates that the user with whom the key has been shared can keep it forever and the value for this key won't change forever.

`<ccd>` 
Required: No
Description: A value of "true" indicates that the cached key needs to be deleted when the @sign user who has originally shared it deletes it.

`<for@sign>`
Required: Yes (Not required when the key is a public key)
Description: @sign of the user with whom the key has been shared

`<@sign>`
Required: Yes 
Description: @sign of the owner

### The `lookup` verb

**Synopsis:**

The `lookup` verb should be used to lookup the value shared by another @sign user.

The following is the regex of the `lookup` verb:

```lookup:((?<operation>meta|all):)?(?<atKey>(?:[^:]).+)@(?<@sign>[^@\s]+)$```

**Response:**

If the operation is not specified the Secondary Server should just respond back with the value saved by the user as is.

```data:<value>```

If the operation is to lookup the metadata only then the result should be wrapped in a JSON in the following format:

```data:<Metadata in a JSON>```

**Example:**    

``` json 
data: 
{
    "createdBy":"@bob",
    "updatedBy":"@bob",
    "createdAt":"2020-10-21 09:46:48.982Z",
    "updatedAt":"2020-10-21 09:46:48.982Z",
    "availableAt":"null",
    "expiresAt":"null",
    "refreshAt":"2020-10-21 09:46:58.982Z",
    "status":"active",
    "version":0,
    "ttl":null,
    "ttb":null,
    "ttr":10000,
    "ccd":false,
    "isBinary":false,
    "isEncrypted":false
 }
```

If the operation is to lookup the metadata and the data together then the result should be wrapped in a JSON in the following format:

```data:<Value and Metadata in a JSON>```

**Example:**    

``` json
data:
{
	"key":"@alice:country@bob",
	"data":"USA",
	"metaData":
	{
	 "createdBy":"@bob",
       "updatedBy":"@bob",
       "createdAt":"2020-10-21 09:46:48.982Z",
       "updatedAt":"2020-10-21 09:46:48.982Z",
       "availableAt":"null",
       "expiresAt":"null",
       "refreshAt":"2020-10-21 09:46:58.982Z",
       "status":"active",
       "version":0,
       "ttl":null,
       "ttb":null,
       "ttr":10000,
       "ccd":false,
       "isBinary":false,
       "isEncrypted":false
     }
}
```

If the other Secondary Server on which the lookup needs to be performed is down then the secondary should return the following error and keep the connection alive.


```error:AT0007-Secondary Server not found.```

If the lookup command is not valid, then the Secondary Server should return the following error and close the connection:


```error:AT0003-Invalid Syntax```

For whatever reasons, If the handshake with another secondary fails, then the Secondary Server should return the following error:


```data:AT0008-Handshake failure```

**Description:**:

The `lookup` verb should be used to fetch the value of the key shared by another @sign user. If there is a public and user key with the same name then the result should be based on whether the user is trying to lookup is authenticated or not. If the user is authenticated then the user key has to be returned, otherwise the public key has to be returned.

### The `plookup` verb:

**Synopsis:**

The `plookup` verb enables to lookup the value of the public key shared by another @sign user.

Following is the regex of the `plookup` verb:

```^plookup:((?<operation>meta|all):)?(?<atKey>[^@\s]+)@(?<@sign>[^@\s]+)$```

**Response:**

The Secondary Server should return the value or metadata or the value and metadata together based on the option specified. 

The response structure should be exactly the same as the `lookup` verb.

If the other Secondary Server on which the `lookup` needs to be performed is not available, then the secondary should return the following error and keep the connection alive.

```error:AT0007-Secondary Server not found.```

If the `lookup` command is not valid, then the Secondary Server should return the following error and close the connection:

```error:AT0003-Invalid Syntax```

**Description:**:

The `plookup` verb should be used to fetch the value of the public key shared by another @sign user. 

### The `llookup` verb

**Synopsis:**

The `llookup` verb should be used to look up one's own secondary and this should return the value as is (i.e. without any resolution).

The Following is the regex of the `llookup` verb:

```^llookup:((?<operation>meta|all):)?(?:cached:)?((?:public:)|(@(?<for@sign>[^@:\s]-):))?(?<atKey>[^:]((?!:{2})[^@])+)@(?<@sign>[^@\s]+)$```

**Response:**

The Secondary Server should return the value or metadata or the value and metadata together based on the option specified. 

The response structure should be exactly the same as the `lookup` verb.

If the other Secondary Server on which the lookup needs to be performed is down then the secondary should return the following error and keep the connection alive.

```error:AT0007-Secondary Server not found.```

> If the lookup command is not valid, then the Secondary Server should return the following error and close the connection:


```error:AT0003-Invalid Syntax```

**Description:**:

The `llookup` verb should be used to fetch the value of the key in the owners secondary store as is without resolving it. For example if a key contains a reference as a value, the `lookup` verb should resolve it to a value whereas llookup should return the value as is.

**Example:**    

If phone@bob is "1234" and altphone@bob is "atsign://phone@bob",
then `lookup` of altphone@bob should return "1234" whereas `llookup` of altphone@bob should return "atsign://phone@bob".

### The `pkam` verb

**Synopsis:**

The `pkam` verb is used to authenticate one's own self as an owner of a Secondary Server using a PKI style authentication.

Following regex represents the syntax of the `pkam` verb:

```^pkam:(?<signature>.+$)```

**Response:**

If the user gets the challenge right, the prompt should change to the @sign of the user.

```<@sign>@```

If the user gets the pkam authentication wrong then it should respond back with the following error and close the connection to the server.

```error:AT0401-Client authentication failed```

**Description:**

The `pkam` verb follows the `from` verb. As an owner of the Secondary Server, you should be able to take the challenge thrown by the `from` verb and encrypt using the private key of the RSA key pair with what the server has been bound with. Upon receiving the `cram` verb along with the digest, the server decrypts the digest using the public key and matches it with the challenge. If they are the same then the secondary lets you connect to the Secondary Server and changes the prompt to your @sign.

**OPTIONS:**

`<digest> `
Required: Yes
Description: Encrypted challenge

### The `stats` verb

**Synopsis:**

The `stats` verb should be used to get the statistics of an atsign.

Following is the regex of the `stats` verb

```stats(?<statId>:((?!0)\d+)?(,(\d+))-)?```

**Response:**

If the user gives stats all the statistics will be returned as JSON. Following statistics are provided:

1. `activeInboundConnections`
2. `activeOutboundConnections`
3. `lastCommitId`
4. `secondaryStorageSize`
5. `topAtSigns`
6. `topKeys`

**Example:**    

```data: [{"id":"1","name":"activeInboundConnections","value":"1"}, {"id":"2","name":"activeOutboundConnections","value":"0"}, {"id":"3","name":"lastCommitID","value":"1"}, {"id":"4","name":"secondaryStorageSize","value":12560}, {"id":"5","name":"topAtSigns","value":{"@bob":1}}, {"id":"6","name":"topKeys","value":{"publickey@alice":1}}]```

Individual statistics can be retrieved using the respective Id.

```
@alice@stats:1
data: [{"id":"1","name":"activeInboundConnections","value":"1"}]
```

### The `sync` verb

**Synopsis:**

The `sync` verb enables to synchronize the keys between the local Secondary Server and remote Secondary Server.

Following is the regex:

```sync:(?<from_commit_seq>[0-9]+$|-1)```

**Response:**

The `sync` verb returns a json array of the commit entries from the given commit id to the current commit id. Further, The `sync` verb accepts -1 as argument which returns all the commit entries.

```
data:[{"atKey":"@bob:phone@alice","operation":"+","opTime":"2020-10-26 11:57:43.732","commitId":0,"value":"12345","metadata":{"ttr":"36000000","ccd":"false"}},
{"atKey":"@bob:shared_key@alice","operation":"-","opTime":"2020-10-26 09:44:54.382219Z","commitId":1}]
```

The `notify` verb

The `notify` verb enables us to notify the atsign user of some data event.

The Following is the regex for the `notify` verb


```notify:((?<operation>update|delete):)?(ttl:(?<ttl>\d+):)?(ttb:(?<ttb>\d+):)?(ttr:(?<ttr>(-)?\d+):)?(ccd:(?<ccd>true|false):)?(@(?<forAtSign>[^@:\s]-)):(?<atKey>[^:]((?!:{2})[^@])+)@(?<atSign>[^@:\s]+)(:(?<value>.+))?```

**Response:**

When a key is notified successfully, returns 


```data:success```

**Description:**

When an atsign user notifies the key to another atsign user, an entry has to be created in received notifications list on the user who has shared the key and an entry has to be created in sent notifications list on the user to whom the key is to be notified. When auto notify is set to true, when a key is created/updated and deleted notification is triggered to another atsign user.


### Notify List

**Synopsis:**

Notify list returns a list of notifications.

Following is the regex

```notify:(list (?<regex>.-)|list$)```

**Response:**

If the user is the owner, returns a list of received notifications. If a user is pol authenticated user, returns a list of sent notifications

```data:[{"id":"0e5e9e89-c9cb-423b-8972-8c5487215990","from":"@alice","to":"@bob","key":"@bob:phone@alice","value":12345,"operation":"update","epochMillis":1603714122636}]```

The `monitor` Verb

**Synopsis:**

The `monitor` verb streams received notifications.

Following is the regex

```^monitor$|^monitor ?(?<regex>.-)?)$```

**Response:**

Returns a stream of notifications.

```
@alice@monitor
notification: {"id":"773e226d-dac2-4269-b1ee-64d7ce93a42f","from":"@bob","to":"@alice","key":"@alice:phone@bob","value":null,"operation":"update","epochMillis":1603714720965}
```
**Description:**

The `monitor` verb accepts an optional parameter to filter the notifications by passing filter criteria as regex to `monitor` verb.

## Error Codes

<table>
  <tr>
   <td>
   <strong>Error Code</strong>
   </td>
   <td><strong>Error Message</strong>
   </td>
   <td><strong>Description</strong>
   </td>
  </tr>
  <tr>
   <td>AT0001
   </td>
   <td>Server exception
   </td>
   <td>Exception occurs when there is an issue while starting the server.
   </td>
  </tr>
  <tr>
   <td>AT0002
   </td>
   <td>DataStore exception
   </td>
   <td>Exception occurs during keystore operations (GET/PUT/DELETE).
   </td>
  </tr>
  <tr>
   <td>AT0003
   </td>
   <td>Invalid syntax
   </td>
   <td>Exception occurs if we give any invalid command to the server.
   </td>
  </tr>
  <tr>
   <td>AT0004
   </td>
   <td>Socket error
   </td>
   <td>Exception occurs when socket connection to secondary cannot be established.
   </td>
  </tr>
  <tr>
   <td>AT0005
   </td>
   <td>Buffer limit exceeded
   </td>
   <td>This exception occurs when input/output message size reaches the maximum limit configured in the server. 
   </td>
  </tr>
  <tr>
   <td>AT0006
   </td>
   <td>Outbound connection limit exceeded
   </td>
   <td>Exception occurs when the number of open connections to other secondaries reaches the maximum limit configured. 
   </td>
  </tr>
  <tr>
   <td>AT0007
   </td>
   <td>Secondary Server not found
   </td>
   <td>Exception occurs when a secondary tries to connect to another secondary which is not available in the root directory or not yet instantiated. 
   </td>
  </tr>
  <tr>
   <td>AT0008
   </td>
   <td>Handshake failure
   </td>
   <td>This exception is for any exception during the handshake process of two secondaries.
   </td>
  </tr>
  <tr>
   <td>AT0009
   </td>
   <td>UnAuthorized client in the request
   </td>
   <td>UnAuthorized Exception
   <p>will occur when an unsuccessful handshake happens between two secondaries.</p>
   </td>
  </tr>
  <tr>
   <td>AT0010
   </td>
   <td>Internal server error
   </td>
   <td>This is for any server related errors.
   </td>
  </tr>
  <tr>
   <td>AT0011
   </td>
   <td>Internal server exception
   </td>
   <td>This exception is used for any server related exceptions.
   </td>
  </tr>
  <tr>
   <td>AT0012
   </td>
   <td>Inbound connection limit exceeded
   </td>
   <td>This exception will occur when the number of active clients reaches the maximum limit configured.
   </td>
  </tr>
  <tr>
   <td>AT0401
   </td>
   <td>Client authentication failed
   </td>
   <td>This exception occurs when client authentication fails or client tries to execute any verb which needs authentication before successful authentication.
   </td>
  </tr>
  <tr>
   <td>AT0013
   </td>
   <td>Connection Exception
   </td>
   <td>This will occur when a blocked user tries to connect to the secondary.
   </td>
  </tr>
  <tr>
   <td>AT0014
   </td>
   <td>Unknown AtClient exception
   </td>
   <td>This exception will be thrown while performing any operations(Get/update/delete) using AtClient SDK.
   </td>
  </tr>
  <tr>
   <td>AT0015
   </td>
   <td>Key not found
   </td>
   <td>This exception will be thrown when the key is not available for encryption/decryption.
   </td>
  </tr>
  <tr>
   <td>AT0021
   </td>
   <td>Unable to connect to secondary
   </td>
   <td>This exception will occur when we are unable to connect to secondary. 
   </td>
  </tr>
</table>

Glossary
> @protocol (Pronounced, at protocol)
<TO DO>

> @sign (Pronounced, at sign)
@sign is a unique name that a user gets when enrolled with @sign.com 

> Root Server
<TO DO>

> Secondary Server
<TO DO>

> Verb
<TO DO>

> Public Key
<TO DO>

> Private Key
<TO DO>

> Shared Secret
<TO DO>

> Default Keys
<TO DO>

> Key
<TO DO>

> Value
<TO DO>

> Metadata
<TO DO>

> Commit Log
<TO DO>

> Access Log
<TO DO>