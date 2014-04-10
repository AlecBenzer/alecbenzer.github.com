---
layout: post
title: "Two Goroutines, One Channel"
---

I was bored during a lecture today and I wanted to play around with [go](http://golang.org) a bit. So, having been a while since I did anything with go's concurrency stuff, I threw together something really simple using goroutines and channels for communication:

{% highlight go %}
func main() {
  const N = 20

  ch := make(chan int)

  go func() {
    for i := 0; i < N; i++ {
      ch <- i + 1
    }
    close(ch)
  }()
  
  for i := range ch {
    fmt.Print(i, " ")
  }
  fmt.Println()
}
{% endhighlight %}

This spawns a single goroutine that counts from 1 to N, sending each number onto a channel, and then closes that channel. The main function then reads each of the numbers with the `range` construct, which reads values from a channel until it's closed.

{% highlight text %}
$ go run main.go
1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 
{% endhighlight %}

Cool-beans. Except this isn't all that special since the code still runs more-or-less sequentially. When a goroutine sends a number on the channel, the program waits until the main function tries to read a value from that channel. We can fix this a bit by giving the channel buffer

{% highlight go %}
ch := make(chan int, 5)
{% endhighlight %}

Now when the goroutine tries to send to the channel, the send will succeed as long as there's an empty spot in the channel's buffer. So our goroutine can go on generating numbers, even if main can't keep up.

But we can get some nicer concurrency if we have _multiple_ worker goroutines all generating numbers

{% highlight go %}
const N = 20
const WORK_PER_THREAD = 10

ch := make(chan int)

for i := 0; i < N; i += WORK_PER_THREAD {
  go func(start int) {
    for i := start; i < start + WORK_PER_THREAD; i++ {
      ch <- i + 1
    }
    close(ch)
  }(i)
}
{% endhighlight %}

{% highlight text %}
$ go run count.go
1 2 11 3 12 4 13 5 14 6 15 7 16 8 17 9 18 10 panic: runtime error: send on closed channel
{% endhighlight %}

Oops. We `close(ch)` at the end each of the goroutine, but a different goroutine might still need to use it.

{% highlight go %}
for i := 0; i < N; i += WORK_PER_THREAD {
  go func(start int) {
    for i := start; i < start + WORK_PER_THREAD; i++ {
      ch <- i + 1
    }
  }(i)
}

for i := range ch {
  fmt.Print(i, " ")
}
fmt.Println()
{% endhighlight %}

{% highlight text %}
$ go run count.go
1 2 11 3 12 4 13 5 14 6 15 7 16 8 17 9 18 10 19 20 throw: all goroutines are asleep - deadlock!
{% endhighlight %}

Uh... okay. So we can't close the channel at the end of the goroutines because we need it to stay open for the other goroutines, but we also can't just not close it ever if we want to use `range`. So what do we do?

## Let's not use range?

Instead of using `range` to read from our channel, we can do it manually with `<-ch`, and rely on some other mechanism for knowing when to stop.

We could make a `done` channel:

{% highlight go %}
done := make(chan bool)
{% endhighlight %}

and have each goroutine signal on `done` when it finishes

{% highlight go %}
for i := 0; i < N; i += WORK_PER_THREAD {
  go func(start int) {
    for i := start; i < start + WORK_PER_THREAD; i++ {
      ch <- i + 1
    }
    done <- true
  }(i)
}
{% endhighlight %}

and in main, we keep track of how many times we've been signaled on `done`

{% highlight go %}
numDone := 0
for numDone < N / WORK_PER_THREAD {
  select {
  case i := <-ch:
    fmt.Print(i, " ")
  case <-done:
    numDone++
  }
}
{% endhighlight %}

We're using `select` here to listen on multiple channels and wait until one of them responds.

## Something better?

This works, but it's a little messy. I figured there should probably be a better way of doing this.

So I asked on [Stack Overflow](http://stackoverflow.com/questions/16020406/better-go-idiomatic-way-of-writing-this-code).

A cleaner solution involves using `sync.WaitGroup`. A `WaitGroup` is basically a semaphore that we can increment by N with `Add(N)` and decrement by 1 with `Done()`. We can also wait for the count to go back to 0 with `Wait()`.

So we declare a `WaitGroup`:

{% highlight go %}
var wg sync.WaitGroup
{% endhighlight %}

increment it when we create a new goroutine and decrement it when we finish one

{% highlight go %}
for i := 0; i < N; i += WORK_PER_THREAD {
  wg.Add(1)
  go func(start int) {
    for i := start; i < start+WORK_PER_THREAD; i++ {
      ch <- i + 1
    }
    wg.Done()
  }(i)
}
{% endhighlight %}

The kind of tricky part that wasn't clear to me at first is this: now, we launch yet another goroutine that waits until all the worker goroutines are done, and then closes the channel

{% highlight go %}
go func() {
  wg.Wait()
  close(ch)
}()
{% endhighlight %}

Since we're closing the channel again, we can go back to our good old `range` loop

{% highlight go %}
for i := range ch {
  fmt.Print(i, " ")
}
{% endhighlight %}

and that's it. Here's the code in its entirety: [http://play.golang.org/p/tFM-OoG6f2](http://play.golang.org/p/tFM-OoG6f2).
