---
layout: post
title: "An Introduction to Real Analysis 1: The Real Numbers"
---

Naturally, the first thing we do in _real_ analysis is to define the real numbers.

To start, we're going to define the **natural numbers**:

$$ \mathbb{N} = \\{0, 1, 2, 3, \ldots \\} $$

Next, we extend $\mathbb{N}$ by adding negative numbers to get the **integers**:

$$ \mathbb{Z} = \\{\ldots,-3,-2,-1,0,1,2,3,\ldots \\}$$

We extend $\mathbb{Z}$ by allowing for fractions of integers to get the **rationals**:

$$ \mathbb{Q} = \\{ a \mathbin{/} b : a, b \in \mathbb{Z}\\}$$

These three steps are fairly straightforward. Seeing how to extend $\mathbb{Q}$ to the full real numbers, however, is a little more complicated.

We notice a kind of inconvenience with $\mathbb{Q}$: consider the following subset of $\mathbb{Q}$:

$$ S = \\{3, 3.1, 3.14, 3.141, 3.1415, 3.14159, \ldots \\} $$

As you may be able to tell, the elements of $S$ are getting closer and closer to $\pi$ (well, we actually don't know what $\pi$ is yet since we've yet to define the reals, but bear with me), though no element of $S$ will be exactly $\pi$. We also see that $\pi$ serves as an upper bound for $S$: that is, for any $s \in S$, $\pi \ge s$.

$\pi$ is certainly not the _only_ upper bound we can get for $S$, though. 4 is an upper bound for $S$, as are 3.2, 3.15, 3.142, 3.1416, etc.
