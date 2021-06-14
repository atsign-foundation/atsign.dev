---
title: "Widgets"
linkTitle: "Widgets"
weight: 3
nav_children: section
notoc: true
simple_list: true
description: >
  Low level reference docs for your project.
---

### The Onboarding Widget

Onboarding for the first time with the @platform isn’t as simple as choosing your @sign from a dropdown menu and clicking “Login” (after all, how would the application know where to retrieve your authentication keys from a given @sign?). 

Implementing onboarding from scratch would be painstakingly difficult. Not only would you have to code the PKAM logic, but you would also have to build your own QR code scanner to extract the CRAM (Challenge-Response Authentication Mechanism) key from your @sign’s QR code generated on our website! The @ Company realized this very quickly, so we developed the at_onboarding_flutter widget to help developers who want to build production-level apps that onboard real @signs (AKA @signs that you get from our .com site).

```
at_onboarding_flutter: ^1.0.0+4
```

 
The “Onboarding” widget is very handy in that you do not need to call the “onboard” or “authenticate” methods from the service file of the application to get it running. Instead, it will ask us to specify the following parameters (descriptions for each parameter are written in the comments):

```dart
class Onboarding {
 ///Required field as for navigation.
 final BuildContext context;

 ///Onboards the given [atsign] if not null.
 ///If [atsign] is null then it takes the atsign from keychain.
 ///If [atsign] is empty then it directly jumps into authenticate 
 ///without performing onboarding. (or)
 ///If [atsign] is empty then it just presents pairAtSign screen 
 ///without onboarding the atsign. (or)
 ///Just provide an empty string for ignoring existing atsign in 
 ///keychain or app's atsign.
 final String atsign;

 ///The atClientPreference [required] to continue with the onboarding.   
 ///atClientPreference is an instance of a class in the  
 ///at_client_mobile library that stores a number of important 
 ///attributes like the namespace of the application, the CRAM key of  
 ///an @sign, the root domain we want the project to communicate 
 ///with, and so on. 
 final AtClientPreference atClientPreference;

 ///The root domain for our project. By default, the plugin connects 
 ///to [root.atsign.org] to perform onboarding.
 final String domain;

 ///The color of the screen to match with the app's aesthetics. 
 ///default it is [black].
 final Color appColor;

 ///If logo is not null, then it displays the widget on the left side 
 ///of appbar. Else, it displays nothing.
 final Widget logo;

 ///Function returns atClientServiceMap on successful onboarding along 
 ///with onboarded @sign. Assign these returned values to the relevant 
 ///variables in your project’s service file.
 final Function(Map<String, AtClientService>, String) onboard;

 ///Function returns error if onboarding fails for an @sign.
 final Function(Object) onError;

 ///After successful onboarding, the app will be redirected to this 
 ///screen if it is not null.
 final Widget nextScreen;

 ///After the first successful onboarding, the app will get redirected 
 ///to this screen if not null.
 final Widget fistTimeAuthNextScreen;

 final AtSignLogger _logger = AtSignLogger('At Onboarding Flutter');

 Onboarding({Key key,
   @required this.context,
   this.atsign,
   @required this.onboard,
   @required this.onError,
   this.nextScreen,
   this.fistTimeAuthNextScreen,
   @required this.atClientPreference,
   this.appColor,
   this.logo,
   this.domain})
 ...
}
```


To see an actual implementation of the onboarding widget, let’s revisit the _login function in the at_hello_world app with some updated code:


```dart
/// Return an “Onboarding” widget that walks the individual through
/// the onboarding procedure for any real @sign.
_login() async {
 return Onboarding(
     context: context,
     /// Ensure that the “root” attribute is assigned to 
     /// “root.atsign.org” 
     domain: AtConfig.root
     atClientPreference: await 
        _serverDemoService.getAtClientPreference(),
     appColor: Color.fromARGB(255, 240, 94, 62),
     onboard: (atClientServiceMap, atsign) {
       _serverDemoService.atClientServiceMap = atClientServiceMap;
       _serverDemoService.atSign = atsign;
     },
     onError: (error) {
       print(error);
     },
     /// Remove the constructor in HomeScreen. You can call the @sign
     /// with the getAtSign() method in the service file. 
     nextScreen: HomeScreen(),
 );
}
```


All of the parameters in the “Onboarding” widget can be populated very easily with either methods from the project’s service file (e.g. getAtClientPreference()) or special variables from the app itself (e.g. context). “Onboarding” is capable of handling all instances of an @sign (e.g. a particular @sign does not exist, a particular @sign exists but needs to be paired with a QR code to the device, a particular @sign exists and its keys are already in the device’s keychain manager). By using this widget, what would have taken several screens and many lines of code can be completely bypassed with a single return statement!

That’s all for the “Onboarding” widget. Before moving on from this subsection, we highly recommend implementing the widget in your own application and onboarding a real @sign to understand its intended user journey. If you’re interested, these are the steps to implement the “Onboarding” widget in the at_hello_world project:

Update your Android Studio, Flutter SDK, and Dart SDK to their latest versions. Place the at_onboarding_flutter dependency in pubspec.yaml.
Follow the setup procedure for the “Onboarding” widget in the “AndroidManifest” (android -> app -> src -> main -> AndroidManifest.xml) and “gradle” file (android -> app -> build.gradle) of the at_hello_world project. You may also need to update the “classpath” of the android gradle build tool to 3.5.4 (this can be done by going to android -> gradle -> build.gradle and editing the first classpath in the “dependencies” brackets). This must be completed in order to set up the permission for the QR code scanner to access your camera. Find those steps on the pub.dev site for at_onboarding_flutter here.
Get a free @sign from atsign.com. Generate its QR code, and drag/drop the created file directly into the emulator. Confirm that the QR code image appears in the “Files” or “Drive” app of the emulator you’re using (assuming that it is an Android emulator).
In “at_conf.dart”, update the “root” variable from 'vip.ve.atsign.zone' to 'root.atsign.org'. This ensures that the project points to the domain that is used in production as opposed to the one for the virtual environment.
Replace the existing code in the _login() function with what we wrote above. Double-check that no errors arise (you’ll likely have to tweak the names of a couple of methods in the service file, because some of them begin with the “_” private designation). 
Fire the app on your emulator. Although the dropdown menu will still appear (since we didn’t change any of that code), we will not be authenticating with any of the testable @signs. If you’d like, simply remove the “DropdownButton” widget so that we can eliminate the list of testable @signs. Click on the “Login” button.
Assuming that you haven’t previously authenticated with a real @sign, the “Onboarding” widget should prompt you with a request to upload your QR code. Upload the QR code you saved onto the emulator earlier and wait for the authentication to complete.
If no errors form, the “Onboarding” widget should take you seamlessly to the “Home” screen, where you can add & retrieve key/value pairs directly from your very own secondary server! The next time you authenticate (i.e. restart the application), the “Onboarding” widget should detect the authentication keys placed in your device’s keychain manager and guide you directly to the “Home” screen.

