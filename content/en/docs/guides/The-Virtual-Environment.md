---
title: "Set up the @platform virtual environment"
SEOtitle: "Set up the  @platform (at_platform or AtPlatform) virtual environment"
linkTitle: "Virtual Environment"
Description: "Create and run your own @platform virtual environment on your machine"
content: "Create and run your own @platform virtual environment on your machine"

weight: 2
date: 2017-01-05
---

Why is there a virtual environment to set up, and what does it do? Jumping directly into the deep end and creating projects on top of the @platform can be overwhelming, so we have made a simple way for you to run the @platform from your machine.

First, why is there a virtual environment to set up, and what does it do?

The virtual environment has two main benefits: you can monitor the status of your test secondary servers (by visiting localhost:9001), and you can bypass the traditional onboarding process completely.

Jumping directly into the deep-end and creating projects on top of the @platform can be overwhelming for some. To combat this overwhelming feeling, we have created a simple way to have you run the @protocol from your very own machine!

This will allow you to run both a [root server](/docs/resources/glossary/#root-server) and [secondary servers](/docs/resources/glossary/#secondary-server) of testable @signs. We have created demo apps that go over specific verbs and methods to help you get oriented.

## Setup Virtual Environment

<!-- Cards for different OS-->
<div class="card-deck mb-8">

  <!-- Windows Card-->
  <a class="card" id="install-windows" href="#windows" style="border-style: solid;border-color: #F05F3E">
    <div class="card-body">
      <header class="card-title text-center m-0">
        <span class="d-block h1">
          <i class="fab fa-windows" style="color: #F05F3E"></i>
        </span>
        <span class="text-muted text-nowrap">Windows</span>
      </header>
    </div>
  </a>

  <!-- MacOs Card-->
  <a class="card" id="install-macos" href="#macos" style="border-style: solid;border-color: #F05F3E">
    <div class="card-body">
      <header class="card-title text-center m-0">
        <span class="d-block h1">
          <i class="fab fa-apple" style="color: #F05F3E"></i>
        </span>
        <span class="text-muted text-nowrap">macOS</span>
      </header>
    </div>
  </a>

  <!-- Linux Card-->
  <a class="card" id="install-linux" href="#linux" style="border-style: solid;border-color: #F05F3E">
    <div class="card-body">
      <header class="card-title text-center m-0">
        <span class="d-block h1">
          <i class="fab fa-linux" style="color: #F05F3E"></i>
        </span>
        <span class="text-muted text-nowrap">Linux</span>
      </header>
    </div>
  </a>

</div>

### Windows

Your machine's BIOS may already have virtualization enabled. You can check [here](https://2nwiki.2n.cz/pages/viewpage.action?pageId=75202968#:~:text=Press%20the%20F10%20key%20for,to%20save%20changes%20and%20Reboot).

{{% alert title="Note" color="warning" %}}
Please ensure that you have [Docker](/docs/get-started/#docker-desktop) up and running before you proceed.
{{% /alert %}}

**Loopback adapter**

Install the Microsoft loopback adapter and configure it. Here's a video showing how:

<iframe src="https://player.vimeo.com/video/506374699?title=0&amp;byline=0&amp;portrait=0" class="video-frame" style="position:relative;top:0;left:-20px;width:750px;height:400px;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="true"></iframe>

**Start up the at_virtual_environment**

Run cmd and enter the following commands. You can run cmd by using the Windows key and the r key then typing cmd.

```
mkdir ve
cd ve
curl -L atsign.dev/curl/virtualenv-compose-vip.yaml -o docker-compose.yaml
```

Now you are ready to spin up the docker containers:

```
docker-compose up -d
```

Okay, you're up. Now you can check the [http://localhost:9001/](http://localhost:9001/).

Not sure what to do now? Try [here](/docs/get-started/the-virtual-environment/#where-should-i-go-next)!

### MacOS

#### Configure Network Adapter

Open the Terminal window and enter this command. This permanently puts the Virtual IP address in place. You only need to run this once!

```
sudo curl -L atsign.dev/curl/atloop.plist -o /Library/LaunchDaemons/atloop.plist && \
```

Once you enter the above command, an arrow “>” should show up to enter the next line:

```
sudo launchctl load /Library/LaunchDaemons/atloop.plist
```

The command line may ask you to enter your password. Go ahead and fill it in if this happens.

#### Start up the Virtual Environment

Make a new directory called “ve” and run the curl command inside of it:

```
mkdir ve
cd ve
curl -L atsign.dev/curl/virtualenv-compose-vip.yaml -o docker-compose.yaml
```

Now you are ready to spin up the docker containers:

```
docker-compose up -d
```

Not sure what to do now? Try [here](/docs/get-started/the-virtual-environment/#where-should-i-go-next)!

### Linux

**Configure Network Adapter**

{{% alert title="Note" color="warning" %}}
Please ensure that you have [Docker](https://www.docker.com/) up and running before you proceed.
{{% /alert %}}

Open the Terminal window and enter this command. This permanently puts the Virtual IP address in place. You only need to run this once!

```
curl -L atsign.dev/curl/rc.local -o setvip.sh
sudo ip addr add 10.64.64.64/32 dev lo
sudo nano /etc/rc.local
```

If the file “/etc/rc.local” is empty, then add the contents of the file “setvip.sh” to /etc/rc.local”. If rc.local already has content, then add the line “ip addr add 10.64.64.64/32 dev lo” above any lines that say “exit 0”. This will ensure that the virtual IP is in place even after a reboot. Ensure the permissions are correct with the following command:

```
sudo chmod 744 /etc/rc.local
```

**Start up the Virtual Environment**

Make a new directory called “ve” and run the curl command inside of it:

```
cd ~
mkdir ve
cd ve
curl -L atsign.dev/curl/virtualenv-compose-vip.yaml -o docker-compose.yaml
```

Now you are ready to spin up the docker containers:

```
docker-compose up -d
```

Okay, you're up. Now you can check the [http://localhost:9001/](http://localhost:9001/).

Not sure what to do now? Try [here](/docs/get-started/the-virtual-environment/#where-should-i-go-next)!

### To Pull Latest Virtual Environment Version

```
docker-compose down
docker-compose pull
docker-compose up -d
```

Congratulations! You’ve set up your virtual environment and can now experiment with the hello_world app. Now you can start building your very own privacy-conscious apps.

When writing code, the only change needed to run in the virtual environment is changing the ROOT_DOMAIN to point to vip.ve.atsign.zone. The production value is root.atsign.org.

### To Authenticate with Demo QR Codes

You will need the PKAM and CRAM Key QR codes in order to properly authenticate your testable atsigns.

You will find the group of these keys on our GitHub [here](https://github.com/atsign-foundation/at_demos/tree/trunk/at_demo_data/lib/assets)

## Where should I go next?

Give your users next steps from the Overview. For example:

- [Sample Apps](/docs/sample-apps/): See apps that show off the power of the @platform on your own machine!
