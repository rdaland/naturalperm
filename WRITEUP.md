
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

Because this value is a prime, the total number of separators is equal to the number of primes that are smaller than this value, and there are no other factors; so we get a string of zeros.

## `pdec`: inverting `penc`

The fundamental question is, is it guaranteed that every canonical binary string can be interpreted as a `penc`-encoded integer? In other words, is it possible to recover a unique prime factorization from every canonical binary string? The short answer is, yes — because we have taken special care that every mapping discussed here is invertible. As a brief, informal argument, consider that every canonical binary string begins with a '1' and continues with some sequence of '1's and '0's. We can split the string on '0', separating it into a sequence of 1-sequences. The 1-sequences can be of length 0, and this will occur exactly whenever the binary string contains two 0's in a row. Since 0's are different than 1's, the parsing is guaranteed to be unique — one symbol is used to separate stacks, and one symbol is used to indicate the size of each stack. So from every canonical binary string, it is possible to recover some prime factorization. And since integer multiplication commutes, the resulting integer is guaranteed to be 1-1 from the prime factorization.

## A detail: Off by one

The prime factorization theorem holds for positive integers (n > 0). Therefore `penc`/`pdec` encode a mapping from/to the **positive** integers to canonical binary strings. 

However, the `benc`/`bdec` encoding does naturally include 0 <—> '0'. The general idea is to define `naturalperm` as the composition of `benc` and `pdec` (or _vice versa_). While the mapping is still invertible if the domain includes 0 and the range does not (or _vice versa_), it will not be a permutation. Fortunately, it is easy to address this issue by adding a shift-by-one operation:
* `benc(n)` returns the canonical binary string for `n - 1`
* `bdec(s)` converts s to an integer, and then adds 1 to it

A similar effect could have been achieved with a shift-by-one operation in `penc`/`pdec`. I opted to do it in `benc`/`bdec` since this generally introduces a smaller perturbation to the binary string representation.

## Another detail: smallest values rightmost

In English, the convention is to render strings left-to-right, and to order binary strings so that the most significant bit is leftmost. I have followed this convention not only for `benc` encoding, but also for `penc` encoding. That is, in the prime mulitplicities list, the primes are sorted so that the highest values occur leftmost; and I ordered the binary string in the same way. This choice was made mostly on the basis of human readability: it has greater parallelism between the string-as-bits and string-as-multiplicity-stacks interpretation; in both cases the most significant base/prime is leftmost.

For the implementation of `benc`/`bdec`, it is more convenient to start from the least significant prime. This is because primes can be efficiently enumerated starting from the least one (2). But to process starting from the most significant prime, one must know in advance how many primes are associated with the multiplicity list. There are several options and any of them can be made to work, though some are more elegant than others. It truly is an implementational details, and it is mentioned here only because one must handle it somehow.

A key thing is that if the similar "least significant bits rightmost" is shared between the `benc` and `penc` mappings, (and `naturalperm` is defined as the composition of `bdec` and `penc` as defined above), then `naturalperm` has the property that smaller integers will in general be mapped to smaller integers, while larger integers will in general be mapped to larger integers. However, as we will show shortly, it is not an identity map.

# `naturalperm`

For the reader's enjoyment I have rendered the mapping for the first 100 values, along with the inverse.

| n  | natperm(n)| natperm^-1 |
|----|-----------|------------|
| 1  |         1 |          1 |
| 2  |         2 |          2 |
| 3  |         3 |          3 |
| 4  |         4 |          4 |
| 5  |         5 |          5 |
| 6  |         6 |          6 |
| 7  |         9 |          9 |
| 8  |         8 |          8 |
| 9  |         7 |          7 |
| 10 |        10 |         10 |
| 11 |        17 |         15 |
| 12 |        12 |         12 |
| 13 |        33 |         25 |
| 14 |        18 |         18 |
| 15 |        11 |         27 |
| 16 |        16 |         16 |
| 17 |        65 |         11 |
| 18 |        14 |         14 |
| 19 |       129 |         21 |
| 20 |        20 |         20 |
| 21 |        19 |         35 |
| 22 |        34 |         30 |
| 23 |       257 |         45 |
| 24 |        24 |         24 |
| 25 |        13 |         49 |
| 26 |        66 |         50 |
| 27 |        15 |         75 |
| 28 |        36 |         36 |
| 29 |       513 |        125 |
| 30 |        22 |         54 |
| 31 |      1025 |         81 |
| 32 |        32 |         32 |
| 33 |        35 |         13 |
| 34 |       130 |         22 |
| 35 |        21 |         33 |
| 36 |        28 |         28 |
| 37 |      2049 |         55 |
| 38 |       258 |         42 |
| 39 |        67 |         63 |
| 40 |        40 |         40 |
| 41 |      4097 |         77 |
| 42 |        38 |         70 |
| 43 |      8193 |        105 |
| 44 |        68 |         60 |
| 45 |        23 |        175 |
| 46 |       514 |         90 |
| 47 |     16385 |        135 |
| 48 |        48 |         48 |
| 49 |        25 |        121 |
| 50 |        26 |         98 |
| 51 |       131 |        147 |
| 52 |       132 |        100 |
| 53 |     32769 |        245 |
| 54 |        30 |        150 |
| 55 |        37 |        225 |
| 56 |        72 |         72 |
| 57 |       259 |        343 |
| 58 |      1026 |        250 |
| 59 |     65537 |        375 |
| 60 |        44 |        108 |
| 61 |    131073 |        625 |
| 62 |      2050 |        162 |
| 63 |        39 |        243 |
| 64 |        64 |         64 |
| 65 |        69 |         17 |
| 66 |        70 |         26 |
| 67 |    262145 |         39 |
| 68 |       260 |         44 |
| 69 |       515 |         65 |
| 70 |        42 |         66 |
| 71 |    524289 |         99 |
| 72 |        56 |         56 |
| 73 |   1048577 |         91 |
| 74 |      4098 |        110 |
| 75 |        27 |        165 |
| 76 |       516 |         84 |
| 77 |        41 |        275 |
| 78 |       134 |        126 |
| 79 |   2097153 |        189 |
| 80 |        80 |         80 |
| 81 |        31 |        143 |
| 82 |      8194 |        154 |
| 83 |   4194305 |        231 |
| 84 |        76 |        140 |
| 85 |       133 |        385 |
| 86 |     16386 |        210 |
| 87 |      1027 |        315 |
| 88 |       136 |        120 |
| 89 |   8388609 |        539 |
| 90 |        46 |        350 |
| 91 |        73 |        525 |
| 92 |      1028 |        180 |
| 93 |      2051 |        875 |
| 94 |     32770 |        270 |
| 95 |       261 |        405 |
| 96 |        96 |         96 |
| 97 |  16777217 |        169 |
| 98 |        50 |        242 |
| 99 |        71 |        363 |
| 100 |       52 |        196 |

Upon cursory inspection, some things jump out to me. 

## Fixed points

Here are the fixed points from the list above:
* 1, 2, 3, 4, 5, 6, 8, 10, 12, 16, 20, 24, 32, 40, 48, 64, 80, 96

This set includes all powers of 2. In fact every fixed point in this set is of the form `p * 2^k` where p is one of {1, 2, 3, 5}. Note that 7 is not a fixed point, and neither is 7 * 2^1 = 14. One is tempted to conjecture that if _m_ and _n_ are both fixed points of this mapping, then so is _m * n_. This conjecture is falsified by _5 * 6 = 3 * 10_: 30 is not a fixed point. 

## Primes

The mapping is nondecreasing on prime numbers across the board. Starting from 7, it is strictly increasing (`natperm(p) > p for all p > 5 if p is prime`). In fact, `natperm(p) = 2^k[p] + 1`, where k is the prime's ordinality (2 is the 0th prime, 3 is the 1th prime, etc..); this fact falls out from the construction of `natperm`. 

## Other k-cycles

There are a number of 2-cycles in the first 100: 
* (7, 9)
* (14, 18) 
* (28, 36)
* (56, 72)

There are no 3-cycles in the first 100. 

## Escaping orbit

The orbit of a value is defined as the sequence of values obtained by repeatedly applying a mapping. Here are the first 7 values in the orbit for 11, shown both as raw numbers and after taking the natural log:
* raw: 11 —> 17 —> 65 —> 69 —> 515 —> 134217733 —> 18447026098442076193
* ln(raw): 2.40 —> 2.83 —> 4.17 —> 4.23 —> 6.24 —> 18.71 —> 44.36

While the log value is increasing by an average of 1 per step at first, it then increases by 12.5 on the fifth step, and then by 26 on the sixth step. This indicates super-exponential growth!

The notion of orbit is familiar from the analysis of fractals and other chaotic dynamic systems. For example, the Mandelbrot set is defined as the set of complex numbers which don't escape under iteration. In the Mandelbrot setting, |z| > 2 implies |f(z)| > |z|, in other once the magnitude gets bigger than 2, it will continue to grow. For quick and dirty analysis of `naturalperm`, I defined escape as reaching a magnitude of 1 billion. 

I then checked which items escape in the first 1000 integers. It turns out that nearly all starting values escape, and the time to escape is between 3 and 8 steps for the first 100 or 200 integers, but quickly drops to 2-3 steps for most integers above 200. The fixed points and 2-cycles reported above already make up the majority of fixed points and 2-cycles I found, and I found no other k-cycles besides 2-cycles. 

I repeated the analysis for the inverse mapping. By symmetry, we might expect similar results; and that is exactly what I found. Both of these mappings then have similar statistical properties. Over some range of small numbers, they generally map about as many numbers to smaller numbers as larger numbers. However, because there are so many more large numbers than small numbers, the vast majority of orbits that start with small numbers "escape" (consist mostly of much larger numbers than they start with).
