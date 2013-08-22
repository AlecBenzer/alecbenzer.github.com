---
layout: post
title: "Linear Algebra: Part 1"
---

This is the first in (hopefully) a series of articles on linear algebra. Linear algebra, in some sense, is just the study of things that are _linear_, and things are linear, roughly speaking, if we can scale them and add them. We call these things things that are linear **vectors**.

You may have heard of vectors before as "arrows" or something that has "both magnitude and direction", or just as lists of numbers written like this: $\langle 4,2,3 \rangle$ or this: $(4,2,3)$. But the vectors we're talking about are much more general than this. For us, a vector is just _anything_ that you can multiply by scalars or add to another vector.

Now we want to go on and define a vector space, but before we do, we need working knowledge of what a field is. Rather than defining this formally here, I'll just [refer you to wikipedia](LINK) if you'd like a formal definition. A common example of a field is $\mathbb{R}$, the set of real numbers. Another is $\mathbb{Q}$, the set of rational numbers. For our purposes, you can pretty much just think of a field as a set of scalars, or just "stuff we can multiply vectors by".

Given that we know about fields, we can now define vector spaces formally.

## Vector spaces

A **vector space** is the 4-tuple $(V,F,+,\cdot)$. This just means we need these 4 things defined to talk about a particular vector space.

$V$ is our set of vectors. $F$ is some field.

$+$ is a function $+ \colon V \times V \to V$. Ie, given two vectors $u,v \in V$, $u + v$ is defined and is another vector in $V$.

$(\cdot)$ is a function $(\cdot) \colon F \times V \to V$. Ie, given a scalar $\alpha \in F$ and a vector $v \in V$, $\alpha \cdot v$ is defined and is another vector in $V$.

To be a valid vector space, the $+$ and $\cdot$ operators also need to follow the following six rules (for all of these rules, $u,v,w \in V$ are any vectors and $\alpha, \beta \in F$ are any scalars).

1. $u + (v + w) = (u + v) + w$. This propery is called _associativity of addition_. It basically means that we can write stuff like $u + v + w$ and not be worried about if we mean $u + (v + w)$ or $(u + v) + w$.

2. $u + v = v + u$. This property is called _commutativity of addition_. It means we talk about adding two vectors without being worried about the order we add them in.

3. $\alpha(u + v) = \alpha u + \alpha v$. This is called _distributivity of scalars over vector addition_.

4. $(\alpha + \beta)v = \alpha v + \beta v$. This is called _distributivity of scalar multiplication over field addition_.

5. $(\alpha\beta)v = \alpha(\beta v)$.

6. If $1 \in F$ is the identity element of our field, and $v \in V$ is a vector, then $1\cdot v = v$.

In addition to all of this, we need to meet two more requirements to have a valid vector space:

1. There exists a vector $\vec{0} \in V$ called the **zero vector**, with the property that for any vector $v \in V$, $v + \vec{0} = v$.

2. For every vector $v \in V$, we have a vector $-v \in V$ called the **additive inverse** of $v$, with the property that $v + (-v) = \vec{0}$.

So finally, after all of that, we're done. Any set $V$ equipped with operators $+$ and $(\cdot)$ over a field $F$ that follows all of the above rules is called a vector space.

## An example

Before talking about more properties of vector spaces, let's show an examples of a vector space.

A good place to start is with "arrow" vectors (ie, those things with "magnitude and direction"). Our arrow vectors $v \in \mathbb{R}^n$ are just lists of $n$ numbers. If $n = 2$, our vector space is the infinite plane. If $n = 3$, our vector space is three-dimmensional space.

Our field $F$ is also just $\mathbb{R}$, and given two vectors $x,y \in \mathbb{R}^n$ where $x = (x_1,\ldots,x_n)$ and $y = (y_1,\ldots,y_n)$, addition of vectors is defined like so:

$$x + y = (x_1 + y_1, \ldots, x_n + y_n)$$

and scalar multiplication (for some scalar $\alpha \in \mathbb{R})$ is defined as:

$$\alpha x = (\alpha x_1, \ldots, \alpha x_n)$$

It's tedious to do so (and we won't do it here), but you could go through all of the six rules above for $+$ and $(\cdot)$ and verify that they hold. Most of them should be pretty straight-forward given knowledge of the real numbers (eg, addition of real numbers is both associative and commutative).

We will go ahead and verify the last two rules though. The zero vector $\vec{0} \in \mathbb{R}^n$ is vector $(0,\ldots,0)$ with every being zero. And indeed, if $x$ is some other vector, we get

$$x + \vec{0} = (x_1 + 0, x_2 + 0, \ldots, x_n + 0) = (x_1,x_2,\ldots,x_n) = x$$

as we need for our zero vector.

Given a vector $x$, the additive inverse of $x$ is

$$-x = (-x_1,\ldots,-x_n)$$

and indeed

$$x + (-x) = (x_1 + (-x_1),\ldots,x_n + (-x_n)) = (0,\ldots,0) = \vec{0}$$.

So we see that $\mathbb{R}^n$ with the standard definitions of addition and scalar multiplication is a valid vector space.

## Some properties of vector spaces

Now, let's suppose that $(V,F,+,\cdot)$ is just _some_ vector space. Not knowing anything else about it, what properties of $V$ can we derive?

One thing we might be wondering about is the uniqueness of $\vec{0}$. Ie, can there be two different vectors $a,b \in V$ so that for any other $v \in V$, $v + a = v$ and $v + b = v$. If this were the case, $a$ and $b$ would both be possible zero vectors. However, we'll see that this is not the case.

_Theorem_: $\vec{0}$ is unique. That is, if we have $a \in V$ such that $v + a = v$  then $a = \vec{0}$.

_Proof_: Let's assume we have some $a \in V$, and assume that $v + a = v$ for all $v \in V$. If ths is true for all $v$, then it's also true for $v = \vec{0}$. So we have $\vec{0} + a = \vec{0}$. But we know that $a + \vec{0} = a$, so we can replace $\vec{0} + a$ in the previous eqation with $a$, and we get that $a = \vec{0}$ $\blacksquare$

So now we know that a vector space can't have two zero vectors -- every vector space has exactly one zero vector.

We might simmilarly wonder about the uniqueness of $-v$. Ie, given $v \in V$, can there be two different vector $a,b \in V$ so that $v + a = \vec{0}$ and $v + b = \vec{0}$? Once, again, no.

_Theorem_: Given $v \in V$, $-v$ is unique. That is, if for some $a \in V$, $v + a = \vec{0}$, then $a = -v$.

_Proof_: $v + a = \vec{0}$, and if we add $-v$ to both sides, we get $v + a + (-v) = \vec{0} + (-v)$. On the left side, $v + (-v)$ becomes $\vec{0}$, and on the right side we're left with $\vec{0} + (-v) = -v$, so we get $\vec{0} + a = -v$, and since $\vec{0} + a = a$, we get $a = -v$ $\blacksquare$

Another thing we'd expect to be true is that if we take a vector and multiply it by the scalar 0, that we'd get the zero vector. While we didn't explicitly state it as one of our conditions, we can prove that this is the case using what we do know about vector spaces.

_Theorem_: $0\cdot v = \vec{0}$, for any $v \in V$.

_Proof_: We know that $0 = 1-1$, so we can rewrite $0\cdot v$ as $(1-1)\cdot v$. We also know that addition of scalars distributes over vector scalar multiplication. So this is the same as $1\cdot v + (-1)\cdot v$. We know $(-1)\cdot v = (-1\cdot 1)\cdot v = -1 (
