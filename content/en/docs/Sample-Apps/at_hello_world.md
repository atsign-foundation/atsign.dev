---
title: "at_hello_world"
linkTitle: "at_hello_world"
weight: 1
date: 2017-01-05
description: >
  Not sure where to start? Take a look at our at_hello_world app to see how some of the common verbs and methods of the @protocol are applied and implemented.
---

If you have gone through the steps of setting up the virtual environment and wish to learn how to implement a few common verbs and methods of the @platform, we highly recommend walking through the at_hello_world application.

Below, you can see a small demonstration of how the at_hello_world application works.

<p align="center">
  <img src="/Sample_Apps/hello_world_demo.gif" alt="at_hello_world" height= "520px" width= "300px"/>
</p>

<div style= "background-color:#F05F3E;color:white; min-height:100px;width:200px;position:relative; float:right;padding:10px;margin-bottom:20px;margin-left: 20px;">
<h3> tl;dr </h3>
Overview too long for you? Watch the <u>
<a href="https://www.youtube.com/watch?v=4VZKuLiHsbU&t=807s" style="color: white;">Tyler Time</a></u> episode that covers this instead!
</div>

## Overview of the at_hello_world app

"at_hello_world" is a bit of a misnomer. Beyond the fact that this app does a lot more than printing “Hello World!” on the console of your IDE, if you lift its hood, you’ll find a tremendous amount of stuff going on (tracing all the functions called in the server_demo_service.dart file will get you several abstraction layers deep into the @protocol!). By no means do you have to understand everything that is happening behind the scenes in the at_hello_world application, but it’ll definitely help to grasp the basics.

Just like the rest of the @platform, all of our demo applications are open source. Feel free to download the at_hello_world code from our GitHub repository [here](https://github.com/atsign-foundation/at_demos).

Upon downloading and booting up the app on an emulator, you are met with the Login screen where you can login after selecting a testable @sign to authenticate with from the dropdown menu.

After successfully authenticating, you will be taken to the home screen where you will see three separate boxes which house the three main functons of the at_hello_world app.

## The Three Main Functions of the at_hello_world app

### Update

The update section, as you see within the code, actually only involves a single if statement (to ensure information is actually passed) and four lines of code within it.

```dart
  _update() async {
    if (_key != null && _value != null) {
      AtKey pair = AtKey();
      pair.key = _key;
      pair.sharedWith = atSign;
      await _serverDemoService.put(pair, _value);
    }
  }
```

Above is the entirety of the update function! The “pair” variable in the first line of the if statement is something that you will see in all @platform applications. The @protocol interprets keys as AtKey objects, which have several attributes like “key”, “metadata”, and “sharedBy” that help the backend understand what to do with them.

In the code snippet above, we are calling the “key” attribute to add a string that will be paired to a value and the “sharedWith” attribute to define with whom we are sharing this AtKey-value pair. If we’d like to store “hello” and “world” on @bob’s secondary server, we would set pair.key to “hello” and pair.sharedWith to “@bob”. This latter detail may be a bit odd: Bob is sharing this AtKey object with himself so that he can access it! You can see use cases of sharing AtKey-value pairs with other @signs in the [at_cookbook](/docs/sample-apps/at_cookbook/) sample app.

Following up with our “hello” and “world” example, the final step in the \_update function is to call the “put” verb from the \_serverDemoService object with “pair” as the AtKey instance and “world” as the corresponding value (which should just be a string). When the verb executes successfully, you will have put the “hello” and “world” key-value pair into @bob’s secondary server!

While this is certainly an impressive feat (after all, these few seemingly unassuming lines of code uniquely encrypts the key-value pair to @bob’s secondary server and makes it persist), we’re still limited by the fact that we can’t retrieve key-value pairs from a secondary server. In the @protocol, retrieving key-value pairs takes two steps: scanning the relevant secondary server for AtKey objects, and getting the value associated with a scanned AtKey object.

### Scan

Now that we've "put" information on our secondary, we'd like to retrieve that key in order to read the information associated with it. In order to display values that we’ve stored, we first need to scan a secondary server for relevant AtKey objects (i.e. those that belong to the “namespace” of the application) and retrieve the values corresponding to those AtKeys.

```dart
_scan() async {
    List<AtKey> response = await _serverDemoService.getAtKeys(
      sharedBy: atSign,
    );
    if (response.length > 0) {
      List<String> scanList = response.map((atKey) => atKey.key).toList();
      setState(() => _scanItems = scanList);
    }
  }
```

The only @protocol verb we’re calling in this snippet is “getAtKeys()”. This verb is an incredibly robust function that can gather and sort AtKeys on a secondary server based on things like who shared those AtKeys (the “sharedBy” optional argument) and regular expressions (e.g. the namespace of the application). Because the at_hello_world app is a special case where we only share AtKey objects with ourselves, we can simply call getAtKeys with the “sharedBy” argument set to our own @sign (i.e. widget.atSign). This will return a List of the AtKey objects we want.

Once you get that List of AtKeys, you’re pretty much finished! In the at_hello_world app, because we want to display keys as strings, we call the “map” method on the List of AtKeys to create a new list that just contains the “key” attribute of each AtKey object. In the last line of code, we call “setState” so that the app loads the newly populated list of keys in the DropdownButton widget.

### Lookup

An individual on the at_hello_world app is given a list of keys, and they select one (\_lookupKey) to find its corresponding value. How do we do this? The answer lies in the \_lookup function of the HomeScreen class:

```dart
 _lookup() async {
    if (_lookupKey != null) {
      AtKey lookup = AtKey();
      lookup.key = _lookupKey;
      lookup.sharedWith = atSign;
      String response = await _serverDemoService.get(lookup);
      if (response != null) {
        setState(() => _lookupValue = response);
      }
    }
  }
```

In the first line of the if statement, we are creating a new AtKey object called “lookup.” The reason for this is we need a dummy AtKey object that can be passed into the @protocol for looking up the correct value. For the at_hello_world app, this dummy AtKey just needs its “key” and “sharedWith” attributes populated before it can be passed into the “get” verb.

By the way, if you think creating a copy of an AtKey object is a hassle, that’s totally valid! In a typical @platform application, you have the \_scan and \_lookup functions merged to some degree so that you can just pass in the AtKey objects we retrieved with the “getAtKeys” verb to the “get” verb. The point of having two separate functions in the at_hello_world project is to define the “scanning” and “getting” steps more concretely.

“Get” is a very straightforward verb: it gets the value corresponding to a specified AtKey.

Once we retrieve the value paired with the “lookup” AtKey, all that’s left is calling “setState” to display the “\_lookupValue” on screen.
