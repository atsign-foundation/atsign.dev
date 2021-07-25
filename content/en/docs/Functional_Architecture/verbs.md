---
title: "The @protocol verbs"
linkTitle: "Verbs"
weight: 0
content : Understand the @platform verbs and their functions
description: >
  Understand the @platform verbs and their functions
---

### from
The “from” verb is used to tell the secondary server what @sign you claim to be, and the secondary server will respond with a challenge. The challenge will be in the form of a full @ address and a cookie to place at that address. Before giving the challenge it will verify the client SSL certificate. The client SSL certificate has to match the FQDN list in the root server for that @sign in either the CN or SAN fields in the certificate.
### cram
The cram verb is used to authenticate the @sign to the secondary server. On successful request, binds the @sign to the secondary server. The secret is appended to the challenge (response of from verb) and gives a SHA512 digest which serves as an input to the CRAM verb. On successful cram verb request, the @sign is successfully authenticated to the secondary server and allows user to Add/Update, Delete and lookup the keys in their respective secondary servers.
We use "cram" authentication for the first time and will create a public/private key pair for pkam authentication for subsequent logins.
### pkam
The pkam( Public Key Authentication Mechanism) verb is used to authenticate the @sign to the secondary server. This is similar to how ssh authentication works. On successful request, binds the @sign to the secondary server.On successful pkam verb request, the @sign is successfully authenticated to the secondary server and allows user to Add/Update, Delete and lookup the keys in their respective secondary servers.
### scan
The "scan" verb scans the available keys. If the key has a '_' character has it first character, then it is omitted from the scan list, although it can still be looked up if known.
The scan verb when used by unauthenticated @sign user, scans for keys that are publicly available to you.The scan when used by an authenticated user via the cram verb, scans all the available keys on the secondary server.
You can use scan verb with regex if you want to get keys matches with the regex.
### lookup
The “lookup” verb allows the lookup of a particular address in the @ handles namespace. The “lookup” verb provides public lookups and specific key look ups when authenticated as a particular @ handle using the “from” and “pol” verbs. If a lookup is valid the resulting information is returned with the data: header and a carriage return and a further @ prompt ready for further commands. If the lookup is not valid then a null is returned again with the data: header.
The @sign should be authenticated using the cram verb prior to use the lookup verb.
### plookup
The "plookup" verb, provides a proxied public lookups for a resolver that perhaps is behind a firewall. This will allow a resolver to contact a @ server and have the @ server lookup both public @ handles information. This will be useful in large enterprise environments where they would want all lookups going through a single secondary server for the entity or where a single port needs to be opened through a firewall to lookup @ handles.
The @sign should be authenticated using cram verb prior to use the plookup verb.
### llookup
The "llookup" verb can be used to locally lookup keys stored on our secondary server. To perform local look up, the user should be successfully authenticated via the "cram" verb.
### update
The "update" verb is used to create/update the keys in the secondary server. We can create/update both public and private keys. kThe update verb is used to set public responses and specific responses for a particular authenticated users after using the pol verb.
The @sign should be authenticated using cram verb prior to use the update verb.
### delete
The "update" verb is used to delete the keys in the secondary server. A delete request must contain the distinguished name of the key to be deleted. The @sign should be authenticated using the cram/pkam verb prior to use the delete verb. 
### notify
The “notify” verb used to notify a key to another atsign. The @sign should be authenticated using the cram/pkam verb prior to use the notify verb.
You can send a notification to multiple users using "notify:all" command. Also you can list out all the notifications using "notify:list". 
### monitor
The “monitor:” verb is used to monitor either all or specific notification events that are sent using the “notify:” verb.  Notifications are both queued and managed by the secondary server, and the status of an individual notification can also be seen.
### stats
The "stats" verb used to get all the available metrics. We can get specific metrics by providing ',' separated list like stats:1,2. If we didn't provide anything it will return all the metrics information.
### sync
The "sync" verb is used to fetch all the changes after a given commit sequence number from the commit log on the server. This verb is helpful when local and remote secondary servers are not in sync. We can sync only specific keys by providing regex pattern(sync:<commit id>:<regex>).
### config
The "config" verb is used for configuring or viewing an @sign's block/allow list. 'from' verb functionality is dertermined by using the configurations of 'config' verb. If an atsign is in block list, secondary server won't allow it for authentication.
### pol
The "pol" verb allows to switch as another @sign user. To switch as another user, use from:<@sign>(The another @sign user) verb which gives a response as proof:<key>; then use pol verb. On successful authentication, the prompt changes to the another @sign user. If we authenticate to other atsign using pol, we can only access public information available. 
