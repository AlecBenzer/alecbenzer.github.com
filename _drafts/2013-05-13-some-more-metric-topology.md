---
layout: 'post'
title: 'Some more metric topology'
excerpt: "<p>We talked about boundaries a lot in the last post, but only using our intuition. Let's now formally define boundary:</p>"
---

A continuation of [this post](/blog/intro-metric-topology/).

## Boundaries

We talked about boundaries a lot in the last post, but only using our intuition. Let's now formally define boundary:

Let $(X,d)$ be a metric space, and consider a subset $S \subseteq X$. An element $x \in X$ is called a **boundary point** of $S$ if for any $\varepsilon > 0$, $B(x,\varepsilon) \cap S \neq \varnothing$, and $B(x,\varepsilon) \cap S^{\mathsf{C}} \neq \varnothing$. (ie, $B(x,\varepsilon)$ intersects both $S$ and the complement of $S$, for any $\varepsilon > 0$ we might choose). The **boundary** of $S$ is simply the set of all boundary points of $S$, and is written as $\partial S$.

You can think of boundary points of a set as the points where, if you walk a tiny bit in one direction, you'll be outside the set, but if you walk a tiny bit in some other direction, you'll be inside the set.

Let's look at an example set: the half-open interval $$S = (0,1] = \\{x \in \mathbb{R} : 0 < x \le 1\\}.$$
You can probably guess that $\partial S = \\{0,1\\}$, but why? Something like $\frac12$ isn't in $\partial S$, because we can look at the ball $$B\left(\frac12, \frac14\right) = \left\\{x : \frac14 < x < \frac34 \right\\},$$ and we notice that $B\left(\frac12, \frac14\right)$ is contained completely with $S$, and doesn't touch $S^{\mathsf{C}}$ at all. Similarlly, something like 1,000 isn't in $\partial S$ because $B(1000, 10)$ is contained within $S^{\mathsf{C}}$, and doesn't touch $S$ at all.

But pick any $\varepsilon > 0$ you want, and $B(0,\varepsilon)$ and $B(1,\varepsilon)$ will always touch some points in $S$ and some points not in $S$. No other numbers have this property. Thus, $\partial S = \\{0,1\\}$.

Previously, we intuitively defined open sets as sets that don't touch their boundaries and closed sets as sets that contain all of their boundaries. We can now prove these things formally!

_Theorem:_ $S$ is an open set if and only if $S \cap \partial S = \varnothing$.

_Proof_: There are two parts to this: $S$ open $\implies S \cap \partial S = \varnothing$, and $S \cap \partial S = \varnothing \implies S$ open.

$S$ open $\implies S \cap \partial S = \varnothing$: We'll do a proof by contradiction -- suppose $S$ is open, and also suppose $S \cap \partial S \neq \varnothing$. Then we have some $s \in S$ so that $s$ is also in $\partial S$. Since $S$ is open and $s \in S$, by the definition of an open set, there exists some $\varepsilon > 0$ so that $B(s,\varepsilon)$ is contained totally within $S$. This means that $B(s,\varepsilon)$ does not touch $S^{\mathsf{C}}$ at all. But if $s \in \partial S$, $B(s,\varepsilon)$ _must_ touch $S^{\mathsf{C}}$ by definition. This is a contradiction -- therefore, $S$ open $\implies S \cap \partial S = \varnothing$.

Now the second part, $S \cap \partial S = \varnothing \implies S$ open: If $S \cap \partial S$ is the empty set, this means that for any $s \in S$, that $s$ is _not_ in $\partial S$. We know that $\partial S$ is the exactly the set of points $b \in \partial S$ for which any ball around $b$ will touch both $S$ and $S^C$. If $s$ is not in $\partial S$, this then means that there's _at least one_ $\varepsilon > 0$ so that $B(s,\varepsilon)$ does not touch $S^{\mathsf{C}}$, which means that $B(s,\varepsilon)$ is contained completely within $S$. Ie, for any $s \in S$, there's a ball $B(s,\varepsilon)$ around $s$ so that $B(s,\varepsilon) \subseteq S$. This is exactly the definition of $S$ being open.

Ie, we've shown $S$ open $\implies S \cap \partial S = \varnothing \implies S$ open, so we have $S$ open $\iff S \cap \partial S = \varnothing$. $\square$

Before we prove the related theorem about closed sets, we need to prove something else we mentioned in the last post -- that a set and its complement have the same boundary.

_Theorem:_ $\partial S = \partial \left( S^{\mathsf{C}} \right)$.

_Proof:_ This is fairly straight-forward. $\partial\left(S^{\mathsf{C}}\right)$ is the set of points where any open ball will touch both $S^{\mathsf{C}}$ and $\left(S^{\mathsf{C}}\right)^{\mathsf{C}}$. $\left(S^{\mathsf{C}}\right)^{\mathsf{C}} = S$, so $\partial\left(S^{\mathsf{C}}\right)$ is the set of points where any open ball touches both $S^{\mathsf{C}}$ and $S$. This is exactly the definition of $\partial S$. $\square$

Now, we can prove our intuition about closed sets: a set is closed exactly when it contains all of its boundary:

_Theorem:_ $S$ is closed if and only if $\partial S \subseteq S$.

_Proof:_ If $S$ is closed, then $S^{\mathsf{C}}$ is open. Since $S^{\mathsf{C}}$ is open, we know that $S^{\mathsf{C}} \cap \partial\left(S^{\mathsf{C}}\right) = \varnothing$. Given the previous theorem, this means that $S^{\mathsf{C}} \cap \partial S = \varnothing$. Ie, none of $\partial S$ is in $S ^{\mathsf{C}}$. This means _all_ of $\partial S$ must be in $\left(S^{\mathsf{C}}\right)^{\mathsf{C}} = S$. Ie, $S$ closed $\implies \partial S \subseteq S$.

Now for the other direction: If $\partial S \subseteq S$, then $\partial S \cap S^{\mathsf{C}} = \varnothing$, or equivelantly, $\partial\left(S^{\mathsf{C}}\right) \cap S^{\mathsf{C}} = \varnothing$. Ie, $S^{\mathsf{C}}$ does not touch its boundary, so $S^{\mathsf{C}}$ is open, meaning $S$ is closed. This proves the other direction of the if-and-only-if. $\square$
