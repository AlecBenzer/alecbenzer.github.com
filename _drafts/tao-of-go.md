---
published: false
---

# The Tao of Go

Lots of people seem to like to critique [Go](http://golang.org) without fully understanding its origins or motivations. Most languages are designed with the aim of providing features that are useful to programmers. This sounds like a no-brainer, but Go was designed (it seems) with the aim of providing a simple langage that's easy to understand and reason about. Those two aims sometimes conflict.

> Why would you have a language that is not theoretically exciting? Because it’s very useful.

> -- Rob Pike

Lots of people complain about the seemingly "backwards" decisions Go made. "Why would you not implement paramatric polymorphism/generics?", "Why would you not allow custom iterables?", etc. etc. Go wasn't built to solve the kinds of problems that these things solve. Go was built to solve a different problem.

I think this is the most telling and informative account of Go's creation and why it is the way it is:

> In the span of an hour at that talk we heard about something like 35 new features that were being planned [for C++11]. In fact there were many more, but only 35 were described in the talk. Some of the features were minor, of course, but the ones in the talk were at least significant enough to call out. Some were very subtle and hard to understand, like rvalue references, while others are especially C++-like, such as variadic templates, and some others are just crazy, like user-defined literals.

> At this point I asked myself a question: Did the C++ committee really believe that was wrong with C++ was that it didn't have enough features? Surely [...] it would be a greater achievement to simplify the language rather than to add to it. Of course, that's ridiculous, but keep the idea in mind.

I think before you can truly understand Go you need to work with it a lot, where "working with it" entails not only writing Go but also _reading_ Go.
