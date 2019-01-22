---
layout: post
title: "Entropy of Android’s unlock patterns"
---

Having just got an Android phone for the first time, I was curious about how
secure it was to try using a pattern unlock instead of a password or pin.

It should be clear right away that a pattern of length $n$ is strictly less
secure than a pin of length $n$. This is because you can assign each of the 9
dots in the pattern a number from 1 to 9:

    1 2 3
    4 5 6
    7 8 9

and now patterns can be mapped to corresponding pins. But not all patterns are
possible: for instance, you can't go from position 1 to 3 directly (you have to
touch 2 first), so 132 is a valid pin but not a valid pattern. You also can't
repeat, so 4924 is also a valid pin but not a valid pattern.

That said, patterns are a little easier to use than pins, so maybe people will
tend to (or be willing to) use longer patterns than pins. Still: how many
patterns are there of a given length.

First, let's establish the rules of the patterns:

1. You can start at any position.
2. You can't visit the same position twice.
3. You can only move from one position to another along a straight line, and
you must move to the _first unvisited_ position on such a straight line.
    * This means that you can't go from 1 to 3, because 2 comes before 3 on the line from 1 to 3.
    * However, if 2 has already been visited in the pattern, it is now possible to go from 1 to 3 directly. So 2413 is a valid pattern, but 1324 is not.

We can almost think of this as a graph: the nodes are the 9 positions, and
there are edges between any two nodes that you can move between. It's easy
enough to BFS through such a graph, but there's the caveat that new edges  can
become available (ie, between 1 and 3) as you traverse the graph. This isn't
too much of an issue though: we can dynamically modify our edge set as we
traverse the graph.

First, we see which edges are not normally available because of a "blocking"
position in between. We note which position is blocking each edge:

    blocking = {
        frozenset([1, 3]): 2,
        frozenset([1, 7]): 4,
        frozenset([1, 9]): 5,
        frozenset([2, 8]): 5,
        frozenset([3, 7]): 5,
        frozenset([3, 9]): 6,
        frozenset([4, 6]): 5,
        frozenset([7, 9]): 8
    }

Edges can be represented "dynamically" by the following function, which checks to see if a given node can be added to the end of an existing path:

    def can_move(path, dest):
        if dest in path:
            return False
        fz = frozenset([path[-1], dest])
        if fz not in blocking:
            return True
        if blocking[fz] in path:
            return True
        return False

Now we can just BFS through all possible paths:

    def num_paths(length):
        q = deque([node] for node in nodes)
        paths = []
        while q:
            path = q.popleft()
            if len(path) == length:
                paths.append(path)
                continue
            for node in nodes:
                if can_move(path, node):
                    q.append(path + [node])
        return len(paths)

Then we just print how many paths exist of each length, as well as the base-2
log of that to get bits of entropy (assuming each path is chosen with equal
probability):

    for i in range(1, 10):
        n = num_paths(i)
        print i, n, math.log(n, 2)

We get the following:

    1 9 3.16992500144
    2 56 5.80735492206
    3 320 8.32192809489
    4 1624 10.6653359172
    5 7152 12.8041310212
    6 26016 14.6671115421
    7 72912 16.1538686552
    8 140704 17.1023038172
    9 140704 17.1023038172

So, for instance, there are 26,016 possible patterns of length 6. If you choose
among those patterns randomly, the pattern you get has about 14.7 bits of
entropy. Similarly, for a length 9 pattern, we have 140,704 possibilities and
about 17 bits of entropy.

This is actually rather low, entropy-wise. For instance, a $n$ digit PIN has
$10^n$ possibilities:

    for i in range(1, 10):
        n = 10 ** i
        print i, n, math.log(n, 2)

    1 10 3.32192809489
    2 100 6.64385618977
    3 1000 9.96578428466
    4 10000 13.2877123795
    5 100000 16.6096404744
    6 1000000 19.9315685693
    7 10000000 23.2534966642
    8 100000000 26.5754247591
    9 1000000000 29.897352854

So we see that a randomly chosen 9 position pattern has entropy somewhere
between a 5 or 6 character PIN. So if you're willing to remember 6 random
digits, you've already got more security than a pattern can provide.

_Note:_ [A stackoverflow answer](http://stackoverflow.com/a/2120815/598940)
with code for this and some combinatorial reasoning.

## Choosing randomly

Note that while when choosing a random pin it suffices to choose $n$ random
digits in sequence, you can't choose a random pattern as easily. This is
because each position in the pattern is dependent on the previous entries in
the pattern, and further, because the dependencies aren't symmetric.

Ie, it may be that more patterns are possible when starting from an "edge"
position than from a "corner" position. So if we're randomly choosing patterns,
we need to weigh against corner positions and towards edge positions. A simpler
way of choosing a random pattern would be to just generate a list of all
patterns and select one final pattern randomly, without worrying about the
weights at each individual step.

## Other factors

Another element of this beyond the math is psychological acceptability: how
easily can people remember pins vs patterns? I would guess patterns are easier
to remember, but it's not clear a) how much easier, and b) whether pins could
be easier to remember as well if the device "drew out" the path between the
numbers.

Patterns are also easier to enter and let you unlock your phone faster. This
may be an important usability consideration, because if a determined attacker
gets your phone, they're probably not going to have much more trouble breaking
into it if you'd used a pin instead of a pattern, and a pattern still provides
decent protection against a casual attacker. Maybe it's worth it to just be
able to unlock my phone quicker.

And of course, there's the fact that the average user is not generating pins or
patterns uniformly randomly. I'm not sure which method gets the advantage
here.  On the one hand, users might tend to pick pins corresponding to things
about them like their birthday, which makes the pins potentially less secure.

On the other hand, it might be that people tend to choose common patterns. Eg,
maybe the "house-shaped" pattern 74269 or other simple shapes are common. But
it seems plausible to me that the average user could at least try to come up
with a decent random pattern, and the interface might encourage this a bit,
whereas picking random numbers for a pin seems much less likely.
