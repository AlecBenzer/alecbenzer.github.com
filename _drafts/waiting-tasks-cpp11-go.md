---
layout: post
title: "Waiting on tasks in C++11 vs Go"
---

We have a slow operation:

{% highlight cpp %}
int slowOp(int n) {
  this_thread::sleep_for(chrono::seconds(1));
  return n * n;
}
{% endhighlight %}

and we want run it a bunch of times:

{% highlight cpp %}
for (int i = 0; i < N; ++i) {
  printf("%d\n", slow_op(i));
}
{% endhighlight %}

This takes N seconds to run. Which is silly -- we should be able to start _all_
of the operations at once and then get their results.

C++11 has `std::async` which we can use for that:

{% highlight cpp %}
vector<future<int>> futures;
for (int i = 0; i < N; ++i) {
  futures.push_back(async(slowOp, i, launch::async));
}

for (auto& future : futures) {
  printf("%d\n", future.get());
}
{% endhighlight %}

`std::async` (when started with a launch policy of `std::launch::async`, as
    above), will start a new thread running `slowOp`, and returns an
`std::future` which will contain the result.

This code should take just about 1 second to run, as all the threads are run in
parallel.

## Variable running time

Maybe the slow operation doesn't take _exactly_ one second:

{% highlight cpp %}
int slowOp(int n) {
  this_thread::sleep_for(chrono::seconds(rand() % 10 + 1));
  return n * n;
}
{% endhighlight %}

The total time taken by the code above is still okay, but we're now waiting too
long to return results. `slowOp(1)` might have finished in one second, but if
`slowOp(0)` is taking ten seconds to finish, we're waiting on that first, and
only later seeing if `slowOp(1)` had finished yet.

Or, perhaps we're only interested in one, or a few of the answers, but not all of
them. Maybe we're actually running this code multiple times with the same input,
  just so we can grab the one that returns most quickly:

{% highlight cpp %}
for (int i = 0; i < N; ++i) {
  // *one* of these should finish relatively quickly
  futures.push_back(async(slowOp, 5, launch::async);
}
{% endhighlight %}
