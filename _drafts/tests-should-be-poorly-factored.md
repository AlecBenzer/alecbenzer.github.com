---
layout: post
title: Tests should be poorly factored
---

Say you have some code like:

```python
def square(x):
    return x
```

A test like:

```python
def test_square(x):
    for x in [1, 2, 3, 5, 6, 9, 14, 101]:
        assert square(x) == x ^ 2
```

is "well-factored", in that it doesn't have a lot of repetition, but isn't a
great a test, since it's basically testing that the function's code does what
the function's code does.

A better test would be something like:

```python
def test_square():
    assert square(1) == 1
    assert square(2) == 4
    assert square(3) == 9
    # ...
```

because, for one, it would expose the bug (`^` is XOR in Python, not exponentiation).

---

That was a really simple example; so simple that the mistake probably seems incredibly obvious. Let's look a little subtler:

```python
def do_stuff(x):
    try:
        stuff(x)
        some_more_stuff(x)
        if x % 2 == 0:
            raise Exception("I hate even numbers.")
    except Exception:
        print("Couldn't do stuff with %s! Try an even number like %s or %s".format(
                x, x + 1))
```

Imagine we want to add a test for some failure cases:

```python
def test_do_stuff_fails():
    mocker.patch(print)
    for x in [3, 5, 7]:
        do_stuff(x)
        print.assert_called_with("Couldn't do stuff with %s!".format(x))
```
