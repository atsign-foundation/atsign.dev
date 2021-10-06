---
title: "What's deprcatedin rSDK?"
SEOtitle: "What is deprecated in rSDK and what are replacements."
linkTitle: "Deprecations"
Description: "Documentation referring What are all the deprecations happened in rSDK."
content: "Everything you need to know before migrating your apps to latest rSDK changes."
parent: /rSDK_migration/
weight: 4
date: 2021-10-05
---

## `isDedicated` flag

Apps no longer have to use the `isDedicated` flag on at_client methods. Sync will be called on a separate connection with the new SDK implementation. App developers can remove references to the isDedicated flag.

## Sync Strategy

Apps no longer have to set `SyncStrategy` in the preferences. Sync will be called automatically after any update or delete operation on the at_client. Refer to the Sync section below for more details.

## `notify` method

## `getSyncManager` method

## `encryptUnEncryptedData` method