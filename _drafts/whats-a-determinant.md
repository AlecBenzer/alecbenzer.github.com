---
layout: post
title: What’s a determinant
---
You probably learned about determinants in high school. Given a square matrix, the determinant is some number you get from that matrix.

You probably learned the formula for the determinant of a 2-by-2 matrix:

$$\det\begin{bmatrix}a & b \\\\ c & d\end{bmatrix} = \begin{vmatrix}a & b \\\\ c & d\end{vmatrix} = ad - bc $$

and how to define determinants of larger matricies in terms of it:

$$\begin{vmatrix} a & b & c \\\\ d & e & f \\\\ g & h & i \end{vmatrix} = a\begin{vmatrix}e & f \\\\ h & i\end{vmatrix} - b\begin{vmatrix}d & f \\\\ g & i\end{vmatrix} + c\begin{vmatrix}d & e \\\\ g & h\end{vmatrix}$$

But what the hell are we calculating when we do that?

## Some definitions

The set of all m-by-n matricies is usually denoted as $\mathbb{M}_{m\times n}(\mathbb{R})$ (where the $\mathbb{R}$ part means that the entries of the matrix are real numbers).

Given that, we could think of the determinant as a function that takes square matricies to real numbers:

$$ \det \colon \mathbb{M}_{n\times n}(\mathbb{R}) \to \mathbb{R} $$

But let's not do that. Instead, given a n-by-n matrix, let's interpret it as a series of column vectors:

$$ \begin{bmatrix} v_1 & v_2 & \cdots & v_n \end{bmatrix} $$

Here, each $v_i \in \mathbb{R}^n$ is an n-dimmensional vector.

For instance, the matrix 

$$ \begin{bmatrix} 3 & 1 & 4 \\\\ 1 & 5 & 9 \\\\ 2 & 6 & 5\end{bmatrix} $$

has columns

$$ v_1 = \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \end{bmatrix}, v_2 = \begin{bmatrix}1 \\\\ 5 \\\\ 6\end{bmatrix}, v_3 = \begin{bmatrix} 4 \\\\ 9 \\\\ 5\end{bmatrix} $$

Given this, we can interpret the determinant as a function that takes n vectors that are each n-dimmensional, and outputs a single real number:

$$\det \colon \left(\mathbb{R}^n\right)^n \to \mathbb{R} $$

Ie, we interpret the determinant of the above matrix as a function of its three columns:

$$ \det\begin{bmatrix} 3 & 1 & 4 \\\\ 1 & 5 & 9 \\\\ 2 & 6 & 5\end{bmatrix} = \det\left( \begin{bmatrix} 3 \\\\ 1 \\\\ 2 \end{bmatrix}, \begin{bmatrix}1 \\\\ 5 \\\\ 6\end{bmatrix}, \begin{bmatrix} 4 \\\\ 9 \\\\ 5\end{bmatrix} \right)$$

## Multilinearity

We note some (perhaps non-obvious) properties of the determinant. First is multi-linearity.

An arbitrary function $f$ is linear if we can distribute it over sums and can pull scalars out of it. Ie,

   $$ f(x + y) = f(x) + f(y) $$

   and 

   $$ f(\alpha x) = \alpha f(x) $$

where $\alpha \in \mathbb{R}$ is some real number.

A function of multiple inputs is _multilinear_ if it is linear in each of its inputs individually. For the determinant, this means:

$$
\begin{eqnarray\*}
\det\left(\ldots, v_i + v'_i, \ldots\right) &=& \det\left(\ldots,v_i,\ldots\right) + \det\left(\ldots,v'_i,\ldots\right) \\\\
  \det\left(\ldots, \alpha v_i, \ldots\right) &=& \alpha\det\left(\ldots,v_i,\ldots\right)
\end{eqnarray\*}
$$

where $i$ can be any number between 1 and n.

## Alternating

The determinant is also _alternating_. A function of multiple inputs is alternating if switching two of the inputs switches the sign of the output:

$$\det(\ldots,v_i,\ldots,v_j,\ldots) = -\det(\ldots,v_j,\ldots,v_i,\ldots)$$

An immediate result of this is that if two of the inputs to an alternating function are the same, then the the output is zero. We can prove this like so:

$$ \det(\ldots,v,\ldots,v,\ldots) = -\det(\ldots,v,\ldots,v,\ldots) $$
$$ \implies 2\det(\ldots,v,\ldots,v,\ldots) = 0 $$
$$ \implies \det(\ldots,v,\ldots,v,\ldots) = 0$$
