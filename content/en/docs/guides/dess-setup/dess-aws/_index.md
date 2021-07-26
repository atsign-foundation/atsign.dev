---
title: "Setup dess on AWS (Amazon Web Services) Platform"
SEOtitle: "Setup @platform (at_platform or AtPlatform) dess in AWS (Amazon Web Services)"
linkTitle: "AWS"
weight: 2
date: 2021-07-26
content: The @platform resources will help you quickly build your end-to-end encrypted app
description: Step-by-Step setup of dess on AWS (Amazon Web Services)
---

# Step-by-Step setup of dess in AWS

In this step-by-step guide I will walk you through all steps required to setup your own private dess in AWS cloud from scratch. Please use index to skip some steps in case you have done them in other way.

## Table of contents

- [Pre-requisites](#pre-requisites)
  - [ Registering your @sign](#Registering)
    - [ Sign-up for AWS account](#sign_up)
  - [Register your own fully qualified domain name](#FQDN)
    - [Register domain name with AWS](#cloud_domain)
    - [Create Cloud DNS zone](#DNS_zone)

* [Preparing AWS instance](#prep_instance)
* [Preparing your instance for network access](#networking)
  - [Assignment of Static IP](#static_IP)
  - [Assignment of Domain name to your static IP](#domain2IP)
  - [Setting up Firewall](#firewall)
* [Instance setup and dess deployment](#deployment)
* [Registration of @sign in your private dess](#dess2@sign)
* [Activation of @sign](#activation)

## Pre-requisites <a name="pre-requisites"></a>

- Register Atsign at http://atsign.com
- Have AWS account
- Have registered Fully Qualified Domain Name (FQDN)

### 1. Registering your @sign <a name="Registering"></a>

This topic is already well documents. Please follow guidance of https://atsign.com/faqs/ and register via https://atsign.com/get-an-sign/.

### 2. Sign-up for GCP account <a name="sign_up"></a>

If you are new to cloud like me and need to create new AWS account, I have good news! The creation is for free and the cost of running your @sing dess costs about 10$/month. You can create your free account at https://aws.amazon.com/ at date of writing 6-Jun-2021 there is “free tier” available and was used for this setup.

![aws-free-trial](images/aws-free-trial.png)

Follow instruction on screen

![aws-sign-up](images/aws-sign-up.png)

Once done with registration you will be able to login to your http://aws.amazon.com/console.

Make sure that you select right region in top right corner.

![aws-region](images/aws-region.png)

Select region that is geographically closest to where you are located to get best performance.

You are now all setup and good to go to prepare your first cloud dess.

### 3. Register your own fully qualified domain name (FQDN) <a name="FQDN"></a>

This step can be performed at range of different sites with different pricing models. You can use sites like http://www.godaddy.com; https://www.namecheap.com/; and many others. Since we have AWS account we can use it to register our domain through Route 53 service.

In your AWS console navigate to services in top left corner and select Route 53 service.

#### a) Register domain name with AWS. <a name="cloud_domain"></a>

In your AWS console search for `Route 53`.

![aws-route53](images/aws-route53.png)

You can start looking for your domain directly from here:

![image-20210726083635919](images/image-20210726083635919.png)

Based on the name you selected and the domain AWS will give you options of free domains and their pricing. As I am looking for best deal .link domain seems like good option at cost of 5$ / year.

In my case 4atsign.link is free and I will register it by clicking “Add to cart” and continue.

![img](images/clip_image002.jpg)

Fill out DNS registration form:

![img](images/clip_image004.jpg)

Continue review details and order. At this point if all is fine you should see your domain request pending:

![img](images/clip_image006.jpg)

This can take some time so why don’t we move on to next step!

### 4. Preparing AWS instance <a name="prep_instance"></a>

Now since I am new to AWS the easiest way to start is using the LightSail service from service catalog. This will enable you to deploy small system which is more then capable of handling dess at pre-set price.

![img](images/clip_image002-16272842283471.jpg)

Welcome to LightSail:

![img](images/clip_image004-16272842283482.jpg)

First step is to create new instance. Fortunately, we have big orange button that can do just that!

There are several options we are presented at this moment. Since I am living in Europe I select “**Frankfurt, Zone A** (eu-central-1a)” as my instance location. Instance region will dictate how well will your instance response based on your geographical location. People located in India should selects APAC region where as people in US should select North America region. You can leave availability zone set as default.

![img](images/clip_image006-16272842283483.jpg)

Next up will be selection of operating system we want to deploy. We know that dess works well with Ubuntu 20.04 LTS so lets select just that.

![img](images/clip_image008.jpg)

You are presented with couple more options, but unless you know what you are doing leave these as is.

![img](images/clip_image010.jpg)

Now let’s select instance plan. dess is relatively light weight so for testing purposes I will select first instance plan for 3.5$/Month. This will provide us with 512 MB of RAM, 1vCPU, 20GB of storage and 1TB of data transfer. This is more then enough to run our dess.

![img](images/clip_image012.jpg)

Lastly we have to name our instance. This is name you will be presented with in your dashboard.

![img](images/clip_image014.jpg)

Last but not least is to press “Create instance”

![img](images/clip_image015.png)

Couple seconds later you should be re-routed to your dashboard and see you instance up and running:

![img](images/clip_image016.png)

### 5. Preparing your instance for network access <a name="networking"></a>

#### a) Assignment of Static IP <a name="static_IP"></a>

Next up our list of activities is providing our instance with static IP and linking our domain to it.

When you click on your instance name it will take you to management console of it which should look like this:

![img](images/clip_image002-16272853840264.jpg)

This is where you control hardware, connectivity and if needed can delete your instance.

Lets configure static IP address for your new instance. Navigate to Networking and click on Create static IP:

![img](images/clip_image003.png)

Our region and instance is selected so the only thing left is to name our static IP. I selected name atsign-static, but it can be any name you like.

![img](images/clip_image005.jpg)

Lets hit create:

![img](images/clip_image007.jpg)

And voila we now have static IP address on the internet that will not change and we can link our domain name with it.

![img](images/clip_image009.jpg)

When you click on your instance name and navigate to Networking static IP is now assigned

![img](images/clip_image011.jpg)

#### b) Assignment of Domain name to your static IP <a name="domain2IP"></a>

We can now move on to linking our static IP address to our domain. This is done via AWS console which can be accessed top right in Lightsail.

![img](images/clip_image001.png)

Verify your email used for registering domain:

By now you should receive verification email that will confirm registration of your domain. Click this link before moving on.

Linking domain with your static address:

Lets navigate to “Route 53” from Services menu.

![img](images/clip_image003.jpg)

From your dashboard click on “Domain” which will take you to “Registered Domains” tab

![img](images/clip_image005-16272854399076.jpg)

Here you can click on your registered domain which will take you to overview page with domain status and contacts.

![img](images/clip_image007-16272854399087.jpg)

Click on “Manage DNS”

![img](images/clip_image009-16272854399088.jpg)

And click on your domain name.

This will show you your DNS records for your domain. We now need to link A type record to your domain linking it to IP address of your instance.

This is done simply by typing your static IP address from previous step into field “Value” and clicking Create record:

![img](images/clip_image011-16272854399089.jpg)

If everything goes well you should see following in your domain dashboard:

![img](images/clip_image013.jpg)

To test if you are successful open command line and ping your domain. You should see your instance static IP address. It will not respond which is normal due to IPv4 firewall. It is actually good thing!

![img](images/clip_image014.png)

At this point we have created DNS record we will use to link our dess, we created instance name which will be running our dess and we have opened port range which is exposed to the internet and we can communicate with @sign root server and our apps with.

#### c) Setting up Firewall <a name="firewall"></a>

Next up we need to make sure we have ports open for our dess to communicate with root server and our apps. In Section networking go to section “IPv4 Firewall” and click “+ Add rule” Our rule will be “Custom” on TCP protocol with Port range in number higher then 1024. In my case I have selected port range 8000-8010. This will enable me to run up to 10 @signs in parallel.

![img](images/clip_image002-16272854074665.jpg)

Click create and verify that your new rule is in list:

![img](images/clip_image002-16272854074665.jpg)

### 6. Instance setup and dess deployment <a name="deployment"></a>

Open your LightSail console at https://lightsail.aws.amazon.com/

By now you should see your instance in “Running state”

![img](images/clip_image002-162728546025210.jpg)

Open it and on tab Connect click on “Connect using SSH”

![img](images/clip_image003-162728546025211.png)

You should be presented by new window with command line:

![img](images/clip_image005-162728546025212.jpg)

Before we do anything we run update:

sudo apt update && sudo apt upgrade

This might take some time, but it will make sure we have latest repository information and the system is up to date and secure.

Next up we need to make sure Git is installed. This can be done with following command:

sudo apt install git

We are now set to download latest copy of the dess through Git. I am following guide prepared by Colin

https://github.com/atsign-foundation/dess/tree/dess.0.0.1-release.1

Run to download fresh copy of the dess

git clone --branch dess.0.0.1-release.1 https://github.com/atsign-foundation/dess.git

![img](images/clip_image007.png)

Lets navigate to dess folder that was created and run installation scripts:

![img](images/clip_image008.png)

At the end you should be presented with message:

![img](images/clip_image009.png)

At this point we are good to go with registering our first @sign in our private dess running in cloud with our own FQDN!

### 7. Registration of @sign in your private dess <a name="dess2@sign"></a>

At this step you should already have your at sign registered at http://atsign.com. If not **go do it!**

I have registered my own free @sign @44likelycanary which I will link to my AWS cloud private dess.

In your instance console navigate to dess folder. If you were following this guide it will be located in:

/home/ubuntu/dess

![img](images/clip_image001-162728549379113.png)

We now need to create service hosting our @sign on our dess by executing ./create.sh script

![img](images/clip_image002.png)

In my case the command will look as following:

ubuntu@ip-172-26-10-58:~/dess$ ./create.sh @44likelycanary 4atsign.link 8000 <email address> likelycanary

To make it more understandable:

I will be registering my @sing **@44likelycanary**

I will be using my domain **4atsign.link** which I have registered through AWS

I am using port **8000** which I have opened in my instance firewall

My registration email address is **<email address>**.

The last **likelycanary** is name which will be used by docker to register my service.

If everything is successful you should see output like this:

![img](images/clip_image004-162728549379914.jpg)

At this moment your atsign is registered on your dess.

## 8. Activation of @sign<a name="activation"></a>

Next up we need to activate it

Login to your dashboard at https://my.atsign.com/dashboard

Open “my @signs”

![img](images/clip_image001-162728550968115.png)

Open “managed” of @sign you are registering”

![img](images/clip_image003-162728550968116.jpg)

Navigate to Advance settings:

![img](images/clip_image005-162728550968117.jpg)

If you have already activated your @sign you will be prompted to erase all your data first

![img](images/clip_image007-162728550968118.jpg)

Once done you are able to link your @sign with your private dess. Use your domain and port number with which you have created service on your cloude instance and press Activate

![img](images/clip_image009-162728550968119.jpg)

You should see that your @sign is being activated in your dashboard:

![img](images/clip_image011-162728550968120.jpg)

This can take several minutes so go get cup of coffee, some tea maybe, stretch your body and pray you haven’t made any mistakes!

Once the activation process completes you are welcomed by green Activated.

![img](images/clip_image013-162728550968121.jpg)

You can now open your @buzz or @wavi and register your atsign via QR code and generate your keys!

**CONGRATULATION**
