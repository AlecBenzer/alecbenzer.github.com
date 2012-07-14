---
layout: post
title: Ordinals and Cardinals
---
Let's pretend the natural numbers don't exist anymore. All we have are sets. How would we go about re-constructing our number system?

The first number we'd want to construct is probably zero. So we'll have to choose some object to be our representation of zero. In our case, we'll pick the empty set to be such a representation. This works out pretty nicely, because a set that doesn't contain anything pretty nicely encapsulates the idea of zero.

So we have this new thing 0 defined to be $ \\{\\} $. Cool. Now we need a representation of one. In the same vein, we'd want some object that encapsulates the idea of one, which would just be a set that contains a single object. What should this single object be? Well, since we just defined 0, that seems like a good choice. So one will be the set containing 0. Ie, $1 = \\{0\\} = \\{\\{\\}\\}$.

Similarlly, we'll define two to be the set containing both one and zero. Ie, $2 = \\{0,1\\} = \\{\\{\\},\\{0\\}\\} = \\{\\{\\}, \\{\\{\\}\\}\\}$.

While it's nice to think of the things we're defining as numbers, for the purpose of this post, we'll call these things **ordinals**. An ordinal's "job" is more or less to define an ordering of things (specifically, a [well-ordering](http://en.wikipedia.org/wiki/Well-order) of things). The way that we interpret the ordering that an ordinal defines is to say that, by definition, an ordrinal is a set that contains all lesser ordinals.

0, for example, does not contain anything, which means there are no ordinals less than 0. Ie -- 0 is the smallest ordinal. By putting 0 into a set and getting {0}, we've defined a new ordinal, which we decided to call 1, that is effectively defined to just be *some* ordinal that's greater than 0, precisely because it contains 0.

The set $\\{0,1\\}$, then, is yet another ordinal that's greater than both 0 and 1, which we'll call 2. Note that, by my sort of "psuedo-definition" of what an ordinal is, $\\{1\\}$ by itself would *not* be a valid ordinal. This is because an ordinal *must* contain all lesser ordinals. By puting 1 into a set, we've defined an ordinal that's greater than 1. But because 1 itself contains the ordinal 0, we have that $0 < 1$. And since orders are transitive, 0 is also less than this new ordinal we're trying to define. But uh-oh, the set $\\{1\\}$ doesn't contain 0, and is therefore not a valid ordinal.

We can continue defining ordinals in this fashion indefinitely. $\\{0,1,2\\}$ is an ordinal we'll call 3, and it defines the ordering $0 < 1 < 2$. $\\{0,1,2,3\\}$ is an ordinal we'll call 4, and it defines the ordering $0 < 1 < 2 < 3$.

We can formally describe this processing of creating new ordinals by definine a successor function that operatres on ordinals. We'll call this function $S$, and define it as $$S(a) = a \cup \\{a\\}$$ where $a$ is some ordinal.
We can see that $$S(0) = 0 \cup \\{0\\} = \\{\\} \cup \\{0\\} = \\{0\\} = 1$$ We also have $$S(1) = 1 \cup \\{1\\} = \\{0\\} \cup \\{1\\} = \\{0,1\\} = 2$$ and so on.

## Infinite Ordinals

So, these are ordinals, and they define orderings of things. So far this has not been too interesting, because it seems like "ordinal" is just kind of a fancy word for "natural number". But, check this out...

I define an ordinal as a set that contains all lesser ordinals. I never said such a set had to be finite though. So, consider the set $\\{0,1,2,3,4,5,\ldots\\}$. Ie, the set of all natural numbers. Is this set an ordinal? Sure -- it's a set that contains other ordinals that are now defined to be less than it. But what do we call this new ordinal? We don't have any names of natural numbers we can use to refer to this ordinal, because it already contains all the natrual numbers. We might feel tempted to call this ordinal "infinity", since it actually seems like it's a number that represents the idea of infinity. But instead, we'll just call this ordinal $\omega$ (omega), which is the commonly accepted name for the first infinite ordinal.

$\omega$ is a special kind of ordinal called a **limit ordinal**, specifically because we didn't get it from an application of our successor function. Ie, there is no ordinal $a$ such that $S(a) = \omega$. Any ordinal that satisifies this rule, except 0, is called a limit ordinal.

Of course, the fun doesn't stop here. We can keep using our handy dandy successor function to get even more ordinals. Consider $S(\omega)$, for example. Going back to our definition, $$S(\omega) = \omega \cup \\{\omega\\} = \\{0,1,2,3,\ldots\\} \cup \\{\omega\\} = \\{0, 1, 2, 3,\ldots, \omega\\}$$ This new ordinal is commonly referred to as $\omega+1$, partly becuase this is just a natural name for the succesor to omega, but also because we can define addition of ordinals in a way that makes this the case. But before we do that, let's look more closely at $\omega+1$.

The first thing to notice about $\omega+1$ is that it is the same size as $\omega$. I point this out to try and motivate why we're calling these things ordinals. $\omega$ and $\omega + 1$ both have the same size, but they're still different ordinals because they describe different well-orderings. $\omega$ describes the ordering $$0 < 1 < 2 < 3 < 4 < \cdots$$ while $\omega+1$ describes the ordering $$0 < 1 < 2 < 3 < 4 < \cdots < \omega$$ Just like we can think about the 4th element of an ordering, we can also think about the "$\omega$-th" element of an ordering as some kind of weird "super element" that's bigger than an infite number of elements.

To try and clarify even further, consider this special ordering of the natural numbers. Imagine that my favorite number is 7, for whatever reason, and I think that 7 is greater than all the other numbers. I could choose to order the natural numbers like this: $$0 < 1 < 2 < 3 < 4 < 5 < 6 < 8 < 9 < \cdots < 7$$ Ie, 7 is the "$\omega$-th" element of the natural numbers, given my weird ordering of them. This should further drive the point home that ordinals correspond to specific orderings, because even though this ordering has all the same elements as $\omega$, the ordinal that corresponds to this ordering is not $\omega$, but $\omega + 1$.

## Operators on Ordinals

Now let's go back to defining addition so that $\omega +1$ is actually the sum of the ordinal $\omega$ and the ordinal 1.

Given two ordinals $S$ and $T$, we'll define $S + T$ to be the well-ordering that we get from doing a "disjoint union" of the two sets, and the "concatenating" their well-orderings.

By "disjoint union" I mean we take the union of $S$ and $T$, but treat $S$ and $T$'s elements as if they're distinct. If they're not distinct, then we're just "pretending" they are, and we'll do some re-labeling. Or, if you prefer, the disjoint union of $S$ and $T$ is the normal union of $(S \times \\{0\\})$ and $(T \times \\{1\\})$.

Concatenating the well-orderings just means that we keep the well-orderings within the sets, but say that any element of $S$ is less than any element of $T$.

So, going back to $\omega+1$, we see that if $\omega = \\{0,1,2,3,4,\ldots\\}$, and $1 = \\{0\\}$, then $\omega + 1 = \\{0,1,2,3,4,5,6,\ldots,0^'\\}$ (that $0^'$ at the end is a "different" 0 than the first 0) with the well-ordering $0 < 1 < 2 < 3 < \cdots < 0^'$. If we arbitrarily decide to re-label $0^'$ as $\omega$, we see that $\omega + 1 $$ = \\{0,1,2,3,4,\ldots,\omega\\} $$ = S(\omega)$. Ie, we've shown that our definition of addition matches up with our sort of intuitive desire to label $S(\omega)$ as $\omega + 1$.


