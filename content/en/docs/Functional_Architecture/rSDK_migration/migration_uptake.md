---
title: "How to migrate?"
SEOtitle: "How to migrate your project to latest rSDK changes."
linkTitle: "Uptake"
Description: "Documentation referring how to migrate your project to latest rSDK."
content: "Everything you need to know before migrating your apps to latest rSDK changes."
parent: /rSDK_migration/
weight: 2
date: 2021-10-05
---

If you have gone through the [rSDK changes](/docs/rsdk_migration/changes),
migrating your app will be easy. If you are ready to migrate your project to
latest rSDK changes, then you are good to go.


## Get instance of atClient.

- `AtClientImpl` has been replace with `AtClientManager` instance.

- `createClient` method has been removed and replaced with `setCurrentAtSign`.

- `atClient` instance can be obtained through `atClientManager` instance.

```dart
/// **SDK 2.X**

await AtClientImpl.createClient('@alice', 'wavi',  <preference>);
var atClient = await (AtClientImpl.getClient(atsign));
```

```dart
/// **SDK 3.X**

var atClientManager = await AtClientManager.getInstance().setCurrentAtSign('@alice', 'wavi', <preference>);
final atClient = atClientManager.atClient;
```

## Starting listening to notifications.

- `startMonitor` method has been removed. With rSDK you must subscribe and listen to `atClient` instance's `NotificationService`.

- `subscribe` method takes a optional parameter `regex` to filter the notifications.

- Decoding the response on callback function is not required.

```dart
/// **SDK 2.X**

await atClient!.startMonitor(<private_key>, _notificationCallBack, regex: 'atmosphere');

void _notificationCallBack(var response) {
    response = response.replaceFirst('notification:', '');
    var responseJson = jsonDecode(response);
    var notificationKey = responseJson['key'];
    var fromAtSign = responseJson['from'];
    // ....... REST CODE .......
}
```

```dart
/// **SDK 3.X**

atClientManager.notificationService.subscribe(regex: 'wavi').listen(_notificationCallBack);

void _notificationCallBack(AtNotification atNotification) {
    var notificationKey = atNotification.key;
    var fromAtSign = atNotification.from;
    // ....... REST CODE .......
}
```

## Send notifications.

- To send notification, you must use `AtClientManager` instance's
`NotificationService` to access `notify` method.

- `notify` method takes a positional parameter `NotificationParams`.

- The `NotificationParams` has all the methods depending to the operation you
do.

    - `forUpdate()` - To send update notification.
    - `forDelete()` - To send delete notification.
    - `forText()` - To send a text message to another atSign.

```dart
/// **SDK 2.X**

await AtClientImpl.createClient('@alice', 'wavi', <preference>);
atClient = await (AtClientImpl.getClient('@alice')); 
AtKey atKey = AtKey()..key = 'phone'
                   ..sharedWith = '@bob'
                   ..sharedBy = '@alice';
String atValue = '+1 445 446 7879';
atClient.notify(atKey, atValue, OperationEnum.update);
```

```dart
/// **SDK 3.X**

AtClientManager atClientManager = await AtClientManager.getInstance()
    	.setCurrentAtSign(‘@alice’, 'wavi', <preference>);
AtClient atClient = atClientManager.atClient;
AtKey atKey = AtKey()..key = 'phone'
                   ..sharedWith = '@bob'
                   ..sharedBy = '@alice';
String atValue = '+1 445 446 7879';
NotificationResult result  = await atClientManager.notificationService
                        .notify(NotificationParams.forUpdate(atKey, value: atValue));
```

## Check whether local and remote server are in sync.

- Instead of using `SyncManager`, use `SyncService` to access `isInSync`
method.

- You must use `AtClientManager` instance's `SyncService` to access
`isInSync` method.

```dart
/// **SDK 2.X**

final syncManager = atClient.getSyncManager();
bool isInSync = await syncManager.isInSync();
```

```dart
/// **SDK 3.X**

final syncService = atClientManager.syncService;
bool isInSync = await syncService.isInSync();
```

## Calling on demand sync.

- This may not be needed by all apps with new SDK changes. sync is performed
automatically on any update/delete operation on atClient.

```dart
/// **SDK 2.X**

final syncManager = atClient.getSyncManager();
await syncManager.sync();
```

```dart
/// **SDK 3.X**

final syncService = atClientManager.syncService;
syncService.sync(); 
```
