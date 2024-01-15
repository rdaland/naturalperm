from collections import Counter
from math import prod
from primefac import primefac, primegen
from naturalperm.isomorphism import Isomorphism

class PrimeFacMorphism(Isomorphism):

    @staticmethod
    def encode(n: int) -> str:
        """Outputs a canonical binary string representing the primefac stack encoding of input"""
        prime_factors = list(primefac(n + 1))
        prime_cts, prime_ceil = Counter(prime_factors), 1 + max(prime_factors)
        pstacks = [prime_cts[p] * '1' for p in primegen(prime_ceil)]
        return '0'.join(pstacks[::-1])

    @staticmethod
    def decode(cbs: str) -> int:
        """Outputs an integer representing the primefac stack decoding of input"""
        plist, pgen = [], primegen()
        for pstack in cbs[::-1].split('0'):
            plist.extend(len(pstack)*[next(pgen)])
        return prod(plist) - 1
