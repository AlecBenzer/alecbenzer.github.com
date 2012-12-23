---
layout: post
title: "There's only one three-element field"
---

I'm home from school, bored, and I feel like writing something. So I'm going to tackle the following problem from an [r/learnmath thread](http://www.reddit.com/r/learnmath/comments/15au4f/show_that_there_is_one_and_only_one_field_with/) that also happens to be from my just-finished real analysis class's textbook:

Prove there is only one three-element field.

Okay, so first of all, we should know what the definition of a field is. You can <a href="http://en.wikipedia.org/wiki/Field_(mathematics)">refer to wikipedia</a> for the details, but just generally speaking, a field is a 3-tuple $(F,+,(\cdot))$, where $F$ is some set, $+$ is a function $+ \colon F \times F \to F$, and $(\cdot)$ is a function $(\cdot) \colon F \times F \to F$. Ie, if $a, b \in F$ are two elements of our field, then we have defined $a + b \in F$ and $a\cdot b \in F$ as element of our field.

There's also a bunch of rules that the $+$ and $(\cdot)$ operators/functions needs to adhere to. I'm not going to list them all out here (you can find them in the wikipedia article), but I will refer to them over the course of the post.

One of the other rules a field has is that there must be an element $0 \in F$ with the property that $a + 0 = a$ for any $a \in F$ ($0$ is called the _additive identity_), and there must also be an element $1 \in F$ with the property that $a \cdot 1 = a$ for any $a \in F$ ($1$ is called the _multiplicative identity_), and furthermore it must be the case that $0 \neq 1$.

This last condition tells us that every field must contain at least two elements, and that one of these elements will be additive identity, and that the other will be the multiplicative identity. We're not interested in a two-element field, though, we're interested in a three-element field, and so _our_ set $F$ is going to contain one additional mystery element, which we'll call $x$.

So now we've settled the fact that $F = \\{0, 1, x\\}$. We now need to look at the two remainin parts of our definition of a field -- namely, the functions $+$ and $(\cdot)$.

Recall that $+$ was a function mapping from $F \times F$ to $F$, meaning that for every possible pair of elements $(a,b) \in F \times F$ from our field, we must assign some other element of our field as their sum (and also their product). A natural way of representing the function $+$, then, is with a three by three table, each cell of which tells us what we get when we add the elements of that cell's row and column. We use a similar table for our representation of $(\cdot)$.

Thus, initially, we start with two blank tables like the following:


<style type="text/css">

table td, table th {
  padding: 6px;
  border: 1px solid black;
}
</style>

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $1$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $x$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $1$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $x$ </th> <td> ? </td> <td> ? </td> <td> ? </td>
</tr>

</table>
</p>

## The easy stuff

Using just very basic rules about our field, we can fill up much of our table. For instance, we know that $0 + a = a$ for all $a \in F$, and because addition is commutative in fields, we also have $a + 0 = a$. With this, we can fill out all the edges of our $+$ table (ie, the places where we're adding to $0$).

The same fact involving $1$ (ie, that $a \cdot 1 = 1 \cdot a = a$, for all $a \in F$) lets us immediately fill out the lines in our table for $(\cdot)$ where we're multiplying by $1$, giving us the following for our tables:

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> ? </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> ? </td> <td> $0$ </td> <td> ? </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> ? </td> <td> $x$ </td> <td> ? </td>
</tr>

</table>
</p>

Another well-known fact about fields is that $a\cdot 0 = 0$, for any $a \in F$. However, this is not actually part of the definition of a field, and requires a proof.

_Theorem_: $a \cdot 0 = 0$.

_Proof_: $a \cdot 0 = a \cdot (0 + 0) = a \cdot 0 + a \cdot 0$. This is true because $0 = 0 + 0$, and because we can distribute multiplication over addition.

It's also true that for every element $b \in F$ of our field, we must also have an element $-b \in F$ such that $b + (-b) = 0$.

$a \cdot 0$ is an element of our field, so there must be some element $-(a\cdot 0) \in F$ with $a\cdot 0 + -(a\cdot 0) = 0$.

If we add $-(a\cdot 0)$ to both sides of our original equation, we get $a \cdot 0 + -(a\cdot 0) = a\cdot 0 + a\cdot 0 + (-a\cdot 0)$ $\implies 0 = a\cdot 0 + (a\cdot 0 + -(a \cdot 0))$ $\implies 0 = a\cdot 0 + 0 \implies 0 = a\cdot 0$. QED

So now we know that $a \cdot 0 = 0$, and can use this to fill in more of our $(\cdot)$ table:

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> ? </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $0$ </td> <td> $x$ </td> <td> ? </td>
</tr>

</table>
</p>

## The trickier stuff

We now are down to the following four quantities we need to assign values to: $1 + 1$, $1 + x$, $x + x$, and $x\cdot x$ (technically we're also missing $x + 1$, but since addition is commutative in fields, $1+x$ and $x+1$ are the same thing).

Let's tackle $x\cdot x$ first, so we can get our multiplication table finished with. There are only three possible cases: $x \cdot x = 0$, $x \cdot x = 1$, or $x \cdot x = x$.

Let's consider the first case. The first thing to recall/note is that $x \neq 0$ and $x \neq 1$, because if this were the case, then our field would actually only have two elements. In order to have a three-element field, $x$ must be an element _distinct_ from the other two.

Now, just as fields have additive inverses, they also have multiplicative inverses. Ie, for every $b \in F$, except $b = 0$, there exists a $b^{-1} \in F$, with the property that $b \cdot b^{-1} = 1$. So if it is the case that $x \cdot x = 0$, let us multiply both sides of this equation by $x^{-1}$ to get $x \cdot x \cdot x^{-1} = 0 \cdot x^{-1} \implies x \cdot (x \cdot x^{-1}) = 0 \implies x \cdot 1 = 0 \implies x = 0$. But we just got finished saying that $x$ could _not_ be equal to $0$. This is a contradiction, and therefore, it cannot be that $x \cdot x = 0$.

Okay, so let's try $x \cdot x = x$. Does this work? Let's do the same thing we did above. We get $x \cdot x \cdot x^{-1} = x \cdot x^{-1} \implies x \cdot 1 = 1 \implies x = 1$. But once again, it cannot be that $x$ is the same as $1$, and so it cannot be that $x \cdot x = x$.

With those two possibilities gone, it must be the case that $x \cdot x = 1$. Note that there's no guarentee that we won't also run into some problem with letting $x \cdot x = 1$, but we know that _if_ there is some three element field, and thus a valid $(\cdot)$ table, that $1$ has to be what goes in this slot.

So now our $(\cdot)$ table is done:

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> ? </td> <td> ? </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> ? </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $0$ </td> <td> $x$ </td> <td> $1$ </td>
</tr>

</table>
</p>

Let's now tackle $x + 1$. We'll do the same thing we did above, run through each of the possibilities and see what happens.

First, let's try $x + 1 = x$. If this it the case, then we can add $-x$ to both sides and get $x + 1 + (-x) = x + (-x) \implies (x + -x) + 1 = 0 \implies 1 = 0$, which is definitely not true in any field. So we don't have $x + 1 = x$.

What about $x + 1 = 1$. Now let's try adding $-1$ to get $x + 1 + -1 = 1 + -1 \implies x + 0 = 0 \implies x = 0$. Just as before, $x$ cannot be $0$, so $x + 1$ cannot be $1$.

This leaves us with $x + 1 = 0$ as our only viable option. And, recall, that because of commutativity of addition, we also have $1 + x = 0$:


<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> ? </td> <td> $0$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> $0$ </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $0$ </td> <td> $x$ </td> <td> $1$ </td>
</tr>

</table>
</p>

## The slightly trickier still stuff

Now let's look at $1 + 1$. Could we have $1 + 1 = 0$? Refer back to the most recent version of our table, and note that $x + 1 = 0$. If $1 + 1$ were also equal to $0$, then we'd have that $1 + 1 = x + 1$. And if we add $-1$ to both sides of that equation, we get $1 + 1 + (-1) = x + 1 + (-1) \implies 1 = x$. And, once again, that can't happen. So $1 + 1 \neq 0$. 

Could we have $1 + 1 = 1$? Here we could simply add $-1$ to both sides and see that we'd have $1 + 1 + -1 = 1 + -1 \implies 1 = 0$, but, we could also refer back to the table and see that $0 + 1 = 1$, and that if $1+1$ were also $1$, that we'd have $0 + 1 = 1 + 1 \implies 0 = 1$. This just seems like a longer way of getting to the same result, $0 = 1$, which tells us that $1 + 1 \neq 1$, but it's following a pattern that I'll refer back to later.

At any rate, it must be that $1 + 1 = x$:

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> $x$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> $0$ </td> <td> ? </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $0$ </td> <td> $x$ </td> <td> $1$ </td>
</tr>

</table>
</p>

We're almost there -- we've just got $x + x$ left to tackle.

Could $x + x$ be $0$? Nope. $1 + x$ is also $0$, so we'd have $x + x = 1 + x \implies x = 1$. Could $x + x$ be $x$? Nope. $0 + x$ is also $x$, so we'd have $x + x = 0 + x \implies x = 0$. So, it has to be that $x + x = 1$, which then completes our tables:

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> $x$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $x$ </td> <td> $0$ </td> <td> $1$ </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $x$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $x$ </td>
</tr>
<tr>
<th> $x$ </th> <td> $0$ </td> <td> $x$ </td> <td> $1$ </td>
</tr>

</table>
</p>

Now, we're technically not done yet. We've gotten down to this single definition for our $+$ and $(\cdot)$ functions, which means that _if_ there is a valid three-element field, then this is it. But nothing we've done actually shows that the tables above neccesarily constitute a valid field.

We could carefully go through each field rule and make sure these tables follow it, but instead, let's do something else. Namely, let's pick a better name for $x$. Well, going to our table, we see that $x = 1 + 1$. Luckily for us, we already have a common name for something that's equal to one added to itself -- two!

That's right, our mystery element $x$ is really just $2$ (sort of):

<p>
<table style="float: left; margin-right: 20px">

<tr>
<th> $+$ </th> <th> $0$ </th> <th> $1$ </th> <th> $2$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $1$ </td> <td> $2$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $1$ </td> <td> $2$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $2$ </th> <td> $2$ </td> <td> $0$ </td> <td> $1$ </td>
</tr>

</table>

<table>

<tr>
<th> $\cdot$ </th> <th> $0$ </th> <th> $1$ </th> <th> $2$ </th>
</tr>
<tr>
<th> $0$ </th> <td> $0$ </td> <td> $0$ </td> <td> $0$ </td>
</tr>
<tr>
<th> $1$ </th> <td> $0$ </td> <td> $1$ </td> <td> $2$ </td>
</tr>
<tr>
<th> $2$ </th> <td> $0$ </td> <td> $2$ </td> <td> $1$ </td>
</tr>

</table>
</p>

Well, saying that $x$ _is_ $2$ is a little misleading. It'd be better to say that $x$ is $2$ in the integers mod $3$, which is in fact exactly the field that we've developed.

Ie, we have that $2 + 1 = 0$, which doesn't seem right. However, $2 + 1 \pmod{3} = 3 \pmod{3}$, and $3 \pmod{3}$ _is_ equal to $0$. Similarlly, $2 \cdot 2 \pmod{3} = 4 \pmod{3} = 1 \pmod{3}$, which is why $2 \cdot 2 = 1$ in our field.

So, rather than going through the tedious work neccesary to prove that we've indeed found a valid field, I'll just observe that our field is the integers mod 3, and quote the theorem that says the integers mod any prime (like 3) is a valid field.

## Some tips for filling out field tables

As a parting note, I'd like to make the following observation, which can be very useful in filling out field tables: excluding the times in our multiplication table where we're multiplying by zero, every element of our field may appear at most _once_ (and therefore exactly once) in every "line" (row or column) of the field tables.

Seeing why this is true is pretty easy. Say that a member of our field $x \in F$ appears twice in one line of our addition table. This means that we have $a + c = x$, and also that $a + b = x$, where $b \neq c$. This means that $a + c = a + b$, which means that $a + c + (-a) = a + b + (-a) \implies b = c$, which is a contradiction.

Similarlly, in a multiplication table, if we have $a \cdot c = x$ and $a \cdot b = x$ where $b \neq c$ and $a \neq 0$ (ie, we're not in a zero line), then $a \cdot c \cdot a^{-1} = a \cdot b \cdot a^{-1} \implies c = b$, leading to the same contradiction (we needed $a \neq 0$ because otherwise $a^{-1}$ isn't defined).

Thus, you can fill out field tables much like you'd fill out sudoku blocks -- every row and every column and only contain each field element once, and since in a field with $|F| = n$, the rows and columns each have $n$ slots, each row and column must contain each element of the field exactly once.
