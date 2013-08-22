---
layout: "post"
title: "\"C++ is bad\" does not imply \"Use C\""
---

I saw [this](http://250bpm.com/blog:4) posted on [HN](https://news.ycombinator.com/item?id=6220049) tonight, and having been using C++ a lot lately at work, I felt like writing up a response.

"There's this bad thing in C++" does not imply "I should use C instead". It might just imply "don't use _that_ thing in C++". Especially since a lot of these pots start out saying "I went into this wanting to use C++ because of this good thing". So use those good things, and don't use the bad things. Preferably with some [clear-cut rules](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml).

## Exceptions

The first half of that post is pretty much "exceptions are bad". You're right, they kind of are. [So don't use them](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Exceptions).

The author himself does in fact say

> Taking the problems described above into account I've decided to use C++ minus exceptions

but

> Unfortunately, the problems don't end up(sic) here...

## Constructor failure

This is a common issue with using constructors:

{% highlight cpp %}
class Foo {
 public:
  Foo() {
    if(SomeOperationFails()) {
      // what do you do here?
    }
  }
};
{% endhighlight %}

So one thing you can do is:

{% highlight cpp %}
class Foo {
 public:
  Foo() {}

  int Init() {
    if (SomeOperationFails()) {
      return 1;
    }
    return 0;
  }
};

...

Foo foo;
foo.Init();
{% endhighlight %}

Same problem with destructors, potentially (though much less frequently, I think):

{% highlight cpp %}
class Foo {
 public:
  Foo() {}
  ~Foo() {}

  int Init() {
    if (SomeOperationFails()) {
      return 1;
    }
    return 0;
  }

  int Destroy() {
    if (SomeOtherOperationFails()) {
      return 1;
    }
    return 0;
  }
};

...

Foo foo;
foo.Init();
...
foo.Destroy();
{% endhighlight %}

Compared to something similar in C:

{% highlight c %}
typedef struct {
  ...
} Foo;

int FooInit(Foo* f) {
  if (SomeOperationFails()) {
    return 1;
  }
  return 0;
}

int DestroyFoo(Foo* f) {
  if (SomeOtherOperationFails()) {
    return 1;
  }
  return 0;
}

...

Foo foo;
FooInit(&foo);
...
DestroyFoo(&foo);
{% endhighlight %}

We've got a grand-total of _three_ additional lines in the C++ version. And that's only because of the empty destructor that you can leave out, and the empty constructor that you _might_ be able to leave out (if any of your member fields don't have default constructors you'd need explicitly initialize them in your constructor's initializer list thing).

> However, the really bad thing about the C++ version of the code is what happens when developers put some actual code into the constructor instead of systematically keeping the constructors empty.

Okay, fair point. It _is_ nice to have your compiler enforce these kinds of things for you, instead of having to worry about them yourself.

[A linter](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#cpplint) can help with some stuff, though that might be a bit tough to automatically detect stuff like non-empty constructors, especially if you want to [allow _some_ work in constructors, just not much](http://google-styleguide.googlecode.com/svn/trunk/cppguide.xml#Doing_Work_in_Constructors).

[Code reviews](http://www.codinghorror.com/blog/2006/01/code-reviews-just-do-it.html) can help as well (though to be fair I would have probably scoffed at that as an answer before dealing with code reviews myself).

The rest of the post was more or less bad things that happen if you do end up with non-trivial constructors/destructors, which, admittedly, is bad.

## Factory methods

Worth mentioning that instead of the initializer approach you can try a factory method:

{% highlight cpp %}
class Foo {
 public:
  static Foo* New() {
    if (SomeOperationFails()) {
      return NULL;
    }
    return new Foo;
  }

 private:
  Foo() {}
};

...

Foo* foo = Foo::New();
...
delete foo;
{% endhighlight %}

This gives the benefits of:

* Completely hiding the plain constructor, so users can't get their hands on an object without it being propertly initialized.
* Removing an additional method call. `Foo foo; foo.Init();` becomes `Foo* foo = Foo::New();`

while suffering from:

* Forcing you to either return a pointer or do an object copy
* Preventing you from returning error information (all you can do is return `NULL`)

Issues with using a pointer aren't too bad when using a smart pointer like `std::unique_ptr`:

{% highlight cpp %}
unique_ptr<Foo> foo = Foo::New();
{% endhighlight %}

If you want to get fancy, you can implement something like Haskell's `Either`

{% highlight cpp %}
// We use the idiom that a "left" value is an error and a "right" value is
// valid
template <class T, class U>
class Either {
 public:
  Either(const T& t) : t_(t), ok_(false) {}
  Either(const U& u) : u_(u), ok_(true) {}

  const T& left() { return t_; }
  const U& right() { return u_; }
  bool ok() const { return ok_; }

 private:
  T t_;
  U u_;
  bool ok_;
};

Either<const char*, double> Sqrt(double x) {
  if (x < 0) {
    return "Can't take squareroot of a negative";
  }
  return sqrt(x);
}

int main() {
  auto nums = {1.0, 4.0, 5.0, -1.0, -2.0, -3.0};
  for (auto num : nums) {
    auto x = Sqrt(num);
    if (x.ok()) {
      printf("%.2lf\n", x.right());
    } else {
      printf("%.2lf: %s\n", num, x.left());
    }
  }
  return 0;
}
{% endhighlight %}

{% highlight shell %}
$ ./a.out
1.00
2.00
2.24
-1.00: Can't take squareroot of a negative
-2.00: Can't take squareroot of a negative
-3.00: Can't take squareroot of a negative
{% endhighlight %}
