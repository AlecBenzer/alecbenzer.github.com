---
layout: post
title: "Bessel's correction"
---

When computing the variance of a sample of data points $x_1,\dots,x_n$ with
mean $\bar{x}$, instead of computing

$$ \frac{\sum(x_i - \bar{x})^2}{n} $$

which is essentially the definition of variance, we use

$$\frac{\sum(x_i - \bar{x})^2}{n-1}$$

This dividing by $n-1$ instead of $n$ is called [Bessel's correction]. Why do
we do this?

---

Suppose we have a _population_ of data points that are distributed in a
particular way. We want to know what the mean $\mu$ and variance $\sigma^2$ of
this population are. But we can't observe the population directly, we can only
take samples and then study said samples.

So if we sample points $x_1,\dots,x_n$ from this population, what can we say
about the population's mean and variance? If we compute the sample mean as

$$ \bar{x} = \frac{\sum_{i=1}^n x_i}{n} $$

then it turns out that $\bar{x}$ is a _good estimator_ for $\mu$, the
population's average. What we mean by this is that expected value of $\bar{x}$
over _all samples we could have drawn_ is the population mean $\mu$.

In other words, instead of just taking one sample of data, imagine taking two samples: $x_1,\dots,x_n$ and $y_1,\dots,y_n$. Then we'd have two sample means: $\bar{x}$ and $\bar{y}$. Or, assume we have $m$ samples: $x\_{1,1}, x\_{1,2}, \dots, x\_{1,n}$, $x\_{2,1}, x\_{2,2}, \dots, x\_{2,n}$, all the way to $x\_{m,1}, x\_{m,2}, \dots, x\_{m,n}$. Then we'd get $m$ sample means: $\bar{x_1}, \dots, \bar{x_m}$. The idea is that all these sample means should be hovering around the true sample mean $\mu$, and that the average of these means should tend toward $\mu$:

$$ \frac{\bar{x_1} + \dots + \bar{x_m}}{m} \sim \mu $$

Being even more formal, if the set of all possible samples of size $n$ is $\mathcal{X}_n$, then what we're saying is that:

$$E_{x \in \mathcal{X}_n}[\bar{x}] = \mu $$

(We're using $x \in \mathcal{X}_n$ as shorthand for $x_1,\dots,x_n \in \mathcal{X}_n$.)

We can prove this, relying principally on the [linearity of expectation]:

$$E_{x \in \mathcal{X}_n}[\bar{x}] = E_{x}\left[\frac{x_1 + \dots + x_n}{n}\right] = \frac{E_{x}[x_1] + \dots + E_{x}[x_n]}{n}$$

$$ = \frac{\overbrace{\mu + \dots + \mu}^{n\text{ times}}}{n} = \mu$$

The point of all this is basically that $\bar{x}$ for a sample gives us a good
estimate of the population mean $\mu$. Now, how do we estimate the population's
variance, $\sigma^2$? We might say that we want to compute:

$$ \frac{\sum_{i=1}^n \left(x_i - \mu\right)^2}{n} $$

But we can't compute that, because we don't know what $\mu$ is. We just know
$\bar{x}$, which approximates $\mu$. So maybe we can try:

$$ \frac{\sum_{i=1}^n \left(x_i - \bar{x}\right)^2}{n} $$

If we call this value $b^2$, then what we want is for $E\_{x \in
\mathcal{X}\_n}\left[b^2\right] = \sigma^2$: we want $b^2$ to be an estimator for the
population variance $\sigma^2$. Well, let's compute $E_{x\in\mathcal{X}_n}[b^2]$:

$$E_{x\in\mathcal{X}_n}\left[b^2\right] = E\left[\frac{\sum_{i=1}^n \left(x_i - \bar{x}\right)^2}{n}\right] = \frac{\sum_{i=1}^n E\left[\left(x_i-\bar{x}\right)^2\right]}{n} $$

[Bessel's correction]: https://en.wikipedia.org/wiki/Bessel%27s_correction
[linearity of expectation]: https://en.wikipedia.org/wiki/Expected_value#Linearity
