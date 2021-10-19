---
title: "What is rSDK?"
SEOtitle: "How to migrate your project to latest rSDK changes."
linkTitle: "rSDK Migration"
content: "Everything you need to know before migrating your apps to latest rSDK changes."
weight: 7
nav_children: section
notoc: true
simple_list: true
date: 2021-10-05
---

Resilient SDK (rSDK) is a new major release of the @platform with several
changes to make apps using the SDK more resilient and fault tolerant.  This
guide is intended to help app developers with the use of rSDK.


## What's new?

rSDK offers three major changes:

1. Simpler abstractions
2. Better feedback on the status of an operation
3. Resilience from network failures

## High Level Architecture ##

![high level architecture](/rSDK/high_level_architecture.png)

## Key Abstractions ##

#### **AtClientManager** ####
Factory class responsible for giving the instances of AtClient and other
services for a given @sign.

#### **AtClient** ####
AtClient should be used to perform Create, Read, Update or Delete (CRUD)
operations on the secondary server.

#### **NotificationService** ####
NotificationService should be used to send and receive notifications from
the secondary server.

#### **SyncService** ####
SyncService should be used to keep local and cloud secondary data in sync.


## Sync

Sync in the @protocol is a process to pull or push data between local and
cloud secondary servers to make sure that the data is in sync.

For example, if an app creates a key called phone@bob and saves it to the
local secondary, the Sync process will push that to the cloud secondary server
and make it available to be consumed by another @app on another device.

## Sync triggers

Sync process is triggered in two ways:

1. App sync
2. System sync

**App sync**

Apps on @protocol can request for an invocation of a Sync process by calling
the “sync” method on “SyncService”.  Calling “sync” would not immediately
trigger the Sync process, rather it is taken as a request that needs to be
fulfilled later. For example when a Sync process is requested an app could be
offline but SyncService still accepts the request through the “sync” method
call and fulfills it when the conditions are right for the data transfer.

**System sync**

SDK initiates a Sync process without any apps requesting when SDK detects
that the local and the cloud secondaries are out of sync. 

Please look at [SyncService Dart code docs](https://github.com/atsign-foundation/at_client_sdk/blob/trunk/at_client/lib/src/service/sync_service.dart) for more details on the usage.


## Sync trigger conditions

When a sync request is submitted, SyncService waits for the following
conditions to be fulfilled for the Sync process to be triggered:

1. Number of sync requests should be greater than 3
2. Time difference between the first sync request and now is greater than 5 seconds

**Note:** These internals are subject to change in future versions of SDK
