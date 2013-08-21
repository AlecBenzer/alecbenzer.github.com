---
layout: post
title: "Traversal Reconstruction"
---

Does a traversal of a binary tree encapsulate all of the information the tree
represents? A traversal contains all of the data that the nodes of the tree
collectively represent, but a tree is more than just the data inside of it. A
tree relates the data by saying that this piece of data is the left-child of
this one, and this piece of data is the parent of that one, etc. Does a
traversal capture this information?

Consider an in-order traversal of a tree:

    A, B, C

There are several different trees that could have produced this traversal. Like
this one: 

<img src="tree1.svg"></img>

Or this one:

<img src="tree2.svg"></img>

Or this one:

<img src="tree3.svg"></img>

Clearly the in-order traversal `A, B, C` does not encapsulate the all of the
information in a tree, exactly because there are different trees we could
generate from it.

Would be a pre-order any better?  Not really.  Consider the pre-order traversal
`D, E, F`.  The tree could still be any of these:

<img src="tree4.svg"></img>

<img src="tree5.svg"></img>

<img src="tree6.svg"></img>

## Try more traversals?

So a single traversal doesn't give us all of the information we want from a
tree. What if we used two traversals instead? For example, let's try using the
pre-order traversal `A, B, C`, and the in-order traversal `B, C, A`, and see how
many trees these two traversals could describe when taken together.

Luckily, it turns out that the _only_ tree that could produce the above
pre-order and in-order traversals is this one:

<div id="tree7" class="tree"></div>

So this result suggests that it might be possible to reconstruct a tree given its in-order traversal and pre-order traversal. To do this, let's analyze what information we can extract from an in-order and a pre-order traversal.

Let's say that some node `M` comes before some other node `N` in a pre-order traversal of a tree. A pre-order traversal generally looks something like this:

    pre_order(node):
      print(node)

      pre_order(node.left_child)
      pre_order(node.right_child)

