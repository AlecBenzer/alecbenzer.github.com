---
layout: post
title: "Is $n$ a multiple of 5 if $n^2$ is?"
...

Say $n$ is a natural number and $n^2$ is a multiple of 5. Does that
mean $n$ is a multiple of 5?

This seems to be true. If we look at squares:

<div>
\[
\begin{align*}
2^2 &= 4 & 3^2 &= 9 & 4^2 &= 16 & \mathbf{5^2} &\mathbf= \mathbf{25} \\
6^2 &= 36 & 7^2 &= 49 & 8^2 &= 64 & 9^2 &= 81 \\
\mathbf{ {10}^2 }&\mathbf= \mathbf{100} & {11}^2 &= 121 & {12}^2 &= 144 & {13}^2 &= 169 \\
{14}^2 &= 196 & \mathbf{ {15}^2 }&\mathbf= \mathbf{225} & {16}^2 &= 256 & {17}^2 &= 289 \\
{18}^2 &= 324 & {19}^2 &= 361 & \mathbf{ {20}^2 }&\mathbf= \mathbf{400} & {21}^2 &= 441\\
\end{align*}
\]
</div>

Seems to be that $n^2$ is a multiple of 5 only when $n$ is. Can we prove it?

If $n^2$ is a multiple of 5, then $n^2 = 5k$ for some $k \in
\mathbb{N}$. Then $n = 5k/n = 5(k/n)$, which means $n$ is a multiple of
5 as long as $k/n$ is an integer... which is true if $k$ is a multiple of
$n$. Is $k$ a multiple of $n$?

Well, $k = n^2/5 = n(n/5)$, which means $k$ is a multiple of $n$
if $n$ is a multiple of 5... ah, we're in a loop here. Let's try
something else.

---

Maybe we need to use something specific about 5. Is this property true for all
numbers? What about 4: is $n$ a multiple of 4 whenever $n^2$ is?

<div>
\[
\begin{align*}
\mathbf{2^2} &\mathbf= \mathbf{4} & 3^2 &= 9 & \mathbf{4^2} &\mathbf= \mathbf{16} & 5^2 &= 25 \\
\mathbf{6^2} &\mathbf= \mathbf{36} & 7^2 &= 49 & \mathbf{8^2} &\mathbf= \mathbf{64} & 9^2 &= 81 \\
\mathbf{ {10}^2} &\mathbf= \mathbf{100} & {11}^2 &= 121 & \mathbf{ {12}^2} &\mathbf= \mathbf{144} & {13}^2 &= 169 \\
\end{align*}
\]
</div>

No! 4, 36, and 100 are multiples of 4, but 2, 6, and 10 are not multiples of 4.

There must be something different about 5 that makes this work for it. 5 is prime... can that help?

The [fundamental theorem of
arithmetic](https://en.wikipedia.org/wiki/Fundamental_theorem_of_arithmetic)
is often handy when dealing with primes. Let's represent $n$ as its prime
factorization:

<div>
\[
n = p_1p_2\cdots p_n
\]
</div>

Then:

<div>
\[
n^2 = p_1^2p_2^2\cdots p_n^2
\]
</div>

If $n^2$ is a multiple of 5, then 5 must be in $n^2$'s prime
factorization. Which means 5 must be one of the primes $p_i$, which in
turn means that $n$ itself must also have $5$ as a factor. Woohoo!

---

So we've proved this is true for 5. And, clearly, it's true for any other
prime number. We know it's not true for 4. Is this true _only_ for primes?
Let's look at 6:

<div>
\[
\begin{align*}
2^2 &= 4 & 3^2 &= 9 & 4^2 &= 16 & {5^2} &= {25} \\
\mathbf{6^2} &\mathbf= \mathbf{36} & 7^2 &= 49 & 8^2 &= 64 & 9^2 &= 81 \\
{10}^2 &= {100} & {11}^2 &= 121 & \mathbf{12}^2 &\mathbf= \mathbf{144} & {13}^2 &= 169 \\
{14}^2 &= 196 &  {15}^2 &= {225} & {16}^2 &= 256 & {17}^2 &= 289 \\
\mathbf{18}^2 &\mathbf= \mathbf{324} & {19}^2 &= 361 & { {20}^2 }&= {400} & {21}^2 &= 441\\
\end{align*}
\]
</div>

Hm... seems like this actually might be true for 6, even though 6 isn't
prime. Can we prove it? It turns out we can make a pretty similar argument:

If $n^2 = p_1^2p_2^2\cdots p_n^2$ is a multiple of 6, 6 _won't_ be any of
the $p_i$ (because 6 isn't a prime). But 6 = 2\*3, which means one of the
$p_i$ must be 2 and another of the $p_i$ must be 3.

In case it isn't clear why: if $m$ is a multiple of 6, then $m = 6k = 2\cdot3\cdot k$. We can prime-factorize $k = q_1q_2\cdots q_n$, which means $m = 2\cdot3\cdot q_1\cdot\cdots\cdot q_n$.
{: .info}

This means $n$'s prime factorization contains 2 and 3, which means
$n$ is a multiple of 6. QED

---

So hang on... since every number has a prime factorization, can't we make
this argument for any number? What goes wrong with 4?

If $n^2 = p_1^2p_2^2\cdots p_n^2$ is a multiple of 4, since 4 = 2\*2, one
of the $p_i$ must be 2 and another of the $p_i$ must be... ah, 2
again. So we can't actually prove that $n$ is a multiple of 4, but we
_can_ prove that it's a multiple of 2.

4 happens to be a perfect square, but we'll actually run into this problem
for other numbers too. 12 = 2\*2\*3. If $n^2 = p_1^2p_2^2\cdots p_n^2$ is
a multiple of 12, one of the $p_i$ is 2, one of the $p_i$ is 2
(again), and one of the $p_i$ is 3. So all we know for sure is that
$n$ is a multiple of 2*3 = 6.

So it's clear that this property holds for any $k$ that doesn't have any
repeats in its prime-factorization. These numbers are called
[square-free](https://en.wikipedia.org/wiki/Square-free_integer).

But even if our number isn't square-free (like 4, or 12), we can still say
something, which is that $n$ is a multiple of the number that you get when
you get rid of all the duplicates in $k$'s prime factorization. The term
for this is an integer's
[_radical_](https://en.wikipedia.org/wiki/Radical_of_an_integer):

<div>
\[
\begin{align*}
\operatorname{rad}({4}) &= \operatorname{rad}({2^2}) = 2 \\
\operatorname{rad}({5}) &= 5 \\
\operatorname{rad}({6}) &= \operatorname{rad}({2\cdot3}) = 2\cdot3 = 6 \\
\operatorname{rad}({12}) &= \operatorname{rad}({2^23}) = 2\cdot3 = 6 \\
\end{align*}
\]
</div>

So the most general thing we can say is: if $n^2$ is a multiple of $k$, $n$ is a multiple of $\operatorname{rad}(k)$.

Inspired by [Putnam 2017 A1](https://www.youtube.com/watch?v=WFTw_3J2HU4).
{: .footnote}
