---
title: Waterfall
layout: post
listed: false
---

Here's some guesses as to why waterfall is a thing and why it doesn't work
well for developing software:

## I think part of the issue with waterfall isn't that it's an inherently bad model...

...but that it's incorrectly applied to software.

I don't know much about hardware development, but I imagine a process with at
least two distinct steps like:

1. Come up with very specific blueprints of what you're making.
2. Use the blueprint to make a bunch of instances of the thing.

The first step is neccesarily going to involve a lot of trial and error to
make sure that the blueprint actually makes sense. If you're doing it well,
it may involve a lot of speaking with the people who are going to actually
use the blueprint to mass-produce things and iterating with them.

It's also important that the second step is separate from the first. There's
a lot of long-lead-time work that goes into preparing to mass-produce a thing
(supply chain stuff, having people approve the product, testing the design).
Only realizing middway through production that something needs to be changed
is expensive.

Thus, there's no infrastructure for a feedback cycle from step 2 to step 1
because it's not something that ought to happen a lot: kinks need to be
worked out in step 1.

(It's important to underscore that the output from step 1 isn't a "rough
plan" of what to do. It's a very precise blueprint. Again: getting even minor
details of things wrong in step #2 is very expensive.)

## How do you map this to software?

The magic of software is that step #2 doesn't exist.

Writing software is _exactly_ producing an unambiguous description of how to
do a thing. The source code _is_ the blueprint. It's just a blueprint
implemented not by factories and people on assesmbly lines but by CPUs.

But we had this waterfall process with two steps (design and then implement)
and we tried to map _both_ these steps to software development.

Again, for waterfall to work, the output of step #1 needs to be an
unambiguous blueprint. And since ["the act of describing a program in
unambiguous detail and the act of programming are one and the
same"](https://twitter.com/kevlinhenney/status/3361631527), the output ought
to just be the source code, and we'd realize there's no other step.

But because we're shoe-horning this into waterfall, we decide that writing 
