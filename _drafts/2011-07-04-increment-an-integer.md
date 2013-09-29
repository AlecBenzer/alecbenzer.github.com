---
layout: post
title: Increment w/o arithmetic operators
---
An interesting problem [came up on Hacker News](http://news.ycombinator.com/item?id=2721032): given an integer `n`, compute `n + 1` without using any of the basic arithmetic operators: `+`, `-`, `*`, `/`. Some interesting (and silly) solutions were given (see the link) -- I came up with this:

{% highlight cpp %}
void inc(int& n)
{
  int off = 1;    //bit offset
  while(n & off)  //while the bit at the offset is 1
  {
    n ^= off;     //flip the 1 bit to a 0
    off <<= 1;    //move the offset over
  }
  n ^= off;       //flip the first 0 bit to a 1
}
{% endhighlight %}

Uses only bitwise AND, bitwise XOR, and single left bit shifts. Seems to work for positive and negative integers.
