---
layout: post
title: "Monads in C++"
---

There's probably already a million and three posts about explaining monads and
implementing monad-like stuff in C++, but screw it, now there's a million and
four.

## Maybes

Maybes are a common kind of monad. But don't worry about that right now. Maybes represent stuff
that can fail.

{% highlight cpp %}
double Inverse(double x) {
  return 1.0 / x;
}

...

Inverse(0.0);
{% endhighlight %}

C++ doesn't like dividing by 0. Now, running that
we'd probably get `inf`, but it wouldn't be surprising for
something like that to be a runtime-crash (or you can at least imagine a function where certain inputs can cause runtime crashes).

So we sanitize the input:

{% highlight cpp %}
double Inverse(double x) {
  if (x == 0) {
    return 0.0;
  }
  return 1.0 / x;
}

...

if (Inverse(0.0) == 0.0) {
  printf("That was an error\n");
}
{% endhighlight %}

But this is kind of hacky. What if 0 was a valid potential output? It'd be better
to have a more concrete way of signaling failure.

A common C-style idiom is to have functions return integer status codes (with 0 indicating success), and store the real results in output parameters:

{% highlight cpp %}
int Inverse(double x, double* answer) {
  if (x == 0) {
    return 1;  // failure
  }
  *answer = 1.0 / x;
  return 0;  // success
}

...

double inv;
if (Inverse(0.0, &inv) != 0) {
  printf("There was an error\n");
} else {
  printf("The answer is %lf\n", inv);
}
{% endhighlight %}

In C++ we can use exceptions:

{% highlight cpp %}
double Inverse(double x) throw(string) {
  if (x == 0) {
    throw "Can't divide by zero";
  }
  return 1.0 / x;
}

...

try {
  printf("The answer is %lf\n", Inverse(0.0));
} catch (string err) {
  printf("That was an error.");
}
{% endhighlight %}


But another thing we can do is to use a Maybe:

{% highlight cpp %}
template<class T>
class Maybe {
 public:
  Maybe() : ok_(false) {}
  Maybe(T t) : t_(t), ok_(true) {}

  bool ok() const { return ok_; }
  const T& get() const { return t_; }

 private:
  T t_;
  bool ok_;
};
{% endhighlight %}

`Maybe<T>` is a type that _might_ be a `T`, but might also be nothing.

`Maybe`'s default constructor constructs a "bad" value, and its single
parameter constructor (which we did _not_ mark as `explicit`, so we can do stuff
    like `Maybe<double> x = 4.0`) constructs "good" values.

{% highlight cpp %}
Maybe<double> Inverse(double x) {
  if (x == 0) {
    return Maybe<double>();
  }
  return 1.0 / x;
}

...

Maybe<double> result = Inverse(0.0);
if (!result.ok()) {
  printf("That was an error\n");
} else {
  printf("The answer is %lf\n", result.get());
}
{% endhighlight %}

We can write some more potentially-failing functions:

{% highlight cpp %}
Maybe<double> Squareroot(double x) {
  if (x < 0) {
    return Maybe<double>();
  }
  return sqrt(x);
}
{% endhighlight %}

And, just for the sake of consistency, we can have functions that won't ever fail
return Maybes as well:

{% highlight cpp %}
Maybe<double> Square(double x) {
  return x * x;
}
{% endhighlight %}

And maybe (no pun intended) to test that everything works together, we write a test like this:

{% highlight cpp %}
bool Test(double x) {
  Maybe<double> result = Squareroot(x);
  if (!result.ok()) {
    return false;
  }

  result = Inverse(result.get());
  if (!result.ok()) {
    return false;
  }

  result = Square(result.get());
  if (!result.ok()) {
    return false;
  }

  result = Inverse(result.get());
  if (!result.ok()) {
    return false;
  }

  return x == result.get();  // x == 1/(1/sqrt(x))^2
}
{% endhighlight %}

As you can probably guess, the point here is that there's a lot of repetition
when it comes to chaining together these kinds of function calls.

One solution might be to change our functions to work like this:

{% highlight cpp %}
Maybe<double> Inverse(Maybe<double> x) {
  if (!x.ok()) {
    return x;
  }
  if (x.get() == 0) {
    return Maybe<double>();
  }
  return 1.0 / x.get();
}

// similarly for Squareroot, Square
{% endhighlight %}

So we could then write

{% highlight cpp %}
bool Test(double x) {
  Maybe<double> result = Inverse(Square(Inverse(Squareroot(x))));
  return result.ok() && x == result.get();
}
{% endhighlight %}

But all we've really done is move the reptition from our `Test` function into
the actual functions themselves.

## Let's do this in Haskell

Defining a Maybe type in Haskell would look something like this:

{% highlight haskell %}
data Maybe a = Just a | Nothing
{% endhighlight %}

which reads something like "there's a new data type called `Mayb` of `a`, for some type `a`, which is either `Just` an `a`, or `Nothing`". `Maybe<double>(5.0)` becomes `Just 5.0`, and `Maybe<double>()` becomes
`Nothing`.

Conveniently, [this is already defined for us in haskell](http://hackage.haskell.org/packages/archive/base/4.2.0.1/doc/html/Data-Maybe.html).

Here's a translation of `Inverse` to haskell:

{% highlight haskell %}
inverse x =
  if x == 0
  then Nothing
  else Just (1.0 / x)
{% endhighlight %}

Though haskell has some neat pattern-matching syntax to let us write this as:

{% highlight haskell %}
inverse 0 = Nothing
inverse x = Just (1.0 / x)
{% endhighlight %}

Translating literally, `Sqaureroot` would become

{% highlight haskell %}
squareroot x = 
  if x < 0
  then Nothing
  else Just (sqrt x)
{% endhighlight %}

but haskell has this other neat thing called guards that let us write:

{% highlight haskell %}
squareroot x
  | x < 0 = Nothing
  | otherwise = Just (sqrt x)
{% endhighlight %}

`Square` is simple:

{% highlight haskell %}
square x = Just (x * x)
{% endhighlight %}

And finally, here's `Test`:

{% highlight haskell %}
test x = 
  let result = squareroot x in
  if isNothing result
  then False
  else let result2 = inverse (fromJust result) in
    if isNothing result2
    then False
    else let result3 = square (fromJust result2) in
      if isNothing result3
      then False
      else let result4 = inverse (fromJust result3) in
        if isNothing result4
        then False
        else x == (fromJust result4)
{% endhighlight %}

Here, we're using haskell's `isNothing` in place of our `!Maybe::ok()` and `fromJust` as
`Maybe::get()`.

`Test` ends up looking the most cumbersome when translated literally like this
into haskell, because `Test` is rather imperative and doesn't translate all that
well into a functional form needed for haskell.

We could try fixing it up a bit,
     but we won't bother right now, because the _real_ way to fix `test` up is
     to take advantage of the fact that `Maybe` is a monad in haskell.

## The &gt;&gt;= operator

Looking at this from a kind of high-level, here's our problem: we have a bunch
of functions that look like this:

    a -> Maybe a

which is haskell type notation for "a function that takes one input of type `a`
and outputs a value of type `Maybe a`".

What we want is to be able to kind of glue them together like this:

    f(g(h(x)))

but this doesn't work because the output `Maybe a` is different than the
expected input type `a`.

Just as in C++, we could rewrite our functions to have type signature `Maybe a
-> Maybe a` like so:

{% highlight haskell %}
inverse Nothing = Nothing
inverse (Just 0) = Nothing
inverse (Just x) = Just (1.0 / x)
{% endhighlight %}

but we'd like to be able fix this without messing with our original functions.

What we can do instead is write a `connect` function, that looks like this:

{% highlight haskell %}
connect Nothing f = Nothing
connect (Just x) f = f x
{% endhighlight %}

Instead of handling the case of a `Nothing` input in `inverse` directly, we
use `connect` to do it for us. If our input is `Nothing`, we just
return `Nothing`. Otherwise, we extract the `x` out of the input and pass it on
to `f`, as function.

{% highlight haskell %}
(connect Nothing inverse) == Nothing  -- this Nothing came from connect
(connect (Just 0.0) inverse) == Nothing  -- this Nothing came from inverse
(connect (Just 4.0) inverse) == Just 0.25
{% endhighlight %}

It turns out "connect" already exists in Haskell, but as an operator written
`>>=`, often pronounced "bind".

{% highlight haskell %}
(Nothing >>= inverse) == Nothing
(Just 0.0 >>= inverse) == Nothing
(Just 4.0 >>= inverse) == Just 0.25
{% endhighlight %}

Having `>>=` be an operator makes it easier to chain this kind of stuff. Eg,
       with connect, we'd have to do:

{% highlight haskell %}
connect (connect (connect (connect (Just 4.0) inverse) squareroot) square) inverse
{% endhighlight %}

Whereas with `>>=`, it's just

{% highlight haskell %}
Just 4.0 >>= inverse >>= squareroot >>= square >>= inverse
{% endhighlight %}

So our test function from before can we written as:

{% highlight haskell %}
test x = let result = Just x >>= sqaureroot >>= inverse >>= square >>= inverse in
  if isNothing result
  then False
  else x == (fromJust result)
{% endhighlight %}

## Let's port bind to C++

It's actually pretty easy to implement something like the bind operator for our
C++ `Maybe`. Just throw this into the `Maybe` class definition:

{% highlight cpp %}
template<class U>
Maybe<U> operator>>(Maybe<U>(*f)(T)) {
  if (ok_) {
    return f(t_);
  } else {
    return Maybe<U>();
  }
}
{% endhighlight %}

Here we're overloading C++'s `>>` (shift-right) operator. C++ does actually have
a `>>=` operator (shit-right-equal), but its associativity doesn't work for use
as bind. Also, warning: Haskell also has a `>>` operator, which is related to,
     but distinct from, its `>>=` operator. But that has nothing to do with what
     we implemented above.

So our `Maybe::operator>>` function take as input a function called `f` with type signature
(in Haskell-like notation):

    T -> Maybe<U>

and returns a `Maybe<U>`. Just like with the `connect` function we wrote in
haskell, `operator>>` simply checks if we're okay, and then passes ourselves
onto `f`, or returns a non-ok `Maybe<U>` if we aren't okay.

So in C++, we can rewrite `Test` like so:

{% highlight cpp %}
bool Test(double x) {
  Maybe<double> result = Maybe<double>(x)
    >> Squareroot
    >> Inverse
    >> Square
    >> Inverse;
  return result.ok() && x == result.get();
}
{% endhighlight %}
