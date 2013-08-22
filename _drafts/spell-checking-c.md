---
layout: post
title: "Spell checking with tries in C"
---

A while ago I wrote [the first part of a post](/spell-checking-part-1) about writing a spell checker, but it was so long ago that instead of just writing a part 2 like I intended I kind of just want to start over and do the whole thing in one go.

I've been helping some ECE friends with C recently, so I'm in more of a C kind of mood than usual, and I'm going to try and implement this in pure C this time.

## Tries

So to recap the theoretical basis of all of this and the data structure we're going to be building, we're going to be using a [trie](http://en.wikipedia.org/wiki/Trie) to store a dictionary of words that are considered valid, and then use this trie to do word look-ups.

A trie is a special kind of tree intended for storing strings, where each node represents some prefix of a string (or a whole string). Each node also has edges going down labeled with letters from our alphabet, and the node you get to by following one of those edges represents a new string that you get by concatenating the letter on that edge with whatever other string you had so far.

<img src="http://upload.wikimedia.org/wikipedia/commons/b/be/Trie_example.svg"></img>

So basically, to query a trie with a particular string, we start at the trie's root node, and then follow an edge down corresponding to each letter of our string (assuming it's present).

You might notice that a trie like this would implicitly store all prefixes of a string you tried to put into it, in addition to the string itself (ie, there's no way to store "inn" without also storing "i" and "in"). To fix this, we give each node a "valid flag", that indicates whether this node represents a string that _should_ actually be in the trie, or if it's just the prefix of some other string.

Something useful about tries is that it's not only easy to do look-ups, but also easy to search "around" a string that we tried to query for. Ie, if we searched for the string "tdm", we wouldn't find it in the above trie. But at the junction where we tried to follow a 'd' label and found nothing, we could instead choose to follow the 'e' label, assuming we typed a 'd' instead of an 'e' by accident.

This lookup flexibility is what will make tries very useful in generating spelling corrections (although tries are still pretty useful as plain-old dictionaries).


## Coding the trie

So let's get started actually implementing our trie. The first thing we'll want to do is have a struct for the trie's nodes:

{% highlight c %}
typedef struct node {
  int valid;
  struct node* child[26];
} node;

node* create_node() {
  node* n = malloc(sizeof(node));
  n->valid = 0;
  int i;
  for (i = 0; i < 26; ++i) {
    n->child[i] = NULL;
  }
  return n;
}
{% endhighlight %}

The `valid` int will be non-zero if and only if this node should represent an actual string in our trie, and isn't just there as a prefix. The 26 element `child` array will contain pointers to the current node's children. Ie, `child[0]` will be the child you get to following an `A`-edge, `child[1]` will be the child you get to following a 'B'-edge, etc.

our `create_node` function just allocates space for a node, sets its valid flag to zero, and sets all of its child pointers to null;

next, we need functions for inserting strings into our trie and querying our trie for membership (querying for spelling corrections will come later)

{% highlight c %}
void insert_string(node* trie, const char* str) {
  int i;
  for (i = 0; str[i] != '\0'; ++i) {
    int j = tolower((int)str[i]) - (int)'a';
    if (trie->child[j] == NULL) {
      trie->child[j] = create_node();
    }
    trie = trie->child[j];
  }

  trie->valid = 1;
}
{% endhighlight %}

This function takes a pointer to the root node of a trie and a c-string. It then walks down the string until it gets to the end (until `str[i]` is `'\0'`) while simultaneously walking down the trie, creating new nodes where it needs to. At the end, we make sure to set the last node we touched to valid.

{% highlight c %}
int find_string(node* trie, const char* str) {
  int i;
  for (i = 0; str[i] != '\0'; ++i) {
    int j = tolower((int)str[i]) - (int)'a';
    if (trie->child[j] == NULL) {
      return 0;
    }
    trie = trie->child[j];
  }

  return trie->valid;
}
{% endhighlight %}

The search functions is almost identical. It walks down the string and trie simultaneously like before, only now, if we encounter a node that isn't present, we just immediately return zero. Ir we manage to get to the end of the trie, we just return the valid status of the node we ended up at.

And that's pretty much all we need for our trie.

## Throwing up a little CLI

So now we'll just throw up a little command line interface so we can interact with the trie:

{% highlight c %}
char cmd[100];
char word[100];

while (1) {
  printf("> ");
  scanf("%s %s", cmd, word);
  if (strcmp(cmd, "insert") == 0) {
    insert_string(trie, word);
    printf("inserted '%s'\n", word);
  } else if (strcmp(cmd, "find") == 0) {
      printf("%d\n", find_string(trie, word));
  } else {
    printf("command '%s' not recognized\n", cmd);
  }
}
{% endhighlight %}

And that's pretty much it. This is all of the code so far (along with the header files we need):

{% highlight c %}
#include <ctype.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct node {
  int valid;
  struct node* child[26];
} node;

node* create_node() {
  node* n = malloc(sizeof(node));
  n->valid = 0;
  int i;
  for (i = 0; i < 26; ++i) {
    n->child[i] = NULL;
  }
  return n;
}

void insert_string(node* trie, const char* str) {
  int i;
  for (i = 0; str[i] != '\0'; ++i) {
    int j = tolower((int)str[i]) - (int)'a';
    if (trie->child[j] == NULL) {
      trie->child[j] = create_node();
    }
    trie = trie->child[j];
  }

  trie->valid = 1;
}

int find_string(node* trie, const char* str) {
  int i;
  for (i = 0; str[i] != '\0'; ++i) {
    int j = tolower((int)str[i]) - (int)'a';
    if (trie->child[j] == NULL) {
      return 0;
    }
    trie = trie->child[j];
  }

  return trie->valid;
}

int main() {
  node* trie = create_node();

  char cmd[100];
  char word[100];

  while (1) {
    printf("> ");
    scanf("%s %s", cmd, word);
    if (strcmp(cmd, "insert") == 0) {
      insert_string(trie, word);
      printf("inserted '%s'\n", word);
    } else if (strcmp(cmd, "find") == 0) {
      printf("%d\n", find_string(trie, word));
    } else {
      printf("command '%s' not recognized\n", cmd);
    }
  }

  return 0;
}
{% endhighlight %}

Put that into something like `spell-check.c`. We can compile and run with something like

    gcc spell-check.c
    ./a.out

or if you like clang:

    clang spell-check.c
    ./a.out

and the program should run like this:

    % ./a.out
    > find apple
    0
    > insert apple
    inserted 'apple'
    > find apple
    1
    > find appl
    0
    > find applee
    0

Note that even though 'apple' is in our trie, we correctly ignore 'appl', a prefix of 'apple'.


## Loading an english dictionary into the trie

Obviously we'd like our program to already be aware of valid English words, and not have to manually tell it things like that 'apple' is a word with 'insert apple' commands.

To do this, all we need to get our hands on is a text file containing a list of all valid English words. Most linux distributions have such a file somewhere in the filesystem. On my Ubuntu install, the file is `/usr/share/dict/words` (which is a sym-link to `/etc/dictionaries-common/words`, which is a sym-link to `/usr/share/dict/american-english'). If you can't find such a file on your computer, you can download from somewhere like [here](http://wordlist.sourceforge.net/). (The file you use should just contain a single dictionary word on each line -- no definitions or anything else)

Once you've got the dictionary file it's easy to just walk through it and load all the words into our trie:

...
