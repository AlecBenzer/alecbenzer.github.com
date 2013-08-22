---
layout: post
title: "Spell checking with tries... in Go! (part 1)"
---

A while ago I wrote the [first part of an article on how to write a spell-checker in C++](/blog/spell-checking-part-1/). I meant to write a follow-up but I got lazy/forgot and it just sat their for a while.

Anyway, in the interest of making myself interested enough to write the second part, I've decided to re-write the first part in [go](http://golang.org/). I'm not going to repeat the explanation of tries and why were using them, so for that refer back to the [first part](blog/spell-checking-part-1/). So we'll jump right into the code.

The first thing we want to do is create a struct for our trie's nodes. To make things a little simpler (and to show off's go's map built-in), we'll use a map from go's character type, `rune`, to pointers to our nodes (instead of just having an array of node pointers):

    type Node struct {
      children map[rune]*Node
      final bool
    }

go's garbage collection and smart initialization saves us the C++ code we'd need to initialize the map's entries to NULL and to free the map's entries in a destructor. We do, however, need to initialize the map itself with `make`, which we'll do in a "constructor", which is realy just a function that for our purposes will act like a constructor

    func newNode() *Node {
      n := new(Node)
      n.children = make(map[rune]*Node)
      n.final = false
      return n
    }

`newNode` is just a function that allocates a Node, initializes its children map, makes it non-final by default, and returns a pointer to it. TODO: do something like `return &Node{children: make(map[rune]*Node), final: false}`

That's all we need for our Node class (well, struct). Now we move on to the struct for trie:

    type Trie struct {
      root *Node
    }

Pretty simple. A neat thing about go is that unlike in C++, where this would be the definition for a trie struct _before_ we add our methods, this is actually the complete definition for our trie. In go, method definitions and struct definitions are done totally seperately. This is pretty nice, because notice how in the last post I gave you a big skeleton for the class because I wanted to define the data first and then define the methods one by one. In go, the syntax matches up with this data first, methods later way of thinking.

So now, on to the methods for our trie. Our "constructor" just initializes the root node:

    func newTrie() *Trie {
      t := new(Trie)
      t.root = newNode()
      return t
    }

Now we move on to the guts of the trie, starting with the `add` method:

    func (t *Trie) add(word string) {
      curr := t.root
      for i := 0; i < word.size(); i += 1 {
        c := word[i]
        if !isAlpha(c) {
          continue
        }
        if curr.children[c] == nil {
          curr.children[c] = newNode
        }
        curr = cur.children[c]
      }
      curr.final = true
    }
