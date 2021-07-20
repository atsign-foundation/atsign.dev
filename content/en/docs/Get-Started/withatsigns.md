---
title: "Option 1 : Set up the @platform with free @signs"
SEOtitle: "Set up the  @platform (at_platform or AtPlatform) with free @signs (AtSign or at_sign)"
linkTitle: "1 : With Free @signs(preferred)"
Description: "Create and run your own @platform with free @signs"
content: "Create and run your own @platform with free @signs"

weight: 1
date: 2017-01-05

---

### Getting @signs and keys.
Your first step is to get a couple of @signs, it is best to get at least two, so you can experiment with sharing end-to-end 
encrypted data across the @platform. 

There are two methods to getting @signs, one is simply a matter 
of going to [atsign.com](https://atsign.com) and clicking [Get an @sign](https://atsign.com/get-an-sign/). If you go 
this route then you have more choice on whether to get a free @sign or pay for one you choose. Once you have your @signs, 
do not forget to activate them. Activating creates a microservice and once that is spun up on The @ Company infrastructure
you will see a QR-Code to scan with an @ enabled application. The pairing consists of your device creating cryptographic
keys and sharing the public keys to the microservice, you keep and will be asked to store your private keys.
Storing your keys is vitally important as you have the only keys.

The experience of getting a @sign via the website is great for developers as you have advanced options available, to reset
@signs and to point your @sign to your own infrastructure. For getting people onboarded quickly a better experience would
be to get a free @sign within the app itself, this is option 2.

The [onboarding widget](https://pub.dev/packages/at_onboarding_flutter) together with an API key provides a button
marked "Generate Free @sign". When selected a number of free @signs given to chose from once one is it is quickly activated, 
then once again you will be asked to store the cryptographic keys for the @sign.

### Once you have your @signs and keys 
You are read to start using the @platform! We have a number [demo apps](https://github.com/atsign-foundation/at_demos) that are constantly being updated, feel free to
clone and try them. 
There is also another nice app in development by [xavierchanth](https://github.com/XavierChanth/chit_chat) which is a 
chat app using the @platform. It is a nice example to follow as it uses the [contacts](https://pub.dev/packages/at_contact)
combined with the [at_chat_flutter](https://pub.dev/packages/at_chat_flutter) widgets to create a simple chat app between
@signs.


### Other widgets and the @platform/@protocol source code
We have an ever-growing number of widgets on [pub.dev](https://pub.dev/publishers/atsign.org/packages)
The @plaform and the @protocol are open source projects on [GitHub](https://github.com/atsign-foundation) so if you see something missing or not working let us know 
or better still contribute!


