---
layout: post
title: "Sorting more elaborate ratings"
---

(psuedo-continuation of ["How to sort ratings"](/how-to-sort-ratings))

So in that last post I explained a derivation of the Wilson score confidence interval, which (as described in a [post by Evan Miller](http://www.evanmiller.org/)) can be used to sort a collection of items by average rating. But this only works when the rating system employed is a binary one of "I like it" or "I don't like it" ratings. But the generalization of the Wilson score confidence interval to more elaborate rating scale (like a 5-star or continuous rating scale) is not obvious.

In this post I'll try and explain the derivation behind some simmilar methods for sorting these more complicated ratings.


## A quick tl;dr of the last post
