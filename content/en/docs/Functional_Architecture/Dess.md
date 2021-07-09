---
title: "dess"
linkTitle: "dess"
weight: 4
description: >
  dess enables you to run your own secondary server wherever you like and on any compatible infrastructure you would like to use.
---

## 1. What is dess?

dess is an acronymn for:  
> d. Distributed  
> e. Edge  
> s. Secondary  
> s. Server  

dess is used to host your own secondary server for your @sign(s).

## 2. How to get started

The first thing you need to know is that there are two parts to setting up dess.  
1. First time setup (run once)  
1. Setup an @sign (run for each @sign)  

## 3. First Time Setup
  
dess will install everything you need to get up and running.  
Run the following command and dess will be installed:

`curl -fsSL https://getdess.atsign.com | sudo bash`

Alternatively, if you would like to save the installation script to your machine:

```BASH
curl -fsSL https://getdess.atsign.com -o getdess.sh
sudo bash getdess.sh
```

The script will be saved as <span>getdess.sh</span>

## 4. Setup an @sign

dess will show you the steps to setup an atsign.
```bash
sudo dess-create
> Usage sudo dess-create <@sign> <fqdn> <port> <email> <service>
> Example sudo dess-create @bob bob.example.com 6464 bob@example.com bob
```

### Arguments

`@sign`: The @sign you want to setup.

`fqdn`: Fully qualified domain name to use for dess.  
(The same as entered in the atsign.com dashboard)

`port`: The port to use for dess.  
(The same as the entered in the atsign.com dashboard)

`email`: An email you own to sign the certificates with.

`service`: A name for the docker service.

## 5. Oops! I forgot to save my QR

Don't worry! dess includes a command to recover lost QR codes.  
Simply run the following:

`dess-reshowqr <@sign>`

## 6. OS Support

(Work in progress - to be updated soon)
