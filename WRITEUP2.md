# Natural Permutations

A permutation is a mapping which reorders elements of a set. The set can be finite, or infinite. There are many "simple" permutations on infinite sets — for example, the identity permutation simply maps an element to itself (no reordering). This writeup takes up the challenge of defining a non-simple permutation on the natural numbers. An encoding is defined as an invertible mapping from the natural onto a subspace of _canonical binary strings_. The approach taken here is to find two different encodings $benc$ and $penc$; the permutation is defined by composing one encoding with the inverse of the other. After walking through the setup, some limited exploration and analysis is presented.

# Preliminaries

A permutation $\sigma : X \rightarrow X$ is a 1-1 mapping from a set onto itself. In other words, it is an invertible mapping which covers an entire set.

## Sets

For concreteness, let us define the following:
* $\mathbb{N} = \{ 0, 1 ,2, \ldots \}$ — (natural numbers)
* $\mathbb{Z} = { \ldots, -1, 0, 1, 2, \ldots \}$ — (integers)
* $\mathbb{Z}^+ = \{1,2,\ldots\}$ — (positive natural numbers)
* $\mathbb{Z}_n = \{ 0, 1, \ldots, n-1 \}$ — (integers mod n)

The last set is special, in that arithmetic operations are computed with respect to modulo $n$; in other words they "wrap around". For example, in $\mathbb{Z}_6, $5 + 2 (mod 6) = 7 (mod 6) = 1$.

The integers mod n are important because they are a model for finite permutations. Every finite permutation can be represented by a permutation on $\mathbb{Z}_n$, for some $n$, by enumerating the elements and their mapping.

## Fixed Points, Orbits, and Cycles

Here is an example of a permutation on $\mathbb{Z}_6$:

```math
P = 
    \begin{pmatrix}
        0 & \rightarrow & 0 \\
        1 & \rightarrow & 2 \\
        2 & \rightarrow & 4 \\
        3 & \rightarrow & 5 \\
        4 & \rightarrow & 1 \\
        5 & \rightarrow & 3 \\
    \end{pmatrix}
```

The **orbit** of an element is the sequence of elements obtained by iteration. Here is the orbit of the element $1$ under $P$:

```math
1 \rightarrow 2 \rightarrow 4 \rightarrow 1 \rightarrow 2 \rightarrow 4 \rightarrow 1 \ldots
```

The orbit eventually returns to $1$. When this occurs, it is called a **cycle**. It turns out that finite permutations can be uniquely represented as a product of their cycles. For example, the cycle notation for the permutation above is $P = (0)(124)(35)$. Note the cycle $(0)$ has a single element — $P$ maps $0$ to itself. This is called a **fixed point**.

## Invertibility

The requirement of invertibility imposes strong constraints on whether a mapping constitutes a permutation. 

For example, define the doubling function $\mu_2(n) = 2n$ on the integers. This mapping cannot define a permutation, because it is not onto (that is, the image does not cover the entire set). For example, the value $3$ does not have an inverse. More generally, the multiply-by-k mapping $\mu_k(n) = kn$ cannot define a permutation on $\mathbb{Z}$ for any value of $k$ (except $|k| = 1$).

Besides the operation, the domain of a mapping can affect its invertibility. For example, let $\rho_1(n) = n + 1$ be the shift-by-one mapping. If the domain is the set of (positive and negative) integers $\mathbb{Z}$, $\rho_1$ defines a permutation. However, if the domain is the set of natural numbers, $\rho_1$ does not define a permutation. This is because the natural numbers have a least element, $0$. The shift-by-one mapping $\rho_1$ is of course defined for the value $0$: $\rho_1(0) = 1$. However, the key point is that the inverse is not defined with respect to the domain of natural numbers: $\rho_1^{-1}(0) = \text{??}$. Put another way, the integer $-1$ could be the inverse, except $-1$ is not a natural number.

## Canonical Binary Strings

Let $\Sigma = \{ 0, 1 \}$, and $\Sigma^{*}$ be the set of finite strings over the alphabet $\Sigma$. A string $s \in \Sigma^{*}$ is in canonical form if any of the following conditions hold:
* $s = \text{"}0\text{"}$
* the initial (most significant) bit of $s$ is a $1$

An example of a non-canonical string is $0101$. It is non-canonical because the initial (most significant) bit is $0$. The canonical binary string that corresponds to $0101$ is $101$. In general, a canonical binary string can be obtained from a non-canonical one by stripping all leading $0$'s. The sole exception is when the string contains no $1$'s; in that case, a single leading $0$ is allowed. Thus, we define canonical binary strings as the set of strings in canonical form, i.e.

```math
\mathbb{B} = \{ \text{"}0\text{"} \} \cup \{ \text{"}1s\text{"} | s \in \Sigma^{*} \}
```

# Encodings

For the purpose of this writeup, an **encoding** is an invertible mapping from $\mathbb{Z}$ onto $\mathbb{B}$, and a **decoding** is the corresponding inverse.

## Binary Encoding/Decoding
## Stack Encoding/Decoding
## Prime-stack Encoding/Decoding

# Definition

# Exploration

# Some Properties

# Final Thoughts

# Simple Permutations

A permutation is a 1-1 mapping from a set onto itself; in other words, an invertible rearrangement.

## Finite Permutations



## "Simple" Infinite Permutations

This section defines and gives examples of various "simple" families of permutations on the integers. In the final subsection we will share a conjecture as to what it means for a countably infinite permutation to be "simple".

### Identity but with finite exceptions

The finite permutation $P$ given earlier can be lifted into a corresponding permutation on the space of all integers by defining

```
P^{\infty} = \begin{cases}
  P(n) & \text{ if } n \in Domain(P) \\
  n    & \text{ otherwise } \\
\end{cases}
```

In the essential ways, $P^{\infty}$ behaves the same as $P$. And the situation is the same for every infinite permutation that has a finite number of non-fixed points — its behavior is entirely captured by the corresponding finite permutation. Note that the identity permutation belongs to this family — the set of non-fixed points is empty!

### Infinite products of 1- and 2-cycles

Like finite permutations, infinite permutations can have cycles. Consider the following permutations on the set of (positive and negative) integers:

```math
\sigma(n) = \begin{cases}
  n + 1 & \text{ if n is even} \\
  n - 1 & \text{ if n is odd} \\
\end{cases}
```

This parity-flipping permutation can be represented as the infinite product of 2-cycles: $\sigma = \ldots (-2,-1) (0,1) (2,3) \ldots$. 

The sign-flipping permutation has one fixed point but otherwise consists of 2-cycles:

```math
\nu(n) = -n \\
\\
\nu = (0) (1,-1) (2,-2) \ldots
```

Up until now, all the permutations we have considered share the property that for some global $\Delta > 0$, $|P(n) - n| < \Delta$. The parity-flipping permutation $\nu$ is a counterexample: it is a very simple mapping with no upper bound to the distance between an element and its image under $\nu$. Finally, we note that the identity permutation belongs to this family — it can be represented by an infinite product of 1-cycles!

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

Of course, a finite permutation is the finite product of finite cycles. This leaves a gap — a permutation which is the infinite product of infinite cycles. It is tempting to speculate that a "complex" permutation is exactly one which fills this gap. (This need not exclude finite cycles.)

# References
