---
title: "What are the changes?"
SEOtitle: "What did we migrate rSDK changes."
linkTitle: "Changes"
Description: "Refernce documentation for rSDK changes."
content: "Everything you need to know before migrating your apps to latest rSDK changes."
parent: /rSDK_migration/
weight: 1
date: 2021-10-05
---

## Get instances of AtClient and other services.

1. To initialize AtClient Instance call setCurrentAtSign method on 
`AtClientManager.getInstance()`.
    
- `setCurrentAtSign` accepts the following arguments: currentAtSign,
namespace and the preferences.

    ```dart
    AtClientManager.getInstance().setCurrentAtSign('@alice', 'wavi', <preferences>);
    ```

2. The `AtClientManger` Instance has getter `atClient` which returns an
instance of `AtClient`.

    ```dart
    AtClient atClient = atClientManager.atClient;
    ```

3. The `AtClientManager` instance has a late initialized variable
`notificationService` which is for accessing notification service methods.

    ```dart
    NotificationService notificationService = atClientManager.notificationService;
    ```

4. The `AtClientManager` instance has a late initialized variable `syncService`
which is for invoking the sync.

    ```dart
    SyncService syncService = atClientManager.syncService;
    ```

**Note**: Above code should be executed every time when the @sign is switched to
get the right instances representing the new @sign.

## Sending and receiving notifications.

1. Get the `AtClientManager` instance initially.

2. Access the `notificationService` variable using atClientManager instance.

3. Listen to notifications via callback and no filter. Ideally you don't
want to do this.

    ```dart
    /// AtClientManager instance.
    AtClientManager atClientManager = AtClientManager.getInstance();

    /// NotificationService variable.
    NotificationService notificationService = atClientManager.notificationService;

    /// Listen to notifications.
    notificationService.subscribe().listen((notification) {
    _notificationCallback(notification);
    });
    ```

4. Listen to notifications via callback and filter notification key by regex.
You can also come up with regexes that match other types of keys. Ex: 
'wavi | buzz' or alternatively multiple listeners can also be registered.
    
    ```dart
    notificationService.subscribe(regex: '.wavi').listen((notification) {
    _notificationCallback(notification);
    });
    ```

5. Send notification. Await variant.
    
    ```dart
    /// AtKey
    AtKey phoneKey = AtKey()
        ..key = 'phone'
        ..sharedWith = '@bob🛠'
        ..sharedBy = '@alice🛠';

    /// AtKey's Value (String)
    String atValue = '+1 100 200 300';

    /// Update the value and capture the notification result.
    NotificationResult notificationResponse = await notificationService
                .notify(NotificationParams.forUpdate(phoneKey, value: atValue));
    ```

6. Validating if a notification failed in the await variant.
    
    ```dart
    if(notificationResponse.notificationStatusEnum == NotificationStatusEnum.undelivered) {
        // Do something on notification error.
        print(notificationResponse.atClientException);
    } else{
        // Do something on successful delivery response.
        print('Successfully delivered notification.');
    }
    ```

7. The other notifications are as follows -

    ```dart
    /// Delete notification
    NotificationResult notificationResponse = await notificationService.notify(NotificationParams.forDelete(phoneKey));

    /// Text notify
    NotificationResult notificationResponse = await notificationService.notify(NotificationParams.forText('phone', '@bob🛠'));
    ```

8. Send notification using Callback.
    
    ```dart
    notificationService.notify(
          NotificationParams.forUpdate(atKey, value: atValue),
          onDone: _onSuccessCallback,
          onError: _onErrorCallback,
          );

    void _onSuccessCallback(notificationResult){
        // Do something on successful delivery response.
        print(notificationResult);
    }

    void _onErrorCallback(notificationResult){
        // Do something on notification error
        print(notificationResponse.atClientException);
    }
    ```

## Syncing the data.

1. The `atClientManger` instance has getter `atClient` which returns an instance
of `AtClient`.

    ```dart
    final AtClient atClient = atClientManager.atClient;
    ```

2. CRUD operations
    
    ```dart
    atClient.put(<params>)
    atClient.delete(<params>)
    ```
    
3. Syncing the data. Apps no longer have to use `SyncStrategy` or 
`isDedicated` flag or manually call `sync`. All sync requests will be
internally kept in a queue and synced to the server at periodic time
interval (approx. 15 seconds). If remote server is updated from some other
device, then those changes will be also synced at periodic intervals.
    
    ```dart
    syncService = atClientManager.syncService;
    ```
    
    -  Optionally, Register to onDone callbacks to get SyncResult when run asynchronously.

    ```dart
    syncService.sync(onDone: _onSuccessCallback);
    void _onSuccessCallback(syncResult){
        print(syncResult);
    }
    ```

4. Optionally, call `setOnDone` for global onDone callback. Call this method
to set the Global onDone callback. This method will be called when a sync is
completed. When a specific onDone function is passed to the sync function, 
then the specific onDone is called.

    ```dart
    syncService.setOnDone(onDone: _onSuccessCallback);
    ```