---
title: "Try your own @platform project"
SEOtitle: "Try an @platform (at_platform or AtPlatform) project"
linkTitle: "Try the @platform"
Description: "Watch the @platform in action with the Snackbar application"
content: "What to do after creating your own @sign"
weight: 1
date: 2021-12-12
---

This tutorial will guide you through a 5 step process to install and run our demo snackbar sender application. Please follow the steps below:

{{% toggleblock title="Step 1: Install at_app" %}}
Run the following command to install at_app, our developer toolkit:
{{% codeblock id="1" %}}dart pub global activate at_app{{% /codeblock %}}
{{% /toggleblock %}}

{{% toggleblock title="Step 2: Install the demo app" %}}
Next install the app like so:
{{% codeblock id="2" %}}at_app create -d snackbar_sender your-folder{{% /codeblock %}}
(Read more on at_app <a href="https://pub.dev/packages/at_app/example" target=_blank>here</a>)
{{% pageinfo %}}
  <b> Note: </b>  Replace "your-folder" with the folder you created your project in.
  {{% /pageinfo %}}

{{% /toggleblock %}}

{{% toggleblock title="Step 3: Run the demo app" %}}
Then run the demo app:
{{% codeblock id="3" %}}cd your-folder
flutter run{{% /codeblock %}}
{{% pageinfo %}}
  <b> Note: </b>  Replace "your-folder" with the folder you created your project in.
  {{% /pageinfo %}}

{{% /toggleblock %}}

{{% toggleblock title="Step 4: Onboard an @sign" %}}

<center>
<p>Watch the GIF below to see how to get a free @sign within the app itself!</p>

<img src="/Sample_Apps/croppedWT.gif" style="margin: auto; height:600px;">
</center>

{{% pageinfo %}}
If you'd like to purchase an @sign or would simply like to create and receive any type of @sign on the website, feel free to visit <a href="https://my.atsign.com/go">atsign.com</a>.
{{% /pageinfo %}}

{{% /toggleblock %}}

{{% toggleblock title="Step 5: Send a snack!" %}}
<center>
<p>
Enter an @sign that will receive the sent snack. Be sure that it is the same @sign that you have entered in the receiver below!
</p>
<iframe src="https://cconstab.github.io/snackbar/#/" title="Snackbar Code" class="receiver"></iframe>
</center>
{{% /toggleblock %}}

### What's next?

If you are looking for a more advanced version of our Snackbar demo, look no further! Follow the step-by-step guide to send end-to-end encrypted snacks (chocolate bars!) to another device [here](/docs/sample_apps/snackbar/)!


<style>
  .receiver {
    margin-top: 1rem;
    min-height: 400px;
  }
</style>
