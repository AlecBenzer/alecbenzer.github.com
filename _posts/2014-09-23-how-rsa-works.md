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

That's it. We raise $M$ to the $e$th power and take the remainder mod $n$. For those who are familiar how private-key crypto systems like AES work, this is refreshingly simple.

Ready for decryption? From a ciphertext $C$, we get our decrypted plaintext $M'$ by doing

$$M' = C^d \bmod{n}$$

If our keys were generated correctly, then we have $M' = M$ (technically, we have $M' \equiv M \bmod{n}$, which means $M' = M$ as long as $M < n$).

That's it; that's all there is to actually performing RSA once we have our keys. The fun, of course, is in how we get the keys so that RSA actually works.

---

From the above explanation you should be able to infer the property that we want our keys to have: we want modular exponentiation by $d$ to undo modular exponentiation by $e$.

It turns out that, given the [prime factorization] of our modulus, $n$, it's easy to find an $e$ and a $d$ so that $\left(M^e\right)^d \equiv M \bmod{n}$ for all messages $M$. I'll explain why later, but for now, just take this as fact. It's also believed that there's no way to find $e$ and $d$ without first finding $n$'s prime factorization.

Well, it turns out that, given only $n$, prime factorization is [pretty hard](http://en.wikipedia.org/wiki/Integer_factorization#Difficulty_and_complexity) for large $n$ (where "large" means on the order of hundreds of bits). This means that if all you have is $e$ and $n$, and $n$ is large enough, finding $d$ is going to border on impossible. Which is good! This means that someone can't use the public key $(e, n)$ to find the private key $(d, n)$.

But then how do we generate our keys? That's easy: we can just _generate_ two primes $p$ and $q$, and multiply them to get $n = p\cdot q$. Now we know that $n$'s prime factorization is just $p\cdot q$, and we can use this to compute $e$ and $d$ (again, I haven't explained _how_ yet, but take my word.)

If you understand everything above, then you're just a little bit of number theory away from understanding RSA! The main thing that's going on is that factoring is hard, so even though we could generate correct keys given our primes $p$ and $q$, once we throw $p$ and $q$ away, it's hard to get them back from $n$, and there's no known better way of computing $e$ and $d$.

## Finding $e$ and $d$

What follows is a non-trivial amount of number theory. Understanding the details of how exactly we get from $p, q$ to $e$ and $d$ isn't super important to having a decent high-level understanding of how RSA works, and so if you don't understand everything that's discussed here it's not a huge deal in my opinion. But, for the curious, it definitely nice to have a better idea of why _exactly_ RSA works.

We'll work bottom-up, introducing some basic tools and them combining them to get the results we need. Varying amounts of number theory review might be needed depending on the reader; I'll just discuss as much number theory as I needed to review when writing this post. This may be too much or too little for you (in the latter case poking around Wikipedia should be helpful.)

### Modular multiplicative inverses

When dealing with rational numbers, we know that we can divide by any number that's not zero. Ie: for any number $x$ unequal to zero, there exists a number $x^{-1}$, such that $x^{-1}\cdot x = 1$ (namely, $x^{-1} = 1 \mathbin/ x$.) $x^{-1}$ is called a multiplicate inverse (it inverts multiplication by $x$.)

When dealing with modular arithmetic, the situation is a little more interesting. First of all, we have multiplicative inverses without needing to deal with fractions. For example: $5 \cdot 2 \equiv 1 \mod{9}$. This means that $5$ and $2$ are multiplicative inverses: $2^{-1} = 5$ and $5^{-1} = 2$.

The second interesting thing to note is that not all non-zero numbers have inverses. For example: does $6$ have an inverse mod $9$? Suppose there _were_ some number $x$ so that $6x \equiv 1 \mod{9}$. Then we'd have $6x = 9k + 1$ for some integer $k$. Rearranging, we get $6x - 9k = 1$. We can factor out a $3$ from $6$ and $9$ to get $3(2x - 3k) = 1$, and then finally we get $2x - 3k = \frac13$. But $2x - 3k$ is an integer, while $\frac13$ is not. So this equality can't hold, and such an $x$ can't possibly exist.

In fact, for any number $a$ and modulo $n$ such that $a$ and $n$ are co-prime, $ax \equiv 1 \bmod{n}$ has no solutions. We can repeat steps similar to above to get to $ax - nk = 1$. If $a$ and $n$ aren't co-prime, they have some common factor $d > 1$, so $\frac{a}{d} x - \frac{n}{d} k = \frac1d$. The left-hand side is an integer, but the right-hand side is not. So this equality can't hold.

Conversely (and more importantly for our purposes), if $a$ and $n$ _are_ co-prime, then $a^{-1}$ _does_ exist, and can be computed using the [extended euclidean algorithm]. As a special case, if $n$ is prime, then _all_ $a < n$ have multiplicative inverses mod $n$.

### Fermat's little theorem

Fermat's little theorem says that for a prime number $p$, $a^p \equiv a \pmod{p}$ for any integer $a$.

There are [many proofs](http://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem) of Fermat's little theorem. One of the most accessible proofs involves thinking about [necklaces of beads](http://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proof_by_counting_necklaces). It even exists in video-form:

{::nomarkdown}
<iframe width="560" height="315" src="//www.youtube.com/embed/OoQ16YCYksw?rel=0" frameborder="0" allowfullscreen></iframe>
{:/nomarkdown}

There's also [a more direct proof involving modular arithmetic](http://en.wikipedia.org/wiki/Proofs_of_Fermat%27s_little_theorem#Proofs_using_modular_arithmetic), which I'll try to explain here.

Consider the sequence:

$$ a, 2a, 3a, \dots, (p-1)a $$

The $k$th element of this sequence is $ka$. Consider the $k$th and $k'$th elements, $ka$ and $k'a$.

Suppose $ka \equiv k'a \pmod{p}$. Because $p$ is prime, we know $a^{-1}$ exists (see above), so we can multiply by it to get

$$kaa^{-1} \equiv k'aa^{-1} \implies k \equiv k' \pmod{p}$$

Since $k,k' < p$, this means that $k = k'$. Ie, if two elements of this sequence are equivalent mod $p$, then they're actually the same element. Another way of saying this is that every element of this sequence is distinct when taken mod $p$.

In addition to be distinct, each of the elements are also clearly between $1$ and $p-1$. This means that $a, 2a, \dots, (p-1)a$, taken modulo $p$, is just a re-ordering of the sequence $1, 2, \dots, p-1$. This then means that if we multiply the elements of each sequence, we should get the same product, since we're multiplying all the same numbers, just in a different order:

$$ a\cdot2a\cdot\dots\cdot(p-1)a \equiv 1\cdot2\cdot\dots\cdot(p-1) \pmod{p}$$

Collecting the $a$ terms on the left-hand side, we get

$$ a^{p-1}\cdot1\cdot2\cdot\dots\cdot(p-1) \equiv 1\cdot2\cdot\dots\cdot(p-1) \pmod{p}$$

Finally, because $p$ is prime, we know once again that each of $1, 2, \dots, p$ has a multiplicative inverse mod $p$, which means we can multiply both sides by $1^{-1}, 2^{-1}, \dots, (p-1)^{-1}$ to cancel out these terms. Leaving us with

$$ a^{p-1} \equiv 1 \pmod{p}$$

Or, by multiplying by $a$:

$$a^p \equiv a \pmod{p}$$

### Compute $d$

Now we'll say how to actually compute $d$. Given $e$ and $n = p\cdot q$, we want $d$ to be the multiplicative inverse of $e$ modulo $(p-1)(q-1)$.

$$ d \equiv e^{-1} \mod{(p-1)(q-1)} $$

Note that this isn't possible for all choices of $e$: as we've seen, $e$ must be co-prime to $(p-1)(q-1)$ for $d$ to exist. But this is fine, we can just choose $e$ so that it's co-prime to $(p-1)(q-1)$.

This sort of comes out of nowhere. Let's see why it works.

The thing that we want to show is that $\left(M^e\right)^d \equiv M \bmod{n}$. Let's try something simpler first: showing that $M^{ed} \equiv M \bmod{p}$ (again, where $n = p\cdot q$).

Because $d \equiv e^{-1} \bmod{(p-1)(q-1)}$, we know $ed \equiv 1 \bmod{(p-1)(q-1)}$, which in turn means that $ed = k(p-1)(q-1) + 1$ for some integer $k$.

This means that

$$M^{ed} = M^{k(p-1)(q-1) + 1} = M^{k(p-1)(q-1)}M = \left(M^{p-1}\right)^{k(q-1)}M$$

If we reduce this modulo $p$, then we can use Fermat's little theorem to replace the $M^{p-1}$ with 1 (unless $M$ happens to be $0$, but you should never use a message of $M = 0$ with RSA anyway, as the ciphertext will then be $M^e = 0^e = 0$).

$$\left(M^{p-1}\right)^{k(q-1)}M \equiv 1^{k(q-1)}M \equiv M \pmod{p}$$

Ie, we've shown that $M^{ed} \equiv M \bmod{p}$. A symmetric argument will show that $M^{ed} \equiv M \bmod{q}$.

We're _almost_ there! The last thing we need is to show that $M^{ed}$ and $M$ being equivalent mod $p$ and mod $q$ means they're equivalent mod $p\cdot q = n$.

We know that $M^{ed} - M = k_1p = k_2q$ for some integers $k_1, k_2$. This means $p$ and $q$ are both prime factors of $M^{ed} - M$, meaning $M^{ed} - M$ has a prime factorization that looks like $p\cdot q\cdot\left(\text{other stuff}\right)$. Thus, $M^{ed} - M$ is a multiple of $pq$, so it is equivalent to $0$ mod $pq$, which means $M^{ed} \equiv M \bmod{pq}$.

We're done! $pq = n$, so we have that $M^{ed} \equiv M \bmod{n}$. We've shown how to use $n$'s prime factorization $n = p\cdot q$ to come up with an integer $d$ (namely, $d \equiv e^{-1}\bmod{(p-1)(q-1)}$) so that exponentiation by $d$ undoes exponentiation by $e$.

Note that what we've proved is just that RSA works, in the sense that when you encrypt something with RSA, you get the same thing back after you decrypt. We've mentioned, but not proved, why RSA does a good job at keeping our data hidden. In fact, there's no real proof that RSA is sufficiently hard to break. It's _possible_ that there is an as-yet undiscovered efficient algorithm for factoring integers, which would allow attackers to break RSA. It's believed/hoped that this is not the case, however.

## Euler's theorem

There's another way of proving RSA's correctness which involves [Euler's theorem] that I want to discuss as well.

### Euler's totient function

The quantity $(p-1)(q-1)$ (where, once again, $p\cdot q$ is $n$'s prime factorization) came up quite a lot in the first proof we gave of RSA, and in particular was needed for actually computing $d$. This number is the [totient] of $n$, often written $\varphi(n)$.

For an arbitrary $n$, $\varphi(n)$ is defined as the number of numbers less than $n$ that are co-prime to it. Or, to help explain $\varphi$'s relevance, $\varphi(n)$ is the number of numbers that have multiplicative inverses mod $n$.

For a prime number $p$, $\varphi(p)$ is just $p - 1$, since all of the positive numbers less than a prime ($1, 2, \dots, p - 1$) are  co-prime to it.

Another interesting case is when $n$ is the product of two distinct primes, $p$ and $q$. In this case, $\varphi(n) = \varphi(pq) = \varphi(p)\varphi(q) = (p-1)(q-1)$, as we mentioned above.

Seeing why this is the case isn't too hard. There are $pq - 1$ numbers less than $pq$. _Most_ of these numbers are co-prime to $pq$. The only exceptions are $p, 2p, 3p, \dots, (q-1)p$, which obviously have $p$ as a common factor with $pq$, and also $q, 2q, 3q, \dots, (p-1)q$, which have $q$ as a common factor. There are $q-1$ numbers in the first list and $p-1$ numbers in the second list that we have to subtract out from our total $pq - 1$. So we get:

$$ (pq - 1) - (p - 1) - (q - 1) = pq - 1 - p + 1 - q + 1 $$
$$= pq - p - q + 1 = (p-1)(q-1)$$

### Euler's theorem

Now to Euler's theorem itself. Euler's theorem says that if $a$ and $n$ are co-prime integers, then

$$ a^{\varphi(n)} \equiv 1 \mod{n}$$

Note that Euler's theorem is actually a generalization of Fermat's little theorem from before. If $n = p$ is a prime number, then $\varphi(p) = p - 1$ as we just explained, and every integer $a$ is co-prime to $p$, so Euler's theorem becomes $a^{p-1} \equiv 1 \bmod{p}$, which is basically exactly Fermat's little theorem (we just need to multiply both sides by $a$).

The proof of Euler's theorem is also very similar to the proof we gave of Fermat's little theorem:

Let $x_1, x_2, \dots, x\_{\varphi(n)}$ be the $\varphi(n)$ numbers less than $n$ that are co-prime to it, and thus have multiplicative inverses mod $n$. Then consider the sequence $ax_1, ax_2, \dots, ax\_{\varphi(n)}$.

Suppose two elements of this sequence are equivalent mod $n$: $ax_i \equiv ax_j \bmod{n}$. Because $a$ is co-prime to $n$, it has an inverse $a^{-1}$ that we can use to cancel out the $a$s and get $x_i \equiv x_j \bmod{n}$. Since all of the $x_i$s were unique and less than $n$, this means that $x_i = x_j$ and thus that $i = j$. In other words, the only way two elements of the sequence can be the same is if they're actually the same element. Another way of saying this is that each of $ax_1, ax_2, \dots, ax\_{\varphi(n)}$ are unique.

Just like in Fermat's little theorem, if we take each of the elements of this sequence and reduce mod $n$, we know we'll end up with values in $x_1,x_2,\dots,x\_{\varphi(n)}$. Seeing why is a little trickier this time. However, note that since both $a$ and $x_i$ (for any $i$) have inverses mod $n$, that $ax_i$ itself has an inverse as $a^{-1}x_i^{-1}$. And since $ax_i$ is invertible mod $n$, it must be one of $x_1,\dots,x\_{\varphi(n)}$, which were _all_ numbers invertible mod $n$.

So this sequence is just a permutation of $x_1, x_2, \dots, x_{\varphi(n)}$.Thus, just like for Fermat's little theorem, if we multiply the elements of each of the sequences, we should get the same result:

$$ ax_1\cdot ax_2 \cdot\dots\cdot ax_{\varphi(n)} \equiv x_1\cdot x_2\cdot\dots\cdot x_{\varphi(n)} \mod{n}$$

Grouping together the $a$s on the left-hand side gets us:

$$ a^{\varphi(n)}x_1\cdot x_2 \cdot\dots\cdot x_{\varphi(n)} \equiv x_1\cdot x_2\cdot\dots\cdot x_{\varphi(n)} \mod{n}$$

And now we cancel out all the $x_i$s, which we can do because they're all co-prime to $n$. Which leaves us with:

$$ a^{\varphi(n)} \equiv 1 \mod{n}$$

Just as we need.

### Completing the RSA proof

Armed with Euler's theorem, we can now prove that $M^{ed} \equiv M \bmod{n}$.

Recall that $d$ was $e$'s multiplicative inverse mod $(p-1)(q-1) = \varphi(n)$, so that $ed \equiv 1 \mod{\varphi(n)}$. This means $ed = k\varphi(n) + 1$ for some $k$.

Then,
  
$$M^{ed} = M^{k\varphi(n) + 1} = M^{k\varphi(n)}M = \left(M^{\varphi(n)}\right)^kM$$

When reducing mod $n$, Euler's theorem lets us replace $M^{\varphi(n)}$ with $1$, so we get

$$\left(M^{\varphi(n)}\right)^kM \equiv 1^kM \equiv M \mod{n}$$

Which is exactly what we need.

Note that by using Euler's theorem we proved that $M^{ed} \equiv M \bmod{n}$ directly, as opposed to first proving that $M^{ed} \equiv M$ mod both $p$ and $q$, and arguing that this meant they were equivalent mod $pq = n$.

There's a caveat here that Euler's theorem only applies if $M$ is co-prime to $n$. $n$ is the product of two primes, so most $M$ will be co-prime to it, but in the case that it isn't, we can still rely on the argument we used in the first proof to conclude that RSA will work.

[modular exponentiation]: http://en.wikipedia.org/wiki/Modular_exponentiation
[prime factorization]: http://en.wikipedia.org/wiki/Prime_factor
[extended euclidean algorithm]: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
[Euler's theorem]: http://en.wikipedia.org/wiki/Euler's_theorem
[totient]: http://en.wikipedia.org/wiki/Euler's_totient_function
