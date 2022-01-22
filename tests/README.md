# Tests

## Nominal scenario

Consider two users, Satoshi and Bortch (so that for once Alice and Bob are left to their own activities).
Each user has a "wallet".
The blockchain is operational through different nodes. 
Thanks to his hard work, Satoshi has coins.
As a humble developer, Bortch has no coins.
We don't know exactly why (and it doesn't matter) Satoshi sends coins to Bortch.

## Requirement

Ouch! I already feel overwhelmed by my approach, but let's be brave, a journey of a thousand miles begins with a single step.

We need 2 wallets. A wallet will just be an address. But if you need an address, you need a public key and therefore a private key. It's still not the most complicated thing.

We need a blockchain with at least one functional node and an interface to communicate with it. Now it's getting slightly more complicated.

It is then necessary to be able to create a transaction, to validate it and to register it in a block which will be attached to the chain.

Great, let's do this!

## Diving

