---
title: "Setup dess on GCP (Google Cloud Platform)"
SEOtitle: "Setup @platform (at_platform or AtPlatform) dess in GCP (Google Cloud Platform)"
linkTitle: "GCP"
weight: 2
date: 2021-06-02
content: The @platform resources will help you quickly build your end-to-end encrypted app
description: Step-by-Step setup of dess on GCP (Google Cloud Platform)
---

dess stands for "Distributed Edge Secondary Server" and it is used to host your @signs on your own secondary server. Refer to the [Setup dess guide](/docs/get-started/get-an-atsign/dess/) under Options to learn more.

In this step-by-step guide we will walk you through all steps required to setup your own private dess in GCP cloud from scratch. Please use index to skip some steps in case you have done them in another way.

## Table of contents

- [Pre-requisites](#pre-requisites)
  - [ Registering your @sign](#Registering)
    - [ Sign-up for GCP account](#sign_up)
    - [Account creation](#create_account)
  - [Register your own fully qualified domain name](#FQDN)
    - [Register domain name with GCP.](#cloud_domain)
    - [Create Cloud DNS zone](#DNS_zone)

* [Preparing GCP instance](#prep_instance)
* [Preparing your instance for network access](#networking)
  - [Assignment of Static IP](#static_IP)
  - [Assignment of Domain name to your static IP](#domain2IP)
  - [Setting up Firewall](#firewall)
* [Instance setup and dess deployment](#deployment)
* [Registration of @sign in your private dess](#dess2@sign)
* [Activation of @sign](#activation)

## Pre-requisites <a name="pre-requisites"></a>

- Register Atsign at http://atsign.com
- Have google account
- Have registered Fully Qualified Domain Name (FQDN)

### 1. Registering your @sign <a name="Registering"></a>

This topic is already well documents. Please follow guidance of https://atsign.com/faqs/ and register via https://atsign.com/get-an-sign/.

### 2. Sign-up for GCP account <a name="sign_up"></a>

#### a) Account creation <a name="create_account"></a>

If you are new to cloud like me and need to create new GCP account, I have good news! The creation is for free. As promotion all new customer will also receive 300$ as credit. That is more than enough to run multiple dess’s for 3 months of offer validity.

![gcp-discount](/docs/guides/dess-setup/dess-gcp/images/gcp-discount.png)

You can register with your gmail account or create new one by clicking “Get started for free” and follow instructions to register

![Get Started](/docs/guides/dess-setup/dess-gcp/images/gcp-get-started.png)

Once done with registration you will be able to login to your https://console.cloud.google.com/
And voila you have your GCP account up and running.

#### b) Setting up billing <a name="billing"></a>

To be able to run some services you have to maintain billing account. Navigation Menu -> Billing

![gcp-navigation-billing](/docs/guides/dess-setup/dess-gcp/images/gcp-navigation-billing.png)

By default GCP creates “My Billing Account” which you can link to your project.

![gcp-billing_project](/docs/guides/dess-setup/dess-gcp/images/gcp-billing_project.png)

Click “Link Billing account” and select “My billing account” from drop down

&#x1F534; Its important to note that this account holds your 300$ free credits! &#x1F534;

We are all setup and ready to go deploy!

### 3. Register your own fully qualified domain name (FQDN) <a name="FQDN"></a>

This step can be performed at range of different sites with different pricing models. You can use sites like http://www.godaddy.com; https://www.namecheap.com/; and many others. Since we have GCP account we can use it to register our domain through Cloud Domain.

#### a) Register domain name with GCP. <a name="cloud_domain"></a>

In your GCP console search for `Cloud Domain`.

![gcp-search-domain](/docs/guides/dess-setup/dess-gcp/images/gcp-search-domain.png)

We first need to enable this service.

![gcp-domain-api](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-api.png)

Once the service activates you will be presented with its dashboard.

Lets register our fully qualified domain name (FQDN) that will be used for registration of our dess.

Click on “Register Domain” and look for suitable name.

![gcp-domain-register](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-register.png)

Reviewing pricing options of GCP .pw is their cheapest option which will work for testing. For my test case I am selecting atsign.pw with price $0.75 / month by clicking add to cart button and continue.

![gcp-domain-lookup](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-lookup.png)

Next we can select where will our DNS record be hosted. Simply select “Use Google Domains” and DNSSEC “Enabled” and click continue.

![gcp-domain-config](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-config.png)

We have no options with Privacy protection so simply click continue.

![gcp-domain-privacy](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-privacy.png)

Fill out contact details and click register. This will trigger registration email you will have to verify.

![gcp-domain-contacts](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-contacts.png)

Once you verify your email your domain should be ready to use

![gcp-domain-status](/docs/guides/dess-setup/dess-gcp/images/gcp-domain-status.png)

#### b) Create Cloud DNS zone <a name="DNS_zone"></a>

Next step is to enable Cloud DNS service. Search for DNS in search bar and select `Cloud DNS`

![gcp-search-dns](/docs/guides/dess-setup/dess-gcp/images/gcp-search-dns.png)

If its your first time activating this service you will have to enable the API. Press enable and wait for the activation to finish.

![gcp-dns-api](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-api.png)

Lets crate new DNS zone by clicking “Create Zone”

![gcp-dns-create](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-create.png)

We will select zone type as Public since we will be connecting to our DNS from internet and provide your registered DNS name. In my case atsign.pw. DNSSEC will be set to off and provide some meaningful Description. Once you filled all your details press create.

![gcp-dns-create-details](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-create-details.png)

You should receive following message:

![gcp-dns-confirm](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-confirm.png)

### 4. Preparing GCP instance <a name="prep_instance"></a>

Now since I am new to GCP the easiest way to start using it is with prebuild solutions. This way you will deploy small system which is more then capable of handling dess at pre-set price.

We can use pre-build “Ubuntu 20”. In Search bar look for `Ubuntu20`

![gcp-search-ubuntu20](/docs/guides/dess-setup/dess-gcp/images/gcp-search-ubuntu20.png)

&#x1F534; **Make sure to use “Ubuntu 20” and not “Hardened Ubuntu 20”. Although the Hardened version will work as well it requires additional manual steps to make work.**&#x1F534;

​

This will take you to this prebuild solution overview page:

![gcp-ubuntu20](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20.png)

Select launch

![gcp-ubuntu20-api-enable](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20-api-enable.png)

And press enable all required API’s

![gcp-ubuntu20-api-enabled](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20-api-enabled.png)

Once all API’s are activated you are taken to configuration page:

![gcp-ubuntu20-type](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20-type.png)

Prices are based on region and power of selected Virtual Machine (VM). To cost optimize you can select US region / N1 / g1-small at cost of $15/Month.

Next up is boot disk which we can leave as is.

![gcp-ubuntu20-disk](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20-disk.png)

This will deploy your Ubuntu 20.04 virtual machine.

![gcp-ubuntu20-confirmation](/docs/guides/dess-setup/dess-gcp/images/gcp-ubuntu20-confirmation.png)

### 5. Preparing your instance for network access <a name="networking"></a>

#### a) Assignment of Static IP <a name="static_IP"></a>

Next up our list of activities is providing our instance with static IP and linking our domain to it.

GCP assigned ephemeral IP address to our newly created VM. We need to change it to static IP.

In search bar look for `External IP addresses`.

![gcp-search-networking](/docs/guides/dess-setup/dess-gcp/images/gcp-search-networking.png)

You should see your external IP address assigned to your VM

![gcp-networking-overview](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-overview.png)

In column Type select ephemeral and change it to Static

![gcp-networking-type](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-type.png)

Give your static IP name and some description.

![gcp-networking-static](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-static.png)

Type should now say Static

![gcp-networking-type-change](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-type-change.png)

#### b) Assignment of Domain name to your static IP <a name="domain2IP"></a>

Next step is to point your domain to your virtual machine running dess.

Search for `Cloud DNS`

![gcp-search-dns](/docs/guides/dess-setup/dess-gcp/images/gcp-search-dns.png)

Open zone you have created in step [3.b Create Cloud DNS zone](#DNS_zone)

![gcp-dns-status](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-status.png)

We now need to link A type record to your domain linking it to IP address of your Virtual machine.

This is done simply press “Add record set”

![gcp-dns-add-record](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-add-record.png)

Select Resource record type “A” and IPv4 address the address of your dess virtual machine.

![gcp-dns-a](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-a.png)

If everything goes well you should see following in your domain dashboard:

![gcp-dns-status-final](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-status-final.png)

Next step is to update Google Name servers. You can follow Googles guide - step 5.

https://cloud.google.com/dns/docs/tutorials/create-domain-tutorial#register-domain

To test if you are successful open command line and ping your domain. You should see your instance static IP address.

![gcp-dns-test](/docs/guides/dess-setup/dess-gcp/images/gcp-dns-test.png)

At this point we have created DNS record we will use to link our dess, we created instance name which will be running our dess and we have opened port range which is exposed to the internet and we can communicate with @sign root server and our apps with.

#### c) Setting up Firewall <a name="firewall"></a>

Search for Firewall in search bar.

![gcp-search-firewall](/docs/guides/dess-setup/dess-gcp/images/gcp-search-firewall.png)

Click on Create firewall rule

![gcp-firewall-create](/docs/guides/dess-setup/dess-gcp/images/gcp-firewall-create.png)

Lets create firewall rule that will enable the @sign root server communicate with our dess.

![gcp-networking-firewall-settings](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-firewall-settings.png)

Important things to note:

1.  Ingress translates to incoming traffic.

2.  Selecting IP range as `0.0.0.0/0` will allow traffic from anywhere on the internet.

3.  For my use case I will enable port range `8000 – 8010` allowing me to register up to 10 @signs.

![gcp-firewall-ranges](/docs/guides/dess-setup/dess-gcp/images/gcp-firewall-ranges.png)

Press `create` and validate that your new rule appears in list of firewall rules.

![gcp-firewall-status](/docs/guides/dess-setup/dess-gcp/images/gcp-firewall-status.png)

Second we need to create firewall rule that will enable your dess server to communicate with certification authority.

![gcp-networking-firewall-80](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-firewall-80.png)

Important things to note:

1.  Ingress translates to incoming traffic.

2.  Selecting IP range as `0.0.0.0/0` will allow traffic from anywhere on the internet.

3.  You need to enable port `80` for communication with Certification authority.

![gcp-networking-firewall-range-80](/docs/guides/dess-setup/dess-gcp/images/gcp-networking-firewall-range-80.png)

Press `create` and validate that your new rule appears in list of firewall rules.

![gcp-firewall-status](/docs/guides/dess-setup/dess-gcp/images/gcp-firewall-status-both.png)

### 6. Instance setup and dess deployment <a name="deployment"></a>

Open your GCP console at https://console.cloud.google.com/compute/instances and search for `VM instances`

![gcp-search-vm](/docs/guides/dess-setup/dess-gcp/images/gcp-search-vm.png)

By now you should see your instance in “Running state”

![gcp-vm-status](/docs/guides/dess-setup/dess-gcp/images/gcp-vm-status.png)

Click on the SSH button and connect to your instance.

You should be presented by new window with command line:

![gcp-vm-connected](/docs/guides/dess-setup/dess-gcp/images/gcp-vm-connected.png)

Before we do anything else, we should update the system:

```
sudo apt update && sudo apt upgrade
```

This might take some time, but it will make sure we have latest repository information and the system is up to date.

Next make sure curl is installed, we will use curl to pull the dess installation file:

```
sudo apt install curl
```

Finally, run the dess installer:

```
curl -fsSL https://getdess.atsign.com | sudo bash
```

Once the installer is finished you should be prompted like so:

```
Dess installed, please move on to the sudo dess-create command.
```

### 7. Registration of @sign in your private dess <a name="dess2@sign"></a>

At this step you should already have your @sign registered at http://atsign.com. If not **go do it!**

I have registered my own free @sign (@44likelycanary) which I will link to my dess.

In your instance console, navigate to dess folder. If you were following this guide it will be located in:

We now need to create the service that will host our @sign by executing the dess-create command:

```
$ sudo dess-create @44likelycanary 4atsign.link 8000 <email address> likelycanary
```

To make it more understandable:

I will be registering my @sign **@44likelycanary**.

I will be using my domain **4atsign.link** which I have registered through AWS.

I am using port **8000** which I have opened in my instance firewall.

My registration email address is **\<email address\>** (this email is used to sign the SSL certificates).

The last **likelycanary** is the name that docker will use to track the service.

If everything is successful you should see output like this:

![img](images/clip_image004-162728549379914.jpg)

At this moment your @sign is registered on your dess.

## 8. Activation of @sign<a name="activation"></a>

Next up we need to activate it

Login to your dashboard at https://my.atsign.com/dashboard

Open “my @signs”

![gcp-atsign-dashboard](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-dashboard.png)

Open “managed” of @sign you are registering”

![gcp-atsign-nonactive](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-nonactive.png)

Navigate to Advance settings:

![gcp-atsign-active](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-active.png)

If you have already activated your @sign you will be prompted to erase all your data first

![gcp-atsign-erase](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-erase.png)

Once done you are able to link your @sign with your private dess. Use your domain and port number with which you have created service on your cloud instance and press Activate

![image-20210617111907819](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-advance.png)

You should see that your @sign is being activated in your dashboard:

![gcp-atsign-activating](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-activating.png)

The activation will be completed once you have used your QR code from dess and retrieved your keys.

Once the activation process completes you are welcomed by green Activated.

![gcp-atsign-activated](/docs/guides/dess-setup/dess-gcp/images/gcp-atsign-activated.png)

<u>**CONGRATULATIONS**</u>
