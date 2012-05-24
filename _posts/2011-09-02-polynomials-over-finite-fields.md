---
layout: post
title: Polynomials over finite fields not functions
---
An interesting fact I learned from my linear algebra professor ([Charles Rezk](http://www.math.uiuc.edu/~rezk/)): polynomials defined over finite fields do not _uniquely_ define functions. Generally, when speaking about the set of polynomials of degree at most `n` (as, for example, a vector space), they can be thought of as functions. But this is when the polynomials are defined over the (infinite) field of real numbers. If we define our polynomials over a finite field, like `{0,1}`, this isn't so. Consider the polynomials:

    f(x) = x
    g(x) = x^2

If we tried to define these polynomials as n-tuples, we might represent `f` as `(0,1,0)` and `g` as `(0,0,1)` (`f` has a coefficient of `0` for its constant term, `1` for its linear term, and `0` for its quadratic term, and similarly for `g`). In this sense `f` and `g` are clearly different. But consider `f` and `g` as functions (ie, maps of inputs to outputs):

    f(0) = 0, f(1) = 1
    g(0) = 0, g(1) = 1

Over the field we've chosen, `f` and `g` are actually the same function. Which means we can't just treat the set of polynomials as a set of functions because they're no longer isomorphic. We need to decide whether we're talking about polynomials as just expressions or as functions.
