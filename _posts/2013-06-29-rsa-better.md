---
layout: post
title: "Better RSA explanation"
---

A few years ago I had no idea what RSA was and so tried to learn about it. To check my own understanding (which is a part of why I write a lot of this kind of stuff), I wrote [a post](/blog/rsa) trying to explain RSA. Re-reading it, the post is mostly accurate, but does a poor job of coherently explaining what's going on and motivating what RSA's used for.

Recently I've been trying to get a better handle on cryptography, so let me try again.

## Motivation

So first of all RSA was the first and is still one of the most popular **asymmetric** crypto schemes. What most people would think of as "normal" encryption is a _symmetric_ crypto scheme. This is one where the same key is used to both lock and unlock something. You know, like doors. You lock a door with a physical key, leave, and then you come back later _with the same key_ and unlock the door.

With an asymmetric scheme, there are two keys: one for locking and another for unlocking. The keys are different, and they can _only_ do the thing they are meant to -- the locking key locks something but then can't unlock it; only the unlocking key can do that.

I would say that the unlocking key also can't lock anything, but that's actually not really true. Instead of an "lock" and "unlock" key, just think of keys 1 and 2. Anything key 1 locks can only be unlocked by key 2, and anything key 2 locks can only be unlocked by key 1.

At first this seems kind of odd -- if you lock something with key 1, you can't undo what you just did. While maybe not so odd in the context of physical keys, it's hard to imagine a way of transforming some data so that you can't transform it back. But it's actually more than that -- not only do you have no way of transforming the data back, but someone _else_ (who has key 2) can. Intuition might tell us that this kind of a thing should be impossible.

On top of being seemingly hard to implement something like this, it's not quite clear why we would want to (ie, it's not clear what asymmetric crypto gives us that we couldn't get from symmetric crypto).

One benefit asymmetric crypto has over symmetric crypto is that with symmetric schemes, there has to be some way of giving the key to both parties that want to share a secret ahead of time.

With RSA this isn't needed (well, it isn't _as_ necessary). If you're trying to send a secret message to someone, you can just send them key 1, while keeping key 2 secret. They encrypt a message with key 1, send it over to you, and now you can decrypt the secret with key 2, which has never left your side. This type of thing is not possible with symmetric cryptography, since giving someone the ability to encrypt messages necessarily means giving them the ability to decrypt messages as well.

While this is a useful property for RSA to have, it actually isn't all that special. There are key-exchange protocols that allow two parties to exchange a key that can be used for symmetric cryptography without giving the key away to third parties.

A much more important problem that RSA allows us to solve is that of authentication. Suppose you want to communicate with some server and be sure that you're communicating with the right person. Using RSA, the person can generate keys 1 and 2, and send you key 2, while keeping key 1 for themselves. They then encrypt a message using their key 1, and send it over to you. You use key 2 to unlock the message, and the fact that the unlocking worked tells you that the locking was done by whoever had key 1.

This is in some sense the more fundamental problem that asymmetric cryptography solves, which couldn't really be done via symmetric cryptography.

But anyway, now that we've had some motivation, let's see how RSA actually works.

## Public & private keys

To recap: in RSA we have two keys, which I was calling one and two. Anything key one locks can only be unlocked with key two, and vice versa.

As was illustrated in the above examples, usually one key is kept secret, while the other is sent to other people publicly. In the case of sending a secret message, the key that stays hidden is the one that's used to do the unlocking, and in the case of authentication, the hidden key is the one that does the locking. But in either case, one key is always secret.

Because of this, we generally refer to one key as the **public key** and the other as the **private key** (not as key 1 and key 2). Asymmetric cryptography is actually sometimes called "public key" cryptography for this reason.

## Modular arithmetic

RSA operates primarily on something called **modular arithmetic**. Modular arithmetic is sometimes explained as "clock arithmetic". What's eleven o'clock plus three hours? 11 + 3 is 14, but three hours after 11 o'clock is 2 o'clock. Instead of going past 12, the numbers wrap around.

For fancy non-Americans, what's 22:00 plus 5 hours? 22 + 5 is 27, but 5 hours after 22:00 is 03:00. Arithmetic using 24-hour time can be said to be arithmetic **modulo 24**. 12-hour time is (sort of) like arithmetic modulo 12 (I say "sort of" because for it to really be modulo 12, the minute before 1:00 would have to be 0:59, not 12:59).

When using modular arithmetic we talk about things being **congruent** instead of equal, using the symbol $\equiv$. That is, 22 + 5 is _equal to_ 27, but it is _congruent to_ 3 modulo 24. Notationally, we'd write this as
$$\begin{eqnarray\*}
22 + 5 &=& 27 \\\\
22 + 5 &\equiv& 3 \pmod{24}.
\end{eqnarray\*}$$

We could also write directly that

$$ 27 \equiv 3 \pmod{24}. $$

Many facts that are true about arithmetic in general remain true for modular arithmetic. For instance, if we say that

$$ a = 4^3 $$

and that

$$ b = a^7 $$

then it'd be the case that

$$ b = \left(4^3\right)^7 = 4^{3\cdot 7} = 4^{21}.$$

None of that changes when we introduce mods. That is, if

$$ a \equiv 4^3 \pmod{24} $$

and

$$ b \equiv a^7 \pmod{24} $$

then

$$ b \equiv 4^{21} \equiv 16 \pmod{24}.$$

We could write that more compactly as

$$\left(\left(4^3\pmod{24}\right)^7\pmod{24}\right) = \left(4^{21} \pmod{24}\right) = 16.$$

Here we're abusing notation a bit and using $\left(a\pmod{m}\right) = b$ to mean that $b < 24$ and that $a \equiv b \pmod{m}$, but I think the idea is clear.

The number $16$, by the way, came from the fact that if we kept subtracting $24$ away from $4^{21}$ until we got to something less than $24$, we'd end up at $16$. Or, said another way, the remainder left after diving $4^{21}$ by $24$ is $16$.

## Discrete roots are hard

So the basic idea behind RSA is this: say we have some message $m$, encoded as a number, that we'd like to encrypt. Something we could is to raise $m$ to some power $e$ to get some 'cipher text' $c = m^e$. This isn't much of an encryption though, because we can undo the process by taking a root. That is, $c^{1/e} = \left(m^e\right)^{1/e} = m$. Taking roots of something is easy, so this encryption can easily be undone. And remember, the idea is that once we encrypt something, we want to not be able to decrypt ourselves.

So what we can do instead is raise $m$ to some power, and then compute that modulo some base number. That is, if $n$ is some large number, we could compute $c = m^e\pmod{n}$. Because we're taking a modulus, the problem of undoing the encryption goes from taking a root to taking a _discrete_ root. And taking discrete roots is hard. I might go into why that is and what exactly is means for something to be "hard", but for now just trust that if $n$ is big enough, it's going to take an infeasible amount of computational power to compute the $e$-th discrete root of $c$.

Of course, on the surface, this actually doesn't solve all that much. Sure, it's hard for us to recover the message, but we need someone else to be able to recover it.

To this end, we'd like to be able to find some other exponent $d$, with the property that 

$$ \left(m^e\right)^d = m^{ed} \equiv m \pmod{n}.$$

$d$ will be the other half of our key, which we'll use to decrypt what we encrypt with $e$ (we'll see later that knowing only what $e$ is won't let us easily compute $d$).

## Euler's totient theorem

So to help compute $d$, we're going to look at a theorem called "Euler's totient theorem", which says that if $n$ and $m$ are coprime (share no factors), then

$$m^{\varphi(n)} \equiv 1 \pmod{n},$$

where $\varphi(n)$ is called the **totient** of $n$, and is defined to be the number of positive integers less than $n$ that are coprime to $n$.

For instance, there are 14 positive integers less than 15:

1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14

Of these, 3, 5, 6, and 9 share factors with 15. Which leaves behind 1, 2, 4, 7, 8, 11, 13, 14: 8 numbers. Therefore, $\varphi(15) = 8$.

Ignoring _why_ this is true (I'm not going to prove it here, but you can refer to [the proof on wikipedia](http://en.wikipedia.org/wiki/Euler%27s_theorem#Proofs) if you'd like), we can see that it's a useful fact. Multiplying both sides of the equation by $m$, we get

$$m^{\varphi(n)}\cdot m \equiv 1\cdot m \pmod{n} $$
$$m^{\varphi{n}+1}\equiv m\pmod{n}$$

So, if we can find a $d$ so that $ed = \varphi(n) + 1$, we will have found a $d$ so that $m^{ed} \equiv m\pmod{n}$, which is what we want. Unfortunately trying to solve this directly as

$$d = \frac{\varphi(n) + 1}{e}$$

won't quite work, because we want $d$ to be an integer. However, if instead of having $ed = \varphi(n) + 1$, we had that, for some positive integer $k$, $ed = k\varphi(n) + 1$, everything would still work out. We'd have:

$$m^{ed} = m^{k\varphi(n) + 1} = m^{k\varphi(n)}m^1 = \left(m^{\varphi(n)}\right)^km$$

because $m^{\varphi(n)} \equiv 1\pmod{n}$, we can replace $m^{\varphi(n)}$ above with 1:

$$\left(m^{\varphi(n)}\right)^km \equiv 1^km \equiv m \pmod{n}.$$

So just as we want, we get $m^{ed} \equiv m\pmod{n}$ when $ed = k\varphi(n) + 1$.

And actually, find a $d$ so that $ed = k\varphi(n) + 1$ is actually just the same thing as find a $d$ so that $ed \equiv 1 \pmod{\varphi(n)}$. Either way of looking at it though, if we know what $\varphi(n)$ is, figuring out $d$ is doable.

## Computing the totient

Unfortunately, being able to compute $\varphi(n)$ for big $n$ isn't that easy. If $n$ were a 100 digit number, for instance, there'd be on the order $10^100$ positive integers less than $n$, and we'd have to go through all of them to find out which ones were coprime. This would take a _very_ long amount of time -- long enough that computing $\varphi(n)$ directly like this is infeasible.

This is actually sort of good -- if computing $\varphi(n)$ were easy, then anyone could do so, and use it to compute $d$ given $e$, allowing them to easily undo an encryption we do with $e$. Which is exactly what we wanted to _not_ be possible.

But it still remains that _we_, in the process of generating $d$ and $e$, need a way of computing $\varphi(n)$ easily, so that others wouldn't be able to do it later.

Well, for certain values of $n$, $\varphi(n)$ can actually be very easy to compute. Suppose $n$ were prime, for instance. In that case, _all_ of the $n-1$ positive integers less than $n$ would be coprime to it (any number is coprime to a prime number). So we'd have $\varphi(n) = n -1$.

This makes computing $\varphi(n)$ easy, but would also make it really easy for anyone else to compute it given $n$. So this doesn't work.

## Factoring is hard

Okay, so what if $n$ isn't itself prime, but is the product of two primes, $p$ and $q$? Here, again, the totient of $n = pq$ is _pretty_ easy to compute. It turns out that $\varphi(pq) = (p-1)(q-1)$. I won't explain why fully but it's not too hard to reason out -- $n$ is coprime with $p, 2p, 3p, \ldots, (q-1)$ as well as $q, 2p, 3q, \ldots, (p-1)q$. Counting those while avoiding double-counting should lead you to $(p-1)(q-1)$.

So if instead of just picking $n$ randomly, we instead randomly pick two primes $p$ and $q$, and multiply them together to get $n = pq$, we can easily compute $\varphi(n) = (p-1)(q-1)$, _and_, we've made it difficult for anyone who doesn't know that $n$ is the result of multiplying $p$ and $q$ to compute it, since going backwards from $n$ to $p$ and $q$ is hard (this is because factoring is hard).

So this is really the "crux" of RSA. We generate two large primes $p$ and $q$, use them to compute $n, e, d$ so that $m^{ed}\equiv m\pmod{n}$, and then we throw $p$ and $q$ away, saving only the pair $(e,n)$ as key 1 (generally $e$ is the public key) and the pair $(d,n)$ as key 2. Because $p$ and $q$ are gone, there is no easy way of recomputing $d$ given only $(e,n)$, or recomputing $e$ given only $(d,n)$. We have two keys, each of which undo the locks of the other, but which themselves cannot be use to undo their own locks.

Ta-da! RSA magic.

## Well actually...

there's one thing we neglected to deal with. If you remember back all the way to the statement of Euler's theorem, we mentioned that in order for it to be true, $m$ and $n$ must be relatively prime. $n$ is the product of two primes, so it's very likely to be coprime with most numbers, _but_, it's not coprime with everything, and there's a chance our message $m$ and $n$ are coprime.

There's a different proof of RSA that deals with this fact but is a bit more lengthy, and involves Fermat's little theorem instead of Euler's theorem. And this proof accounts for the case where $m$ and $n$ aren't coprime. <a href="http://en.wikipedia.org/wiki/RSA_(algorithm)#Proof_using_Fermat.27s_little_theorem">You can see the proof here</a>. Long story short though, it still works. :P

## Summary

So, to reiterate: given a message $m$, we want to find an $n$ and keys $e, d$ so that

$$m^{ed} \equiv m \pmod{n}.$$

If $n$ is a large non-prime, this problem is too hard -- it's basically impossible to find $e$ and $d$.

If $n$ is a large prime, this problem is easy -- so easy that anyone given $e$ and $n$ can find $d$ (or can find $e$ given $d$ and $n$). So that's no good.

But, if $n$ is the product of two large primes, then this problem is easy _if_ you know what the two primes are, but hard otherwise.

So this last thing is what we do. We generate large primes $p, q$, set $n = pq$, use $p$ and $q$ to compute $e$ and $d$, and then throw $p$ and $q$ away, thus making it impossible for anyone else to do what we just did.
