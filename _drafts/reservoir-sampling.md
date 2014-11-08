---
layout: post
title: "Reservoir sampling"
---

Given a pool of $n$ items, how to we choose a random sample of them of size
$k$? If the items are just sitting in a list, somewhere, it's easy: we pick
an element from the list randomly to be part of our sample, and then remove
that selected element from our list. Using a technique similar to a
[Fisher-Yates shuffle], this can be done in $O(n)$:

    for i in range(k):
      x[i] = random.choice(x[i:])
    sample = x[:k]

Okay. Let's make things harder. Say that our data is coming from a stream,
and we don't how much data there's going to be. This is a problem for
`random.choice`, which might look something like:

    def choice(x):
      return x[randint(0, len(x) - 1)]

If `x` is a stream instead of a list, then we don't know `len(x)`, the
number of elements we're sampling from.

A simple solution is to just read all of the data from our stream and use the method above. But what if there's too much data to store? What if the stream never ends, and we just always want to have a random sample of the data we've seen so far?

The answer is [Reservoir sampling]. The idea is simple: Let $n$ be the
number of items we've seen so far. For every new piece of data we get, we
increment $n$, and then decide to keep it with probability $\frac{k}{n}$. If
$n \le k$ (ie, if we don't yet have $k$ items), we store the item no matter
what. Otherwise, we decide whether or not to store it randomly. If we do
want to keep it as part of our sample, we randomly select one of the
existing $k$ items to replace with our new item.


    sample = []
    for item in x:
      if len(sample) < k:
        sample.append(x)
      else:
        keep_pr = k / n
        if random.random() < keep_pr:
          i = random.randint(0, k - 1)
          sample[i] = item

Why does this work? That is, it's pretty clear that this will result in
`sample` being a list of $k$ things chosen from our stream, but how do we
know this will be a uniform random sample?

---

Given $n$ things, how likely is it that any of them appear in a random sample of size $k$?

Well, each item could get picked as the first item in the sample. This happens with probability $\frac{1}{n}$.

Or, an item could not get picked first but get picked second. This happens with probability

$$\frac{n-1}{n} \cdot \frac{1}{n-1} = \frac{1}{n}$$

That is, there's a $1 - \frac{1}{n} = \frac{n-1}{n}$ chance we don't get chosen first, and then a $\frac{1}{n-1}$ chance we get chosen second.

The probability of being chosen third is:

$$ \frac{n-1}{n}\cdot\frac{n-2}{n-1}\cdot\frac{1}{n-2} = \frac{1}{n}$$

We have to not be chosen first or second, and then get chosen third.

Extrapolating, the chance of getting picked last is:

$$\frac{n-1}{n} \cdot \frac{n-2}{n-1}\cdot\frac{n-3}{n-2}\cdot\dots\cdot\frac{n-(k-1)}{n-(k-2)}\cdot\frac{1}{n-(k-1)} = \frac{1}{n}$$

We have to not get chosen for the first $k-1$ rounds and then get picked in the $k$th round.

So the chance of being picked at any position is always $\frac{1}{n}$. This means the probability of being in the sample at all is:

$$ \overbrace{\frac{1}{n} + \frac{1}{n} + \dots + \frac{1}{n}}^{k\text{ times}} = \frac{k}{n} $$

---

So the chance that any item gets into a true random sample is $\frac{k}{n}$. We want our sampling algorithm to gaurentee this property.

...

[Fisher-Yates shuffle]: http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle
[Reservoir sampling]: http://en.wikipedia.org/wiki/Reservoir_sampling
