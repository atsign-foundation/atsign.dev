---
title: "Namespaces"
SEOtitle: "Namespaces on the @platform (at_platform or AtPlatform) with free @signs (AtSign or at_sign)"
linkTitle: "Namespace"
Description: "An overview to namespaces and their importance"
content: "Easily setup your own @platform secondary server for free!"

weight: 1
date: 2022-01-17
---

## What are Namespaces?

The @sign namespace, unlike DNS, extends to Unicode (specifically UTF-8), which allows characters beyond the Latin script. Emojis and other Unicode character sets are allowed thus expanding the namespace1.

There are however some rules when choosing a fully qualified @sign, like location@alice, it cannot include UTF-8 white space ,invisible characters, or control characters. @signs are also Latin case insensitive ensuring that @alice and @Alice refer to the same @sign.

Following conventions set out in DNS and the URI internet RFCs, the following characters are reserved and cannot be used as part of an @sign.

! \* ' ( ) ; : @ & = + $ , / ? # [ ] { }

Whilst the @protocol itself has no real limits on the namespace being used, the @sign namespace has been constrained because of reasonable limits for the underlying keypair databases used in the clients of the @protocol. If needed in the future, this can be opened up further with no changes needed to the protocol, but it will need changes to client databases.

In the persistence layer, UTF-8 characters in the namespace are translated to UTF-7 and the UTF-7 namespace is used to store data in key/value databases.

Whilst the wire protocol uses UTF-8, the fully qualified @signs are translated to UTF-7 and need to fit in the namespace below.

The @sign itself is unique, so it’s also usable as a unique identifier for the application namespace that makes up a composite key. For example, if an application was called @buzz then to ensure the application has no namespace clash, the application owner should own the @buzz @sign. In effect, if you own the @alice you also own alice@ in the namespace for every @sign.

<center>
<img src="/Func_Arch_images/namespace.png" style="height:300px;"></img>
</center>

While this may look limiting at first glance, the namespace is actually immense.

Feel free to read more about namespaces [here](https://atsigncompany.medium.com/the-hidden-beauty-of-protocol-namespaces-6f5fab7f7a09).

<!-- ## Getting @signs and keys.

Your first step is to get a couple of @signs, it is best to get at least two, so you can experiment with sharing end-to-end
encrypted data across the @platform.

### There are two methods to get @signs.

#### The first

Go to [atsign.com](https://atsign.com) and clicking [Get an @sign](https://atsign.com/get-an-sign/). If you go
this route then you have more influence on your free @sign or pay for one of your choosing. Once you have your @signs,
do not forget to activate them.

![activate @sign](/docs/Get-Started/get-an-atsign/images/activate-ui.png)

Activating creates a microservice (we call the secondary server) and once
that is spun up on The @ Company infrastructure you will see a QR-Code to scan with an @ enabled application.

![activated @sign](/docs/Get-Started/get-an-atsign/images/activated.png)

The pairing consists of your device creating cryptographic
keys and sharing the public keys to the secondary server, you will be asked to store your private keys.
Storing your keys is vitally important as only you have the keys.

#### The second

The experience of getting a @sign via the website is great for developers as you have advanced options available, to reset
@signs and to point your @sign to your own infrastructure. For getting people onboarded quickly, a better experience would
be to get a free @sign within the app itself, this is option 2.

![generate @sign](/docs/Get-Started/get-an-atsign/images/generate-free-@sign.png)

The [onboarding widget](https://pub.dev/packages/at_onboarding_flutter) together with an API key provides a button
marked "Generate Free @sign".

![generate @sign-pair](/docs/Get-Started/get-an-atsign/images/generate-free-@sign-pair.png)

When selected a number of free @signs given to chose from, once selected it is quickly activated,
then once again you will be asked to store the cryptographic keys for the @sign.

### Once you have your @signs and keys

You are ready to start using the @platform! We have a number [demo apps](https://github.com/atsign-foundation/at_demos) that are constantly being updated, feel free to
fork or clone and try them.
There is also another nice app in development by [xavierchanth](https://github.com/XavierChanth/chit_chat) which is a
chat app using the @platform. It is a nice example to follow as it uses the [contacts](https://pub.dev/packages/at_contact)
combined with the [at_chat_flutter](https://pub.dev/packages/at_chat_flutter) widgets to create a simple chat app between
@signs.

![ChitCh@t](/docs/Get-Started/get-an-atsign/images/ChitCh@t-low.png)

Each @ enabled application will ask you once for your @sign and then your keys, so it can synchronize with your secondary server.
This means you might like to store your keys on a personal network drive or service (e.g. gdrive/idrive/onedrive) so
you can connect other @ enabled apps to your @sign easily. Remember not to share and protect your keys.

### Other widgets and the @platform/@protocol source code

We have an ever-growing number of widgets on [pub.dev](https://pub.dev/publishers/atsign.org/packages)
The @plaform and the @protocol are open source projects on [GitHub](https://github.com/atsign-foundation). If you see something missing,
or not working let us know or better still contribute with a PR!

## Where should I go next?

First, if you haven't setup Flutter, do that [here](/docs/get-started/setup-your-env/).

Otherwise, continue to building your first app [here](/docs/get-started/create-a-project/). -->
