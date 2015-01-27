---
layout: 'post'
title: 'Lattices & Data flow analysis'
---

A lower semilattice is a partially ordered set $(P, \preceq)$ such that every
_finite_ subset $S$ of $P$ has a greatest lower bound. Similarlly, an upper
semilattice is a partially ordered set where every subset has a least upper
bound. A lattice in general is a partially ordered set that is both an upper
and lower semilattice. Without much loss of generality will focus on lower
semilattices.

Every semilattice has an associated binary operator $\wedge$ (called "meet"),
such that $x \wedge y$ is the greatest lower bound of the set $\\{x,y\\}$. $\wedge$ actually _uniquely_ defines its semilattice, since $x \preceq y \iff x \wedge y = x$.

Note some properties of $\wedge$:

1. $\wedge$ is associative: $x \wedge (y \wedge z) = (x \wedge y) \wedge z)$. This is because $x \wedge (y \wedge z) = \inf \\{x, \inf\\{y, z\\}\\} = \inf\\{x,y,z\\} = \inf \\{\inf\\{x, y\\}, z\\} = (x \wedge y) \wedge z$.

2. $\wedge$ is commutative: $x \wedge y = y \wedge x$. This is because $x \wedge y = \inf \\{x, y\\} = \inf \\{y, x\\} = y \wedge x$.

3. $\wedge$ is idempotent: $x \wedge x = x$. This is because $x \wedge x = \inf \\{x, x\\} = \inf \\{x\\} = x$.

<span style="display: none">
$$ \newcommand{starle}{\mathbin{\preceq_\star}} $$
</span>

These three properties are special because _any_ binary operator with these properties can "become" the meet operator for an appropriate semilattice. Ie, let $\star$ be a binary operator on some set $P$ satisfying the above three properties. Then we can _define_ a partial order $\starle$ as follows:

$$ x \starle y \iff x \star y = x$$

We claim $\starle$ is indeed a partial order, and further that $(P, \starle)$ is a semilattice (which we'll call the semilattice _induced_ by $\star$).

_Proof:_ First we show that $\starle$ is a partial order:

1. Suppose $x \starle y$ and $y \starle z$. Then $x \star y = x$ and $y \star z = y$. Then $x \star z = (x \star y) \star z = x \star (y \star z) = x \star y = x$, so $x \starle z$. So $\starle$ is transitive.

2. Suppose $x \starle y$ and $y \starle x$. Then $x \star y = x$ and $y \star x = y$. But by $\star$'s commutativity, $y = y \star x = x \star y = x$, so $x = y$. So $\starle$ is antisymmetric.

3. $x \star x = x$ by $\star$'s idempotence, so $x \starle x$. So $\starle$ is reflexive.

So $\starle$ is a partial order. Now we have to show that $(P, \starle)$ is a semilattice, by showing that every finite subset of $P$ has a greatest lower bound. We can do this inductively.

Suppose $S = \\{x, y\\}$ is _any_ size two subset of $P$. We claim $\ell = x \star y$ is the greatest lower bound of $\\{x, y\\}$. To see why, first note that

$$x \star \ell = x \star (x \star y) = (x \star x) \star y = x \star y = \ell$$

so $\ell \starle x$, and similarlly $\ell \starle y$, so $\ell$ is actually a lower bound for $\{x,y\}$. Now, suppose we have some $z \neq x,y$ that is also a lower bound of $\{x,y\}$. Then

$$z \star \ell = z \star (x \star y) = (z \star x) \star y = z \star y = z,$$

so $z \starle \ell$. So we have that $\ell$ is in fact the greatest lower bound of $\\{x,y\\}$. (Note that because the greatest lower bound of $\\{x,y\\}$ is $x \star y$, $\star$ _is_ $\wedge$ for our induced semilattice.)

Now, suppose for all size $n$ subsets $S \subseteq P$, $S$ has a greatest lower bound $\inf S$, and consider a subset $S$ of size $n + 1$. Pick any element $s \in S$ and "remove" it, obtaining $S' = S \setminus \\{s\\}$, a set of size $n$. By our inductive hypothesis, $S'$ has a greatest lower bound; call it $\ell'$. We claim $\ell = s \star \ell'$ is $S$'s greatest lower bound.

First, we show that it is a lower bound:

1. $\ell \star s = (s \star \ell') \star s = (s \star s) \star \ell' = s \star \ell' = \ell$. Ie, $\ell \star s = \ell$, so $\ell \starle s$.

2.    Pick any $s' \in S'$. Because $\ell'$ is $S'$'s lower bound, we have
$\ell' \starle s'$, and thus $\ell' \star s' = \ell'$. So

      $$\ell \star s' = (\ell' \star s) \star s' = s \star (\ell' \star s') = s
      \star \ell' = \ell$$

      Ie, $\ell \star s' = \ell$, so $\ell \starle s'$.

And now we show it is greater than or equal to any other lower bound.

Let $\hat\ell$ be some lower bound of $S$, so $\hat\ell \star s = \hat\ell$ for any $s \in S$. We know inductively that $\ell'$ is $S'$'s greatest lower bound, and also that $\hat\ell$ is a lower bound for $S'$, so

$$\hat\ell \starle \ell' \implies \hat\ell \star \ell' = \hat\ell$$

Then

$$\hat\ell \star \ell = (s \star \ell') \star \hat\ell = (s \star \hat\ell) \star \ell' = \hat\ell \star \ell' = \hat\ell$$

Ie, $\hat\ell \star \ell = \hat\ell$, so $\hat\ell \starle \ell$. So $\ell$ really is $S$'s greatest lower bound.

We've shown inductively that every finite subset of $P$ has a greatest lower bound. So, we can finally conclude that $(P, \starle)$ is a semilattice. $\blacksquare$

## Examples of $\star$-like operators

What are some examples of "$\star$-like" operators (ie, binary operators that are associative, commutative, and idempotent)?

Essentially, an operator is $\star$-like if it is a way of "mixing things together" (ie, without concern for the order we do it in) so that mixing something with itself leaves us with the same thing.

For instance, the maximum of two numbers is $\star$-like. It's associative and commutative, and $\max(x,x) = x$ for any $x$. $\min$ is also $\star$-like. In the realm of sets, set union and intersection are also $\star$-like.

Let's examine the semilattices induced by each of these operators. The semilattice induced by $\min$ has an ordering relation $\preceq$ such that

$$ x \preceq y \iff \min(x,y) = x $$

This relation $\preceq$ is just the standard $\le$ operator for numbers.

On the other hand, the semilattice induced by $\max$ is characterized by the relation

$$ x \preceq y \iff \max(x,y) = x$$

Here, $\preceq$ is the relation $\ge$ for natural numbers.

What about set intersection and set union? The lattice relation induced by $\cap$ (intersection) is

$$A \preceq B \iff A \cap B = A$$

where $A$ and $B$ are sets. Now, $\preceq$ is the subset relation $\subseteq$. For set union, the induced relation is

$$A \preceq B \iff A \cup B = A$$

Now $\preceq$ is the superset relation $\supseteq$.

## Applications of induced lattices

Pretend we have a fine, directed graph $G$ connecting a bunch of nodes together, and say each node has a natural number associated with it. Then, we go through several rounds of a "game". In every round, we go to each node in order, and replace the node's number with the minimum of its number and the numbers of all incoming nodes.

Our question is: will such a game ever "stabilize"? Ie, will the values of the nodes stop changing after a certain point?

Well, note that any time you update a node's value $v$ with a new value $v'$, we will have $v' \le v$, because of how $\min$ works. And note that because we're dealing with natural numbers, we can't go below $0$, and so it's impossible to have infinite chains that go $v_1 > v_2 > v_3 > \dots$. We have to stop eventually.

And because $G$ is finite, we know that values can only keep changing for so long. ...
