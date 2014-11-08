---
layout: post
title: "How Bitcoin works"
---

Ignoring economic or political considerations, the "cryptographic problem" that
Bitcoin solves is that of a token-passing system. Ie, you have a bunch of
people who all have tokens of some kind, and you want to allow these tokens to
be passed between them, guaranteeing that no one can claim to have a token that
they don't.

There's essentially two ways to falsely claim that you have a token: you can
claim to have a token that you never had, or you can claim to have a token that
you once had but then gave to someone else.

A simple, non-distributed solution to this problem is just to have some central
server keeping track of who has what tokens. Each transaction notifies the
server that a token transfer is taking place. The server knows not to allow
anyone to give away a token that they either never had or no longer have. In
fact this distinction is less meaningful in the case of a central server: to
the server, all that matters is whether you currently have a token or not.

Of course, this solution is not distributed: a single entity is responsible for
keeping track of everyone's tokens, and the system has a single point of
failure.

We want to try something else. An initial attempt at a distributed solution
might be something like this: assume some initial distribution of tokens is
known to everyone. If Alice wants to transfer a token to Bob, she'll use a
private [RSA] key to digitally sign the message "Alice gives token X to Bob."

Now, say Bob wants to give this token to Carol. He can show Carol this signed
message, and Carol can use Alice's public key to verify the message's
authenticity. Carol now knows that Alice gave her token to Bob, and Carol also
knows that token X initially belonged to Alice, so she knows that Bob now has
the token. Then, Bob will take the message "Bob gives token X to Carol", along
with the signed message "Alice gives token X to Bob", sign both of those with
his own private RSA key, and give the final signed message to Carol. Now Carol
can prove to some other party that she is the rightful owner of token X.

Well, actually, no, she can't prove this. What she can prove is that she _was_
the owner at one point, but she has no way of proving that she hasn't since
given it away: this scheme doesn't prevent double-spending. For instance,
suppose that after Alice gave her token to Bob, but before Bob gives it to
Carol, Alice herself approached Carol and tries to transfer the token to her.
Carol has no way of knowing Alice has already given the token away to Bob.

Later, when Bob comes around with his "copy" of Alice's token, Carol will
realize Alice double-spent, but only after she's already accepted Alice's copy
of the token. Even then, she won't know if Alice duped her or if Bob is trying
to dupe her. That particular issue can be resolved by timestamping
transactions, but the primary issue remains that no one knows they've been
duped until some other person happens to come along with a copy of the same
token. Thus, there's no way to be sure that a transaction is legitimate at the
time that it happens.

## Keeping track of transactions

In order to prevent double-spending at transaction-time (instead of after the
fact), we need the system to be aware of transactions that have taken place.

A straight-forward approach would be to have nodes broadcast pending
transactions to other nodes. Thus, before a node accepts any transaction as
legitimate, it will need to hear from all the other nodes and be sure that the
token in the pending transaction isn't simultaneously pending in some other
transaction and also hasn't already been spent. 

This approach is essentially equivalent to taking the centralized server
approach and replicating the storage across all nodes participating in the
system. It's a natural first solution, but it has several problems.

1. It requires that a node speak to all other currently participating nodes
before a transaction can be verified. This isn't easy. Links between nodes
might go down and communication can be temporarily impossible. Even assuming
totally reliable links, it's a fair amount of communication overhead.

2. If nodes can enter and exit the network, then nodes that enter the network
need to have a way of finding out the transaction histories of nodes that were
once in the network but have since exited. They can get this history from other
nodes still in the network, but how are they to know which history to trust?
How do they know transactions aren't being left out?

In a sense, issue 2 is a form of issue 1, just spread over time: two nodes that
existed in the network at different times definitely can't communicate with
each other, just like two nodes that existed in the network at the same time
can't necccesarily communicate with each other.

Standard techniques exist in the realm of distributed systems for solving these
kinds of problems. [Leader election] and [consensus] algorithms, for instance,
can be used to disseminate a single transaction history throughout the network.
However, these algorithms only work as long as a majority of nodes in network
are "honest".

Since anyone can join the Bitcoin network, it'd be very easy for someone to
connect lots and lots of nodes to the network, all under their control, and use
it to disrupt the system. "Nodes" in this sense are not necessarily difficult
or expensive to add. A node is basically uniquely identified by its IP
addresses, and it wouldn't be too hard for someone to have lots of IP addresses
available to them by simulating machines; they don't need actual separate
hardware for the various nodes in the system.

Instead of performing leader election and consensus based on the number of
nodes in the system, we want to use the amount of computing power in the
system, which incurs more of a cost for an attacker to control. The Bitcoin
paper describes this as "one vote per CPU" instead of "one vote per IP".

## Proof of work

We want a way for the network to agree on a which transactions have happened
without having all nodes speak to all others, and we want this to work even if
many nodes in the system are trying to cheat, but such nodes don't control a
majority of the processing power of the network.

To this end, pending transactions get broadcast to the network so that they can
be validated. Other nodes collect these transactions in batches called
_blocks_, and then, if they want, try to *mine* them, which requires that node
to devote a significant amount of CPU power to the task.

Mining a block of transactions is done by finding some value, called a nonce,
such that the [SHA] hash of the nonce appended to the block begins with a
certain number of zero bits.

The idea is that the output of cryptographic hash functions like SHA is
effectively random, and so all miners can do is randomly try different nonce
values until they get an output with sufficiently many leading zeros (the
probability that a hash begins with $n$ zeros is approximately
$\frac{1}{2^n}$). The more leading zeros we require, the more nonces a miner
will need to try before they find one that works, and thus the more CPU cycles
a miner will have to expend to find a valid nonce.

Once an initial batch of transactions has been mined, it gets broadcast to the
network, for all other nodes to see. Because of how cryptographic hashes work,
once a block has been mined, no transactions can be added or removed from the
block without re-mining it (which, again, requires a non-trivial amount of CPU
power).

Now, as more transactions come in, they are again broadcast to the network to
be mined. Only now, the mining nodes include the header of the first block in
their hashes: that is, they're trying to find a nonce so that SHA(first block +
second block + none) starts with sufficiently many zeros. This has the effect of "chaining" the blocks together: this new block that's being mined comes right after the first one.

## Trust the longest chain

Chaining the blocks allows us to have a single, linear history of all
transactions, which is neccesary to know exactly who has what coin (otherwise
two blocks could both be mined, but the network wouldn't know which of them
came first).

However, this could just as easily be solved by including timestamps or
sequence numbers in the blocks. The real power in including previous blocks in
the hashes for new blocks is that the transactions in the first block are now
even more secure. We said before that in order to modify the transaction
history once a block has been mined, someone would need to re-mine the block.
This is hard, but not impossible. However, say someone succesfully mines the
_second_ block in the chain. Now, if we want to modify the the first block, we
need to re-mine that block *and* the newly-mined second block. This is because
the network resolves conflicts in the transaction history by always trusting
the longest mined chain.

So the further back into the block chain a transaction goes, the more CPU power
someone is going to have to expend to take that transaction out of the chain
and convince other nodes of this.

## Incentives

We said the nodes *can* mine blocks if they want, but why would they want to?
One reason might be to have the system work, but we can run into free-rider
problems with that. If a node is going to devote processing power to the
network, and they don't have a guarentee that other nodes are going to do this
as well, it'd be nice to reward them. This is the approach Bitcoin takes. After
succesfully mining a transaction block, a node is allowed to reward itself with
a Bitcoin.

This incentives people to actually devote processing power to the system, and
also to do so honestly. Ie, someone might want to instead devote CPU power to
making transactions disappear, so that they're able to double-spend coins,
effectively increasing their own wealth. But, if they were to just devote their
CPU power to honestly mining transactions, they would be increasing their
wealth anyway, without decreasing people's trust in Bitcoin.

[RSA]: https://en.wikipedia.org/wiki/RSA_(cryptosystem)
[Leader election]: https://en.wikipedia.org/wiki/Leader_election
[consensus]: https://en.wikipedia.org/wiki/Consensus_(computer_science)
[SHA]: https://en.wikipedia.org/wiki/Secure_Hash_Algorithm
