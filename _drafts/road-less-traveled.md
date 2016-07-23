---
layout: post
title: 'How much less traveled is the less traveled road?'
---

A [_Quanta Magazine_ puzzle](https://www.quantamagazine.org/20150903-the-road-less-traveled/), courtesy of [r/math](https://www.reddit.com/r/math/comments/3jmm80/can_you_solve_this_puzzle_the_road_less_traveled/):

Say you have 200 cars going from point A to point B. Each car may take one of
two roads to get there: call them roads 1 and 2. Suppose that each car flips a
fair coin to decide which road to take: road 1 for heads, road 2 for tails.
_How many more cars there be on the busier road, on average?_

The question may sound kind of odd at first. "What do you mean, 'the
busier road'? Both roads are just as likely to be chosen, so they should be
just as busy."

On _average_, yes, this is true. But for any given instance of this experiment,
it's unlikely that the cars will be divided between the two roads perfectly
evenly. To be precise, the odds of the 200 cars splitting into exactly 100 cars
for road 1 and 100 for road 2 is about 5%. The other 95% of the time, one of
the roads will have more cars than the other.

The odds of a 101-99 split, for example, is also about 5%. The odds of a 99-101
split are the same. So there's about a 10% chance that the busier road will
have 2 more cars than the less busy road. A 110-90 split and a 90-110 split
each have about a 2% chance, so there's a 4% chance that the busier road will
lead by 20 cars.

On the other hand, a 120-80 or 80-120 split will happen less than 0.1% of the
time, and the odds continue to decrease drastically for more and more extreme
splits.

## How do we compute these odds?

Suppose $X$ is the number of cars that take road 1 in our experiment. Then $X$
has a [binomial
distribution](https://en.wikipedia.org/wiki/Binomial_distribution) $X \sim
B\left(200,\frac{1}{2}\right)$: $X$ is the number of success out of 200 trials,
where each trial has probability $\frac{1}{2}$ of succeeding.

We then know that, for any value $k$, $\Pr(X = k) =
\binom{n}{k}\frac{1}{2^{200}}$. So a 101-99 split, for instance, happens with
probability $\binom{200}{101}\frac{1}{2^{200}}$, which, if we plug in to
[wolfram](http://www.wolframalpha.com/input/?i=choose%28200%2C+101%29+*+1%2F2%5E200),
we see is about 5.6%.

## Okay, so what's the answer?

If $X = k$, then this means road 1 got $k$ cars, and road 2 got the other
$200-k$ cars. This means that the absolute difference in the numbers of cars is
$\left\|(200 - k) - k\right\| = \left\|200-2k\right\|$. We already know the
probability of $X$ landing on any particular value of $k$, so we can compute the expectation like so:

$$\sum_{k=0}^{200}\left|200-2k\right|\Pr\left(X = k\right) = \sum_{k=0}^{200}\left|200-2k\right|\binom{200}{k}\frac{1}{2^{200}}$$

To get around the absolute value signs, we can take advantage of the symmetry of absolute values and binomials:

$$ \sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor} 2\left(200-2k\right)\binom{n}{k}\frac{1}{2^n} = \frac{1}{2^{n-1}}\sum_{k=0}^{\left\lfloor \frac{n}{2} \right\rfloor}\left(200-2k\right)\binom{n}{k}$$
