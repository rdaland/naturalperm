from collections import Counter
from typing import List, Optional
from math import prod, log
from primefac import primefac, primegen

REALLY_BIG_NUMBER = 1000000000


def benc(n: int) -> str:
    return format(n - 1, "b")


def bdec(binstr: str) -> int:
    return int(binstr, 2) + 1


def penc(n: int) -> str:
    if n < 1:
        raise ValueError("Can only encode positive integers")
    if n == 1:
        return '0'
    prime_factors = list(primefac(n))
    prime_cts, prime_ceil = Counter(prime_factors), 1 + max(prime_factors)
    pstacks = [prime_cts[p] * '1' for p in primegen(prime_ceil)]
    return '0'.join(pstacks[::-1])


def pdec(primstr: str) -> int:
    pstacks = primstr[::-1].split('0')
    plist, pgen = [], primegen()
    for pstack in primstr[::-1].split('0'):
        plist.extend(len(pstack)*[next(pgen)])
    return prod(plist)


def natperm(n: int) -> int:
    if n < 1:
        raise ValueError("Can only permute positive integers")
    return bdec(penc(n))


def natperminv(n: int) -> int:
    if n < 1:
        raise ValueError("Can only permute positive integers")
    return pdec(benc(n))

##def orbit(x: int, escape: int = REALLY_BIG_NUMBER, f = natperm) -> List[Optional[int]]:
##    orb = [x]
##    while orb[-1] < escape:
##        orb.append(f(orb[-1]))
##        if orb[-1] == orb[0]:
##            return orb[:-1]
##    orb.append(None)
##    return orb


def main():
    for i in range(1, 50 + 1):
        print(i, natperm(i))


if __name__ == '__main__':
    main()
