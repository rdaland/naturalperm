from typing import Protocol
from abc import abstractmethod

class Isomorphism(Protocol):

    @staticmethod
    def encode(n: int) -> str:
        pass

    @staticmethod
    def decode(cbs: str) -> int:
        pass
