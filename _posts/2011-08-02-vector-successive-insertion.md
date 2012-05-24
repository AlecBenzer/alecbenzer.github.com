---
layout: post
title: Vector successive insertion much faster than list
---
I always thought that because of the reallocation vectors need to do as they grow in size, successively adding elements to one would be slower than doing the same to a list. But apparently that's far from true. Successively adding elements to a vector takes much less time than doing the same to a list:

{% highlight cpp %}
//vec.cpp
#include <vector>
using namespace std;

int main()
{
  vector<int> vec;
  for(int i = 0;i < 100000000;++i)
    vec.push_back(i);
  return 0;
}
{% endhighlight %}

{% highlight cpp %}
//lst.cpp
#include <list>
using namespace std;

int main()
{
  list<int> lst;
  for(int i = 0;i < 100000000;++i)
    lst.push_back(i);
  return 0;
}
{% endhighlight %}

The list code runs in around 19 seconds. The vector code? Less than 3 seconds - over 6 times faster. I suppose that's because batch allocation of ints runs much faster than allocating linked list nodes one by one by one.

Note: of course, because we know ahead of time exactly how many elements we need, the vector code can be optimized even further to allocate the right number of elements to begin with:

{% highlight cpp %}
#include <vector>
using namespace std;

int main()
{
  vector<int> vec(100000000);
  for(int i = 0;i < vec.size();++i)
    vec[i] = i;
  return 0;
}
{% endhighlight %}

...which runs in less than 1.5 seconds.

Note: it was brought to my attention that for larger data structures (ie, things larger than ints), the vector's advantage will begin to degrade as the reallocation and copying begin to take more time.
