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


#def encode_primefac_as_binary_string()


def main():
    x = binary_string_to_int('100')
    print(x)

if __name__ == '__main__':
    main()
