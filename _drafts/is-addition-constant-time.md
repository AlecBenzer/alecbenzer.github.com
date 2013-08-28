---
layout: post
title: Is addition constant time?
---

Practically speaking addition is certainly a constant time operation, and it "realistically" is for most hardware. But is it "theoretically" constant time?

## Fast Fibonacci numbers

Detour time: the traditional, iterative Fibonacci algorithm is something like this:

{% highlight go %}
a, b := 0, 1
for i := 0; i < N-1; i++ {
  a, b = b, a + b
}
// b is the Nth Fibonacci number
{% endhighlight %}

It runs in $O(n)$ time. But we can get a better asymptotic bound than that.

This is a "Fibonacci matrix":

$$\begin{bmatrix}
0 & 1 \\\\ 1 & 1
\end{bmatrix}$$

When applied to a pair $(a,b)$, it yields $(b,a+b)$:

$$
\begin{bmatrix}
0 & 1 \\\\
1 & 1
\end{bmatrix}
\cdot
\begin{bmatrix}
a \\\\
b
\end{bmatrix} =
\begin{bmatrix}
0\cdot a + 1\cdot b \\\\
1\cdot a + 1\cdot b
\end{bmatrix} =
\begin{bmatrix}b \\\\
a + b
\end{bmatrix}
$$

Ie, it's a matrix-version of the multiple-assignment:

    a, b := b, a + b

To iterate this assignment N-1 times, starting with `a = 0` and `b = 1`, we just apply the matrix N-1 times to the pair $(0,1)$, which is equivalent to raising the matrix to the (N-1)th power:

$$\begin{bmatrix}0 & 1 \\\\ 1 & 1\end{bmatrix}^{N-1}\cdot\begin{bmatrix}0 \\\\ 1\end{bmatrix}$$

So the Nth Fibonacci number is just the bottom element of the resulting pair.

## Fast exponentiation

So we've established that computing the Nth Fibonacci number is equivalent to raising some matrix to the (N-1)th power and applying it to (0,1). So how fast can we compute something to the (N-1)th power?

A simple $O(N)$ implementation would be:

{% highlight go %}
result := a
for i := 0; i < N-1; i++ {
  result *= a
}
{% endhighlight %}

But we can actually get a better solution using the [expontentiation by squaring](http://en.wikipedia.org/wiki/Exponentiation_by_squaring) algorithm:

{% highlight go %}
func pow(base, power int) int {
  if power == 0 {
    return 1
  } else if power % 2 == 0 {  // even
    return pow(base * base, power / 2)
  } else {  // odd
    return base * pow(base * base, (power-1)/2)
  }
}
{% endhighlight %}

The above is for ints, but the algorithm works for any objects that can be multiplied, using $O(\log(N))$ such multiplications.

Since our matrix is always 2x2, each matrix multiplication is 4 int multiplications and 2 int additions. And if we expect interger addition/multiplication to be constant time, then we'd expect exponentiation-by-squaring to take $O(\log(N))$ time.

So this means we can compute the Nth Fibonacci number in logarithmic time! Which is neat, but actually isn't too useful since except for very large N the simple iterative solution would probably be faster. That's not that point though.

What _is_ the point, is that an apparent contradiction arises.

---

There happens to be a closed form for the Nth Fibonacci number. It's this:

$$\frac{\left(1 + \sqrt{5}\right)^N - \left(1 - \sqrt{5}\right)^N}{2^N\sqrt{5}}$$

which is complicated looking, but the important thing to notice is that it's exponential in $N$. Which means that the logarithm of the Nth Fibonacci number is linear in $N$. Which means that the Nth Fibonacci number takes $O(N)$ bits to store.

The contradiction is this: we somehow computed $O(N)$ bits of data using only $O(\log(N))$ time. Surely, if we only spent $O(\log(N))$ time, we could have output at _most_ $O(\log(N))$ bits of data, since outputting a bit itself must take some time.

The contradiction arises because there's an implicit practical limit on how big the Nth Fibonacci number can get -- if we're in 32-bit integer land, we can't store the 48th (or higher) Fibonacci number, as it's greater than $2^{32} - 1$.

Another way of looking at this is to say that addition and multiplication aren't _really_ constant time in general -- they just are for 32-bit numbers, or whatever fixed size your hardware supports.

If we wanted to store arbitrarily large Fibonacci numbers, we'd have to use arbitrary-length integers, which would in fact _not_ allow for constant time arithmetic.
