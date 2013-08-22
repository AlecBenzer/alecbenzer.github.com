---
title: "Let's build a deque"
layout: post
---

A vector is common container structure used for containing an arbitrary amount
of data. Internally, a vector is just an array that gets reallocated to larger
and smaller sizes as needed.

Here's a somewhat naive vector implementation in C++:

{% highlight cpp %}
template<class T>
class Vector {
 public:
  Vector() : len_(0), cap_(1), array_(new T[cap_]) {}

  void Push(T new_element) {
    // make a bigger array
    T* new_array = new T[len_ + 1];

    // copy over the existing data
    for (int i = 0; i < len_; ++i) {
      new_array[i] = array_[i];
    }
    delete[] array_;
    array_ = new_array;

    // add the last element
    array_[len_] = new_element;
    ++len_;
  }

  void Pop() {
    // make a smaller array
    T* new_array = new T[len_ - 1];

    // copy over all but last
    for (int i = 0; i < len_ - 1; ++i) {
      new_array[i] = array_[i];
    }
    delete[] array_;
    array_ = new_array;
    --len_;
  }

  T& get(int i) {
    return array_[i];
  }

 private:
  size_t len_;
  T* array_;
};
{% endhighlight %}
