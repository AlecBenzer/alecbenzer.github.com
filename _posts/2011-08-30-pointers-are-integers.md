---
layout: post
title: Pointers are integers
---
I feel like it's so much easier to understand what pointers are and how they work (but maybe not necessarily why they're useful) if you just think about them as integers, which is really all they are. A pointer is an integer with some extra type information that helps the compiler out. Let's declare a pointer to some type `foo`:

    foo* x;

By the way, I always put the asterisk closer to the type, as opposed to `foo *x`. I feel like it's only natural that way. `x` is not a `foo`, it's a pointer to a `foo`, which is just a special type of integer. My choice in syntax might have to do with how I choose to think about pointers, though. Someone who viewed pointers as a way to access their underlying objects more than just integers might find `foo *x;` to be the more appropriate syntax (and unfortunately C syntax rules for declaring multiple pointers would agree with them: `foo *x, *y;`).

Anyway, so we have our pointer. Right now it doesn't really "point" to anything in the sense that we purposely pointed it to some instance of a `foo`, but just like `int x;` would have some strange "uninitialized" value, our `foo*` has some random integer in it which, if we attempted to dereference, would cause our program to try and go to some random spot in memory and attempt to interpret the data there as a `foo` object. That would of course be bad. So let's have our pointer point to something:

    foo y;  //some foo object we just created
    x = &y;

The unary `&` "address-of" operator can be thought of as operating on a variable and returning an integer. This integer identifies the spot in memory where the variable (`y`, in our example) lives. This integer doesn't have type `int`, however, it has type `foo*`, and you'll see why, but it's really just a special kind of integer. So we take this integer and store it in our pointer `x`. Because `x` contains as its value the address where `y` is located, we say that `x` points to `y`. But `x` itself doesn't really know that it's pointing to `y`. It just has some address stored it in, which happens to be the address of `y`. If, for example, we somehow just _knew_ that `y` was going to be created in memory location `0x4AC`, we could have also said `x = 0x4AC`. To the compiler it works the same way. We have no mention of `y`, but `x` still "points" to `y`. (Note that we'd probably need to cast 0x4AC to get our compiler to accept it happily, like `x = (foo*)0x4AC`).

If instead of a stack-variable we want a heap-variable we can just use `new` instead:

    x = new foo;

Like `&y`, the expression `new foo` returns an integer representing the address of a `foo` that exists somewhere in memory. The difference is that with `&y` we get the address of an already existing `foo`, whereas `new foo` makes a new `foo` for us on the spot somewhere in memory. This new `foo` object is on the "heap", which for now just means that you allocated it yourself as opposed to having the compiler allocate it for you on the "stack". This also means that you need to deallocate the memory yourself. You do that with `delete`.

`delete` is an operator that instead of returning an address, expects an address as an operand. So, if we were done with the `foo` that we allocated and want to give that memory back to the system, we do:

    delete x;

And now the memory address that is stored in `x` represents memory that no longer belongs to our program. Like we saw previously though, if we magically knew that `x` contained the address `0x42B`, we could have just as easily done `delete 0x42B`.

Double pointers are sometimes regarded as mysterious, but if you think of pointers as just integers, they're not strange at all. When you declare an int with `int x` you store an `int` somewhere on the stack. This `int` has a memory address. You can get at it with `&x`. So just like integers are variables that exist somewhere in memory, so are pointers. `foo* x` declares an "integer" somewhere in memory. How do you access it's address? `&x`, just like we did with the `int`. We want to store this address? We can do so by putting it in a double pointer: `foo** y = &x`. `y` is a pointer just like any other, so it's just an "integer", too. Nothing magic going on here at all.

If all I'm saying is true though (that is, if pointers really are just integers), then why they hell do we even have pointer types? Well, so far we've talked about storing memory address in pointers, but what about actually accessing the objects? You do so with the unary `*` dereference operator.

    foo* x = //the address of some foo object
    foo y = *x;

The dereference operator expects a memory address and returns a "reference" (really, an lvalue - a value that can appear to the left of an assignment operator) to the object stored at that point in memory. But there's an issue there - how does the dereference operator know how large the object stored at the address is? It needs to know what kind of object you are attempting to retrieve so it knows how many bytes to read. This is the reason we need to specify the variable as a `foo*`, and not just an `int`, or a `ptr`, if there were such a type. Because the compiler knows how big a `foo` is it knows how to properly read the data at `x`, interpret it as a `foo`, and store the resulting object in `y`. 

Another confusion that can arise from not thinking of pointers are integers is what happens when a function returns a pointer. Consider:

    foo* get_the_foo()
    {
      //get the man his foo
    }

Because a pointer is something that "points" to things, one might think that it's possible to do something like:

    get_the_foo() = new foo;

After all, `get_the_foo` returns a pointer to a `foo`, and we should be able to point that `foo*` at something else. But a pointer is just an integer. `get_the_foo` returns just an integer. People would very rarely, for example, assume that you could do the following:

    int square(int x)
    {
      return x*x;
    }

    ...

    square(5) = 7;

You can't _assign_ to `square(5)` - it's just a number. In the same sense, you can't assign to `get_the_foo()`, because it's just a number, an address.

Another way this line of thinking helps is when considering uninitialized pointers. One might be surprised, for example, that this code:

    foo* x;
    f->doSomething();

and this code:

    foo* x = new foo;
    x->doSomething();
    delete x;
    x->doSomething();

have what is essentially the same error. They both access memory that doesn't belong to the program. This is clear in the second case, but in the first case, one might think that you're just dereferencing nothing, since x was not set to point to anything. But just as an `int` has some random value when it is uninitialized, so does a pointer. So attempting to dereference an uninitialized pointer is attempting to access a random location in memory, and odds are that it does not belong to you.
