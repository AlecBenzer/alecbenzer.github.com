---
layout: post
title: "Defining line integrals without physics"
---

Most introductory Calculus courses define line integrals using Physics as motivation, but I think it's a bit more direct to derive the definition from the idea of an infinite sum of some function evaluated over a line.

If you know how to do a simple one-dimensional integral, then you really already know how to do a line integral. Integrating some scalar field `f(x)` over an interval `[a,b]` is essentially the same as evaluating the line integral of `f(x)` over the line on the x-axis that goes from `a` to `b`. All that's left is extending this idea to lines that aren't straight.

When defining normal one-dimensional integrals, we usually talk about measuring the area under the graph of `f(x)`, but forget that for now. Focus on the idea of evaluating `f(x)` at every point on the line connecting `a` and `b`. Since there are an infinite number of points on this line, we need to take an approximation, and then take a limit of that approximation.

For our approximation, we just break the line up into a bunch of points: `a, a+dx, a + 2dx, ... , b`. We then evaluate the function at each of these points, `f(x_i)`, and then pretend that the function has the same value on every point between `x_i` and `x_(i+1)`. So our approximation ...
