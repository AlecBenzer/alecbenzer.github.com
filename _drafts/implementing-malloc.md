---
layout: post
title: Implementing malloc
---

Any C programmer will likely know `malloc` as the function that gets them heap memory to use. But actually, getting heap memory is rather easy: programs on UNIX-like machines have a data segment, which represents memory the program owns.

When a program starts running, the data segment is generally filled only with things like string literals which exist only once throughout the entirety of the program. But the data segment can grow (and shrink) as the program needs more memory.

On UNIX-like systems, you can increase the size of the data segment by `n` bytes by calling `sbrk(n)`, which then returns a `void*` pointing the beginning of your new `n` bytes.

## A stupid malloc implementation

So what, is `malloc` just a wrapper around `sbrk` (and an equivelant function on non-UNIX systems)?

{% highlight c %}
void* malloc(size_t n) {
  return sbrk(n);
}
{% endhighlight %}

Well, technically a "malloc library" also has an associated `free` function, but we can just ignore that:


{% highlight c %}
void free(void* ptr) {}
{% endhighlight %}

Well as it turns out this is actually a "valid" `malloc` implementation, in that it will work "correctly". Just not efficiently.

Consider this code:

{% highlight c %}
int i;
for (i = 0; i < 1000000000; ++i) {
  char* str = malloc(10 * sizeof(char));
  // do stuff with str
  free(str);
}
{% endhighlight %}

This snippet only ever requires 10 bytes of memory on the heap. But, with our stupid malloc implementation above, it will use around 10 _gigabytes_ of memory. Which could exhaust your system's resources, or at the very least just piss off the user who might be trying to run other programs at the same time as yours.

## "But this is a stupid example!"

Well, ok, yeah, it is. Since we know we'll only ever need `str` in the body of the loop we could just use a stack variable instead:

{% highlight c %}
int i;
for (i = 0; i < 1000000000; ++i) {
  char str[10];
  // do stuff with str
}
{% endhighlight %}

Or even just have one instance of `str` outside the loop:

{% highlight c %}
char str[10];

int i;
for (i = 0; i < 1000000000; ++i) {
  // do stuff with str
}
{% endhighlight %}

Which would be a good way of writing that program given that we know exactly how our program will use memory at compile-time. But sometimes we don't know when we'll be done with memory until run-time:

{% highlight c %}
typedef struct {
  int id;
  char* name;
  int age;
} record_t;

...

int next_id = 0;

while (1) {
  switch(getchar()) {
  case 'c':  // user wants to create a new record
    record_t* record = malloc(sizeof(record));
    record->id = ++next_id;
    register_record(record, id);
    printf("Created new record with id: %d\n", record->id);
    break;

  case 'd':  // user wants to delete an existing record
    int id;
    scanf("%d", &id);
    free(retrieve_record(id))
    break;

  // other operations
  }
}
{% endhighlight %}

Here we're implementing a kind of in-memory database where the user tells us when to create new records and when to delete them. We can't predict our memory usage patterns at compile-time.

This is still sort of a toy example, but you can imagine other, more "real-world" programs with memory usage patterns that aren't known at compile-time.

## A non-empty free

Obviously, the existence of the `free` function implies that we should actuallly be doing something in it. But what?

When the `free(ptr)` is called, the caller is indicating that they no longer care about or need the data stored at `ptr` that they had initially allocated with `malloc`. Rather than ignoring this information, we should take advantage of it and attempt to re-use this unneeded memory later.

{% highlight c %}
void* last_used = NULL;

void* malloc(size_t n) {
  if (last_used == NULL) {
    return sbrk(n);
  } else {
    return last_used;
  }
}

void free(void* ptr) {
  last_used = ptr;
}
{% endhighlight %}

This new malloc makes our previous toy program use the desired 10 bytes of memory instead of 10 gigabytes. But except for this one specific example, this malloc is still pretty bad.

One issue with this implementation is that if we ever call `free` twice without a `malloc` in between, we'll lose track of some memory we could potentially re-use.

But this implementation actually has a more serious problem. Consider this program:

{% highlight c %}
int i;
for (i = 0; i < 1000000000; ++i) {
  size_t length = (rand() % 10) + 1;
  char* str = malloc(length * sizeof(char));
  // do stuff with str and length
  free(str);
}
{% endhighlight %}

Suppose for the first iteration of our loop we get `length == 4`, and for the second iteration we get `length == 8`. In this case, our malloc implementation will return the previously allocated 4 bytes, but we need 8 bytes.

Clearly, the issue here is that when `free(ptr)` is called, we need to record not only that we can re-use `ptr`, but also what `ptr`'s size is.

## A non-trivial free

One way to fix this (and our other issue of being able to store more than one free pointer) is with free-lists. Basically, when we free a pointer `ptr` of size `n`, we add it to a list of records that contains both the pointer and its size.

But in order to do this, we need to somehow be able to infer the size of the pointer `ptr`, since `free` is not explicitly passed a size.

We can do this by storing a little bit of meta-data when we `sbrk` memory. Instead of doing `sbrk(n)`, we can do `sbrk(sizeof(size_t) + n)`, and use the first `sizeof(size_t)` bytes to store the amount of memory requsted:

{% highlight c %}
void* malloc(size_t n) {
  // if there are no free pointers available
  void* ptr = sbrk(sizeof(size_t) + n);
  *(size_t*)ptr = n;
  return ptr + sizeof(size_t);
}
{% endhighlight %}

Then, we can extract this information when `free` is called:

{% highlight c %}
void free(void* ptr) {
  size_t n = *(size_t*)(ptr - sizeof(size_t));
  // add (ptr,n) to our records
}
{% endhighlight %}

But how do we add `(ptr,n)` to our records?
