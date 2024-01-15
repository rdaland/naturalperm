from .naturalperm import natperm

REALLY_BIG_NUMBER = 100000


def orbit(x: int, escape: int = REALLY_BIG_NUMBER, f=natperm) -> list[int]:
    orb = [x]
    while orb[-1] < escape:
        orb.append(f(orb[-1]))
        if orb[-1] == orb[0]:
            return orb[:-1]
    return orb[1:]


print(f"| n   | orbit |")
print(f"| :-- |  :--  |")
for i in range(1, 51):
    print(f"| {i}  | {orbit(i)} |")
