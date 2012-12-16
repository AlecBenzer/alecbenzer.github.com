---
layout: post
title: "Exponentials are really big"
---

How long ago is 2<sup>x</sup> nanoseconds? (The fun things I think about when I should be studying).

2<sup>19</sup> nanoseconds ago is a little under a millisecond ago.

2<sup>30</sup> nanoseconds ago is a little over a second ago.

2<sup>40</sup> nanoseconds ago is about 18 minutes ago.

2<sup>47</sup> nanoseconds ago it was two days ago.

2<sup>55</sup> nanoseconds ago it was last year.

Kurt Cobain was still alive 2<sup>60</sup> nanoseconds ago.

Leonardo da Vinci was born a little over 2<sup>64</sup> nanoseconds ago.

Julius Caesar was killed about 2<sup>66</sup> nanoseconds ago.

The last glacial period began about 2<sup>72</sup> nanoseconds ago.

The dinosaurs went extinct around 2<sup>80</sup> nanoseconds ago.

The earth was formed around 2<sup>87</sup> nanoseconds ago.

And, finally, the universe began around 2<sup>89</sup> nanoseconds ago.


## That's pretty long

Modern laptops can process millions of things in what seems like an instant, so I think a lot of people are doubtful when you try and convey just _how_ bad exponential time algorithms are. "So there are just a lot of possibilities to check. How long could it really take for a computer to just run through them?"

Consider integer-factoring: given an n-bit integer, compute its prime factorization (or just compute all of its factors). Suppose n = 100. I can generate two random 50 bit numbers x and y and multiply them together to get a 100 bit number z = x\*y in virtually no time. How long would it take you to get a list of possible values for (x,y), if you're only given z?

There are only so many combinations, right? z/1, z/2, z/3, ..., z/(z-2), z/(z-1). How long could it really take to check them all? Well, if I went back in time to the beginning of the universe, built a computer that could check if z divides a particular number in one nanosecond, and started it off, I'd have 2<sup>100</sup> numbers to check. 2<sup>89</sup> nanoseconds is already the age of the universe, which means that after running for the few billion years between the beginning of the universe and now, my program would only be 2<sup>89</sup>/2<sup>100</sup> = 0.04% done.
