---
layout: post
title: "Copy constructors and \"explicit\" in C++"
---
At one point you were probably told that something like:

{% highlight cpp %}
int x;
x = 4;
{% endhighlight %}

could be simplified to:

{% highlight cpp %}
int x = 4;
{% endhighlight %}

While it's true that both of these result in x having the value of 4, they're sort of different things. The `=` operator is a little different in each case.

You may also have been told at one point that `int x = 4` could also be written as `int x(4)`. In fact this is what's really going on when we do the initialization-assignment. It's just syntactic sugar for invoking the copy constructor. This is different from first allocating an object, and then assigning its contents.

If you don't believe me, trying running this code:

{% highlight cpp %}
#include <iostream>
using namespace std;

class Foo
{
  public:
    Foo() { cout << "ctor" << endl; }
    Foo(const Foo& f) { cout << "cctor" << endl; }
    Foo& operator=(const Foo& f) { cout << "op=" << endl; }
};

int main()
{
  cout << "Foo a;" << endl;
  Foo a;

  cout << "\nFoo b; b = a;" << endl;
  Foo b;
  b = a;

  cout << "\nFoo c(a);" << endl;
  Foo c(a);

  cout << "\nFoo d = a;" << endl;
  Foo d = a;

  return 0;
}
{% endhighlight %}


You'll get this output:

{% highlight text %}
Foo a;
ctor

Foo b; b = a;
ctor
op=

Foo c(a);
cctor

Foo d = a;
cctor
{% endhighlight %}

If you think about it this makes sense - initialization and assignment are two different things. Initialization is about figuring out what to make memory look like when an object first springs into existence. Assignment is about taking an already created object and replacing its current data with new data.

Now, consider an expression like this:

{% highlight cpp %}
Foo f(v);
//or equivalently:
Foo f = v;
{% endhighlight %}

What type does `v` have in this context? In the code above `v` was a `Foo`,  which made sense because we were invoking a copy constructor that expects a `Foo` as its only parameter. But it turns out that the type of `v` above doesn't really matter -- _any_ `v` for which there is an appropriately defined `Foo` constructor will work:

{% highlight cpp %}
Foo(int x) { cout << "Foo(int)" << endl; }

...

Foo e = 4;
{% endhighlight %}

The above is perfectly valid. The `Foo e = 4` gets translated into `Foo e(4)`, which is a valid way of constructing a `Foo`. It actually also turns out that `Foo(int)` works like any copy constructor would:

{% highlight cpp %}
Foo do_stuff(Foo f)
{
  //stuff happens
  return 7;
}

...

Foo f = do_stuff(17);
{% endhighlight %}

The copy constructor is used to pass `17` as a `Foo`, and again to return `7` as a `Foo`.

This is actually kind of neat. Imagine if we were writing a `BigInt` class. It might look something like this:

{% highlight cpp %}
class BigInt
{
  public:
    BigInt() { /*stuff*/ }
    BigInt(int x) { /*other stuff*/ }
    //some other public methods
  private:
    //magic instance data
};
{% endhighlight %}

We can now create BigInts from ints really simply, like this:

{% highlight cpp %}
BigInt a = 42;
{% endhighlight %}

and also pass them to functions simply:

{% highlight cpp %}
void stuff(BigInt x)
{
  //stuff
}

...

stuff(73);         // <- looks much nicer
stuff(BigInt(73)); // <- than this
{% endhighlight %}

That's pretty convenient and allows for some nice syntax. But it can also be a bit of an issue. What if we were implementing some kind of container class:

{% highlight cpp %}
template<class T>
class Container
{
  public:
    Container(int size) { /*stuff*/ }
    //etc
  private:
    //etc
};
{% endhighlight %}

We can do this to make a container with room for 4 things:

{% highlight cpp %}
Container box(4);
{% endhighlight %}

But we can also do this:

{% highlight cpp %}
Container box = 4;
{% endhighlight %}

That's not so good. Unlike with BigInts, 4 is in no way a Container, and it's misleading to use that kind of syntax. It can also get much more dangerous with things like this:

{% highlight cpp %}
T add(Container<T> a, Container<t> b)
{
  //"add" the two containers
}
{% endhighlight %}

One might accidentally assume that `add(box,5)` is meant to add 5 to all the elements inside of `box`. Normally, the compiler would tell us that this is a type mis-match. But with the way we've defined our constructors, C++ will happily convert `5` into an empty container with room for 5 elements.

To fix this, we have the `explicit` keyword. Prefixing a constructor definition with `explicit` tells the compiler "don't use this single-parameter constructor as a copy constructor".

{% highlight cpp %}
explicit Foo(int x) { cout << "Foo(int)" << endl; }
{% endhighlight %}

Now, trying to do something like `Foo e = 4` will result in a compiler error.
