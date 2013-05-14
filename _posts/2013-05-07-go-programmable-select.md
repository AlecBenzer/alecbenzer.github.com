---
layout: post
title: Go 1.1's "programmable selects"
---

In a [post from a few days ago](/blog/two-goroutines-one-channel) we used go's `sync.WaitGroup` structure to facilitate reading from multiple goroutines until they were done producing data. Here, we'll look at how we can also achieve this with go 1.1's new "programmable" select statements.

Go has a cool built-in `select` statement that lets you try and read from multiple channels, potentially blocking until at least one of them is available. So, if you have a worker function:

{% highlight go %}
func worker(n int, ch chan int) {
  count := rand.Intn(5) + 3
  x := n
  for i := 0; i < count; i++ {
    ch <- x
    x *= n
  }
  close(ch)
}
{% endhighlight %}

and launch a few goroutines running it:

{% highlight go %}
ch1 := make(chan int)
ch2 := make(chan int)

go worker(2, ch1)
go worker(3, ch2)
{% endhighlight %}

we can use a select put into a for loop to read from these two channels:

{% highlight go %}
num_done := 0
for num_done < 2 {
  select {
  case x, ok := <-ch1:
    if ok {
      fmt.Println("From 2:", x)
    } else {
      num_done++
    }
  case x, ok := <-ch2:
    if ok {
      fmt.Println("From 3:", x)
    } else {
      num_done++
    }
  }
}
{% endhighlight %}

{% highlight text %}
$ go run select.go
From 2: 2
From 3: 3
From 2: 4
From 3: 9
From 3: 27
From 2: 8
From 3: 81
From 2: 16
From 3: 243
{% endhighlight %}

As an aside, the reason we would do this with multiple channels (as opposed to just one) is because now our workers are free to `close()` their channels when they're done with them, whereas otherwise, we'd need some other mechanism for figuring out when we're done reading (as explained in [that last post](/blog/two-goroutines-one-channel))

## N worker goroutines

The problem with this solution is that it doesn't really generalize to an arbitrary number of workers. Because of the nature of the `select` statement, we're stuck having to hard-code all the channels we're trying to read from. This is where the "programmable" selects from go 1.1's reflect package comes in.

So let's say that now we have an arbitrary number of channels/workers:

{% highlight go %}
chs := make([]chan int, N)
for i := 0; i < N; i++ {
  chs[i] = make(chan int)
  go worker(2 + i, chs[i])
}
{% endhighlight %}

We now need to construct a slice of `relect.SelectCase` objects, each of which represents one case in our programmable select:


{% highlight go %}
selectCases := make([]reflect.SelectCase, N)
for i := 0; i < N; i++ {
  selectCases[i].Dir = reflect.SelectRecv
  selectCases[i].Chan = reflect.ValueOf(chs[i])
}
{% endhighlight %}

`Dir` is set to `SelectRecv` for each case because we're receiving from a channel in each case of our select. `Chan` is just the channel we intend to receive from, but because we're dealing with the reflect package (and because the channels can potentially have different types, even though ours don't), we need to pass a `reflect.Value` representing the channel (as opposed to the channel itself), which is achieved via `reflect.ValueOf`.

Now, we can enter our loop and actually execute the select:


{% highlight go %}
numDone := 0
for numDone < N {
  chosen, recv, recvOk := reflect.Select(selectCases)
  if recvOk {
    fmt.Printf("From %d: %d\n", 2 + chosen, recv.Int())
  } else {
    numDone++
  }
}
{% endhighlight %}

This is pretty straight-forward. `chosen` is the index in our `selectCases` array of the case that was triggered, `recv` is the value we read from the channel (though its type is once again `reflect.Value`, and we need to use the `.Int()` method to actually extract the int data), and `recvOk` is a bool telling us if the channel is closed.

And that's it! Here's the code: [http://play.golang.org/p/ByUVTPAGBJ](http://play.golang.org/p/ByUVTPAGBJ)
