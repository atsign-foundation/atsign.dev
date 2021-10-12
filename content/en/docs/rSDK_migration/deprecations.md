---
title: "What's deprecated in rSDK?"
SEOtitle: "What is deprecated in rSDK, and what are replacements."
linkTitle: "Deprecations"
Description: "Documentation referring What are all the deprecations happened in rSDK."
content: "Everything you need to know before migrating your apps to latest rSDK changes."
parent: /rSDK_migration/
weight: 4
date: 2021-10-05
---

## **isDedicated** flag

Apps no longer have to use the `isDedicated` flag on `at_client` methods. Sync
will be called on a separate connection with the new SDK implementation. App
developers can remove references to the `isDedicated` flag.

## SyncStrategy

Apps no longer have to set `SyncStrategy` in the preferences. Sync will be
called automatically after any update or delete operation on the `at_client`;
Refer to the Sync section below for more details.

## **notify** method

The method `notify` from `AtClient` is deprecated. Use
`AtClientManager.notificationService` instance to call `notify` method instead.
This method will be taking a positional argument of type `NotificationParams`.

**Usage :**
```dart
/// Get [AtClientManager] instance.
AtClientManager atClientManager = AtClientManager.getInstance();

/// From the [AtClientManager] instance access the `notificationService` instance.
/// Using `NotificationService` instance call the `notify` method. 
atClientManager.notificationService.notify(
    /// With respect to the operation type, 
    /// the notification will be sent to the server.
    NotificationParams.forUpdate(
        atKey,
        value: value,
    ),
);
```

## **getSyncManager** method

The method `getSyncManager` used to get the instance of `SynaManager` is
deprecated in favor of `SyncService`; Can be able to access from
`AtClientManager` instance.

**Usage :**
```dart
/// Get [AtClientManager] instance.
AtClientManager atClientManager = AtClientManager.getInstance();

/// Get [SyncService] instance.
/// Use this sync service instance wherever 
/// you want to perform sync operations.
SyncService _syncServcie = atClientManager.syncService;
```

## **startMonitor** method

The method `startMonitor()` from `AtClient` has been deprecated in favor
of `subscribe()` from `NotificationService`. This method gives a back stream
of notifications from the server to the subscribing client. Optionally pass a
regex to filter notification keys matching the regex.

**Usage :** 
```dart
/// Get [AtClientManager] instance.
AtClientManager atClientManager = AtClientManager.getInstance();

/// Get [NotificationService] instance from [AtClientManager].
NotificationService notificationService = atClientManager.notificationService;

/// Subscribe to notificationService.
/// Pass optional regex to filter notification 
/// keys matching the regex as namespace.
notificationService.subscribe(regex: '.myatapp');
```