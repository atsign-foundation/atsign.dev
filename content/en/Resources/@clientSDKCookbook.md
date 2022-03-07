---
title: "The @client/AtClient SDK Cookbook"
SEOtitle: "@client SDK Cookbook part of the @platform (at_platform or AtPlatform)"
linkTitle: "@client SDK Cookbook"
weight: 1
content : This cookbook contains recipes that demonstrate how to solve common problems while writing apps that implement the @protocol(at_protocol or atprotocol). Each recipe is self-contained and can be used as a reference to help you build up an application.
description: This cookbook contains recipes that demonstrate how to solve common problems while writing apps that implement the @protocol. Each recipe is self-contained and can be used as a reference to help you build up an application.
---



# **The Verb tree**

Before we look at some of the sample code, the verb tree gives you a big picture of all of the verbs and what can be executed where.



![alt_text](/Resources/verbtree.png "Verb Tree")


##  1. Scan

The scan verb is used to scan the available @ addresses for you either at the public level or all authorized data once the pol process has been completed. This allows addresses to be discovered and perhaps be harvested so if an address has a _ character as its first character then it is omitted from the scan list although it can still be looked up if known. The following example shows just that.

Following are the steps to run the scan verb using the @Client SDK



1. Get an instance of AtClient
2. Execute the scan verb using the AtClient

#### 1.1 Get an instance of AtClient


To get an instance of the AtClient by calling the getClient method on the Client Impl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // Namespace is mandatory to be passed. E.g me, buzz, etc.,
  await AtClientImpl.createClient('@bob','me', preference);
  var atClient = await AtClientImpl.getClient('@bob');
}
```



#### 1.2 Execute the scan verb using @AtClient



##### a.Simple Scan - Returns all keys

```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
// Scans keys stored in app storage
await atClient.getKeys();
```


##### b.Scan keys matching a regular expression
 ```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
// Scans keys in .me namespace
await atClient.getKeys(regex:'.me');
```


##### c.Scan keys shared with another atSign
 ```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
// Scans keys shared with @alice
await atClient.getKeys(sharedWith:'alice');
```


##### d.Scan keys shared by another atSign
 ```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
// Scans keys shared by @alice. This performs authenticated scan on @alice's secondary.
await atClient.getKeys(sharedBy:'alice');
```





## 2. Update

Update verb used to add entries in the @server. @signs have to be authenticated for one to run the update verb on the @server. 

Following are the steps to run the scan verb using the @Client SDK



1. Get an instance of AtClient
2. Execute the update verb using the AtClient


#### 2.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  //create atClient
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```



#### 2.2 Execute the update verb using AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// create phoneKey
var phoneKey = AtKey()..key = 'phone';
// Update a phone number visible only to @bob
await atClient.put(phoneKey, ''+1-123-4567');
// create emailKey
var emailKey = AtKey()..key = 'email'
                      ..sharedWith = '@alice';
// Update an email visible only to @alice
await atClient.put(emailKey, 'bob@atsign.com');
// Update an email visible only to everyone
// create metadata with isPublic true
var metadata = Metadata()..isPublic=true;
// create emailKey and update metadata
var emailKey = AtKey()..key = 'email'
                      ..metadata = metadata;
await atClient.put(emailKey, 'bob@gmail.com');
// Update a location that expires in 10 minutes
 var metadata = Metadata()..ttl=600000;
var locationKey = AtKey()..key = 'current_location'
                      ..metadata = metadata;
await atClient.put(locationKey, 'https://goo.gl/maps/Trs5Dao562tLFK5Q9');
```



## 3. Lookup

The lookup verb is used to lookup a value on a @server of another @sign. The following demonstrates the use of lookup verb.

Following are the steps to run the scan verb using the @Client SDK

#### 3.1 Get an instance of AtClient


To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  // Get 
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```


####  3.2 Execute the lookup verb using AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// Look up phone number sharedBy @alice
//lookup:phone.me@alice
var atKey = AtKey()..key = 'phone'
                   ..sharedBy = '@alice';
await atClient.get(atKey);
```


## 4. Plookup

The plookup verb is used to lookup a public value on a @server of another @sign if the client is authenticated. Plookup verb can only be executed on a remote @server. The following demonstrates the use of plookup verb.

Following are the steps to run the scan verb using the @Client SDK

####  4.1 Get an instance of AtClient


To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  //Get 
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```

#### 4.2 Execute the plookup verb using AtClient

```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// plookup public phone number of @alice
var metadata = Metadata()..isPublic=true;
var publicPhoneKey = AtKey()..key = 'phone'
                            ..sharedBy = '@alice'
                            ..metadata = metadata;
await atClient.get(publicPhoneKey);

```

## 5. Llookup

The llookup verb is used to lookup a value on a local @server storage of current @sign.  The following demonstrates the use of llookup verb.


####  5.1 Get an instance of AtClient


To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  //Get 
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```

####  5.2 Execute the llookup verb using AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// Local lookup a self key e.g @bob:email.me@bob
var privateEmailKey = AtKey()
 ..key = 'email'
 ..sharedWith = '@bob';
var alicePrivateEmail = await atClient.get(privateEmailKey);
// Local lookup phone shared with @alice e.g @alice:email.me@bob
var phoneKey = AtKey()
 ..key = 'phone'
 ..sharedWith = '@alice';
await atClient.get(phoneKey);
// Local lookup a public key 
var metadata = Metadata()..isPublic=true;
var firstnameKey = AtKey()
 ..key = 'firstname'
 ..metadata = metadata;
await atClient.get(firstnameKey);
// Local lookup a key ignoring namespace
var metadata = Metadata()..namespaceAware=false;
var firstnameKey = AtKey()
 ..key = 'firstname'
 ..metadata = metadata;
 await atClient.get(firstnameKey);

```



## 6. Delete

The “delete” verb is used for deleting @addresses.

Following are the steps to run the scan verb using the @Client SDK


#### 6.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // create AtClient 
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```

#### 6.2 Execute the delete verb using AtClient

```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// delete self key e.g @bob:phone.me@bob
var phoneKey = AtKey()..key = 'phone'
                      ..sharedWith = '@bob';
await atClient.delete(phoneKey);
// delete email shared with @alice e.g @alice:phone.me@bob
var phoneKey = AtKey()..key = 'phone'
                      ..sharedWith = '@alice';
await atClient.delete(phoneKey);

// delete a public key e.g public:phone.me@bob
var metadata = Metadata()..isPublic=true;
var phoneKey = AtKey()
 ..key = 'phone'
 ..metadata = metadata;
await atClient.delete(phoneKey);

```



## 7. Stats

The “stats” verb is used to get certain predefined statistics from the @server. 

#### 7.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // Get 
  var atClient = await AtClientImpl.createClient('@bob', 'me', preference);
}

```

#### 7.2 Execute the stats verb using AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
// Execute the verb e.g stats:1,stats:1,2 etc.,
// You can use stats number from 1 to 10
// If you want to request multiple types use as , separated values
// Ex: stats:1,2,5
await atClient.getRemoteSecondary().executeCommand('stats:1');

```



## 8. Config

The “config” verb is used to configure block list entries in the @server. If an @sign is added to the block list then connections to the @server will not be accepted.

Following are the steps to run the scan verb using the @Client SDK



1. Get an instance of AtClient
2. Set up a ConfigVerbBuilder & execute the verb using the AtClient


#### 8.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // Get 
  var atClient = await AtClientImpl.getClient('@bob', preference);
}

```



#### 8.2 Set up a ConfigVerbBuilder & execute the verb using the AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob, AtClientPreference());
var builder = ConfigVerbBuilder()..block = '@rachel';
// Execute the verb
await atClient.getLocalSecondary().executeVerb(builder);

```



## 9. Notify

The “notify” verb is used to notify another @server of change related to a @address. 

Following are the steps to run the notify verb using the @Client SDK



1. Get an instance of AtClient
2. Set up a NotifyVerbBuilder
3. Execute the scan using the AtClient


#### 9.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // Get 
  var atClient = await AtClientImpl.getClient('@bob');
}
```


#### 9.2 Execute the notify verb using AtClient


```
// Create Atclient Instance
await AtClientImpl.createClient('')
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
var atKey = AtKey()
..key = 'phone@bob'
..sharedWith = '@alice'
..sharedBy = '@bob'
// Execute the verb
await atClient.notify(atKey, '+1 987 986 2233', OperationEnum.update);
// Sending Notification with Notification Strategy 'ALL'
await atClient.notify(atKey, '+1 987 986 2233', OperationEnum.update, 
                      priority: PriorityEnum.low,
                      strategy: StrategyEnum.all);

// Sending Notification with Notification Strategy 'Latest N'
await atClient.notify(atKey, '+1 987 986 2233', OperationEnum.update, 
                      priority: PriorityEnum.high,
                      strategy: StrategyEnum.latest,
                      latestN:3,  
                      Notifier: 'wavi');                                               
```



#### 9.3 Execute the notify status verb using AtClient


```
// Create Atclient Instance
await AtClientImpl.createClient('')
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob);
var atKey = AtKey()
..key = 'phone@bob'
..sharedWith = '@alice'
..sharedBy = '@bob'
// Execute the notify verb
var notiticationId = await atClient.notify(atKey, '+1 987 986 2233', OperationEnum.update);
// get notification status of the above notificationId
var status = await atClient.notifyStatus(notificationId);                                              
```



## 10. Monitor

The “monitor” verb is used to stream incoming notifications from the @server to @Client.

Following are the steps to run the notify verb using the @Client SDK



1. Get an instance of AtClient
2. Execute the monitor using the AtClient


#### 10.1 Get an instance of AtClient

To get an instance of the AtClient by calling the getClient method on the AtClientImpl class.


```
import 'package:at_client/at_client.dart';
import 'package:at_client/src/client/at_client_impl.dart';

void main() async  {
  
  // Construct  AtClientPreference
  var preference = AtClientPreference();
  preference.hiveStoragePath = '/hive/storage/path';
  preference.commitLogPath = '/commit/log/path';
  // Get 
  var atClient = await AtClientImpl.getClient('@bob', preference);
}

```



#### 10.2 Execute the monitor verb using AtClient


```
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
var builder = MonitorVerbBuilder();
// Execute the verb
await atClient.startMonitor(<privateKey>,<NotificationCallback>);

```



```
//Using Regex on Monitor verb
// Get an instance of AtClient for @bob
var atClient = await AtClientImpl.getClient('@bob');
var builder = MonitorVerbBuilder();
// Execute the verb
await atClient.startMonitor(<privateKey>,<NotificationCallback>,regex: '.wavi');
```



## Verb Parameter Reference

**required* optional’**


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
   <td>atSign<strong>*</strong>  -   @ sign you claim to be
   </td>
  </tr>
  <tr>
   <td><strong>cram</strong>
   </td>
   <td>digest<strong>*</strong>    -   SHA512 digest
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
   <td> ttl<strong>’</strong>             - Time to live in milliseconds. Value for the key won't be available after the ttl’
<p>
ttb<strong>’</strong>             - Time to birth in milliseconds. Value for the key will be available after the ttb’
<p>
Scope<strong>’</strong>       - Public vs Private
<p>
forAtSign<strong>*</strong> - For whom the value is being set 
<p>
atKey<strong>*</strong>        - Name of the @address
<p>
value<strong>*</strong>         - Value for the @address
   </td>
  </tr>
  <tr>
   <td><strong>lookup</strong>
   </td>
   <td>atKey<strong>*</strong>   - Name of the @address
<p>
atSign<strong>*</strong>  - @ signs namespace
   </td>
  </tr>
  <tr>
   <td><strong>llookup</strong>
   </td>
   <td>atKey<strong>*</strong>   - Name of the @address
<p>
atSign<strong>*</strong>  - @ signs namespace
   </td>
  </tr>
  <tr>
   <td><strong>plookup</strong>
   </td>
   <td>atKey<strong>*</strong>   - Name of the @address
<p>
atSign<strong>*</strong> - @ signs namespace
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
   <td>statId<strong>’</strong> - Id’s of the statistics to display 
   </td>
  </tr>
  <tr>
   <td><strong>config</strong>
   </td>
   <td>whatToConfig<strong>*</strong> - Thing to configure  
<p>
configValue<strong>*</strong>     - Value of the thing to configure
   </td>
  </tr>
  <tr>
   <td><strong>notify</strong>
   </td>
   <td>forAtSign<strong>*</strong>  - @sign to notify
<p>
key<strong>*</strong>             - Key to which the change has happened
<p>
change<strong>*</strong>     - Change it self
   </td>
  </tr>
  <tr>
   <td><strong>monitor</strong>
   </td>
   <td>regex<strong>’</strong>         - Regex that needs to be matched for the value to be monitored   
   </td>
  </tr>
</table>


