---
layout: post
title: "Some information theory"
---
How much information have I given you if I tell you that aliens are invading the earth? What if I tell you that aliens are _not_ invading the earth? You'd probably expect the first statement to convey quite a lot of information, whereas the second doesn't really convey much information at all. Why is that?

Ultimately, this is because one of the events is much less likely to occur than the other. For this reason, formal information theory is actually based off of probability theory. Given some event $A$ that occurs with probability $\Pr(A)$, we want to define the **information content** of that event, $I(A)$.

What criteria should the information content of an event adhere to? Well, for one thing, we'd like it to be a function solely of the probability of that event occurring. That is, $$I(A) = f(\Pr(A)).$$ We'd also like information to increase the less likely an event is. Telling me that aliens aren't invading the earth doesn't convey much information because of how likely it is for aliens to not be invading the earth. So $$\Pr(A) < \Pr(B) \implies I(A) > I(B).$$ Lastly, we'd like information content to be additive. Ie, if I tell you that event $A$ has occurred, I've conveyed some information to you. I later tell you that event $B$ has occurred, and convey some more information. The total amount of information conveyed should be the same as what would be conveyed had I just said "events $A$ and $B$ have occurred" in one go. So this means we want $$I(A\mbox{ and }B) = I(A) + I(B \mid A).$$

(The event $B \mid A$ is just $B$ occuring after/given that $A$ has occured).

So to reiterate, our three rules/desired properties are

1. $I(A) = f(\Pr(A))$
2. $\Pr(A) < \Pr(B) \implies I(A) > I(B)$
3. $I(A\mbox{ and }B) = I(A) + I(B \mid A)$

If we combine rules 1 and 3, we end up with the result $$f(\Pr(A\mbox{ and }B)) = f(\Pr(A)) + f(\Pr(B \mid A)).$$ We know from Bayes' theorem that$$\Pr(A\mbox{ and }B) = \Pr(A)\cdot\Pr(B \mid A),$$ which gives us that $$f(\Pr(A)\cdot\Pr(B \mid A)) = f(\Pr(A)) + f(\Pr(B \mid A)).$$

Ie, we want $f$ to "turn products into sums". A well-known function with this property is the logarithm: $$\log(x\cdot y) = \log(x) + \log(y)$$

Thus, we might like to define $I(A) = \log(\Pr(A))$. However, this doesn't quite work because of rule 2. As $\Pr(A)$ decreases, so would $I(A)$, where we would want it to increase. To fix this we can just throw in a negative sign (or equivalently take the reciprocal of the probability)

$$ I(A) = -\log(\Pr(A)) = \log\left(\frac{1}{\Pr(A)}\right)$$

This is then our definition for the information content of a particular event.

You might have noticed that we neglected to specify a base for our logarithm. Because logarithms of all bases are just constant multiples of each other, the base of our logarithm only effects scale, so we can mostly ignore it. Most of the time, we use a base-2 logarithm, in which case the unit of $I(A)$ is **bits**. If we use a natural logarithm, the unit of $I(A)$ is called a **nat**, and if we use a base-10 logarithm, $I(A)$ is measured in **bans** or **hartleys**.

## Bits? I've heard of those

Bits, in a more general sense, are often just thought of zeros or ones. So how does this relate to the information theory definition of bit we've just introduced?

Let's say you're listening on some network channel expecting either a 0 or 1 to come, with equal probability. We'd then have that $\Pr(0) = 0.5$ and $\Pr(1) = 0.5$. So let's say you get a 0. How much information has this event conveyed? Well,
  $$ I(0) = -\log_2(\Pr(0)) = -\log_2(0.5) = \log_2(1/.5) = \log_2(2) = 1.$$
  The same would be the case for getting a 1 instead of a 0. So, receiving one "bit" on the channel corresponds to getting one information theory "bit" of information.
  
  We could also compute this in nats or bans:
  $$-\ln(0.5) = \ln(2)\approx 0.69$$
  $$-\log_{10}(0.5) =\log_{10}(2) \approx 0.30$$

  So we get that 1 bit is approximately 0.69 nats is approximately 0.30 bans.

Another way of viewing this is that getting one bit of information corresponds to reducing the possible outcomes by a factor of 2. If you were expecting 3 bits, there are $2^3 = 8$ possible outcomes. If you get the first bit and it's a 1, there are now only $2^2 = 4$ possible outcomes remaning. You've cut the realm of possibilities in two, so you've received one bit of information.

## Expected values and entropy

Given a real-valued random variable (ie, a random variable that takes values in $\mathbb{R}$), we can define an **expected value** for this random variable, which is the average value that this variable will take on.

$$ E(X) = \sum_{n} n\cdot \Pr(X = n) $$

So for the random variable above,

$$ E(X) = 0\cdot\Pr(X = 0) + 1\cdot\Pr(X = 1) + 2\cdot\Pr(X = 2) $$$$= 0\cdot0.25 + 1\cdot0.5 + 2\cdot0.25 = 0.5 + 0.5 = 1$$

Ie, on average, we'd expect to get 1 head from two fair coin tosses.

**Entropy**, written $H(X)$, is defined as the expected value of the information content of a random variable. If we have some random variable $X \colon \Omega \to V$, then
$$ H(X) = E(I(X)) = \sum_{v \in V} I(X = v)\cdot\Pr(X = v) $$$$= -\sum_{v \in V}\log(\Pr(X = v))\cdot\Pr(X = v)$$

For instance, a fair coin with $\Pr(X = \mbox{H}) = 0.5$ and $\Pr(X = \mbox{T}) = 0.5$ has entropy
$$\begin{eqnarray\*}
H(X) &=& \Pr(\mbox H)\log(\Pr(\mbox H)) + \Pr(\mbox T)\log(\Pr(\mbox T))\\\\
     &=& -0.5\log(0.5) + -0.5\log(0.5)\\\\
     &=& 0.5\log(2) + 0.5\log(2) \\\\
     &=& 0.5\cdot 1 + 0.5\cdot 1 = 1.
\end{eqnarray\*}$$
Ie, a fair coin has one bit of entropy.

On the other hand, a weighted coin with $\Pr(X = \mbox{H}) = 0.01$ and $\Pr(X = \mbox{T}) = 0.99$ has entropy
$$H(X) = -0.01\log(0.01) + -0.99\log(0.99) $$$$= 0.01\log(100) + 0.99\log(1/.99) $$$$\approx 0.01\cdot6.644 + 0.99\cdot0.014 = 0.076,$$

a much lower entropy than the fair coin. It's true that there's a chance we'll end up getting a lot of information when the coin lands heads, but most (99%) of the time the coin will be coming up tails, which is an event that carries very little (0.014 bits) of information, dragging the weighted average down. 

It's pretty easy to see (and somewhat tedious but not too difficult to prove) that the entropy of a coin toss will be maximized at 1 bit when the coin is fair, and any non-fair weighted coin will have an entropy less than 1 bit.

In fact, for any discrete random variable with $n$ potential outcomes, the entropy of that random variable will be maximized at $\log(n)$ when each of the outcomes occurs with equal probability $\frac1n$.

## Passwords & Entropy

One of the first times I heard about information theory entropy was from [this xkcd](https://xkcd.com/936/):

![xkcd 936](http://imgs.xkcd.com/comics/password_strength.png)

To quote [wikipedia](https://en.wikipedia.org/wiki/Password_strength#Entropy_as_a_measure_of_password_strength):

> It is usual in the computer industry to specify password strength in terms of information entropy.... Instead of the number of guesses needed to find the password with certainty, the base-2 logarithm of that number is given, which is the number of "entropy bits" in a password. A password with, say, 42 bits of strength calculated in this way would be as strong as a string of 42 bits chosen randomly

I thought I'd mention this, but to be honest I'm still not totally clear on what exactly is gained by expressing password strength in terms of entropy. For one thing I suppose, it makes strength easier to express. Saying a password gotten from a random sequence of 10 letters has around 47 bits of entropy is perhaps easier than saying that there are 141,167,095,653,376 possibilities for the password.

I guess it's also easier to see how modifications to the password generation change entropy. If I decide between making the letters either all capital or all lowercase, I've added one binary decision, which increases the entropy by 1 bit (to around 48). This is easier than computing whatever two times 141,167,095,653,376 is.

Entropy might also be useful in examining actual probabilities involving how people choose passwords. As the xkcd kind of indicates, just because you use a string of however many letters and numbers doesn't mean each possible sequence is equally likely. 'Tr0ub4dor&3' is a more likely password than '12@tDfuLsq'. Certain passwords being more likely would then make the entropy less than the log of the number of raw possibilities (which as we mentioned before is the maximum for any discrete random variable), and thus make the password easier to guess.

