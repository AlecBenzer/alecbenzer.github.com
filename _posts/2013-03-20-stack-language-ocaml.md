---
layout: post
title: "Implementing a stack language in OCaml with continuations"
---
I'm subscribed to my school's SigPLAN chapter's mailing list, and we just got mailed out a challenge to implement a stack language in OCaml.

We don't care about parsing or anything here; we're just interested in getting the functionality into an OCaml interpreter (ie, having OCaml to the parsing for us, basically). The challenge came with some particular syntax in mind, but I'll get to that later.

So my first thought was just to have a type corresponding to possible commands

{% highlight ocaml %}
type command = Push of int | Pop | Add
{% endhighlight %}

and to have a recursive function that just executes a list of them

{% highlight ocaml %}
let rec run' cmds stack = match cmds with
  | Push x :: rest -> run' rest (x :: stack)
  | Pop :: rest -> run' rest (tl stack)
  | Add :: rest -> run' rest (((hd stack) + (hd (tl stack))) :: (tl (tl stack)))
  | [] -> hd stac
{% endhighlight %}

and then just a simple driver function to start us off with an empty stack

{% highlight ocaml %}
and run cmds = run' cmds []
{% endhighlight %}

I got some feedback to use pattern-matching for the add clause, which indeed looks a lot nicer (or so I think)

{% highlight ocaml %}
let rec run' cmds stack = match cmds with
  | Push x :: rest -> run' rest (x :: stack)
  | Pop :: rest -> run' rest (tl stack)
  | Add :: rest ->
      let (a :: b :: stack') = stack
      in run' rest (a + b :: stack')
  | [] -> hd stack
{% endhighlight %}

All in all it's some pretty simple code

{% highlight ocaml %}
(* Example execution:
       # run [Push 1; Push 2; Push 3; Pop; Push 4; Add; Add] ;;
       - : int = 7
 *)

open List

type command = Push of int | Pop | Add

let rec run' cmds stack = match cmds with
  | Push x :: rest -> run' rest (x :: stack)
  | Pop :: rest -> run' rest (tl stack)
  | Add :: rest ->
      let (a :: b :: stack') = stack
      in run' rest (a + b :: stack')
  | [] -> hd stack
and run cmds = run' cmds []
{% endhighlight %}

Awesome, works great. Until I saw the syntax that was intended:

{% highlight text %}
# start push 1 push 2 add stop;;
- : int = 3
# start push 1 push 2 push 3 pop push 4 add add stop;;
- : int = 7
{% endhighlight %}

Say _what?_ I wasn't really sure what kind of black-magic I was looking at at first. `start` just seemed like some magic function that took a fuck-ton of arguments and executed them as a program.

But then I got a hint, and afterwards it really wasn't all that bad.

## Currying &amp; Partial Application

So an important part of understanding what's going on here is understanding how OCaml (and other functional languages like Haskell) deal with function calls.

Consider a function like this:

{% highlight ocaml %}
let f a b = a + b
{% endhighlight %}

We would generally call it by doing something like this:

{% highlight text %}
# f 1 2;;
- : int = 3
{% endhighlight %}

But what's really going on here is something a little different than what you might expect. In reality, all OCaml functions take only _one_ argument. So really, `f 1 2` gets evaluated as `(f 1) 2`. That is, we apply `f` to 1, take the result (which is another function), and apply that to 2.

So the following is totally legal:

{% highlight ocaml %}
let f' = f 1;;
{% endhighlight %}

`f'` is a function that takes just one parameter, and adds one to it. So `f' x` is the exact same thing as `f 1 x`.

## Continuations and chaining function calls

So using partial application, and this other thing called continuations, we can implement a way to chain lots of functions calls together like we want for our stack language syntax.

A continuation is basically a function that gets called on the results of another function. For example:

{% highlight ocaml %}
let add_continuation a b k = k (a + b)
{% endhighlight %}

We call `add_continuation` with two numbers to add, as well as a third argument `k`, which is a function to be called on the result of the addition (ie, `k` is the 'k'ontinuation)

{% highlight ocaml %}
let square x = x * x
in add_continuation 4 5 square
{% endhighlight %}

Here, `k` gets bound to `square`. The above expression evaluates to `square (4 + 5)`.

Of course, there's no reason the continuation function needs to only take one argument, just because we pass it only one. We can use partial application to do stuff like this:

{% highlight ocaml %}
let mult a b = a * b
in add_continuation 4 5 mult
{% endhighlight %}

_This_ expression evaluates to `mult (4 + 5)`, but since `mult` expects 2 arguments, this is just a partial application of `mult`. Ie, `mult (4 + 5)` represents a function that multiplies whatever you pass it by 9.

## Back to the stack

Now, using this, we're able to chain function calls together, carrying along some state with us. In this case, our state is just the stack.

First, we have the `start` function, which starts off this whole process by initializing our state and passing it on

{% highlight ocaml %}
let start k = k []
{% endhighlight %}

All that `start` does is take a continuation function `k`, and pass it an empty list, which represents our initial empty stack.

So say we had some function

{% highlight ocaml %}
let push5 stack = 5 :: stack
{% endhighlight %}

We can now do something like

{% highlight ocaml %}
start push5
{% endhighlight %}

which would evaluate to just `[5]`.

The problem with `push5`, as it is, is that it ends the chain. We need to modify it so that instead of just returning the modified stack, it passes the modified stack on to some other function

{% highlight ocaml %}
let better_push5 stack k = k (5 :: stack)
{% endhighlight %}

Of course, we do _eventually_ want to stop the chain of functions. So we have a function specifically for ending the chain

{% highlight ocaml %}
let stop stack = stack
{% endhighlight %}

So now we can do 

{% highlight ocaml %}
start better_push5 better_push5 stop
{% endhighlight %}

to get `[5; 5]`.

Obviously a function that pushes only 5 isn't particularly useful. We want a function that takes any integer and pushes it onto the stack

{% highlight ocaml %}
let push stack x k = k (x :: stack)
{% endhighlight %}

The only potentially confusing part of this is why we want the `x` parameter to be in between the `stack` and `k` parameters, but looking at the syntax we're aiming for and the way each function gets called, it should be clear why this is.

From there, it's just a matter of defining functions that take in the stack as their first parameter, modify the stack, and pass the stack along to a continuation function. So, using some pattern matching, pop looks like

{% highlight ocaml %}
let pop (_ :: stack') k = k stack'
{% endhighlight %}

and add looks like

{% highlight ocaml %}
let add (a :: b :: stack') k = k (a + b :: stack')
{% endhighlight %}

So all in all we get these nice five lines of code (modified `stop` so that it returns the head of the stack instead of the whole stack)

{% highlight ocaml %}
let start k = k []
let push stack x k = k (x :: stack)
let pop (_ :: stack') k = k stack'
let add (a :: b :: stack') k = k (a + b :: stack')
let stop (x :: _) = x
{% endhighlight %}
