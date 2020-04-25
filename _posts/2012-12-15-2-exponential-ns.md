---
layout: post
title: "2<sup>x</sup> nanoseconds ago"
...

* **2<sup>19</sup> ns ago**: One millisecond ago
* **2<sup>30</sup> ns ago**: One second ago
* **2<sup>40</sup> ns ago**: 18 minutes ago
* **2<sup>47</sup> ns ago**: Two days ago
* **2<sup>50</sup> ns ago**: Two weeks ago
* **2<sup>55</sup> ns ago**: Last year
* **2<sup>60</sup> ns ago**: Kurt Cobain was still alive
* **2<sup>64</sup> ns ago**: Leonardo da Vinci was born
* **2<sup>66</sup> ns ago**: Julius Caesar was killed
* **2<sup>72</sup> ns ago**: The last glacial period began
* **2<sup>80</sup> ns ago**: The dinosaurs went extinct
* **2<sup>87</sup> ns ago**: The earth was formed
* **2<sup>89</sup> ns ago**: The big bang

Expontentials are _big_.

---

Computers can process millions of things in what seems like an instant, so I think initially people are doubtful when you try and convey just _how_ bad exponential time algorithms are. "So there are just a lot of possibilities to check. How long could it really take for a computer to just run through them all?"

How long would it take to compute all the factors of a 100 bit number? There are only so many possibilities, right? Divide by 2, divide by 3, by 4, ... How long could it really take to check them all? 

Well, say I went back in time to the beginning of the universe, programmed a computer that checks in one nanoseconds if one integer divides another. I have 2<sup>100</sup> numbers to check. 2<sup>89</sup> nanoseconds is already the age of the universe, which means that after running for the few billion years between the beginning of the universe and now, my program would only be 2<sup>89</sup> / 2<sup>100</sup> = 0.04% done.
