---
layout: post
title: "Left and right inverses"
---
Here's a pretty simple-seeming question: what's the inverse of the function

$$f(x) = (x+1)^2$$

A quick look might lead to the answer "f has no unique inverse", since

$$
\begin{eqnarray\*}
f(g(x)) = x &\iff& (g(x) + 1)^2 = x \\\\
&\iff& \sqrt{(g(x) + 1)^2} = \sqrt{x} \\\\
&\iff& \left|g(x) + 1\right| = \sqrt{x} \\\\
&\iff& g(x) + 1 = \pm \sqrt{x} \\\\
&\iff& g(x) = \pm \sqrt{x} - 1
\end{eqnarray\*}
$$

so we have that both $\sqrt{x} - 1$ and $-\sqrt{x} - 1$ are potential inverses. But this isn't actually the answer.

Functions can have two kinds of inverses: left-inverses and right-inverses. A right-inverse of a function $f$ is a function $g$ so that $$f(g(x)) = x.$$ So the calculations above computed two _right-inverses_ for $f$. A left-inverse for $f$ is a function $g$ so that $$g(f(x)) = x.$$ If $g$ is both a left inverse and a right inverse, then $g$ is a "general" inverse.

So we have two right-inverses for $f$. If either of these is also a left-inverse, then they are inverses for $f$. So let's try it.

Let $g_1(x) = \sqrt{x} - 1$ and $g_2(x) = -\sqrt{x} - 1$.

Note that both these functions have a domain of $\\{x : x \ge 0\\}$, since this is the range of $f$.

$$
g_1(f(x)) = \sqrt{(x+1)^2} - 1 = \left|x+1\right| - 1.
$$

Since $x \ge 0$, $x + 1 \ge 1 > 0$, so $|x + 1| = x + 1$. Therefore,


$$
g_1(f(x)) = (x + 1) - 1 = x.
$$

Okay, so $g_1(f(x)) = x = f(g_1(x))$, so $g_1$ is a general inverse for $f$.

$$
g_2(f(x)) = -\sqrt{(x+1)^2} - 1 = -|x+1| - 1 = -(x+1) - 1 = -x -1 -1 = -x -2.
$$

So we see that $g_2(f(x)) \neq x$, which means that while $g_2$ is a right-inverse for $f$, it isn't a left-inverse, and thus not a general inverse.

So actually, the only general inverse $f$ has is $g_1$, meaning that $f$ does indeed have a unique inverse, despite not having a unique right-inverse.
