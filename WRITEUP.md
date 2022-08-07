
# Introduction

A permutation is a 1-1, onto mapping from a set to itself, in other words an invertible re-arrangement of the set elements. Permutations are well-studied on finite sets, such as Z_n (the set of integers modulo n). A key behavior is a **cycle** — a sequence of elements which repeat under iteration. For example, consider the following mapping on Z_6:

```
P:
1 —> 2
2 —> 4
3 —> 5
4 —> 1
5 —> 3
6 —> 6
```

This permutation generates 3 cycles: `(124)`, `(35)`, and `(6)`. The notation `(124)` means that P maps 1 to 2, 2 to 4, and 4 back to 1. Permutations on finite sets always give rise to cycles; and can be uniquely identified with their cycles. The permutation above can be compactly represented `P = (124)(35)(6)`.

There are various "simple" permutations which can be defined in a nearly set-independent way. For example, the identity permutation simply maps an element to itself. Finite sets can always be identified with Z_n; and then it is straightforward to defined to define a "shift-by-1" permutation `P(k) = k + 1 (modulo n)`. This will always yield a single cycle of length `n`, which is the longest a cycle can be for a finite set.

For countably infinite sets, some things are different, while others are the same. For example, the shift-by-one permutation `f(n) = n + 1` can also be defined on the integers. However, unlike with the finite set Z_n, iteration of this permutation does not yield a cycle. Iterating `k` times simply adds `k` to the integer; because the integers are endless, one can do this indefinitely without repeating. This permutation has no fixed points, and no cycles whatsoever.

There is another class of 'simple' permutations on the natural numbers — mappings which are the same as the identity mapping, except on a finite set of elements. This class is not importantly different from the permutation on the non-identity elements. 

These facts led me to wonder — is there an 'interesting' permutation on the natural numbers — one which cannot be reduced to a finite permutation alone? It is worth noting that the structure of the natural numbers already rules out "shift-by-k" permutations. This because permutations must be invertible. For the purposes of this writeup, we will say that the natural numbers begin with 1 and go upwards (0 is excluded). For the shift-by-1 mapping f(n) = n + 1, the minimal element 1 lacks an inverse — `f^-1(1)` is undefined. Therefore `f` is not truly a permutation. The same logic applies more generally — if a mapping is nondecreasing (or nonincreasing) everywhere, it must have at least one element that lacks an inverse (unless it is the identity mapping, of course). Put more simply, any nontrivial permutation on the natural numbers must map some numbers downwards, and an equal amount of numbers upwards. The goal of this project is to implement just such an 'interesting' permutation.

