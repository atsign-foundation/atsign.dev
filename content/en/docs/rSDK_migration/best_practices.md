---
title: "What are the best practices?"
SEOtitle: "Practice it in the best way you can."
linkTitle: "Best practices"
parent: /rSDK_migration/
weight: 5
date: 2021-10-05
---

- Do not cache instances of `AtClient` or any other services in the app code.
Always make use of "AtClientManager" to get the right instance.


- Subscribe to only specific notifications.

    - Secondary servers send certain system-level notifications to the SDK.
    All of these system notifications will not be of interest to the apps.


- Use response parsers where the app has to deal with raw responses from the
server.

    - Secondary servers send responses in various forms for various verbs.
    Ideally, app developers should not have to know the specific response
    format. Response parsers are made available in SDK to parse these
    responses and give back simple beans that the app can operate on.


- Build feedback loops into the apps when an operation fails

    - For example, if @X wants to notify @Y, the operation might fail for
    many reasons. The SDK would let the caller know the reason for the
    failure. It is better to act on the failure in the app code. It could
    be as simple as logging it.


- Do not write any services to optimize the SDK code. There is a good chance
that we are already working on it. Make sure that you raise an enhancement
request for any such requirement. 


- Use sync with regex with caution. It is advised to use without regex unless
you are sure about it.
