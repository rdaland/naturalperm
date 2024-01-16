from .naturalperm import natperm, natperminv

REALLY_BIG_NUMBER = 10000


def orbit(x: int, escape: int = REALLY_BIG_NUMBER, f=natperm) -> list[int]:
    orb = [x]
    while orb[-1] < escape:
        orb.append(f(orb[-1]))
        if orb[-1] == orb[0]:
            return orb[:-1]
    return orb[1:]


print(f"| n   | orbit |")
print(f"| :-- |  :--  |")
for i in [91, 92, 93, 94, 96, 100]:
    print(f"| {i}  | {orbit(i, f=natperminv)} |")
