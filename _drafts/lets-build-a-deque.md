---
title: "Let's build a deque"
layout: post
---

A vector is common container structure used for containing an arbitrary amount
of data. Internally, a vector is just an array that gets reallocated to larger
and smaller sizes as needed.

Here's a somewhat naive approach to writing a vector in C++:

{% highlight cpp %}
template<class T>
class Vector {
 public:
  Vector() : len_(0), cap_(1), array_(new T[cap_]) {}

  void Push(T new_element) {
    if (len_ + 1 == cap_) {
      ++cap_;
      T* new_array = new T[cap_];
      for (int i = 0; i < len_; ++i) {
        new_array[i] = array_[i];
      }
      delete[] array_;
      array_ = new_array;
    }

    array_[++len_] = new_element;
  }

 private:
  size_t len_;
  size_t cap_;
  T* array_;
};
{% endhighlight %}
