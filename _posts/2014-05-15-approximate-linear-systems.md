---
layout: 'post'
title: 'Approximating solutions to linear systems'
---

Given an $n\times n$ matrix $A \in \mathbb{R}^{n\times n}$ and a vector $b \in \mathbb{R}^n$, we can find a solution to the linear system $Ax = b$ via [Guassian elimination][gaussian]. But for a general matrix $A$, Guassian elimination can take $O(n^3)$ time. Can we do better?

There are various iterative methods for approximating solutions to $Ax = b$. Typically such methods work by choosing some guess $x_0 \approx x$, and then using some formula to obtain $x\_{k+1} = f(x_k)$, where $x_{k+1}$ serves as a better guess for the true solution $x$. The method then hinges on finding a suitable $f$.

At any point, the error of current guess is $e_k = x_k - x$. If we knew what $e_k$ was, then we could actually obtain an exact solution by applying the update rule

$$x_{k+1} = x_k - e_k = x_k - (x_k - x) = x$$

Of course, as we don't know $x$, we can't compute $e_k = x_k - x$ directly. However, we do know how to compute the [residual][residual] $r_k = Ax_k - b$. If in addition we were to know what $A^{-1}$ was, we could compute

$$A^{-1}r_k = A^{-1}\left(Ax_k - b\right) = A^{-1}\left(Ax_k - Ax\right)$$

$$= A^{-1}A(x_k-x) = x_k - x = e_k$$

And then an update rule of $x\_{k+1} = x_k + A^{-1}r_k$ would give us an exact solution after a single iteration. However, computing $A^{-1}$ directly requires [roughly $O(n^3)$][matrixinv] time -- just as much as Gaussian elimination!

So the idea behind approximate iterative methods is to approximate the error $e_k$ by approximating $A \approx Q$ in a way such that $Q^{-1}$ is easy to compute, and then getting $e_k \approx Q^{-1}r_k$.

# Jacobi method

For what kind of matricies $Q$ is $Q^{-1}$ easy to compute? One example is a diagonal matrix: for a diagonal matrix

$$D = \begin{bmatrix}
d_{1,1} & 0 & \cdots & 0 \\
0 & d_{2,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & d_{n,n}
\end{bmatrix}$$

we have

$$D^{-1} = \begin{bmatrix}
1 \mathbin/ d_{1,1} & 0 & \cdots & 0 \\
0 & 1 \mathbin/ d_{2,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & 1 \mathbin/ d_{n,n}
\end{bmatrix}$$

which can be computed in $O(n)$.

So we can somewhat crudely approximate $A$ by taking just the entries on its diagonal:

$$Q = \begin{bmatrix}
a_{1,1} & 0 & \cdots & 0 \\
0 & a_{2,2} & \cdots & 0 \\
\vdots & \vdots & \ddots & \vdots \\
0 & 0 & \cdots & a_{n,n}
\end{bmatrix}$$

Now we can (efficiently) approximate our error as $e_k \approx Q^{-1}r_k$, and our update rule becomes $x_{k+1} = x_k - Q^{-1}r_k$. This is the [Jacobi method][jacobi].

Here it is implemented as a python generator:


    def jacobi(A, b):
        n = A.shape[0]
        assert A.shape == (n, n)
        assert b.shape == (n,)

        # a random initial guess
        x = np.random.rand(n)

        Qinv = np.diag(1 / np.diag(A))
        while True:
            r = A.dot(x) - b
            err = Qinv.dot(r)
            x -= err
            yield x

## Analysis

Let's try and analyze how well the Jacobi method will converge. Recall that $e_k = x_k - x$, and so obviously we also have $e\_{k+1} = x\_{k+1} - x$. Substituting in our update rule, we see that

$$e_{k+1} = \left(x_k - Q^{-1}r_k\right) - x = (x_k - x) - Q^{-1}\left(Ax_k - b\right)$$

$$ = (x_k - x) - Q^{-1}\left(Ax_k - Ax\right) = (x_k - x) - Q^{-1}A(x_k - x)$$

$$ = (I - Q^{-1}A)(x_k - x) = (I-Q^{-1}A)e_k$$

So essentially we have that

$$e_{k+1} = \left(I - Q^{-1}A\right)e_k$$

which is equivelant to saying

$$e_k = \left(I - Q^{-1}A\right)^k e_0$$

The error after $k$ iterations of Jacobi is the matrix $(I - Q^{-1}A)^k$ applied to the error $e_0$ of our initial guess $x_0$.

Remember, $x$ and $x_k$ are vectors, so our errors $e_k = x_k - x$ are also vectors. A more illustrative quantity to look at might be the norm of the error:

$$\|e_k\| = \left\|(I - Q^{-1}A)^ke_0\right\| = \left\|(I - Q^{-1}A)^k\right\|\|e_0\|$$

where $\\|\cdot\\|$ applied to a matrix denotes a [matrix norm][matrixnorm].

Now we employ the [spectral radius theorem][specradthm], which tells us that for a matrix $M$, $\\|M^k\\| \sim \rho(M)^k$ as $k \to \infty$, where $\rho(M)$ is $M$'s spectral radius: the absolute value of $M$'s largest eigenvalue.

This tells us that $\\|e_k\\| \sim \rho\left(I - Q^{-1}A\right)^k \\|e_0\\|$ as $k\to\infty$. This means that if $\rho\left(I - Q^{-1}A\right)^k < 1$, that $\\|e_k\\| \sim 0$ as $k \to \infty$, which tells us that $x_k \sim x$ as $k \to \infty$.

In other words, for matricies $A$ such that $\rho\left(I - Q^{-1}A\right)$ is less than one, the Jacobi method will converge to the true solution $x$. If $\rho\left(I - Q^{-1}A\right) \ge 1$, then we have no guarentees.

It turns out (for reasons I won't go into here) that a matrix $M$ will satisfy $\rho\left(M\right) < 1$ if the sum of the elements in each row of $M$ is less than one. This will occur for $M = I - Q^{-1}A$ when $A$ is [diagonally dominant][diagdom] (you should be able to work out why based on the definition of $Q$).

## Performance

We can implement a version of the Jacobi method that takes a tolerance parameter $t$ and stops iterating once our estimate for the error becomes small enough: $\\|Q^{-1}r_n\\| < t$.

    def jacobi(A, b, tol=1e-10):
        n = A.shape[0]
        assert A.shape == (n, n)
        assert b.shape == (n,)

        # a random initial guess
        x = np.random.rand(n)

        Qinv = np.diag(1 / np.diag(A))
        while True:
            r = A.dot(x) - b
            err = Qinv.dot(r)
            if np.linalg.norm(err) < tol:
                return x
            x -= err

To ensure that Jacobi will eventually concern, we can test it only on matricies that are constructed to be diagonally dominant:

    def random_diagonally_dominant(n):
        'Returns a random (n, n) np.array guaranteed to be diagonally dominant'
        D = np.diag(np.random.uniform(n, 2 * n, size=n))
        return D + np.random.rand(n, n)

Let's compare `jacobi`'s performance to `np.linalg.solve`'s:


    jacobi_times = []
    solve_times = []
    ns = np.floor(np.logspace(0, 3, num=100))
    for n in ns:
        A = random_diagonally_dominant(n)
        b = np.random.rand(n)

        start = time.time()
        x = jacobi(A, b)
        end = time.time()
        jacobi_times.append(1000 * (end - start))

        start = time.time()
        x_actual = np.linalg.solve(A, b)
        end = time.time()
        solve_times.append(1000 * (end - start))

    plt.xlabel('n')
    plt.ylabel('milliseconds')
    plt.plot(ns, jacobi_times, label='jacobi',)
    plt.plot(ns, solve_times, label='np.linalg.solve')
    plt.legend()
    plt.savefig('fig.png')

![graph](/images/approx-linsystem-1.png)

We see that starting at around $n = 300$ Jacobi starts to gain an advantage over `np.linalg.solve` and continues to become much faster as $n$ grows larger, getting to about 8 times faster at $n = 1000$.

Of course, this test isn't completely fair, as we are purposefully only generating matricies we know Jacobi can solve. In general, `np.linalg.solve` will guarentee a solution, whereas Jacobi can simply diverge. But, in cases where we know that $A$ is diagonally dominant, Jacobi offers an efficient way to solve $Ax = b$.


[gaussian]: http://en.wikipedia.org/wiki/Gaussian_elimination
[residual]: http://en.wikipedia.org/wiki/Residual_(numerical_analysis)
[matrixinv]: http://en.wikipedia.org/wiki/Computational_complexity_of_mathematical_operations#Matrix_algebra
[jacobi]: http://en.wikipedia.org/wiki/Jacobi_method
[matrixnorm]: http://en.wikipedia.org/wiki/Matrix_norm
[specradthm]: http://en.wikipedia.org/wiki/Spectral_radius#Theorem_.28Gelfand.27s_formula.2C_1941.29
[diagdom]: http://en.wikipedia.org/wiki/Diagonally_dominant_matrix
