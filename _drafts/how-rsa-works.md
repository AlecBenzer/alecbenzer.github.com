---
title: "How RSA works"
layout: post
---

If you'll indulge me, I want to have a go at explaining how RSA works (something I've had trouble doing in the past.)

RSA is an algorithm for public-key cryptography. Public-key cryptosystems are a little less intuitive than "traditional" private-key cryptography. With private-key crypto you have something you're trying to keep hidden so you use a shared secret (ie, a private key) to protect it. It's like a locked box: you put something in it and then you lock the box with a key, and then whoever else has the key can open the box and see what's inside.

With public-key crypto, instead of a box with one key, you have a box with two keys. When you lock the box with one of they keys, only the other key can open it. The idea is that one of these keys is something everyone has access to, the public key, and the other is a non-shared secret (ie, only one person has it), the private key.

This lets you do two things. First, anyone with the public key can put something in the box, and know that only the person with the private key (call her Alice), can see it. Or, Alice can put something in the box with her private key, and anyone with the public key who looks at the box knows that whatever's in there was put there by Alice. More on this later.

You might see why public key crypto seems unintuitive. Getting away from the boxes and thinking in terms of computers and data, public-key crypto gives you a way of transforming data with a public key so that you can't undo what you just did, *but*, the person with the private key *can* undo it. Let's see how this is possible.

---

Let's walk through how encryption and decryption work with RSA _assuming we already have the public and private keys_. Unlike private-key crypto, where the keys are basically just random strings of bits, the key pairs in RSA are carefully chosen, and most of the magic of RSA comes in generating keys for it. Once we have them, the rest is straightforward.

Both of our keys are just pairs of two numbers. The public key is a pair $(e, n)$, and the private key is a pair $(d, n)$. Note that both keys contain $n$. The public key has a number $e$ used for **e**ncrypting, and the private key has a number $d$ used for **d**ecrypting (really, we could also encrypt things with the private key and decrypt them with the public key, but don't worry about that for now).

Now say we have some message $M$ that we want to transmit. For simplicity assume $M$ is a number. Everything on computers is ultimately represented as a string of bits anyway, which we can just interpret as a number.

To encrypt our plaintext message $M$ and get our ciphertext $C$, we perform the following [modular exponentiation]:

$$C = M^e \bmod{n}$$

That's it. For those who are familiar how private-key crypto systems like AES work, this is refreshingly simple.

Ready for decryption? From a ciphertext $C$, we get our decrypted plaintext $M'$ by doing

$$M' = C^d \bmod{n}$$

If our keys were generated correctly, then we have $M' = M$ (technically, we have $M' \equiv M \bmod{n}$, which means $M' = M$ as long as $M < n$).

That's it; that's all there is to actually performing RSA once we have our keys. The fun, of course, is in how we get the keys so that RSA actually works.

---

From the above explanation you should be able to infer the property that we want our keys to have: we want modular exponentiation by $d$ to undo modular exponentiation by $e$.

It turns out that, given the [prime factorization] of our modulus, $n$, it's easy to find an $e$ and a $d$ so that $\left(M^e\right)^d \equiv M \bmod{n}$ for all messages $M$. I'll explain why later, but for now, just take this as fact. It's also believed that there's no way to find $e$ and $d$ without first finding $n$'s prime factorization.

Well, it turns out that, given only $n$, prime factorization is [pretty hard](http://en.wikipedia.org/wiki/Integer_factorization#Difficulty_and_complexity) for large $n$ (where "large" means on the order of hundreds of bits). This means that if all you have is $e$ and $n$, and $n$ is large enough, finding $d$ is going to border on impossible. Which is good! This means that someone can't use the public key $(e, n)$ to find the private key $(d, n)$.

But then how do we generate our keys? That's easy: we can just _generate_ two primes $p$ and $q$, and multiply them to get $n = p\cdot q$. Now we know that $n$'s prime factorization is just $p\cdot q$, and we can use this to compute $e$ and $d$ (again, I haven't explained _how_ yet, but take my word.)

If you understand everything above, then you're just a little bit of number theory away from understanding RSA! The main thing that's going on is that factoring is hard, so even though we could generate correct keys given our primes $p$ and $q$, once we throw $p$ and $q$ away, it's hard to get them back from $n$, and there's no known better way of getting $e$ and $d$ from $n$.

## Finding $e$ and $d$

What follows is a non-trivial amount of number theory. Understanding the details of how exactly we get from $p, q$ to $e$ and $d$ isn't super important to having a decent high-level understanding of how RSA works, and so if you don't understand everything that's discussed here it's not a huge deal in my opinion. But, for the curious, it definitely nice to have a better idea of why _exactly_ RSA works.

We'll work bottom-up, introducing some basic tools and them combining them to get the results we need.

### Fermat's little theorem

Fermat's little theorem says that for a prime number $p$, $a^p \equiv a \pmod{p}$ for any integer $a$.

There are [many proofs](http://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem) of Fermat's little theorem. One of the most accessible proofs involves thinking about [necklaces of beads](http://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_by_counting_necklaces). It even exists in video-form:

{::nomarkdown}
<iframe width="560" height="315" src="//www.youtube.com/embed/OoQ16YCYksw?rel=0" frameborder="0" allowfullscreen></iframe>
{:/nomarkdown}

I'll try and explain one of the more direct proofs here.


[modular exponentiation]: http://en.wikipedia.org/wiki/Modular_exponentiation
[prime factorization]: http://en.wikipedia.org/wiki/Prime_factor
