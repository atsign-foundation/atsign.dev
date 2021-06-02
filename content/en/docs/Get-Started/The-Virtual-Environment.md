---
title: "The Virtual Environment"
linkTitle: "The Virtual Environment"
weight: 1
date: 2017-01-05
description: >
  This page displays the proper steps in which developers can follow to successfully create and run their own virtual environment to utilize the @platform on their own machine.
---

## Setup Virtual Environment

<!-- Cards for different OS-->
<div class="card-deck mb-8">

  <!-- Windows Card-->
  <a class="card" id="install-windows" href="/docs/get-started/the-virtual-environment/#windows" style="border-style: solid;border-color: #F05F3E">
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
  <a class="card" id="install-macos" href="/docs/get-started/the-virtual-environment/#macos" style="border-style: solid;border-color: #F05F3E">
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
  <a class="card" id="install-linux" href="/docs/get-started/the-virtual-environment/#linux" style="border-style: solid;border-color: #F05F3E">
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
Though, your machine's BIOS may already have virtualization enabled, you can check [here](https://2nwiki.2n.cz/pages/viewpage.action?pageId=75202968#:~:text=Press%20the%20F10%20key%20for,to%20save%20changes%20and%20Reboot).

*Note*: Please ensure that you have Docker up and running before you proceed.

**Loopback Adapter**

Install the Microsoft loopback adapter and configure it. The video showing how to do that is here:

<iframe src="https://player.vimeo.com/video/506374699?title=0&amp;byline=0&amp;portrait=0" class="video-frame" style="position:relative;top:0;left:-20px;width:750px;height:400px;" frameborder="0" allow="autoplay; fullscreen" allowfullscreen="true"></iframe>

**Start up the at_virtual_environment**

Run cmd and enter the following commands. You can run cmd by using the windows key and the r key then typing cmd.
            
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

**Configure Network Adapter**

Open the Terminal window and enter this command. This permanently puts the Virtual IP address in place. You only need to run this once!            
```
sudo curl -L atsign.dev/curl/atloop.plist -o /Library/LaunchDaemons/atloop.plist && \
```
              
            
          
Once you enter the above command, an arrow “>” should show up to enter the next line:            
```
sudo launchctl load /Library/LaunchDaemons/atloop.plist
```
            
          
The command line may ask you to enter your password. Go ahead and fill it in if this happens.

** Start up the Virtual Environment**
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

*Note*: Please ensure that you have Docker up and running before you proceed.


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

## Where should I go next?

Give your users next steps from the Overview. For example:

* [Sample Apps](/docs/sample-apps/): See apps that show off the power of the @platform on your own machine!

