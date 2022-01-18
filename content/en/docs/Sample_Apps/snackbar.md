---
title: "SnackBar"
SEOtitle: "SnackBar Demo App on the @platform"
linkTitle: "SnackBar"
Description: "Understand the inner-workings of the Snackbar app"
content: "Understand the inner-workings of the Snackbar app"
weight: 1
date: 2021-12-12
---

SnackBar is a simple end-to-end encrypted application that allows for securely sending snacks (chocolate bars!) to a receiving @sign. Below is the step-by-step process that will assist you in getting the SnackBar application up and running.

{{% pageinfo %}}
Note: This application demo works with two devices. A connected physical device and an emulator is suitable for this demo as well.
{{% /pageinfo %}}

### 1. Get SnackBar Running on your Machine

You are able to download application templates from our at_app project! Copy and paste the following code in your terminal to activate at_app on your machine:

```shell
flutter pub activate at_app
```

{{% pageinfo %}}
Verify your system PATH variable

When you run the command above, it may prompt you that the pub cache bin is missing from the system PATH variable.
The prompts will tell you the appropriate steps to add it to the PATH variable.
Please complete this step before continuing.
{{% /pageinfo %}}

After successfully activating at_app on your machine, simply change directories to where you wish to have your snackbar application exist. After having your desired directory active, copy and paste the following command into your terminal:

```shell
at_app create -d snackbar ...
```

{{% pageinfo %}}
Note: Replace the above "..." with the folder name you wish for the snackbar application to be built within.
{{% /pageinfo %}}

After creating the snackbar application, run the project on your physical device or emulator using the following command:

```shell
cd ...
flutter run
```

{{% pageinfo %}}
Note: Replace the above "..." with the folder name you built the snackbar application.
{{% /pageinfo %}}

### 2. Understand how SnackBar Works

The first thing you will see when the SnackBar application is built and running on your device is the Onboarding screen.

<<Screenshot To Be Added>>

#### How does Onboarding work?

Below is the snippet of code that houses the Onboarding method. After every line of code, documentation has been written to make the code as readable as possible.

```dart
Onboarding(
  context: context, //Build context of the screen

  atClientPreference: atClientPreference!, //This specifies several
  // attributes such as domain and namespace

  domain: AtEnv.rootDomain, // This is pointing the application's connection to
  // the production level of the @protocol

  rootEnvironment: AtEnv.rootEnvironment,

  appAPIKey: AtEnv.appApiKey, // This APIKey makes your application unique from
  // other applications created on the @platform

  onboard: (value, atsign) {
    _logger.finer('Successfully onboarded $atsign');
  }, // This is the onboard function which will take the map of atsigns (which
  // have been authenticated already)/atCLient preferences  along with the current
  // atsign attempting to authenticate.
  // If the authentication is successful, it will be logged and you will be taken
  // to the next screen

  onError: (error) {
    _logger.severe('Onboarding throws $error error');
  }, // If the authentication process fails, an error is thrown

  nextScreen: const HomeScreen(), // The next screen after successful
  // authentication will be the HomeScreen
);
```
