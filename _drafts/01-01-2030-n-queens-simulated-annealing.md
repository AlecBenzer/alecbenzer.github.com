---
layout: post
title: "Solving n-queens with simulated annealing"
---
The n-queens problem is as follows\: Given an n by n chess board, place queens on n different cells so that no two queens are in each other's "line of sight". Ie, no two are in the same row, same column, or on the same diagonal.

Computing a configuration for a given value of n is NP-hard, but using simulated annealing, we can write a program that approximates a solution (and often gets it right).

Simulated annealing can be used to solve minimization problems. Suppose we have a set of states, $Q$, and a cost function $c \colon Q \to \mathbb{R}$ that assigns each of our states a cost. Cost is like the "badness" of a particular state, and we want to find the state (or a state) with minimal cost.

The other thing we need to use simulated annealing is for each state $q \in Q$ to have a set of neighbors $N(q)$. The idea here is that a states neighbors are other states that are pretty similar to $q$, and thus do not differ too greatly in cost. Graphically, if a state $q$ were represented by a point in a plane, and the cost function was continuous, $N(q)$ would just be a disk of a particular radius centered at $q$.

In this sense you can also think of our input space being a graph $G = (Q,E)$, with an edge $(q_1,q_2) \in E$ representing the fact that $q_1$ and $q_2$ are neighbors.

## A naive approach

So given such a graph $G$ and some starting point $q \in Q$, one thing we could do to try and minimize our cost is randomly pick one of $q$'s neighbors. and check if that neighbor's cost is less than $q$'s. If it is, we change our current state to the neighbor. If not, we try a different neighbor of $q$'s.

The problem with this is that we would be finding a _local_ minimum of our cost function. Again, looking at things graphically, if we find ourselves standing somewhere on a graph where the graph is sloping down, we'd continue to follow that slope down until we reach a local minimum -- but we have no way of "peeking" at what the world looks like outside of the hill, to see if we might end up at a better solution by moving to states that, in the short run, end up increasing our cost, but will eventually bring us down to a better minimum (or, hopefully, a global minimum).

Many problems when modeled in this fashion will have a lot of local minima, so doing this kind of blind optimization technique doesn't really cut it.

## Simulated annealing

What we can try to do to get around this problem is to allow ourselves to sometimes make decisions that seem bad in the short run, but may end up helping us in the long run. So let's say we have a state $q \in Q$, and we randomly select one of its neighbors, $q' \in N(q)$. We then compare their costs. If $c(q') < c(q)$, then we can safely move our current state to $q'$. However, in the event that $c(q') \ge c(q)$, we don't immediately decide to not move our current state to $q'$.

What we do instead is assign some probability to this transition between $q'$ and $q$, and then roll a dice to decide if we do end up taking the transition or not.

The probabilities we assign to transitions that increase cost are based on two things. The first is the actual change in cost. We'd like changes in cost between two neighbors to generally be low, but there will still be variation, and so a transition that ends up increase our cost by 1 would be prefered over (and thus taken more often than) a transition that increases our cost by 4.

The other factor in deciding whether or not to take a transition is what we'll call our **temperature variable**. Basically, what we're doing is pretending that our system has some kind of temperature. The system starts out with a high temperature, and in this situation, our system is volatile, meaning we're more likely to take costly transitions.

The key idea behind simulated annealing is that we slowly decrease the temperature of the system. As the temperature decreases, the system becomes more "rigid", and becomes less accepting of state transitions that end up increasing our cost. So in the beginning, we can jump around a lot and move in the "wrong" direction in the hopes of finding a global minimum, but as the annealing goes on, we eventually "settle down" and act more like we're doing local optimization.

**TODO: mention exact formulas for the probability**

## Modeling n-queens for simulated annealing

So if we'd like to use simulated annealing to solve n-queens, we need to come up with a system of states, edges between states, and a cost function.

The states are pretty easy. $Q$ is just the set of all possible configurations of n queens on an n by n chess board (we don't care about if the queens are in each other's line of sight yet -- any assignment of queens to the cells on the board goes here). We'll end up starting with some random assignment of queens.

A particular state's neighbors are all the states we can get to by moving any of ours queens one unit away in any direction. Ie, given a state, we randomly select a neighbor state by randomly picking one of the queens, and moving it 1 unit in some random direction.

Finally, we have our cost function. The cost of a state is just how many ...
