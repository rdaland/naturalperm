from typing import List
from primefac import primefac, primegen

def int_to_binary_string(n: int) -> str:
    return format(n, "b")


def binary_string_to_int(bs: str) -> int:
    return int(bs, 2)


SOME_BIG_INT = 600851475143
def main():
    x = binary_string_to_int('100')
    print(x)

if __name__ == '__main__':
    main()
