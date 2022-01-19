---
title: "Encryption"
SEOtitle: "dess : distributed edge secondary server  - @platform(at_platform or AtPlatform)"
linkTitle: "Encryption"
weight: 5
content: Run your @platform secondary server on your own infrastructure
description: Run your @platform secondary server on your own infrastructure
---

The @protocol supports end-to-end encryption for all the data handled through it. This is difficult to do, especially for information that is shared with a large number of people and very frequently, so we had to come up with a clever mechanism to make the technology work.

Let’s describe a simple use case: @alice wishes to share her phone number with her friend @bob. To do this, @alice, who is on her own device, prompts her own secondary server to direct phone@alice at her friend @bob’s secondary server. From here, a shared key is generated for @bob (@bob:shared_key@alice).

This shared key uses the same encryption process as the Symmetric Key Encryption, which is called AES (Advanced Encryption Standard) and involves three block ciphers: AES-128, AES-192 and AES-256.

The @protocol specifically uses AES256 for Data Encryption Keys.

The RSA (Rivest–Shamir–Adleman) encryption algorithm is then used to encrypt the shared key from the above example with @bob’s public key. The @protocl specifically utilizes RSA 2048. Note, that because the RSA algorithm is an Asymmetric Key Encryption method, a public and private key are generated.

As this is a brief overview as to how encryption works on the @platform, you may read more [here](https://atsigncompany.medium.com/data-encryption-caching-with-the-protocol-debe9efc0f49).
