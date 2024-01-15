from typing import Protocol

class Isomorphism(Protocol):

    @staticmethod
    def encode(n: int) -> str:
        pass

    @staticmethod
    def decode(cbs: str) -> int:
        pass
