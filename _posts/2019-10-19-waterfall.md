---
title: Waterfall
layout: post
listed: false
...

Here's some guesses as to why waterfall is a thing and why it doesn't work
well for developing software.

_tl;dr_:

* In the real world you first design things and then implement the designs.
* The magic of software is that implementing is ~free.
* We didn't quite get this, and tried to split what's really a "design" step
  into two "design" and "implement" steps.

## Building physical things is expensive

I don't know much about making hardware but that won't stop me from
speculating.

Building a physical thing takes time. Mass-producing a lot of physical
things takes a lot of time, and also a lot of up-front work. You need to:

* Get factories ready and configured correctly
* Prepare to have enough supply of the things you'll need to build
  the thing
* Make sure that things being built actually work, without
  side-effects, and that they do what you wanted them to do
* Y'know, uh... other hardware stuff?

Because of all this effort, before you start mass-producing a thing, you need
to be really sure you're doing it right. Finding out part-way through the
process of mass-producing that you got something wrong is really expensive.

## Design well, then implement

Faced with this, it makes sense to break your process up into two steps:

1. Come up with very specific blueprints of what you're making.
2. Use the blueprint to make a bunch of instances of the thing.

Note that the output from step 1 here isn't a "rough plan" of what to do.
It's a very specific, precise blueprint. Getting even minor details of things
wrong in step #2 is very expensive.

Thus, the first step is probably going to involve a lot of trial and error to
make sure that the blueprint actually makes sense. If you're doing it well,
it may involve a lot of speaking with the people who are going to actually
use the blueprint to mass-produce things and iterating with them.

## The magic of software is that there's no step #2

<blockquote class="twitter-tweet"><p lang="en" dir="ltr">The act of describing a program in unambiguous detail and the act of programming are one and the same.</p>&mdash; Kevlin Henney (@KevlinHenney) <a href="https://twitter.com/KevlinHenney/status/3361631527?ref_src=twsrc%5Etfw">August 17, 2009</a></blockquote> <script async src="https://platform.twitter.com/widgets.js" charset="utf-8"></script>

Writing software is _exactly_ producing an unambiguous description of how to
do a thing. Source code _is_ a blueprint: it's just a blueprint implemented
not by factories and people on assesmbly lines but by CPUs.

Any kind of English-language/block-diagram based specification of a software
system that tries to be unambiguous but can't actually be executed by a CPU is:

* at worst, too imprecise to be considered a "blueprint" for the purposes of
  this process
* at best, a lot of extra work with not much benefit vs. just expressing it as
  source code

Once you do have the software, "implementing" it in a mass-production kind of
way is just a matter of copying bits. You obviously still need machines to
execute the code, devops is definitely a thing, etc., but it's:

* a) Still much cheaper than mass-producing physical things, but more importantly:
* b) _Largely_ agnostic to the actual software being executed. Again, the whole
  _point_ of ***soft***ware is that a CPU can execute whatever code you give it
  (vs. having to print specific circuits to do specific things).

## Shoehorning

Nonetheless, we had this waterfall process that worked for hardware, and it
had two steps: first design, then implement. So we tried to map both these
steps to software development, despite the fact that it's really only the
"design" part.

I think **this is the real, core failure of waterfall**. It's not neccarily a
bad system in the abstract: it's applied to software _incorrectly_.

Going in to step #2, we only have a vague plan of what to do. It hasn't been
battle-tested down to the details (if it really had been, you'd already have
the source code -- because that's how you'd battle-test it.). So of course,
there's going to be issues that come up. But the system is not at all
engineered around these conflicts and/or how to resolve them.