---
layout: post
title: "Defining the squareroot"
---

It's well-known that the squareroot of 2 is not rational. That is, if $x^2 = 2$, then $x \notin \mathbb{Q}$. Proving this is fairly simple:

Suppose $x \in \mathbb{Q}$. Because $x$ is rational, it can be written as $x = \frac{a}{b}$, where $a$ and $b$ are in lowest terms, for some $a,b \in \mathbb{Z}$.

Since $x^2 = 2$, then $\frac{a^2}{b^2} = 2 \implies a^2 = 2b^2$. $b$ was just some integer, meaning $b^2$ is also an integer, which means that $a^2$ is twice some integer. This means that $a^2$ is even (from the definition of even).

$a^2$ being even implies that $a$ is even. Why? Because if $a$ were odd, then we'd have $a = 2k+1$ for some $k \in \mathbb{Z}$, which would mean that $$a^2 = (2k+1)^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$ $2k^2 + 2k$ is an integer (since $k$ is an integer), which means that $a^2$ is odd (from the definition of odd). Thus, $a \mbox{ odd } \implies a^2 \mbox{ odd}$, so, taking the contrapositive, we get $a^2 \mbox{ even } \implies a \mbox{ even}$.

So $a$ is even because $a^2$ is even. This means there exists some integer $k_1 \in \mathbb{Z}$ such that $a = 2k_1$. Plugging this back in to $a^2 = 2b^2$, we get that $4k_1^2 = 2b^2 \implies b^2 = \frac{4}{2}k_1^2 = 2k_1^2$. $k_1^2$ is an integer because $k_1$ was an integer, so this means that $b^2$ is even, which then means that $b$ is even (ie, $b = 2k_2$ for some $k_2 \in \mathbb{N}$).

This is a problem. Why? Because $a$ and $b$ are both even, this means that $\frac{a}{b}$ cannot possibly be in lowest terms ($\frac{a}{b} = \frac{2k_1}{2k_2} = \frac{k_1}{k_2}$). This is a contradiction, and so our assumption that $x$ was rational must be false. QED

## The least upper bound property

It's clear that we can't reasonably define squareroots over the rationals (ie, we can't have some function $\mbox{sqrt} \colon \mathbb{Q} \to \mathbb{Q}$) since $\mbox{sqrt}(2)$ wouldn't be defined (and in fact $\mbox{sqrt}$ wouldn't be defined for tons of other rationals as well).

If we want to define squareroots for our numbers, we're going to have to _extend_ our number system by adding more numbers. We do this by constructing the reals, $\mathbb{R}$, based off of the rationals, $\mathbb{Q}$.

To do this, we need to discuss the **least upper bound property**. An ordered set $S$ has the least upper bound property if for all subsets $S' \subseteq S$, if $S'$ is bounded above (ie, if there is some $b$ such that $s \in S \implies s \le b$) then $S'$ has a _least upper bound_. That is, it has some upper bound $\hat{b}$ such that if $b$ is some other bound, then $\hat{b} \le b$.

This is kind of confusing, so let's see some examples. Here is a set of rational numbers: $S = \\{1, 3, 7\\}$. 10 is clearly an upper bound for this set. So is 9. So is 8. 6, however, is _not_ an upper bound for this set, because 7 is in the set, but 7 is bigger than 6.

<p>6.9 is also not an upper bound of $S$, for the same reason. Neither is 6.9999. 7, though, <em>is</em> an upper bound for $S$. In fact, 7 is the <em>least</em> upper bound, precisely because there can be no upper bound less than 7.</p>

Let's look at another set of rationals: $S = \left\\{\frac{1}{2}, \frac{2}{3}, \frac{3}{4}, \frac{4}{5}, \ldots \right\\}$.

This set is bounded above by 1, because no matter what element of $S$ we pick, it will be smaller than 1. 0.9999, however, is not an upper bound for $S$, because we can go and pick out some element of $S$ that's bigger than 0.9999. In particular, the elements of $S$ are of the form $\frac{n-1}{n} = \frac{n}{n} - \frac{1}{n} = 1 - \frac{1}{n}$, so if we want $1 - \frac{1}{n} > 0.9999$, we just pick an $n > \frac{1}{1 - 0.9999}$. From this, it should be clear that 1 is the least upper bound for $S$.

So far, both sets we've picked have had least upper bounds. Is there a set of rational numbers that doesn't have a least upper bound, but is still bounded? What about this set: $S = \\{x \in \mathbb{Q} \mid x^2 \le 2 \\}$. It's not that hard to see that 2 is an upper bound for $S$, but is there any _least_ upper bound for $S$? The answer is no. I won't prove it formally right now, but the idea is that given any rational estimate for the squareroot of 2 that's an underestimate, we can always generate an estimate that's closer to the actual squareroot of 2, but still less than it.

## Constructing the reals

So as it turns out the rationals do _not_ have the least upper bound property. That is, just because a subset of the rationals is bounded from above does _not_ mean that we can get a least upper bound for it.

But the least upper bound property is a nice property to have for our number system. So we'd like to construct a new set of numbers, called the reals, which _does_ have the least upper bound property.

The set of real numbers is written as $\mathbb{R}$, and can be defined like this:

1. $\mathbb{Q} \subseteq \mathbb{R}$. This says that every rational number is included in the reals.

2. For all $X \subseteq \mathbb{R}$ such that $X$ has an upper bound, $X$ has a _least_ upper bound which is also in $\mathbb{R}$.

So, perhaps surprisingly, we've actually literally _defined_ $\mathbb{R}$ to have the property we wanted it to. In some sense, from our definition of $\mathbb{R}$, the only thing we really know about $\mathbb{R}$ is that it has the least upper bound property, because we said it had to.

## Defining the squareroot of 2

What does any of this have to do with squareroots? Well, it turns out that we can use the least upper bound property to show that the squareroot of 2 is in $\mathbb{R}$.

Let $S = \\{x \in \mathbb{R} \mid x^2 \le 2\\}$, and let $y$ be the least upper bound of $S$ (which must exist and must be in $\mathbb{R}$). We claim that $y^2 = 2$.

Why is this the case? Well, suppose it weren't. Ie, suppose $y^2 \neq 2$. Then we have to have either $y^2 < 2$ or $y^2 > 2$.
