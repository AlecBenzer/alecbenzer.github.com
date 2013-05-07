---
layout: post
title: Introduction to Metric Topology
---

Metric topology generally begins with a construction of the real numbers, $\mathbb{R}$, but we will simply assume their existence. Informally, you can think of $\mathbb{R}$ as the set of numbers that can be formed from arbitrary infinite strings of decimals.

The fundamental property of $\mathbb{R}$ that you need to be aware of is the **least upper bound** property, which basically says that given any subset $X \subseteq \mathbb{R}$, _if_ $X$ is bounded above by some number, then $X$ has a _least_ upper bound.

To see what this means, we'll look at a few possible subsets of $\mathbb{R}$. Consider the set of naturals:

$$A = \\{0, 1, 2, 3, \ldots\\} \subseteq \mathbb{R}$$

$A$ is not bounded above by anything. Ie -- there is no number $x$ so that $x \ge a$ for all $a \in A$. So there's nothing to check here.

Now let's look at this set:

$$B = \left\\{\frac{n-1}{n} : n \in \\{1,2,3,\ldots\\}\right\\} = \left\\{0, \frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \ldots\right\\}$$

It should be easy to see that $B$ is bounded above by 1 (for any $b \in B$, $b \le 1$). But it's also the case that 1 is the _least_ upper bound for $B$. Ie, consider any number $x < 1$. Then some element of $b$ will eventually get past $x$.

The least upper bound property for $\mathbb{R}$ says that this is always the case -- that for any set that has some upper bound, we can find some real number $x$ that is smallest possible upper bound.

If this seems like an obvious property: consider this subset of $\mathbb{Q}$, the rational numbers:

$$C = \left\\{1, 1.4, 1.41, 1.414, 1.4142, 1.4142, 1.41421\right\\} \subseteq \mathbb{Q}$$

$C$ just consists of succesively more accurate approximations of $\sqrt{2}$. $C$ is clearly bounded above by $2$, but considered as a subset of $\mathbb{Q}$, $C$ has _no_ least upper bound. Given any rational upper bound, we can always pick one that's smaller, but still an upper bound. This is basically because the "true" least upper bound, $\sqrt{2}$, is not rational.

So we see that $\mathbb{Q}$ does not have the least upper bound property, but $\mathbb{R}$ does. This is in some sense the fundamental property that makes $\mathbb{R}$ unique.

## Metric spaces

Now we go on to define **metric spaces**. A metric space is some set $X$, together with a **distance function** $d$, which maps from pairs of elements in $X$ to non-negative real numbers. Ie,
   $$ d\colon X \times X \to \mathbb{R}^+.$$
   where $\mathbb{R}^+ = \\{x \in \mathbb{R} : x \ge 0\\}$.

Given two elements $x,y \in X$, $d(x,y)$ is intended to represent the distance between $x$ and $y$. To this end, $d$ must adhere to the following rules:

1.$d(x,y) = 0$ if and only if $x = y$. This rule says the distance between an object and itself is 0, and that the distance between an object and some _other_ object (ie, not itself) is not 0.
2. $d(x,y) = d(y, x)$. This rule says that distances are symmetric -- the distance between two objects is defined independently from the order in which we consider the two objects.
3. $d(x,y) + d(y,z) \ge d(x,z)$. This is called the triangle inequality. It basically says that you can't possibly get from $x$ to $z$ more quickly by taking a detour through $y$.

Any set $X$ and function $d \colon X \times X \to \mathbb{R}^+$ that observes these three rules is a metric space, and is written as $(X,d)$ (but a lot of the time we'll get lazy and just write $X$, when it's clear what the function $d$ is).

What are some examples of metric spaces? A very simple one is $\mathbb{R}$ itself, with the distance function
$$ d(x,y) = \left|x - y\right|.$$

We should verify that this function does in fact observe the three metric space rules. First we check that if $x=y$, then $d(x,y) = 0$:
$$ d(x,y) = \left|x - y\right| = \left|x-x\right| = \left|0\right| = 0.$$

We also have to check the converse: that if $d(x,y) = 0$, then $x = y$:
$$ d(x,y) = 0 \implies \left|x-y\right| = 0.$$
If $x \ge y$, then $\left|x - y\right| = x - y$, and so we get
$$\left|x-y\right| = 0 \implies x-y = 0 \implies x = y.$$
If, on the other hand, $x \le y$, then $\left|x-y\right| = y-x$, so
$$\left|x-y\right| = 0 \implies y-x = 0 \implies y = x.$$

Lastly, we must check the triangle inequality. We will skip this part, because it's kind of tedious, but you should be able to convince yourself that it's true.

$\mathbb{R}^n$ can also be made into a metric space, using the distance function
$$d(\mathbf{x},\mathbf{y}) = \sqrt{\left(x_1-y_1\right)^2 + \cdots + \left(x_n - y_n\right)^2}$$
where $\mathbf{x} = \left(x_1,\ldots,x_n\right)$ and $\mathbf{y} = (y_1,\ldots,y_n)$. This is known as the **euclidean distance** function for $\mathbb{R}^n$, and is often considered the standard or "normal" way of calculating distances in $\mathbb{R}^n$. There are other distance functions that are sometimes used (like [Manhattan distance](http://en.wikipedia.org/wiki/Taxicab_geometry) or [Chebyshev distance](http://en.wikipedia.org/wiki/Chebyshev_distance)), but we will just focus on euclidean distance. You should again go through the metric space rules and see that euclidean distance does indeed satisfy them.

## Open balls

Given any metric space $(X,d)$, we can now begin to introduce certain topological concepts.

The first thing we define are **open balls**. An open ball centered at some point $x \in X$ of radius $r \in \mathbb{R}$ is defined as

$$ B(x,r) \equiv \left\\{y \in X : d(x,y) < r \right\\}$$

Informally, a ball centered at $x$ is just the set of all points that are "close" to $x$.

We can look at examples of open balls in the metric spaces we've discussed. Let's look at $\mathbb{R}$ with the metric $\left|x - y\right|$.

$$\begin{eqnarray\*}
B\left(0, 1\right) &=& \left\\{y \in \mathbb{R} : d\left(0,y\right) < 1\right\\}\\\\
          &=& \left\\{y \in \mathbb{R} : \left|0-y\right| < 1\right\\}\\\\
          &=& \left\\{y \in \mathbb{R} : \left|-y\right| < 1\right\\}\\\\
          &=& \left\\{y \in \mathbb{R} : -1 < y < 1\right\\}
\end{eqnarray\*}$$

So in $\mathbb{R}$ the ball centered at 0 of radius 1 is just the interval $(-1,1)$. $B\left(1\mathbin{/}2, 1\mathbin{/} 2\right)$ would be the interval $(0,1)$. In general, $B(x,r)$ is just the interval $\left(x-r, x+r\right)$.

Now let's look at open balls in $\mathbb{R}^2$, with euclidean distance. The ball centerted at $\mathbf{0} = (0,0)$ of radius $1$ is just

$$\begin{eqnarray\*}
B(\mathbf{0},1) &=& \left\\{(x,y) \in \mathbb{R}^2 : d(\mathbf{0}, (x,y)) < 1 \right\\}\\\\
    &=& \left\\{(x,y) \in \mathbb{R}^2 : \sqrt{(0-x)^2 + (0-y)^2} < 1\right\\}\\\\
    &=& \left\\{(x,y) \in \mathbb{R}^2 : \sqrt{(-x)^2 + (-y)^2} < 1\right\\}\\\\
    &=& \left\\{(x,y) \in \mathbb{R}^2 : x^2 + y^2 < 1\right\\},\\\\
    \end{eqnarray\*}$$

which is just the set of all points contained within the unit circle (but not the unit circle itself).

In general,
   
   $$\begin{eqnarray\*}
   B((x_0,y_0),r) &=& \left\\{(x,y) \in \mathbb{R}^2 : d((x_0,y_0),(x,y)) < r\right\\}\\\\
                  &=& \left\\{(x,y) \in \mathbb{R}^2 : \sqrt{(x-x_0)^2 + (y-y_0)^2} < r\right\\}\\\\
                  &=& \left\\{(x,y) \in \mathbb{R}^2 : (x-x_0)^2 + (y-y_0)^2 < r^2\right\\}
    \end{eqnarray\*}.$$

This is the set of points contained within the circle centered at $(x_0,y_0)$ of radius $r$ (but again, not the circle itself). This is often called an **open disk**.

Similarlly, in $\mathbb{R}^3$ with the euclidean distance, open balls are just the set of points contained within a sphere, but not the sphere itself. (If you're interested, look into the Manhattan and Chebyshev distances linked to above, and think about what open balls would be using those distances for $\mathbb{R}^2$ and $\mathbb{R}^3$).

## Open sets

Once we have open balls, we can define what open sets are. Informally speaking, a set is called "open" if, given any point in the set, you can pick any direction, and move _some_ small amount in that direction while remaining in the set. We formalize this concept using open balls:

Given a metric space $(X,d)$, a subset $S \subseteq X$ of the metric space is called **open** if, for every $s \in S$, there exists some value $\varepsilon \in \mathbb{R}, \varepsilon > 0$ such that $B(s,\varepsilon) \subseteq S$.

In the above definition, you should think of $B(s,\varepsilon)$ as the points that you get to by moving less than $\varepsilon$ away from $s$ in any direction.

Another way of intuitively thinking about open sets is that an open set is a set that does not touch its boundary (we'll formally define boundary later, but for now you can use your intuition about what boundary means).

Since _open_ balls have "open" in their name, you would probably think that open balls are open sets. And they are. Let's prove this.

*Theorem:* Let $(X,d)$ be a metric space, let $x \in X$, and let $r \in \mathbb{R}, r > 0$. Then $B(x,r)$ is an open set.

*Proof:* Pick some $b \in B(x,r)$, and let $\varepsilon = r-d(b,x)$. Now, consider some $b' \in B(b,\varepsilon)$. Then we know that
$$\begin{eqnarray\*}
&& d(b,b') < r - d(b,x)\\\\
&\implies& d(b,b') + d(b,x) < r\\\\
&\implies& d(b',b) + d(b,x) < r \quad\mbox{(by symetry of $d$)}\\\\
&\implies& d(b',x) \le d(b',b) + d(b,x) < r \quad\mbox{(by the triangle inequality)}\\\\
&\implies& d(b',x) < r\\\\
&\implies& b' \in B(x,r).
\end{eqnarray\*}$$

Ie, we have shown that given some arbitrary $b' \in B(b,\varepsilon)$, that $b' \in B(x,r)$. This is equivalent to showing that $B(b,\varepsilon) \subseteq B(x,r)$. Ie, we have shown that, for any point $b$ in $B(x,r)$, that there exists an $\varepsilon$ so that $B(b,\varepsilon) \subseteq B(x,r)$. This is the definition of $B(x,r)$ being open. $\square$

So since open balls are sets, we immediately see a lot of examples of open sets. In $\mathbb{R}$, _open_ intervals $(a,b)$ are open sets. In $\mathbb{R}^2$, open disks are open sets.

Can you try to think of a set that _isn't_ open? One would be the "half-open" interval $(a,b] = \\{x \in \mathbb{R} : a < x \le b \\}$. Why isn't this set open? Well, if we find ourselves at $b$, consider what any open ball $B(b,\varepsilon)$ will look like. No matter how small $\varepsilon$ is, $B(b,\varepsilon)$ will always contain some point to the right of $b$, and thus some point which is _not_ in the set.

## Some properties of open sets

Let's look at some properties of open sets.

Two simple ones are the fact that given any metric space $(X,d)$, the set $X$ itself is open, and the empty set, $\varnothing$, is open.

Seeing that $\varnothing$ is open is trivial. The definition for an open set says "if for all $s \in \varnothing$", but we can actually stop right there, because there aren't any $s$ in $\varnothing$. Thus, the fact that $\varnothing$ is open is [vacuously true](http://en.wikipedia.org/wiki/Vacuous_truth).

Seeing that $X$ is open in $(X,d)$ is also fairly simple. Recall the definition of an open ball:

$$B(x,r) \equiv \left\\{y \in X : d(x,y) < r\right\\}.$$

Note that every element of an open ball is also a member of $X$, so every open ball is a subset of $X$. This makes the part of the definition of an open set that says "$B(s,\varepsilon) \subseteq X$" true in all cases (ie, it's true for any $s$ and any $\varepsilon$).

Now let's look at something a little more interesting: openness is "closed" over unions. That is, given any (potentially infinite) collection of open sets, their union will also be an open set:

*Theorem:* Let $\mathcal{O}$ be a set of sets so that $O \in \mathcal{O} \implies O$ is open, and let $U = \bigcup_{O \in \mathcal{O}}O$. Then $U$ is open.

*Proof:* Let $u \in U$. Then (by the definition of union), there is some $O \in \mathcal{O}$ such that $u \in O$. Since $O$ is open, there exists some $\varepsilon > 0$ such that $B(u,\varepsilon) \subseteq O$. $O$ is also a subset of $U$ (again, by definition of union), so we have that for any arbitrary $u \in U$, $B(u,\varepsilon) \subseteq U$. $\square$

We might think that the same fact about intersections is also true. It sort of is. Given any _finite_ collection of open sets, the intersection of the sets is open (but this may fail for infinite intersections).

First, let's just prove this is true in the finite case. We first prove a lemma:

*Lemma:* If $r_1 \le r_2$, then $B(x,r_1) \subseteq B(x,r_2)$.

*Proof:* Let $b \in B(x,r_1)$. Then $$d(x,b) < r_1 \le r_2 \implies d(x,b) < r_2 \implies b \in B(x,r_2).$$ Since for arbitrary $b$, $b \in B(x,r_1) \implies b \in B(x,r_2)$, we have that $B(x,r_1) \subseteq B(x,r_2)$. $\square$

Now we can prove our theorem:

*Theorem:* Let $O_1,\ldots,O_n$ be open sets, and let $U = \bigcap_{i=1}^n O_i$. Then $U$ is open.

*Proof:* Let $u \in U$. Then $u \in O_i$, for $i \in \\{1,\ldots,n\\}$ (definition of intersection). Since each $O_i$ is open, we have an $\varepsilon_i$ for $i \in \\{1,\ldots,n\\}$ so that $B(u,\varepsilon_i) \subseteq O_i$. Let $\varepsilon = \min\left(\varepsilon_1,\ldots,\varepsilon_n\right)$. Let $b' \in B(u,\varepsilon)$. Then since $\varepsilon < \varepsilon_i$, $B(x,\varepsilon) \subseteq B(x,\varepsilon_i) \subseteq O_i$, for each $i$. This implies that $B(x,\varepsilon) \subseteq \bigcap_{i=1}^nO_i = U$. Ie, for arbitrary $x \in U$, we found an $\varepsilon$ so $B(x,\varepsilon) \subseteq U$. So $U$ is open. $\square$

The part of this proof that relies on having only a finite collection of sets is the part where we take a minimum. This minimum is guaranteed to exist for finitely many inputs (easy to prove with a simple induction). Infinite sets _may_ have minima, but they also might not, and so this proof won't work (in general) for infinite intersections.

To make this concreate, let's look at an actual example of an infinite intersection that doesn't work: In $\mathbb{R}$, let $$O_n = B(0,1\mathbin{/}n) = (-1\mathbin{/}n, 1\mathbin{/}n),$$ and let $U = \bigcap_{i=1}^nO_n$. Here, $U = \\{0\\}$ (the set containing only $0$). Why this is is fairly straight-forward: _every_ $O_n$ is a ball centered at $0$, so every $O_n$ contains $0$, but for any other number $x$, we'll eventually get to an $n$ so that $\frac{1}{n} \le x$, which implies $x \notin O_n$, which implies $x$ is not in the intersection.

We also see that $\\{0\\}$ is not an open set, since any open ball will contain some points to the left of zero and to the right of zero.

## Closed sets

One of our intuitive definitions of open sets was that a set was open if it conainted _none_ of its boundary. We'll now use some complementary intuition to define a closed set as a set that contains _all_ of its boundary.

Given a metric space $(X,d)$, a subet $S \subseteq X$ is **closed** if $S^{\mathsf{C}} = X \setminus S$ is open ($X \setminus S$ denotes set subtraction -- it's the set of all elements in $X$ that are not in $S$).

The way you should rationalize this definition is as follows: First, note (using your intuition about "boundaries") that a set and its complement share a boundary. Eg, the boundary of the set $\\{x \in \mathbb{R} : 1 < x < 2\\}$ is the two points $\\{1,2\\}$; the complement of the set is $\\{x : \mathbb{R} : x \le 1 \mbox{ or } x \ge 2 \\}$, and its boundary is also the set of two points $\\{1,2\\}$.

So this being the case, we note that if an open set contains _none_ of its boundary, then _all_ of its boundary must exist outside the set. Ie, all of its boundary must exist in the set's complement. Since the complement of the open set contains all of its boundary, then the complement must be a closed set.

An example of a closed set in $\mathbb{R}$ is the _closed_ interval $\[a,b\] = \\{x \in \mathbb{R} : a \le x \le b\\}$. The complement of this set is $\[a,b\]^{\mathsf{C}} = \\{x \in \mathbb{R} : x < a \mbox { or } x > b\\}$, which is indeed an open set.

The union and intersection properties sort of reverse themselves for closed sets: _any_ intersection of closed sets is closed, and any _finite_ union of closed sets is closed. The proofs for these follow directly from the definition of closed sets and the rules for how complements work with unions/intersections (ie, [De Morgan's laws](http://en.wikipedia.org/wiki/De_Morgan's_laws))

Ie, if $O_1,\ldots,O_n$ are open sets, then a finite union of closed sets looks like

$$U = \bigcup_{i=1}^n O_i^{\mathsf{C}}.$$

The complement of this set is then

$$U^{\mathsf{C}} = \left(\bigcup_{i=1}^n O_i^{\mathsf{C}}\right)^{\mathsf{C}} = \bigcap_{i=1}^n \left(O_i^{\mathsf{C}}\right)^{\mathsf{C}} = \bigcap_{i=1}^n O_i$$

which is a finite intersection of open sets, and is therefore open. Ie, $U^{\mathsf{C}}$ is open, so $U$ is closed.

A very similar proof shows that an infinite intersection of closed sets is closed.
