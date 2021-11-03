---
title: 'Create your own @platform project'
SEOtitle: 'How to create an @platform (at_platform or AtPlatform) project'
linkTitle: 'Create an app'
Description: 'Taking one step closer to developing your privacy-first app on the @platform'
content: 'What to do after creating your own @sign'
weight: 3
date: 2021-7-26
---

If you've ever used Flutter and have gone through the process of creating a new Flutter Application Project, you're more than likely aware of what a fresh application should look like. We've decided to create our own toolkit here on the @platform to make your 'Getting Started' experience that much smoother!

As of now, the only way to use this toolkit is via the command line. In the future we plan on supporting IDE extensions, be sure to check for when those come out!

## Getting started via the command line

[at_app](https://pub.dev/packages/at_app) is our command line toolkit that can be installed via pub. Behind the scenes, it uses flutter create in order to create your project, and it completes the necessary steps to setup your @platform application for you!

### Install the command line toolkit

```sh
flutter pub global activate at_app
```

{{% pageinfo color="primary" %}}
Verify your system PATH variable

- When you run the command above, it may prompt you that the pub cache bin is missing from the system PATH variable.
- The prompts will tell you the appropriate steps to add it to the PATH variable.
- Please complete those steps before continuing.
  {{% /pageinfo %}}

### Run the program

{{% pageinfo color="primary" %}}
Note for Windows users

- In the following commands you will see the `at_app` command, please replace it with `at_app.bat`.
  {{% /pageinfo %}}

### Command Format

```sh
at_app create [...options] path/to/your/project
```

In practice the command looks like this:

```sh
at_app create --namespace=myatsign myproject
```

In addition to the same options available for flutter create, at_app create includes three new ones to help you automatically configure your application.

| Flag           | Shorthand | Description                                             | Value                |
| -------------- | --------- | ------------------------------------------------------- | -------------------- |
| -‎-namespace   | -n        | The @protocol app namespace to use for the application. | (defaults to "‎")    |
| -‎-root-domain | -r        | The @protocol root domain to use for the application.   | [prod (default), ve] |
| -‎-api-key     | -k        | The api key for at_onboarding_flutter.                  | (defaults to "‎")    |

Note: at_app create **does not** include `--template`, `--sample`, or `--list-samples` (Coming soon).

Okay great, we know what the flags are but what do they do?

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

### Updating your configuration

If you would like to update your environment at any point in time, it is safe to do so. Just specify the options you would like to change.

{{% pageinfo color="primary" %}}
Warning

- Do not use the `--overwrite` flag when doing so, or it will overwrite the changes you have made to `lib/main.dart`
  {{% /pageinfo %}}

### Congratulations!

You have successfully created your first @platform application!

Time to start coding!

### Where should I go next?

We recommend checking out the demo apps that we have to offer! Reviewing these will greatly assist in your understanding of verb implementation on the @platform! It would also be a good idea to check out our @dev program which will show you how to have your app @certified and released to the market!

- [Sample Apps](/docs/sample-apps/): See apps that show off the power of the @platform on your own machine!

- [@dev Program](/dev_tools/): Read up on how to get your @certification and go to market with your privacy-focused application!
