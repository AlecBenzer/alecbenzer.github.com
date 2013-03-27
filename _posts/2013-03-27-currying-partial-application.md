---
layout: post
title: "Currying vs. Partial Application"
---

I feel like there's a lot of confusion as to the difference between currying and partial application, especially as they're often brought up together in similar contexts.

Partial application addresses the following: given that we have multi-parameter functions, we want to fix certain parameters of a function.

Explicit partial application is possible in almost any language. In C:

{% highlight c %}
int foo(int a, int b, int c) {
  return a + b + c;
}

int foo23(int a, int c) {
  return foo(a, 23, c);
}
{% endhighlight %}

`foo23` is essentially a partial application of `foo`, with the parameter `b` fixed to the value 23.

Of course, explicit partial application like this isn't all that useful; we'd generally want our language to support some kind of partial application for us.

In python, for example, we can do

{% highlight python %}
from functools import partial

def foo(a,b,c):
  return a + b + c

foo23 = partial(foo, b=23)

foo23(a = 1, c = 3)  # => 27
{% endhighlight %}

Currying addresses an ostensibly fairly different issue: Given that we have _only single parameter functions_, and we're in a language with first-class functions, how can we implement multi-parameter functions? Currying is a **way of implementing multi-parameter functions.**

Here's a single-parameter javascript function:

{% highlight javascript %}
var foo = function(a) {
  return a * a;
}
{% endhighlight %}

If we we're only allowed to write single-parameter functions, we could simulate a multi-parameter function like this:

{% highlight javascript %}
var foo = function(a) {
  return function(b) {
    return a * a + b * b;
  }
}
{% endhighlight %}

and call it by doing `(foo(3))(4)`, or just `foo(3)(4)`.

Note that currying offers a very natural way to implement certain partial applications. If I want to partially apply `foo` by fixing its first parameter to `5`, all I need to do is `var foo5 = foo(5)`. There -- done. `foo5` is our partially applied `foo`. Note, though, that there isn't much of a natural way to partially apply `foo`'s second parameter (without first applying its first parameter).

Of course, javascript does support multi-parameter functions

{% highlight javascript %}
var bar = function(a, b) {
  return a * a + b * b;
}
{% endhighlight %}

`bar`, as we've defined it, is not a curried function. Calling `bar(5)`, for example, won't return a function that we can then apply `12` to. We can only call `bar` as `bar(5,12)`.

Other languages, though, like Haskell and OCaml, implement all multi-parameter functions via currying.

Here's `foo` from above translated to OCaml:

{% highlight ocaml %}
let foo = fun a ->
  fun b ->
    a * a + b * b
{% endhighlight %}

and here's `bar` translated into OCaml:

{% highlight ocaml %}
let bar = fun a b ->
  a * a + b * b
{% endhighlight %}

We might call the first function "explicitly curried" and the second one "implicitly curried".

Unlike in the javascript case, in OCaml, `foo` and `bar` are really exactly the same thing. We call them in the exact same way

{% highlight text %}
# foo 3 4;;
- : int = 25
# bar 3 4;;
- : int = 25
{% endhighlight %}

and both can be called with just one argument to create a partial application

{% highlight text %}
# let foo5 = foo 5;;
val foo5 : int -> int = <fun>
# let bar5 = bar 5;;
val bar5 : int -> int = <fun>
# foo5 12;;
- : int = 169
# bar5 12;;
- : int = 169
{% endhighlight %}

In fact, we can consider the anonymous function form

{% highlight ocaml %}
fun arg1 arg2 ... argN -> exp
{% endhighlight %}

as syntactic sugar for

{% highlight ocaml %}
fun arg1 -> fun arg2 -> ... -> fun argN -> exp
{% endhighlight %}

## TL ; DR

* Partial application is just taking a function, fixing some of its parameters, and getting a new function.
* Currying is a way of using anonymous single-parameter functions to implement multi-parameter functions.
* Currying allows you to implement certain kinds of partial application easily.
* Some languages (eg Haskell, OCaml) internally implement _all_ multi-parameter functions via currying.
