---
layout: post
title: "π is a silly constant"
---

When I was young, I remember thinking that a circle's radius seemed like a strange thing to care about. Diameter seemed like a much more natural value. Caring about a circle's radius instead of its diameter seemed like describing a square by what half of its side length was, or like describing a line by half of its length. I didn't understand why people told us the formula for a circle's circumference was 2πr; circumference = πd seemed much more direct.

But if we're going to be formal about defining the set of points that make up a circle, the radius starts to seem like a much more natural value to look at.

Formally, a circle of radius r centered at some point $p \in \mathbb{R}^2$ is just the set

$$ \left\{x \in \mathbb{R}^2 : \|x-p\| = r \right\}$$

This is a compact, natural way of defining a circle. It also translates well into English: a circle is the set of all points that are r away from the circle's center.

There's no real nice way to describe a circle based on its diameter, though, without ending up saying something like "a circle is all points that are a distance d/2 away from some center point".

So while we might be tempted to describe a circle by its diameter, a circle's radius is really the more natural value to talk about.

## What does this have to do with π ?

π is often defined kind of informally as the ratio of a circle's circumference to its diameter. But that's silly! What we really care about is a circle's radius, not its diameter. A better constant would be the ratio of a circle's circumference to its _radius_.

So we can do that. Let's define a new constant τ (tau), and say that τ is the ratio of a circle's circumference to its radius.

For a circle with circumference C, radius r, and diameter D = 2r, we see that

$$ π = \frac{C}{D} = \frac{C}{2r} = \frac{1}{2}\cdot\frac{C}{r} = \frac{1}{2} τ $$

So in terms of π, we see that τ = 2π and π = τ/2.

In decimal form,

$$
\begin{align*}
τ &= 2 \cdot \left(3.1415926535897932384626433832795\ldots\right) \\
&=\mathbf{6.28}3185307179586476925286766559\ldots
\end{align*}
$$

So tau-day would be June 28.

The formulas for area and circumfrence of a circle become

$$
A = \frac12τ r^2
$$

$$
C = τ r
$$

Perhaps more importantly, things like radians and trigonometry become a lot simpler with τ. In terms of π, what's the angle that's 3/4 of the way around a circle? It's $\frac{3π}{2}$. In terms of τ, though, 3/4 of the way around a circle is just $\frac{3 τ}{4}$. Half-way around a circle is $\frac{τ}{2}$, and a full turn around a circle is just τ.

A lot of stuff makes a lot more sense with τ instead of π. Some people are quite serious about this. Read Michael Hartl's [Tao Manifesto](http://tauday.com/) for a much more thorough case for τ over π.

Anyway, happy half-tau day!
