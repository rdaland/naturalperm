from collections import Counter
from typing import List
from math import prod
from primefac import primefac, primegen

def int_to_binary_string(n: int) -> str:
    return format(n, "b")


def binary_string_to_int(bs: str) -> int:
    return int(bs, 2)


def int_to_prime_factorization(n: int) -> List[int]:
    return sorted(primefac(n))


def prime_factorization_to_int(plist: List[int]) -> int:
    return prod(plist)


def encode_primefac_as_binary_string(factors: List[int]) -> str:
    if not factors:
        return '0'
    multiset = Counter(factors)
    sbuf = [multiset[prime] * '1' for prime in primegen(max(factors) + 1)]
    return '0'.join(sbuf[::-1])


def decode_binary_string_as_primefac(bs: str) -> List[int]:
    if bs == '0':
        return []
    plist, pgen = [], primegen()
    for prime_multiplicity in bs[::-1].split('0'):
        prime = next(pgen)
        for tick in prime_multiplicity:
            plist.append(prime)
    return plist


def natperm(n: int) -> int:
    if n < 1:
        raise ValueError("natperm is only defined for positive integers")
    prime_factorization = int_to_prime_factorization(n)
    encoded_binary_string = encode_primefac_as_binary_string(prime_factorization)
    return 1 + binary_string_to_int(encoded_binary_string)

def natperminv(n: int) -> int:
    if n < 1:
        raise ValueError("natperm is only defined for positive integers")
    binary_string = int_to_binary_string(n - 1)
    prime_factorization = decode_binary_string_as_primefac(binary_string)
    return prime_factorization_to_int(prime_factorization)


def main():
    for i in range(1, 100):
        print(i, natperm(i), natperminv(i))

if __name__ == '__main__':
    main()
