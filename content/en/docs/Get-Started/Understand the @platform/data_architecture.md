---
title: 'Data Architecture'
SEOtitle: 'No Backend Data Architecture Infrastructure Free'
linkTitle: 'Data Architecture'
weight: 2
content: Run your @platform secondary server on your own infrastructure
description: Run your @platform secondary server on your own infrastructure
toc_hide: true
hide_summary: true
draft: true
---

## 1. What is dess?

dess is the self-hosted option for secondary servers,
and a great tool for developers to debug their applications!
You can run several secondary servers on a single instance of dess,
as each secondary scales to use 6MB of ram or less.

dess is an acronymn for:

> d. Distributed  
> e. Edge  
> s. Secondary  
> s. Server

## 2. How to get started

There are two parts to setting up dess:

1. First time setup (run once)
1. Setup an @‎sign (run for each @‎sign)

## 3. First Time Setup

### Get a server

First get yourself a microserver to run dess on.

We recommend AWS, GCP, or IONOS for hosting.

1 Core + 1 GB is more than enough to run dess comfortably.

### Install dess on the server

dess will install everything you need to get up and running.  
Run the following command to install dess:

`curl -fsSL https://getdess.atsign.com | sudo bash`

Alternatively, if you would like to save the installation script to your machine:

```BASH
curl -fsSL https://getdess.atsign.com -o getdess.sh
sudo bash getdess.sh
```

The script will be saved as <span>getdess.sh</span>

### Setup a domain for your server

If you don't have a domain available you will have to purchase one to continue.

Once you have a domain available, set an A record pointing to the IP of your server.

For example:

```
Domain: example.com
Server IP: 123.123.123.123
```

Example A record:

```
A    dess    123.123.123.123
```

You may replace "dess" with any valid value for a subdomain.  
In this example, my fully qualified domain name (fqdn) is:

```
dess.example.com
```

Once you have completed these steps, please move on to setting up your secondary server!

## 4. Setup a secondary server

### On my.atsign.com/dashboard

1. Go to "My @‎signs."
1. Select "Manage" for the @‎sign you would like to setup.
1. Open "Advanced Settings".
1. If the atsign is activated, follow the steps to reset it. (Warning: this will erase your data!)
1. Under "settings" enter the fully qualified domain name from initial setup.
1. Enter an unused port number.
1. Press "Activate"

### On your dess server

dess will show you the steps to setup a secondary server.

```bash
sudo dess-create
> Usage sudo dess-create <@‎sign> <fqdn> <port> <email> <service>
> Example sudo dess-create @‎bob bob.example.com 6464 bob@‎example.com bob
```

#### Arguments

`@‎sign`: The @‎sign you want to setup.

`fqdn`: Fully qualified domain name to use for dess.  
(The same as entered in your atsign.com dashboard )

`port`: The port to use for dess.  
(The same as entered in your atsign.com dashboard)

`email`: An email you own to sign the certificates with.

`service`: A name for the docker service.

## 5. OS Support

| Distribution | Version     | x86 | arm64 | armv7 |
| ------------ | ----------- | --- | ----- | ----- |
| Amazon Linux | 2           | ✔   | ✔     |       |
| Centos       | 7,8         | ✔   | ✔     |       |
| Debian       | 10          | ✔   | ✔     |       |
| Raspbian     | 10          |     |       | ✔     |
| Rocky Linux  | 8           | ✔   | ✔     |       |
| Ubuntu       | 20.04-21.04 | ✔   | ✔     |       |

## 6. dess Setup Guides

If you are ready to get started, please check to see if we have a [specific guide](/docs/guides/dess-setup/) available for your platform of choice.

We have guides available for the following platforms:

- [GCP (Google Cloud Platform)](/docs/guides/dess-setup/dess-gcp/)
- [AWS (Amazon Web Services)](/docs/guides/dess-setup/dess-aws/)
- IONOS (Coming soon)

## 7. Tips & Tricks

### Oops! I forgot to save my QR code!

Don't worry! dess includes a command to recover QR codes.  
Simply run the following:

`dess-reshowqr <@‎sign>`

### Debugging Applications with Dess

dess runs as a docker swarm, to debug an application first run the following:

```bash
docker service ls
```

Docker will list the services running:

```bash
ID             NAME                   MODE         REPLICAS   IMAGE                          PORTS
b61ty3y5g41a   secondaries_shepherd   replicated   1/1        mazzolino/shepherd:latest
ex2d0kmiqinn   wolverine_secondary    replicated   0/1        atsigncompany/secondary:dess   *:6464->6464/tcp
```

For example, I have the service called "wolverine_secondary" running.  
To debug this secondary using docker:

```bash
docker service logs -f <service_name>
# OR
docker service logs -f wolverine_secondary
```

While this is running, you will be able to see the secondary in action.

## Where should I go next?

First, if you haven't setup Flutter, do that [here](/docs/get-started/setup-your-env/).

Otherwise, continue to building your first app [here](/docs/get-started/create-a-project/).
