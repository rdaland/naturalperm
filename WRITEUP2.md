# Natural Permutations

A permutation is a mapping which reorders elements of a set. The set can be finite, or infinite. There are many "simple" permutations on infinite sets — for example, the identity permutation simply maps an element to itself (no reordering). This writeup takes up the challenge of defining a non-simple permutation on the natural numbers. An encoding is defined as an invertible mapping from the natural onto a subspace of _canonical binary strings_. The approach taken here is to find two different encodings $benc$ and $penc$; the permutation is defined by composing one encoding with the inverse of the other. After walking through the setup, some limited exploration and analysis is presented.

# Permutations

A permutation is a 1-1 mapping from a set onto itself; in other words, an invertible rearrangement.

## Finite Permutations

Finite sets can be represented by $\mathbb{Z}_n$ (the set of integers modulo _n_). Here is an example of a permutation on $\mathbb{Z}_6$:

```math
P = 
    \begin{pmatrix}
        1 & \rightarrow & 2 \\
        2 & \rightarrow & 4 \\
        3 & \rightarrow & 5 \\
        4 & \rightarrow & 1 \\
        5 & \rightarrow & 3 \\
        6 & \rightarrow & 6 \\
    \end{pmatrix}
```

The **orbit** of an element is the sequence of elements obtained by iteration. Here is the orbit of the element $1$ under $P$:

```math
1 \rightarrow 2 \rightarrow 4 \rightarrow 1 \rightarrow 2 \rightarrow 4 \rightarrow 1 \ldots
```

The orbit eventually returns to $1$. When this occurs, it is called a **cycle**. It turns out that finite permutations can be uniquely represented in terms of their cycles. For example, the cycle notation for the permutation above is $P = (124)(35)(6)$. Note the cycle $(6)$ has a single element — $P$ maps $6$ to itself. This is called a **fixed point**.

## "Simple" Infinite Permutations

This section defines and gives examples of various "simple" families of permutations on the integers. In the final subsection we will share a conjecture as to what it means for a countably infinite permutation to be "simple".

### Identity but with finite exceptions

The finite permutation $P$ given earlier can be lifted into a corresponding permutation on the space of all integers by defining

```
P^\inf = \begin{cases}
  P(n) & \text{ if } n \in Domain(P) \\
  n    & \text{ otherwise } \\
\end{cases}
```

In the essential ways, $P^\inf$ behaves the same as $P$. And the situation is the same for every infinite permutation that has a finite number of non-fixed points — its behavior is entirely captured by the corresponding finite permutation. Note that the identity permutation belongs to this family — the set of non-fixed points is empty!

### Infinite products of 1- and 2-cycles

Like finite permutations, infinite permutations can have cycles. Consider the following permutations on the set of (positive and negative) integers:

```math
\sigma(n) = \begin{cases}
  n + 1 & \text{ if n is even} \\
  n - 1 & \text{ if n is odd} \\
\end{cases}
```

This parity-flipping permutation can be represented as the infinite product of 2-cycles: $\sigma = \ldots (-2,-1) (0,1) (2,3) \ldots$. 

It is also possible to define a permutation which consists of a mixture of 1- and 2-cycles:

```math
\nu(n) = -n
```

This sign-flipping permutation has $0$ as a fixed point but otherwise consists of 2-cycles: $\nu = (0) (1,-1) (2,-2) \ldots$. Up until now, all the permutations we have considered share the property that for some global $\Delta > 0$, $|P(n) - n| < \Delta$. The parity-flipping permutation $\nu$ is a counterexample: it is a very simple mapping with no upper bound to the distance between an element and its image under $\nu$. Finally, we note that the identity permutation belongs to this family — it can be represented by an infinite product of 1-cycles!

### Shift permutations

Unlike finite permutations, permutations on countably infinite sets do not have to produce any cycles at all. Consider the following shift-by-1 permutation:

```math
\rho_1(n) = n + 1
```

The orbit of every integer $k$ is the set $\{ k, k+1, \ldots \}$. There are no cycles; or put differently, there is 1 cycle of infinite length.

It is instructive to consider the shift permutation when the shift constant is larger than 1. For example, consider $\rho_6(n) = n + 6$. The orbit of $0$ is $\{0, 6, 12, \ldots \}$. The orbits of $1$, $2$, $3$, $4$, and $5% do not overlap with the orbit of $0$, nor with each other. But $6$ is different — the orbit of $6$ contains all the same values as the orbit of $0$, except for $0$ itself. Formally, we could say that (the orbit of) $6$ _eventually agrees_ with the orbit of $0$ (and with $-6$, and with $12$, etc..). In fact, we could partition the integers into 6 classes, depending on whether their orbit eventually agrees with the orbit of $0$, $1$, $2$, $3$, $4$, or $5$. If we agreed to call each element of that partition a cycle (of infinite length), then we could say that $\rho_6$ is represented by a finite product of 6 infinite cycles. (Readers familiar with finite groups will immediately note the connection with $\mathbb{Z}_6$).

We finally note that the identity permutation belongs to the class of shift permutations; it is simply that the shift constant is zero!

### A formal definition of "simple"?

The permutations given in this section are all "simple" in some sense. While we are not prepared to rigorously define "simple", we note that all of the examples given above fall into one of two classes:
* infinite product of finite cycles
* finite product of infinite cycles

The "cycles" are better viewed as partitions of the integers; and in both cases the values which make up a cycle are determined arithmetically. In the former case (infinite product, finite cycles), the cycles of $\sigma$ are just even-odd pairs of the form $(2k, 2k+1)$; and the cycles of $\nu$ are just negative-positive pairs of the form $(k, -k)$. In the latter case (finite product, infinite cycles), the cycles of the "shift by $k$" permutation can be identified with the elements of $\mathbb{Z}_k$ (except for $k=0$, the identity permutation).

A finite permutation is of course the finite product of finite cycles. We have seen that various simple infinite permutations are either the infinite product of finite cycles, or the finite product of infinite cycles. There is a notable gap — a permutation which is the infinite product of infinite cycles. It is tempting to speculate that a "complex" permutation is exactly one which fills this gap.

## Single-Sided vs. Double-Sided Infinity

# Preliminaries

## Canonical Binary Strings
## Binary Encoding/Decoding
## Stack Encoding/Decoding
## Prime-stack Encoding/Decoding

# Definition

# Exploration

# Some Properties

# Final Thoughts

# References
