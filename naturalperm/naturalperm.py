from .binary import BinaryMorphism
from .primestack import PrimeFacMorphism


def natperm(n: int) -> int:
    return BinaryMorphism.decode(PrimeFacMorphism.encode(n))


def natperminv(n: int) -> int:
    return PrimeFacMorphism.decode(BinaryMorphism.encode(n))
