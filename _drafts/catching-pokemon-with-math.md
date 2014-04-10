---
layout: post
title: "Catching Pokemon (with math!)"
---

When I was young, a frustrating part of Pokemon was always throwing ultra ball after ultra ball at a legendary in what seemed like a hopeless attempt to catch them. Most legendaries have an immensely low chance of being caught, even after taking measures to drive their health down and get them asleep.

With math, though, our attempts can begin to seem less hopeless.

## Catch rates

The most obvious approach here would be to figure out how the game actually computes catch probabilities for pokemon. The details differ from generation to generation, but are roughly the same from gen 3 and on.

Every kind of pokemon has a base **catch rate**, which is an integer between 1 and 255, indicating how easy it is to catch (1 being the most difficult and 255 being the easiest). An early pokemon like [Wurmple](http://bulbapedia.bulbagarden.net/wiki/Wurmple_(Pok%C3%A9mon), for instance, has a catch of 255 (meaning nothing is easier to catch), while later pokemon like [Wailmer](http://bulbapedia.bulbagarden.net/wiki/Wailmer) have a catch rate of 125, and a rarer still pokemon like [Relicanth](http://bulbapedia.bulbagarden.net/wiki/Relicanth_(Pok%C3%A9mon) has a catch rate of 25. Legendaries have even lower catch rates: [Kyogre's](http://bulbapedia.bulbagarden.net/wiki/Kyogre) is 5 and [Rayquaza's](http://bulbapedia.bulbagarden.net/wiki/Rayquaza) is 3.

When actually throwing a poke ball at a pokemon, a **modified catch rate** is computed, which is effected by the specifics of the situtation.

How much health the pokemon has effects the catch rate linearly: if the pokemon is at full health, the catch rate is divided by 3, whereas at "0" health (if a pokemon could have 0 health and still be alive), it would be unaffected. So basically we multiply by a factor of $(1 - \frac23h)$, where $h$ is the pokemon's health percentage.

Statuses effect the catch rate as well: if the pokemon is asleep, the catch rate is doubled, and if it has some other status (paralyzed, burned, etc.), the catch rate is multiplied by $1.5$.

Lastly, the kind of ball you use also effects the catch rate. Basic pokeballs do not modify the rate at all, while using an ultra ball will double it.

So ultimately we get a formula that looks like this for computing the modified catch rate:

$$ a = \left(1 - \frac23h\right)\cdot b \cdot s \cdot r $$

where $h$ is the pokemon's health percentage, $b$ is the ball bonus (ie, $b = 2$ for an ultra ball), $s$ is the status bonus (ie, $s = 1.5$ for paralysis), and $r$ is the pokemon's base catch rate.

## Shakes

Once we have the modified catch rate $a$, we can compute the **shake probability**, which is the probability of an individual shake of the poke ball succeeding (with four successful shakes being neccesary to catch the pokemon).

Modified catch rates in the range $[1,255]$ are mapped to probabilities in the range $[0,1]$ by an appropriately scaled fourth-root curve. So we have

$$ p = \sqrt[4]{\frac{a}{255}} $$

Although a modified catch rate of $a = 0$ would lead to $p = 0$, modified catch rates won't go below $1$, which means in practice the lowest possible $p$ is $\sqrt[4]{1\mathbin/255} \approx 25.02\%$.

Once $p$ is computed, all the game does is perform 4 shake checks in order, each with probability $p$ of succeeding. If any of them fail, the pokemon is released, and the pokemon is only captured when all four checks pass.

Now this somewhat mysterious fourth-root seems to make some more sense. The probability we care more about is the probability of actually catching the pokemon (all four shakes passing), and this is $$p^4 = \left(\sqrt[4]{\frac{a}{255}}\right)^4 = \frac{a}{255}$$

## How many tosses?

Ok, so this is all nice, but what we really care about is how many tosses we're going to need to catch the pokemon.

One thing we could do is compute the expected number of tosses need to catch a pokemon. Given that each toss works with probability $\frac{a}{255}$, it's relatively simple to see with some basic probability theory that the expected number of tosses is $\frac{255}{a}$ (this is just the intuitive result that if something happens with a 1 in 20 chance, the expected number of tries is 20).

So, say we're trying to catch a paralyzed Kyogre who's basically at 0 health with ultra balls. Our modified catch rate is $a = 1.5 \cdot 2 \cdot 5 = 15$, which means the expected number of tosses is $\frac{255}{15} = 17$.

But how useful is this number, really? Even if it's more likely to take 17 tosses than any other number of tosses, how likely is it to catch Kyogre within 17 tosses? How likely is it that we'll actually need more tosses?

Well, the probability that we take more than 17 tosses is just the probability that we fail the first 17 times, which is just $\left(1 - \frac{15}{255}\right)^{17} \approx 35.7\%$ (or $\left(1 - \frac{a}{255}\right)^{255/a}$ for an arbitrary catch rate.)

So there's actually a pretty non-negligble chance that we'll need more than 17 tosses to catch Kyogre. Perhaps a more useful number would be the _maximum_ number of tosses you'd need to guarentee catching Kyogre. But of course, since probability is involved, we can never be 100% sure that we'll catch Kyogre with finitely many tosses. But maybe we can be 90% sure. Or 95%, or even 99% sure.

Put another way, for some probability $\epsilon$, we can compute the number of tosses $k$ that we need so that the odds of us _not_ catching Kyogre is less than $\epsilon$.

To do this we just solve $\left(1-\frac{15}{255}\right)^k = \epsilon$ and round up. We get

$$\log\left(\left(1 - \frac{15}{255}\right)^k\right) = \log(\epsilon) $$
$$\implies k\log\left(1 - \frac{15}{255}\right) = \log(\epsilon)$$
$$\implies k = \frac{\log(\epsilon)}{\log\left(1 - \frac{15}{255}\right)}$$

So for $\epsilon = 0.1$, we get $k = \frac{\log(0.1)}{\log\left(1 - \frac{15}{255}\right)} \approx 37.98$, which rounds up to 38. So the odds of needing more than 38 tosses is 10%, meaning we're 90% sure that we'll get Kyogre in 38 tosses or less.

For $\epsilon = 0.01$, we get $k = \frac{\log(0.01)}{\log\left(1 - \frac{15}{255}\right)} \approx 75.96$, so the odds of needing more than 76 tosses is less than 1%.

## Using a MLE

Let's go back to the shakes for a bit.

If the probability of catching a pokemon is actually just $a \mathbin/ 255$, why bother with all this shake check stuff? Presumably its to make catch attempts more interesting and to keep the player awake.

The modified catch rate for a "0 health" Rayquaza that's asleep trying to be caught with an ultra ball is $2 \cdot 2 \cdot 3 = 12$, meaning we've got $p \approx 4.7\%$. If it weren't for shakes, there'd be a $95.3\%$ chance of the user just seeing "Rayquaza wasn't caught" when throwing a ball, which could get old fast. With shakes, we now have at least a $46.6\%$ chance of one shake passing, meaning _something_ will happen roughly half the time.

What's interesting though is that we can actually _recover_ information about the pokemon's catch rate based on the number of shakes we're getting.
