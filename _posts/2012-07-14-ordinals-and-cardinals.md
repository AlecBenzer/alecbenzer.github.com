---
layout: post
title: Ordinals and Cardinals
---
Let's pretend the natural numbers don't exist anymore. All we have are sets. How would we go about re-constructing our number system?

The first number we'd want to construct is probably zero. And since all we have our sets, we'll have to choose some object to be our representation of zero. And, well, since _all_ we have are sets, we actually don't really have any kinds of objecst to put into our sets (yet). So it seems natural to start out with a set that contains nothing. Thus, the empty set is our representation for zero. This works out pretty nicely, because a set that doesn't contain anything pretty nicely encapsulates the idea of what zero is. In fact, in some sense, we could essentially think of zero as just some symbol representing the number of things in the empty set, which is just what our assignment of $0 \equiv \\{\\}$ does.

So we have this new thing 0 defined to be $ \\{\\} $. Cool. Now we need a representation of one. In the same vein, we'd want some object that encapsulates the idea of one, which would just be a set that contains a single object. What should this single object be? Well, since we just defined 0, that seems like a good choice. So one will be the set containing 0. Ie, $1 \equiv \\{0\\} = \\{\\{\\}\\}$. ADD NOTE ON EQUIV VS EQUAL

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

Given two ordinals $S$ and $T$, we'll define $S + T$ to be the well-ordering that we get from doing a "disjoint union" of the two sets, and then "concatenating" their well-orderings.

By "disjoint union" I mean we take the union of $S$ and $T$, but treat $S$ and $T$'s elements as if they're distinct. If they're not distinct, then we're just "pretending" they are, and we'll do some re-labeling. Or, if you prefer, the disjoint union of $S$ and $T$ is the normal union of $(S \times \\{0\\})$ and $(T \times \\{1\\})$.

Concatenating the well-orderings just means that we keep the well-orderings within the sets, but say that any element of $S$ is less than any element of $T$.

So, going back to $\omega+1$, we see that if $\omega = \\{0,1,2,3,4,\ldots\\}$, and $1 = \\{0\\}$, then $\omega + 1 = \\{0,1,2,3,4,5,6,\ldots,0^'\\}$ (that $0^'$ at the end is a "different" 0 than the first 0) with the well-ordering $0 < 1 < 2 < 3 < \cdots < 0^'$. If we arbitrarily decide to re-label $0^'$ as $\omega$, we see that $\omega + 1 $$ = \\{0,1,2,3,4,\ldots,\omega\\} $$ = S(\omega)$. Ie, we've shown that our definition of addition matches up with our sort of intuitive desire to label $S(\omega)$ as $\omega + 1$.

There's two other interesting things to notice about our definition of addition. One is that, when we're dealing with finite ordinals, additions of ordinals corresponds with "normal" addition of numbers. This is good, because it means that ordinals so far seem to be a good extension/reconstruction of the naturals.

Another important thing to note is that addition involving infinite ordinals (and so, addition with ordinals in general), is *not* commutative, specifically because the concatenation of orderings is not commutative.

For example, consider $1 + \omega$. This is the set $\\{0^', 0, 1, 2, 3, 4, \ldots\\}$ with the ordering implied by the way I've written the set (ie, $0^' < 0 < 1 < 2 < \cdots$). If we decide to relabel $0^'$ as $0$, $0$ as $1$, $1$ as $2$, etc., we see that we end up with the ordering $0 < 1 < 2 < 3 < \cdots$. The ordinal that corresponds to this ordering is $\omega$. Thus, we see that $1 + \omega = \omega \neq \omega + 1$.

Of course, there's no reason to stop with $\omega + 1$. We could apply $S$ to $\omega+1$ to get $S(\omega+1) = \\{0,1,2,\ldots,\omega\\} \cup \\{\omega+1\\} = \\{0,1,2,\ldots,\omega,\omega+1\\}$. This new ordinal is called $\omega+2$, both because this is a natural name for it, but, perhaps more appropriately, because it is actually the ordinal we get when we add $\omega$ and $2$.

In the same fashion we can get $\omega + 3$ and $\omega + 4$, and, in general, $\omega + n$, for any finite ordinal $n$. Once we get all of these ordinals, we can actually do something interesting and put them all into a set together, just like we did with the natural numbers. Ie, we have the set $$\\{0, 1, 2, 3, \ldots, \omega, \omega + 1, \omega + 2, \omega + 3,\ldots\\}$$ This is a set that contains a bunch of lesser ordinals, just like $\omega$ was. Also just like $\omega$, this new set is our second limit ordinal. What do we call this new limit ordinal? It turns out that we'll end up calling it $\omega\cdot 2$.

There's two ways to look at this. One way is to think of $\omega\cdot 2$ as $\omega + \omega$, the sum of two infinite ordinals. Going back to our definition of ordinal addition, we see that $\omega + \omega$ would be $\\{0, 1, 2, \ldots, 0^', 1^', 2^', \ldots\\}$, with the ordering implied by the way I've written the set. If we decide to re-label $0^'$ as $\omega$, $1^'$ as $\omega + 1$, and in general, $n^'$ as $\omega + n$, we see that $\omega + \omega$ is in fact the new ordinal that we constructed above.

Perhaps more directly, we can also attempt to define multiplication of ordinals so that $\omega\cdot 2$ works out to be the new ordinal we defined above.

Given two ordinals $S$ and $T$, define $S \cdot T$ to the be the set $S \times T$ with a lexicographic ordering of the pairs in $S \times T$. Ie, if we have $(s_1, t_1)$ and $(s_2, t_2)$, we first compare $s_1$ to $s_2$ using $S$'s ordering. If $s_1 = s_2$, then we fall-back to comparing $t_1$ and $t_2$.

So, going back to $\omega\cdot 2$, we recall that $\omega = \\{0,1,2,3\ldots\\}$ and $2 = \\{0,1\\}$. $\omega\cdot 2$ is then the set $$\omega \times 2 = \\{(0,0), (1,0), (2,0), \ldots, (0,1), (1,1), (2,1), \ldots\\}$$ with the implied ordering $$(0,0) < (1,0) < (2,0) < \cdots < (0,1) < (1,1) < (2,1) < \cdots$$

If we relabel $(n,0)$ as $n$ and $(n,1)$ as $\omega + n$, we see that $\omega \cdot 2 = \omega + \omega$.

Once again, notice that multiplication of ordinals is *not* commutative, because of our lexicographic ordering that favors comparing elements from the first ordinal, and then falling back to the second ordinal. Consider $2 \cdot \omega$. This is the set $\\{(0,0), (1,0), (0, 1), (1, 1), (0,2), (1,2), (0,3), (1,3), \ldots\\}$. We see that this ordering is actually the ordering for the ordinal $\omega$, and not $\omega\cdot 2$. So, we have that $2\cdot\omega = \omega \neq \omega\cdot 2$.

We should also take note of the fact that even though we have gone to yet another limit ordinal, $\omega \cdot 2$ is actually the same size as $\omega$. To see how, we can try to order the natural numbers according to $\omega \cdot 2$. Consider the following ordering of the naturals: $$0 < 2 < 4 < 6 < 8 < \cdots < 1 < 3 < 5 < 7 < \cdots$$ Ie, we've decided that we prefer odd numbers to even numbers, and want to consider any odd number "greater than" any even number. This ordering of the natural numbers corresponds to order type $\omega\cdot 2$, since we can change all the even numbers $0, 2, 4, 6, \ldots$ to $0, 1, 2, 3, 4, \ldots$, and change all the odd numbers $1, 3, 4, 7, \ldots$ to $\omega, \omega + 1, \omega + 2, \omega + 3, \ldots$.

Now that we have $\omega \cdot 2$, we can look at $S(\omega \cdot 2) = \omega \cdot 2 + 1$ (make sure you see why this is the case -- ie, why the sum of $\omega \cdot 2$ with $1$ is the same as the successor to $\omega \cdot 2$.) We also have $\omega\cdot 2 + 2$, $\omega\cdot 2 + 3$, and so on. Then, we can collect all of those ordinal to get yet *another* limit ordinal that looks like: $$\\{0, 1, 2, \ldots, \omega, \omega + 1, \omega + 2, \ldots, \omega\cdot 2, \omega\cdot 2 + 1, \omega\cdot 2 + 2, \ldots\\}$$ Can you guess what this ordinal is called? If you guessed $\omega\cdot 3$, you'd be right! Again -- make sure you see why it's the case that the product of $\omega$ and $3$ yields the ordinal above.

We can continue in this fashion to get $\omega\cdot 4$, $\omega\cdot 5$, and $\omega\cdot n$, for any finite ordinal $n$.

And *now*, for the grand-finale, we're going to take all of these ordinals and stick them into yet *another* ordinal. Ie, we're going to consider the following ordinal:

$$\\{0, 1, 2, \ldots, \omega, \omega + 1, \omega + 2, \ldots, \omega\cdot 2, \omega\cdot 2 + 1, \omega\cdot 2 + 2, \ldots, \omega\cdot 3, \omega\cdot 3 + 1, \omega\cdot 3 + 2, \ldots \\}$$

This is the ordinal $\omega^2$. To see why, let's see what happens when we multiply $\omega$ with itself.

Going back to our definition of multiplication, $\omega\cdot\omega$ is the set $$\omega\times\omega = \\{(0,0), (0,1), (0,2), (0,3), \ldots, (1,0), (1,1), (1,2), (1,3), \ldots, (2,0), (2,1), (2,2), (2,3), \ldots \\}$$ If we replace each $(a,b)$ in $\omega\times\omega$ with $(\omega\cdot a + b)$, we'll end up with the set we had above.

However, just like with multiplication, instead of defining $\omega^2$ to be $\omega\cdot\omega$, we could also actually define the operation of exponentiation in a way such that this is so. This is, however, a bit beyond the scope of this post. If you're interested though, you can [see wikipedia's article on ordinal arithmetic](http://en.wikipedia.org/wiki/Ordinal_arithmetic#Exponentiation).

## Cardinals

We've talked a lot about ordinals, but we were mentioned that so far, all of the ordinals we've mentioned are actually countable. Even $\omega^2$ is countable, and we can order the natural numbers according to $\omega^2$.

To do this, we'll start our order with 0, 1, and then all even numbers:

$$ 0 < 1 < 2 < 4 < 6 < 8 < \cdots $$

Then, of the remaining (odd) numbers, we'll order the numbers that are multiples of three

$$ \cdots < 3 < 9 < 15 < 21 < \cdots $$

Then, of the remaning numbers, we'll order the one that are multiples of 4. Well, actually, there are none, since we exhausted all of those with the even numbers. But we can use multiples of 5:

$$ \cdots < 5 < 25 < 35 < 55 < 65 < \cdots $$

Multiples of 6 were all exhausted along with multplies of 2, but we can use multiples of 7:

$$ \cdots < 7 < 49 < 77 < \cdots $$

and so on. We can continue this pattern to create an infinite chain of sets of infinite ordinals. This type of ordering corresponds to $\omega^2$.

But that's enough talk about orderings for now. Now, we'll start talking about a different kind of object (well, sort of) called a **cardinal**. A cardinal is a number that, instead of representing a particular ordering of things, represents a particular size.

Formally, we'll define cardinals as just being those ordinals that have distinct sizes. So the first cardinal is also the first ordinal: 0. The next ordinal is 1, and since 0 and 1 are of different sizes, 1 is the next cardinal. The same goes for 2. In fact, all finite ordinals (ie, the natural numbers) are also cardinals.

Things get interesting when we get to the infinite case, though. $\omega$ is the first infinite ordinal. And, since it is larger than any of the other ordinals so far, $\omega$ is also a cardinal. However, taken as a cardinal, we don't use the name $\omega$ and instead use the name $\aleph_0$ (aleph-naught).

Once we get to $\omega+1$, however, we find that $\omega+1$ is actually the same size as $\omega$, and thus we do not get a new cardinal number from $\omega+1$. In fact, as we've already said, all of the ordinals that we've mentioned so far are in fact all the same size. So how do we get the next cardinal number?

Well, just by definition, we know the next cardinal number is going to be the first ordinal that is not countable. And so this is how the next cardinal, $\aleph_1$, is defined. If we want to be formal, let $$S = \\{\alpha \mid \alpha \mbox{ is an ordinal and } \aleph_0 < \alpha\\}$$ and then $\aleph_1$ is just the infimum of $S$.

This doesn't stop with just $\aleph_1$. In fact, for *any* finite ordinal $\alpha$, we have that $$\aleph_{\alpha} = \inf\\{\lambda \mid \lambda \mbox{ is an ordinal and } \aleph_{\alpha-1} < \lambda\\}$$

If $\lambda$ is a limit ordinal, our definition changes to $$\aleph_{\alpha} = \bigcup_{\lambda < \alpha} \aleph_{\lambda}$$
