---
layout: post
title: "An Introduction to Group Theory"
---

<span style="display: none"> $$ \newcommand{id}{\text{id}} $$ </span>

You probably know how addition of real numbers works. Addition of real numbers has some notable properties.

1. For one, it's **closed**, which means adding two real numbers always gives you another real number.
2. It's **associative**, meaning that $(a + b) + c = a + (b + c)$ for $a,b,c \in \mathbb{R}$.
3. There's an **identity** element with respect to addition, $0$, which has the property that $a + 0 = a$ for any $a \in \mathbb{R}$.
4. And every number $a \in \mathbb{R}$ has an **inverse** with respect to addition, a number $b \in \mathbb{R}$ so that $a + b$ is the identity, $0$ (namely, $b = -a$).

These properties aren't at all exclusive to addition of reals. Consider multiplication of reals. $a\cdot b \in \mathbb{R}$ for all $a,b \in \mathbb{R}$, so we have closure. $(a\cdot b)\cdot c = a \cdot(b\cdot c)$ for all $a,b,c \in \mathbb{R}$, so we have associativity. $a\cdot 1 = a$ for each $a \in \mathbb{R}$, so $1 \in \mathbb{R}$ is our identity. And for _almost_ every $a \in \mathbb{R}$, we have that $a \cdot \frac{1}{a} = 1$, with the only exception being $a = 0$.

Consider also the composition of [bijective](http://en.wikipedia.org/wiki/Bijection) functions. Let $A$ be any set, and denote by $S_A$ the set of all bijections from $A$ to $A$. Ie,

$$ S_A = \\{f\colon A \to A \mid f \text{ is bijective}\\}. $$

Then we can take two functions $f,g \in S_A$ and consider their composition $f \circ g$, the function that sends $a \in A$ to $f(g(a))$. Function composition is closed over $S_A$ (ie, $f\circ g$ is also bijective), it has as an identity element the identity function $\id_A$, which maps each $a \in A$ to itself. And each function $f \in S_A$ has an inverse function $f^{-1}$ which maps $f(a)$ to $a$, satisfying $f \circ f^{-1} = \id_A$.

These properties come up in even more places. The addition of matricies, for example, or the multiplication of invertible matricies. They come up enough that it is worthwhile to study these properties on their own, without worrying or caring about which specific "instance" of these properties we're dealing with. This is essentially what group theory is -- the study of these 4 properties.

## Definition of a group

Things which have these four properties are called groups. Let's formalize:

_Definition_: Let $G$ be some set, and let $\* \colon G \times G \to G$ be an operator on this set, satisfying the following:
1. Associativity: $\forall g,h,r \in G$, $g * (h * r) = (g * h) * r$
2. Identity: $\exists e \in G$ such that for each $g \in G$, $g * e = g$
3. Inverse: $\forall g \in G$, $\exists h \in G$ such that $g * h = e$

Then the pair $(G,\*)$ is a **group**.

Normally, when dealing with groups, we will use _multiplicative notation_, where the operator $\*$ is written as just $\cdot$ or omitted, the identity element $e$ is written as $1$ or $1_G$, and inverses are written $g^{-1}$.

So using multiplicative notation, a group is written as $(G,\cdot)$ satisfying $g(hr) = (gh)r$, $g\cdot 1 = g$, and $gg^{-1} = 1$.

We will also occasionally use _additive notation_ for groups, where $\*$ is written as $+$, $e$ is written as $0$ or $0_G$, and inverses are written $-g$, though this is less common.

Notice that the first property we talked about above, closure, was stated implicitly in the definition of $\*$ as $\* \colon G \times G \to G$, which means that $\*$ takes two things in $G$ and gives us a third thing in $G$.

## Some examples of groups

What are some examples of groups? We basically mentioned a bunch at the beginning of the post. $(\mathbb{R},+)$, real numbers with respect to addition, is a group. So is $(\mathbb{Q},+)$ and $(\mathbb{Z},+)$, respectively, the rationals and the integers with respect to addition.

What about $(\mathbb{N},+)$, the set of natural numbers with respect to addition. Is this a group? No! Why not? Because we don't have inverses -- there is no _natural number_ $n \in \mathbb{N}$ so that $2 + n = 0$. In fact, the only natural number that has an inverse with respect to addition is $0$.

What about $(\mathbb{R}, \times)$, the real numbers with respect to multiplication. Is this a group? Again, no, and again, it's because of inverses. But this time, instead of $0$ being the only thing that has an inverse, $0$ is the only thing that _doesn't_ have an inverse. However, we can "fix" this issue by taking $0$ out. Ie, $(\mathbb{R}\setminus\\{0\\},\times)$, the set of _non-zero_ reals with respect to multiplication, is a group.

What are some other examples of non-groups, maybe this time involving something other than inverses not working? What about $(\mathbb{R}, -)$, the reals with respect to multiplication. Is this a group? No -- and this time it's because of associativity. Given $a,b,c \in \mathbb{R}$, it is _not_ the case that $a - (b - c) = (a - b) - c$ in general. The same goes for $(\mathbb{R}, \div)$.
