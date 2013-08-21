---
layout: post
title: "Spell checking with tries in C++: Part 2"
---
In [part 1](/blog/spell-checking-part-1) we built a class for a trie that would store strings, loaded the trie with words from a dictionary, and then built a little command-line interface used to check if a given word was in the trie or not. Now, we're going to try and implement the "actual" spell-checker. Ie, the part of the program used to generate corrections for misspelled words.

We generate corrections based on the idea that when spelling words, people make 4 fundamental kinds of mistakes. The first is a missing letter. We meant to type "apple" but typed "appe" instead. The second is an extra letter. We meant to type "apple" but typed "appple" instead. The third is a mis-typed letter. We meant to type "apple" but typed "apole" instead. And last, we have swapping letters. We meant to type "apple" but typed "appel". Each of the mis-types above are all one mistake or one edit "away" from their target words. Another way of saying this is to say that the **edit distance** between, for example, "apple" and "appel", is 1.

So when we want to generate spelling corrections, we want to search through our trie of words for words that are a certain edit distance away from the word we typed in, hoping that one of these words was the target word. This where tries become especially handy, because searching through them for corrections of the nature we're looking for is very easy, as we'll see in a bit.

## Back to coding

Let's go back to our `Trie` class and add a new method to the private section of the class:

{% highlight cpp %}
private:
  void corrections(string word, int d, Node* curr, set<string>& res)
  {
{% endhighlight %}

`corrections` is a function that takes in 4 inputs: `word`, the string we're searching for corrections for, `d`, the maximum edit distance we want to search within, `curr`, the current node we're at in our traversal of the trie, and `res`, an `std::set` which will hold the results of our search.


{% highlight cpp %}
if(word.size() == 0)
{
  if(curr->final)
    res.insert(curr->word,d,curr->freq);
  return;
}
{% endhighlight %}

We first check to see if `word` is an empty string. If it is, and the current node we're at is final, it means we've found a potential string in our trie, so we add it to the result set.

{% highlight cpp %}
char c = word[0];
if(curr->child(c))
  corrections(word.substr(1),d,curr->child(c),res);
{% endhighlight %}

Next, we recur on the current string minus its first character, also moving down to the next node in the trie. This bit of code basically just simulates the for-loop we had in the `add` and `search` functions, except as recursion.
