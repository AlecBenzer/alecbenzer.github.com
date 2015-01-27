---
layout: post
title: "Transpose notation sucks"
---

By "transpose notation" I don't mean the use of $^T$ to indicate a
matrix transpose, but of some authors' insistence that vectors be thought of as
specifically either $n\times 1$ "columns" or $1\times n$ "rows", and not
simply as sequences of $n$ numbers.

When discussing vectors in texts using such conventions, vectors are generally
assumed to be columns unless otherwise specified. This is likely due primarily
to the fact that if we wish to express the application of a matrix $M$ to a
vector $v$ in terms of matrix _multiplication_, we must multiply $M$ with the
_column_ $v$.

However, this is usually obvious. If $M$ is a $m \times n$ matrix and $v$ is an
$n$ dimensional vector, and write $Mv$, $v$ _must_ be interpreted as a column
for the multiplication to work.

On the other hand, if we wish to express that a vector $v$ contains the $n$
numbers $x_1, \dots, x_n$, this convention means we must write either

$$ v = \begin{pmatrix} x_1 \\ x_2 \\ \vdots \\ x_n\end{pmatrix} $$

which takes up a lot of space, or $v^T = (x_1, x_2, \dots, x_n)$ or $v = (x_1,
x_2, \dots, x_n)^T$, both of which introduce a transpose operation for no real
reason. These alternatives are all, in my opinion, less preferable than $v =
(x_1, \dots, x_n)$.

## Vertical stacking

Suppose we have $m$ vectors, $v_1, \dots, v_m$, and we want to express the
matrix consisting of the $v_i$ as its rows. If the $v_i$ we assumed to be
columns, we would write

$$ \begin{pmatrix} v_1^T \\ \vdots \\ v_m^T \end{pmatrix} $$

But it would be about just as clear to write

$$ \begin{pmatrix} v_1 \\ \vdots \\ v_m \end{pmatrix} $$

The fact that we are vertically stacking the vectors should be enough to
indicate that each is being used as a row, and not a column. The _only_ other
possible intepretation is that instead of being an $m \times n$ matrix, we
have a $mn \times 1$ column. I imagine this interpetation of the notation comes
up so rarely that it would never cause any confusion.

## Dot products

Suppose $x$ and $y$ are $n$ dimensional vectors. If we think of them both as
columns, we can express the dot product as $x^Ty$, using a transpose and a
matrix multiplication. Or, we could forget about the columns and write $x \cdot
y$. This makes the operation being performed clearer and doesn't confuse us by
referencing matrix transposes and making us remember what happens when you
multiply a row by a column.

Maybe proponents of transpose notation would argue that it conveniently allows
us to express both inner (dot) and outer products using only transposes and
matrix multiplications: $xy^T$ is the outer product of the columns $x$ and $y$.
Again, I don't see this as much of a win: it seems much clearer to me to be
explicit and just write $x \otimes y$ to make it clear that an outer product is
being performed.
