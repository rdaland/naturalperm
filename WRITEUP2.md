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

## "Simple" Infinite Permutation
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
