---
layout: post
title: "A chat server in Go with AJAX long-polling"
---

If your web browser supports WebSockets, that's a very nice way of setting up a chat server where you can listen for incoming messages. In the absense of WebSockets, though, one "hack" that's sometimes employed is to use AJAX "long-polling".

Long-polling works like this: when a client wants to receive a message, they send an AJAX request to the server. The server then holds onto this request until it has something it wants to say to the client, at which point it responsds to the request. The client will receive the response, do something with whatever it got back from the server, and then (if it wants to remain "subscribed" to the server) send off a _second_ AJAX request. And so on.

It's easy to run into some problems with this, though, especially if your messages are frequent and you don't want clients to miss any of them. In particular, it's reasonable to expect some amount of lag between the time the server responds to a particular long-polling request and when a client sends another one back to the server. So we could get a sequence of events like this:

1. Alice sends the server an AJAX request.
2. New message `"Hello, world!"` comes in to the server.
3. Server responds to Alice's AJAX request with `"Hello, world!"`
4. _Before Alice is able to send off another request_, a second message comes into the server: `"Salve, munde!"`
5. Because the server currently has no AJAX request from Alice, it drops the message.
6. Bob now gets around to sending her 2nd AJAX request to the server.
7. Bob missed the `"Salve, munde!"` message :(

To solve this we introduce some form of client identification. Ie, first, Alice registers with the server and gets some id, which she'll include in all of her long-polling requests. The server will then keep some list of all ids it's seen in the past X minutes. When it gets a new message, but has no corresponding long-polling request from Alice, it will hold onto it for Y seconds, waiting for a new long-polling request.

## Generating IDs

So the first thing we should do is figure out how we'll be generating and assigning ids. Using the natural numbers on a first-come-first-serve basis should be fine. Ie, something like this

{% highlight go %}
var nextId = 1

func getId() int {
  id := nextId
  nextId++
  return id
}
{% endhighlight %}

Except this is bad because we'd expect our server to be concurrent, and so this reading and incrementing of global `nextId` is non-atmoic. The boring way to solve this is with a mutex:

{% highlight go %}
import "sync"

var nextId = 1
var nextIdLock sync.Mutex

func getId() int {
  nextIdLock.Lock()
  defer nextIdLock.UnLock()  // will be called when the function exits

  id := nextId
  nextId++
  return id
}
{% endhighlight %}

But this is go, and in go we like channels:

{% highlight go %}
idGenerator := make(chan int)
go func() {
  for i := 1; ; i++ {
    idGenerator <- i
  }
}()

// use <-idGenerator to get an id
{% endhighlight go %}

See [play.golang.org/p/LlkGHkIS-1](http://play.golang.org/p/LlkGHkIS-1).

## Serve the ids

Now that we can generate ids we need a way of actually serving them via http. Go's `net/http` package makes this easy:

{% highlight go %}
package main

import (
  "fmt"
  "net/http"
)

func main() {
  // idGenerator code from above

  http.HandleFunc("/register", func(w http.ResponseWriter, r *http.Request) {
    fmt.Fprint(w, <-idGenerator)
  })

  http.ListenAndServe(":8080", nil)
}
{% endhighlight %}

This will start a local http server on port 8080 listening for requests at /register.

Of course, part of the point was for us to keep track of the ids that we've given out. We could keep them in a slice:

{% highlight go %}
ids := make([]int, 0)
http.HandleFunc("/register", func(w http.ResponseWriter, r *http.Request) {
  id := <-idGenerator
  ids = append(ids, id)
  fmt.Fprint(w, id)
})
{% endhighlight %}

Except once again this can cause thread-unsafe access to `ids`. So, again, we use a channel instead

{% highlight go %}
newId := make(chan int)

http.HandleFunc("/register", func(w http.ResponseWriter, r *http.Request) {
  id := <-idGenerator
  newId <- id
  fmt.Fprint(w, id)
})

go func() {
  ids := make([]int, 0)
  for {
    ids = append(ids, <-newId)
  }
}()
{% endhighlight %}

Now the `ids` slice is local to a go-routine that just runs in a for loop waiting on new ids to come in on the `newId` channel.

Let's add a debugging `Println` and try out the server.

{% highlight go %}
go func() {
  ids := make([]int, 0)
  for {
    ids = append(ids, <-newId)
    fmt.Println(ids)
  }
}()
{% endhighlight %}

[Here's a play.golang.org link](http://play.golang.org/p/e07yvwW97J) with the code, but you'll have to run it locally to test out the web server.

{% highlight shell %}
$ go run server.go
[1]
[1 2]
[1 2 3]
[1 2 3 4]
[1 2 3 4 5]
[1 2 3 4 5 6]
^C
{% endhighlight %}

while running `curl localhost:8080/register` in a different shell (or just viewing the page in a web browser)

## Listener channels

Just keeping a list of ids is okay, but really we want some way to comunicate "with" the different ids. For that we should use channels. So we replace our `ids` slice with `listeners`, a map from ids to channels, and when we receive a new id on `newId`, we create a corresponding channel

{% highlight go %}
go func() {
  listeners := make(map[int]chan string)
  for {
    listeners[<-newId] := make(chan string)
  }
}()
{% endhighlight %}
