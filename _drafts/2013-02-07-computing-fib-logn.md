---
layout: post
title: "Computing Fibonacci numbers in logarithmic time (sort of)"
---

As you likely know, the Fibonacci numbers are defined like so:

$$ \begin{aligned} F_0 &= 0 \\\\ F_1 &= 1 \\\\ F_n &= F_{n-1} + F_{n-2}, \quad \forall n \ge 2 \end{aligned} $$

A recursive algorithm that basically "reads off" that recursive definition to compute the nth Fibonacci number looks like this:

{% highlight cpp %}
int fib(int n) {
  if (n == 0) {
    return 0;
  } else if (n == 1) {
    return 1;
  } else {
    return fib(n - 1) + fib(n - 2);
  }
}
{% endhighlight %}

Of course, as you also likely know, this algorithm runs in $O(2^n)$, and exponential time is [very bad](/blog/exponentials-are-big).

The fundamental issue with the recursive algorithm is that it recomputes certain values of `fib(n)` many times. We could us some fancy memoization to fix this, or we could just iteratively compute the nth Fibonacci number like this:

{% highlight cpp %}
int fib(int n) {
  int a = 0, b = 1;
  for (int i = 0; i < n; ++i) {
    int old_b = b;
    b = a + b;
    a = old_b;
  }
  return a;
}
{% endhighlight %}

This algorithm runs in $O(n)$. Much better. But can we do even better still?

## A Fibonacci transformation

Let's look a little more closely at that last algorithm. At every stage, the algorithm has some pair $(a,b)$. $a$ and $b$ start off as the first two Fibonacci numbers, 0 and 1. After the loop runs once, we set $a$ to $b$'s old value, and set $b$ to old $a$ + old $b$. So now $a$ is the second Fibonacci number, and $b$ is the third. And so on and so on, until we've computed the Fibonacci number we're looking for.

Instead of representing this transformation via code, we could represent it as a matrix. In particular, we could use this matrix:

$$ M = \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} $$

and apply it to the pair $(a,b)$ like so:

$$ \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} a \\\\ b \end{bmatrix} = \begin{bmatrix} 0\cdot a + 1\cdot b \\\\ 1\cdot a + a\cdot b \end{bmatrix} = \begin{bmatrix} b \\\\ a + b \end{bmatrix} $$

The pair $(b, a + b)$ is then the new value for the pair. For instance, since the first pair is $(0,1)$, we see that the second pair is $(1, 0 + 1) = (1,1)$. If we want the third pair, all we have to do is apply the transformation again:

$$\begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 1 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 1 \\\\ 2 \end{bmatrix}$$

We could also look at this computation like so:

$$\begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} \cdot \left(   \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} \cdot \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}   \right) = \begin{bmatrix} 1 \\\\ 2 \end{bmatrix}$$

Ie, we get the third pair by applying the transformation to the first pair, and then applying the transformation to the output of that.

Since matrix multiplication is associative, this is equivelant to:

$$\left(\begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix} \cdot   \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix}\right) \cdot \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} = \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix}^2 \cdot \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}$$

And so, in general, if we want the nth Fibonacci number, all we need to do is apply this transformation to the starting pair $n$ times, like so:

$$ \begin{bmatrix} 0 & 1 \\\\ 1 & 1 \end{bmatrix}^n \cdot \begin{bmatrix} 0 \\\\ 1 \end{bmatrix} = M^n \cdot  \begin{bmatrix} 0 \\\\ 1 \end{bmatrix}$$

## Fast exponentiation

Okay, great, so we can compute $F_n$ by computing $M^n$ and applying that to $(0,1)$. Who cares?

Well, it turns out that there's a fast way we can compute $M^n$, which actually applies to anything that can be squared (ie, not just matricies, although that's why we care in this context)

First, observe that $M^n = \left(M^{n/2}\right)^2$ if $n$ is even, and $M^n = \left(M^{\lfloor n/2 \rfloor}\right)^2M$ if $n$ is odd.


