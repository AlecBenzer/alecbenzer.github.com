---
layout: post
title: "The Curse of Dimensionality"
---

The ["curse of dimensionality"][curse-wiki] is the informal idea that problems
become much harder as the dimensions of the problem increase. A little more
specifically, it's the idea that intuitions we have about things in low
dimensions do not carry over well to higher dimensions.

The different manifestations of the curse are all fairly connected. A simple
observation that explains a lot of the curse is that as dimension increases,
the volume of a $d$-dimensional unit [hypercube] becomes increasingly
concentrated at the edges of the cube.

Specifically, if we consider the region of hypercube that's within 5% of the cube's boundaries:

$$ B_d = \left\{(x_1,\dots,x_d) \mid 0 \le x_j \le 0.05 \text{ or } 0.95 \le x_j \le 1, \text{ for some }j\right\}$$

then this "boundary region" $B_d$ accounts for an exponentially larger fraction of the cube's overall volume as $d$ increases.

To see why, note that the part of the hypercube _outside_ of $B_d$ is the set

$$ \left\{(x_1,\dots,x_d) \mid 0.05 < x_j < 0.95 \text{ for all }j\right\}$$

which is a $d$-dimensional hypercube with side length $0.95 - 0.05 = 0.9$. Thus, it has volume $0.9^d$. Accordingly, $B_d$'s volume is $1 - 0.9^d$.

At $d = 1, 2, 3$ the volume of $B_d$ is $0.1, 0.19, 0.271$ respectively. At $d
= 10$, $B\_{10} \approx 0.65$, and $B\_{50} \approx 0.995$. So 99.5% of the
volume of a 50-dimensional hypercube is concentrated with 5% of the cube's
boundaries, leaving just 0.05% of the cube's volume in the middle.

An analogous situation comes up with [hyperspheres][hypersphere]. Given a $d$-dimensional hypersphere, what percent of its volume is within 5% of the sphere's boundary?

...


[curse-wiki]: https://en.wikipedia.org/wiki/Curse_of_dimensionality
[hypercube]: https://en.wikipedia.org/wiki/Hypercube
[hypersphere]: https://en.wikipedia.org/wiki/Hypersphere
