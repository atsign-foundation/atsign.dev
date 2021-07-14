---
title: "at_cookbook"
linkTitle: "at_cookbook"
weight: 3
date: 2021-06-01
description: >
  This is an intermediate-level @platform based application that uses the verbs we learned in the at_hello_world and at_chats applications to make a working cookbook for the chef inside of us all!
---

<p align="center">
  <img src="/Sample_Apps/at_cookbook_demo.gif" alt="at_cookbook" height= "520px" width= "300px"/>
</p>

<!-- IMPORTANT NOTE: Current episode of Tyler Time at_cookbook walkthrough not uploaded -->
<div style= "background-color:#F05F3E;color:white; min-height:100px;width:200px;position:relative; float:right;padding:10px;margin-bottom:20px;margin-left: 20px;">
<h3> tl;dr </h3>
Overview too long for you? Watch the <u>
<a href="https://www.youtube.com/watch?v=Yj8KekimmpM" style="color: white;">Tyler Time</a></u> episode that covers this instead!
</div>

## Overview of the at_cookbook app

The at_cookbook app allows a testable @sign to create a recipe with a name, description, list of ingredients, and a picture. After doing this, the @sign is capable of sharing this entire recipe with another testable @sign. A dishWidget class is created which encapsulates an individual recipe with each instance. Its parameters are defined below:

```dart
class DishWidget extends StatelessWiatdget {
 final String title;
 final String ingredients;
 final String description;
 final String imageURL;
 final String prevScreen;

 DishWidget({
   @required this.title,
   @required this.ingredients,
   @required this.description,
   @required this.imageURL,
   @required this.prevScreen,
});
...
```

After we pull dishWidgets that exist in a secondary server, we display them on the home screen, where the list of recipes are located.

Now that you have the recipe itself, you’re able to pass this through the notify verb. When an @sign wishes to share a recipe, the \_share function will be called. This function is structured as so:

```dart
_share(BuildContext context, String sharedWith) async {
 if (sharedWith != null) {
   AtKey lookup = AtKey()
     ..key = widget.dishWidget.title
     ..sharedWith = atSign;

   String value = await _serverDemoService.get(lookup);

   var metadata = Metadata()..ttr = -1;
   AtKey atKey = AtKey()
     ..key = widget.dishWidget.title
     ..metadata = metadata
     ..sharedBy = atSign
     ..sharedWith = _otherAtSign;

   var operation = OperationEnum.update;
   await _serverDemoService.notify(atKey, value, operation);
   Navigator.pop(context);
 }
}
```

Here, we’re initializing a variable called lookup as an AtKey object (lookup will be our recipe). You’ll notice that we’re defining a couple of the attributes of the AtKey object (mainly the name of the recipe and what @sign is this recipe being shared with).

We would like to “get” the values of our recipe, so we use the get verb from the serverDemoService file of the application. ttr (Time To Refresh), a metadata attribute, is called with a value of -1, which means that we’re confident that the values of our recipe won’t change. Once the recipe has been cached on the secondary server that has received the recipe, it will not need to worry about updating its values at any point.

After passing all of the necessary values such as the metadata, the appropriate @signs, and the type of notification we’d like to send, we simply pass the values through the notify verb!
