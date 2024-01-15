from collections import Counter
from typing import List, Optional
from naturalperm.binary import BinaryMorphism
from naturalperm.primefac import PrimeFacMorphism
REALLY_BIG_NUMBER = 100000


def natperm(n: int) -> int:
    return BinaryMorphism.decode(PrimeFacMorphism.encode(n))


def natperminv(n: int) -> int:
    return PrimeFacMorphism.decode(BinaryMorphism.encode(n))


def orbit(x: int, escape: int = REALLY_BIG_NUMBER, f = natperm) -> List[Optional[int]]:
    orb = [x]
    while orb[-1] < escape:
        orb.append(f(orb[-1]))
        if orb[-1] == orb[0]:
            return tuple(orb[:-1])
    return orb[1:-1]


def main():
    print(f"| n   | orbit |")
    print(f"| :-- |  :--  |")
    for i in range(50):
        print(f"| {i}  | {orbit(i)} |")


if __name__ == '__main__':
    main()
