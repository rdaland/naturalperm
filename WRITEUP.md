
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

# Approach

There is a natural, invertible mapping between nonnegative integers and strings over the alphabet '0' and '1' — the canonical binary representation. For example, the canonical binary representation of the integer 13 is "1101": 1*2^3 + 1*2^2 + 0*2^1 + 1*2^0. This writeup will refer to this mapping as `benc` (for **b**inary **enc**oding), and the inverse mapping (from canonical binary strings to integers) as `bdec` (for **b**inary **dec**oding).

Note that binary string representations of integers are not unique. For example, "01101" corresponds to same integer as "1101" does; it simply contains an unnecessary leading "0". We restrict the mappings to canonical binary strings so that `benc` is onto (and `bdec` is 1-1).

The approach take here is to look for a *different* invertible mapping between canonical binary strings and the integers. For reasons that will become clear momentarily, let us refer to these hypothetical mapping as `penc` and `pdec`. (This writeup will always use `enc` to mean mapping from integers to canonical binary strings, and `dec` to mean mapping from canonical binary strings to integers.) Then we can achieve an invertible mapping from the integers to the integers by composing one encoding method with the other decoding method:

```
naturalperm(n) = pdec(benc(n))
naturalperm^-1(n) = bdec(penc(n))
```

Of course, if the other set of mappings is chosen in a way that "too close" to `benc`/`bdec`, it is possible that this would result in a trivial permutation (such as the identity permutation). So the goal of finding a permutation on the natural integers can be achieved by finding a `penc`/`pdec` pair that is different enough from `benc`/`bdec` to produce a nontrivial permutation.

The general approach we will take here is for `penc` to encode an integer as a string of 0's and 1's in a way that represents its prime factorization. Some bookkeeping and technical details are required to ensure an invertible mapping, and these are the topic of the next section.

# Prime factorization coding

The general idea is to generate an invertible mapping by exploiting the prime factorization of an integer. The prime multiplicities are encoded as a sequence of '1's using stack encoding, and '0' is used as a separator. 

## Stack encoding

The Peano axioms define the natural numbers according to a special element '0' and the successor relation 'S'. For example, 1 is defined by a single application of the successor relation, while 2 is defined by 2 applications:

```
1: "S0"        # 1 is the successor of 0
2: "SS0"       # 2 is the successor of 1, i.e. the successor of the successor of 0
...
5: "SSSSS0"    # 5 is the successor of the successor of ... the successor of 0
```

This can be thought of as the "stack-of-plates" representation of a nonnegative integer. This is closely related to what I will refer to as the stack encoding. The stack encoding of a nonnegative integer is a sequence of repeated '1's, where the integer value is encoded by the number of repeats. For example the stack encoding of 0 is the empty string, the stack encoding of 1 is "1", and the stack encoding of 5 is "11111". Observe that the stack encoding is invertible (when the integer 0 is included in the domain).

## Prime factorization

It is well-known that all positive integers can be expressed as the product of primes. Moreover, the prime factorization is unique, up to the order of factors. Here are a couple of examples:

```
18 = 3^2 * 2^1                            # [2,1]
13 = 13^1 * 11^0 * 7^0 * 5^0 * 3^0 * 2^0  # [1,0,0,0,0,0]
```

The order of primes is fixed, just as is the order of powers of 2. Thus, we can invertibly encode the prime factorization of an integer by the sequece of prime multiplicities. (Just as with just as with the binary string encoding, the canonical sequence must be defined to exclude all primes above the greatest prime with a nonzero multiplicity; for example we do not include the term "17^0" in the prime factorization of 13).

## `penc`: combining prime factorization with stack encoding

The trick is to use stack encoding for the prime multiplicities, with '0' as the separators.

The same examples from above are shown again:

|----|-------------------------------------|---------------|--------|
| 18 |                           3^2 * 2^1 |         [2,1] |   1101 |
| 13 | 13^1 * 11^0 * 7^0 * 5^0 * 3^0 * 2^0 | [1,0,0,0,0,0] | 100000 |

For the multiplicity list [2,1] in the first line:
* the leftmost value 2 is stack-encoded with '11' (two 1's)
* a separator of '0' follows
* the rightmost value 1 is stack-encoded with '1'

For the multiplicity list [1,0,0,0,0,0] in the second line:
* the leftmost value 1 is stack-encoded with '1'
* a separator of '0' follows
* the next value 0 is stack-encoded with the empty string (0 repeats of '1')
* a separator of '0' follows
* the next value of 0 is also stack-encoded with the empty string
* ...

Because this value is a prime, the total number of separators is equal to the number of primes that are smaller than this value.

