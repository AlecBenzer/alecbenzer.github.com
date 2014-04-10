---
layout: post
title: "Spell checking with tries in C++: Part 1"
---

[Tries](http://en.wikipedia.org/wiki/Trie) are a really cool data structure used for storing strings (and potentially other things) efficiently and compactly. They can have speed and space advantages over trees for and hash tables when used as associative arrays, but the linked nature of tries lets you do other cool things with them. As an example, let's write a spell-checker in C++.

A trie (<i>technically</i> pronounced "tree", but commonly "try") is basically just a special kind tree. Generally speaking, each node in the trie can have any number of children, but for our purposes, we'll say that each node has 26 slots for children, one for each letter of the alphabet.

Each node in the trie represents some string. Starting from the root of the tree, any path to any other node will go over edges labeled by letters of the alphabet. The sequence of letters you pass through to get to the node in question tell you what string is associated with that node. For example, starting from the root, if you take a 'c' edge, then an 'a' edge, and then a 't' edge, the node you end up at represents the string "cat".

Each node also has a `final` property, intended to indicate whether we want to actually count that word as part of the trie. For example, in the "cat" trie above, "c" and "ca" are also strings stored by the trie. If we want to make it so that only "cat" (and not "ca" or "c") should be considered part of our trie, we'll set the "cat" node be final, and set the "c" and "ca" nodes to not final.

From this description, searching for a string in a trie is easy. If we have a particular string, all we need to do is follow the edges in the trie that correspond to the letters of the string. If we end up at a final node, the string is stored by the trie. If the node we get to is not final, or if we hit a null node along the way, then the string isn't stored by the trie.

## Coding the trie

So fire up your text editor and get coding. The first thing we'll need is a `Node` class (which will end up being embedded in the `trie` class). The skeleton for the `Node` class looks like this:

{% highlight cpp %}
struct Node
{
  Node* children[26];
  bool final;
};
{% endhighlight %}

Simple enough. We have our 26 children and our final property. Now we just initialize stuff with a constructor:

{% highlight cpp %}
Node() : final(false)
{
  for(int i = 0;i < 26;++i)
    children[i] = 0; //ie, NULL
}
{% endhighlight %}

We also need a destructor for memory cleanup (technically we'd also want a copy constructor, but we'll be careful about not passing tries by value)

{% highlight cpp %}
~Node()
{
  for(int i = 0;i < 26;++i)
    if(children[i]) delete children[i];
}
{% endhighlight %}

We'll also make a method that makes accessing the `children` array easier:

{% highlight cpp %}
Node*& child(char c)
{
  return children[tolower(c)-'a'];
}
{% endhighlight %}

This method converts all characters to lowercase (using the `tolower` function found in `cctype`) so we don't need to worry about the case of the strings we index/search. Note that it also returns a reference, so we can modify the contents of `children` via this method (which is what we want, `child` is just a convenience access method).

Now, onto the class for the trie itself:

{% highlight cpp %}
class Trie
{
  public:
    struct Node
    {
      //...
    };

    Trie()
    {
      root = new Node;
    }

    ~Trie()
    {
      delete root;
    }

    void add(string word)
    {
      //...
    }

    void search(string word)
    {
      //...
    }

  private:
    Node* root;
};
{% endhighlight %}

We have just one instance variable: a pointer to the root node of the trie. The constructor allocates memory for the root and the destructor deals with clearing it. The interesting stuff is in `add` and `search`.

`add` takes a string and iterates over its characters, adding new nodes along the way if it needs to, and setting the node it ends up at to final.

{% highlight cpp %}
void add(string word)
{
  Node* curr = root;
  for(int i = 0;i < word.length();++i)
  {
    char& c = word[i];
    if(!isalpha(c)) continue;
    if(!curr->child(c))
      curr->child(c) = new Node;
    curr = curr->child(c);
  }
  curr->final = true;
}
{% endhighlight %}

`search` looks almost identical. We still iterate over the string, except now we just fail if we see a missing node, and, if that never happens, we check to see if the node we end up at is final.

{% highlight cpp %}
bool search(string word)
{
  Node* curr = root;
  for(int i = 0;i < word.size();++i)
  {
    char& c = word[i];
    if(!isalpha(c)) continue;
    if(!curr->child(c)) return false;
    curr = curr->child(c);
  }
  return curr->final;
}
{% endhighlight %}

And that's it. Here's the whole `Trie` class:


{% highlight cpp %}
class Trie
{
  public:
    struct Node
    {
      Node() : final(false)
      {
        for(int i = 0;i < 26;++i)
          children[i] = 0;
      }

      ~Node()
      {
        for(int i = 0;i < 26;++i)
          if(children[i]) delete children[i];
      }

      Node*& child(char c)
      {
        return children[tolower(c)-'a'];
      }

      Node* children[26];
      bool final;
    };

    Trie()
    {
      root = new Node;
    }

    ~Trie()
    {
      delete root;
    }

    void add(string word)
    {
      Node* curr = root;
      for(int i = 0;i < word.length();++i)
      {
        char& c = word[i];
        if(!isalpha(c)) continue;
        if(!curr->child(c))
          curr->child(c) = new Node;
        curr = curr->child(c);
      }
      curr->final = true;
    }

    bool search(string word)
    {
      Node* curr = root;
      for(int i = 0;i < word.size();++i)
      {
        char& c = word[i];
        if(!isalpha(c)) continue;
        if(!curr->child(c)) return false;
        curr = curr->child(c);
      }
      return curr->final;
    }
  private:
    Node* root;
};
{% endhighlight %}

## A little command line interface

Now all that's left to do is throw up a simple little interface to our program. We'll have a simple command line interface with two commands: `add <word>`, and `search <word>`.

{% highlight cpp %}
int main()
{
  Trie trie;
  string tmp;

  for(;;) //loop fo-evah (or until Ctrl+C)
  {
    cout << "> ";
    cin >> tmp;
    if(tmp == "add")
    {
      cin >> tmp;
      trie.add(tmp);
      cout << "added \"" << tmp << "\"";
    }
    else if(tmp == "search")
    {
      cin >> tmp;
      cout << trie.search(tmp);
    }
    else
      cerr << "unrecognized command";
    cout << endl;
  }
}
{% endhighlight %}

And that's that. Compile your code (`g++ -o spell-check main.cpp` should work on UNIX) and fire her up.

{% highlight text %}
$ ./spell-check 
> search bob
0
> add bob
added "bob"
> search bob
1
> add jacob
added "jacob"
> search jacob
1
> search jaco
0
> search jacobb
0
{% endhighlight %}

## Pre-filling the trie with a dictionary

Being able to index our own words is pretty cool, but really, we'd like to have our trie pre-packaged with words from a dictionary. Luckily, most UNIX systems have a dictionary file available that makes this really easy. For me, the file is `/usr/share/dict/words`. All you have to do is open that file with an `ifstream` and add all the words in it to our trie before we enter the command-line loop.

{% highlight cpp %}
cout << "indexing dictionary...";
ifstream dict("/usr/share/dict/words");
while(!dict.eof())
{
  dict >> tmp;
  trie.add(tmp);
}
cout << " done" << endl;
{% endhighlight %}

And now just re-compile and run:

{% highlight text %}
$ ./spell-check 
indexing dictionary... done
> search apple
1
> search hello
1
> search helo
0
> search helloo
0
{% endhighlight %}

Of course, we can still index our own words if we want:

{% highlight text %}
search helloo
0
> add helloo
added "helloo"
> search helloo
1
{% endhighlight %}

Now we have our little spell-checker. Well, sort of. _Technically_ what we've made is a spell-checker: it checks to see if you've spelled things right. What we really want though, is something that can recognize when we've spelled something wrong and also give us suggested corrections. This is when our trie will start becoming useful (after all, we could have done all this with a hash-table or other associative array as well, although our trie is most likely slightly more efficient).

I'll put out a part 2 soon, where I'll cover actually generating the suggestions. For your reference, here's [the code so far, in its entirety](https://gist.github.com/2504661).
