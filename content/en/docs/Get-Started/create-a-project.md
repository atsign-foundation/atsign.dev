---
title: "Create your own @platform project"
SEOtitle: "How to create an @platform (at_platform or AtPlatform) project"
linkTitle: "Try the @platform"
Description: "Taking one step closer to developing your privacy-first app on the @platform"
content: "What to do after creating your own @sign"
weight: 1
date: 2021-12-12
---

<!-- If you've ever used Flutter and have gone through the process of creating a new Flutter Application Project, you're more than likely aware of what a fresh application should look like. We've decided to create our own toolkit here on the @platform to make your 'Getting Started' experience that much smoother!

As of now, the only way to use this toolkit is via the command line. In the future we plan on supporting IDE extensions, be sure to check for when those come out! -->

## Creating the Snackbar Sample App

### Get started via the command line

[at_app](https://pub.dev/packages/at_app) is our command line toolkit that can be installed via pub. Behind the scenes, it uses flutter create in order to create your project, and it completes the necessary steps to setup your @platform application for you!

### Step 1) Install the command line toolkit (at_app)

```sh
flutter pub global activate at_app
```

{{% pageinfo color="primary" %}}
Verify your system PATH variable

- When you run the command above, it may prompt you that the pub cache bin is missing from the system PATH variable.
- The prompts will tell you the appropriate steps to add it to the PATH variable.
- Please complete those steps before continuing.
  {{% /pageinfo %}}

### Step 2) Create the project

{{% pageinfo color="primary" %}}
Note for Windows users

- In the following commands you will see the `at_app` command, please replace it with `at_app.bat`.
  {{% /pageinfo %}}

Using command format:

```sh
at_app create [...options] path/to/your/project
```

In practice the command looks like this:

```sh
at_app create --namespace=@myatsign myproject
```

In addition to the same options available for flutter create, at_app create includes three new ones to help you automatically configure your application. If you wish to learn more about these flags, read about them more in-depth [here](/docs/faqs/atapp/).

| Flag           | Shorthand | Description                                             | Value                |
| -------------- | --------- | ------------------------------------------------------- | -------------------- |
| -‎-namespace   | -n        | The @protocol app namespace to use for the application. | (defaults to "‎")    |
| -‎-root-domain | -r        | The @protocol root domain to use for the application.   | [prod (default), ve] |
| -‎-api-key     | -k        | The api key for at_onboarding_flutter.                  | (defaults to "‎")    |

Note: at_app create **does not** include `--template`, `--sample`, or `--list-samples` (Coming soon).

### Step 3) Implement the Snackbar Receiver code

### Step 3) Implement your own code

You can git clone the project <a href="https://github.com/cconstab/snackeater" target="_blank">here</a>.

<iframe src="https://cconstab.github.io/snackbar/#/" title="Snackbar Code" style="height: 350px; width: 62vw;"></iframe>

#### Congratulations!

You have successfully created your first @platform application!

Time to start coding your own end-to-end encrypted projects!

### Where should I go next?

We recommend checking out the demo apps that we have to offer! Reviewing these will greatly assist in your understanding of verb implementation on the @platform! It would also be a good idea to check out our @dev program which will show you how to have your app @certified and released to the market!

- [Sample Apps](/docs/sample-apps/): See apps that show off the power of the @platform on your own machine!

- [@dev Program](/dev_tools/): Read up on how to get your @certification and go to market with your privacy-focused application!
