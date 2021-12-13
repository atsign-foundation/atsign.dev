---
title: "What's new with rSDK?"
SEOtitle: "What is new with rSDK and how to use it."
linkTitle: "Enhancements"
Description: "Documentation referring What is new with rSDK and how to use it."
content: "Everything you need to know before migrating your apps to latest rSDK changes."
parent: /rSDK_migration/
weight: 3
date: 2021-10-05
---

## Network availability callback service.

Apps can subscribe to the network availability callback service to know when
the network goes off and on. Some of the services offered by SDK is
subscribing to this service internally.

 ```dart
final ConnectivityListener connectivityListener = ConnectivityListener();
connectivityListener.subscribe().listen((isConnected) {
if(isConnected) {
print('connected');
} else {
print('disconnected');
}
});

// call this when app is closed or you no longer need the subscription
connectivityListener.unSubscribe() 
```

## Response objects.

Notification Response Object.

```dart
class AtNotification {
late String id;
late String key;
late String from;
late String to;
late int epochMillis;
String? value;
String? operation;
}
```

Sync Response Object

```dart
class SyncResult {
SyncStatus syncStatus = SyncStatus.not_started;
AtClientException? atClientException;
DateTime? lastSyncedOn;
bool dataChange = true;
}
enum SyncStatus { not_started, success, failure }
```