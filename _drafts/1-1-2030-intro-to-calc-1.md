---
layout: 'post'
title: 'An Introduction to Calculus: Part 1'
---

This is the first of a (hopefully) series of articles introducing calculus.

The best definition of calculus I've heard is the one given to me by my calc III professor:

> Calculus is about approximating curvy things with straight things.

Or, thought of in another way, calculus is about _defining_ curvy things by approximations based on their more straight alternatives. For example, everyone knows how to measure the length of a stright line with a ruler. Something more difficult, though, is measuring the length of some curving line with a ruler. One way you could approximate this is to use ruler to get an approximate measurement for a segment of the curving line that's more or less straight, and then repeat this for the whole curve. Obviously there will be some error involved with this, but you can get better and better approximations by breaking the curvy line up into smaller and smaller "stright-ish" segments.

Mathematically speaking, we can actually go ahead and _define_ the length of a curve by the _limit_ of a sequence of better and better approximations. All that's sort of hand-wavy right now, but this will hopefully give some intuition about the "spirit" of calculus.

## Average rates of change

To start really getting into formal calculus, we'll look at the average rate of change of a function.

For example, when I first moved in to my dorm, I drove a distance of 835 miles in about 13 hours. We could have some function, $f(t)$, that represents how far I had driven after $t$ hours of driving.

$f(0)$ would be equal to $0$, obviously, because having driven for no time at all, I obviously wouldn't have gone anywhere. We also have that $f(13) = 835$, because after driving for all 13 hours, I would have gotten to my destination, 835 miles away.

I might be wondering how fast I was going during this trip, on average. Well, to get a rough average for my speed during the whole trip, I could calculuate how far I traveled, and divide it by the amount of time I spent traveling. Ie, I'd compute

$$ \frac{f(13) - f(0)}{13 - 0} = \frac{835 - 0}{13 - 0} = \frac{835}{13} \approx 64.23$$

So my average speed of the trip was about 64 miles per hour.

This speed, however, might not be too indicative of my speed at any particular time during the trip. Having just pulled out of my driveway, going around residential streets, my speed would be much lower than 64 miles per hour, and on the highways, I might be going at around 70 or 80 miles per hour. So basicaly, while my average speed is easy to compute, it doesn't really give a good picture of my speed at any point during the trip.

Something we could try instead is to calculuat my average rate of change during various legs of the trip.
