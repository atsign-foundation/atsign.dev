---
title: "at_app FAQs"
SEOtitle: "at_app  FAQs on the @platform (at_platform or AtPlatform)"
linkTitle: "at_app FAQs"
nav_children: section
notoc: true
simple_list: true
weight: 5
date: 2021-07-29
content: FAQs for at_app on the @platform
description: >
  FAQs for at_app on the @platform
---

### What are the different flags that can be used with at_app?

#### Namespace

The namespace is the most important flag to include when creating your application.

When storing keys on the secondary server, the namespace is used to filter the data produced by your app from the other @platform applications.
To create a namespace for your app, make sure to register an @sign from [atsign.com](https://atsign.com) and use that as your namespace. By owning the @sign, you can ensure that you also own the namespace.

You can specify the namespace with `--namespace=YOUR_NAMESPACE_HERE`.

#### Root Domain

By default the root domain is set to prod (production). In the production domain, you can use real @signs to test your application.

Alternatively you can specify `--root-domain=ve` in the command to choose the virtual environment, and test with those @signs instead.

#### API Key

When you are ready to publish your application, you can request an api-key for the [Onboarding Widget](https://pub.dev/packages/at_onboarding_flutter). This api-key will authorize your app when attempting to generate a free @sign within the widget.

You can specify this with `--api-key=YOUR_API_KEY_HERE`.

<!-- ## Can I Update my at_app configuration?

If you would like to update your environment at any point in time, it is safe to do so. Just specify the options you would like to change.

You can reconfigure your at_app project simply by recalling the `at_app create` command with any of the new flags or adjustments you wish to make. -->

<!-- {{% pageinfo color="primary" %}}
Warning

- Be careful of using the `--overwrite` flag when updating your configuration. This will overwrite any changes you have made to `lib/main.dart`
  {{% /pageinfo %}} -->
