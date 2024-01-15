from naturalperm.isomorphism import Isomorphism


class BinaryMorphism(Isomorphism):

    @staticmethod
    def encode(n: int) -> str:
        """Outputs a canonical binary string representing the binary encoding of input

        Example: encode(13) = "1101"
        """
        return format(n, "b")

    @staticmethod
    def decode(cbs: str) -> int:
        """Outputs an integer representing the binary decoding of the canonical binary string

        Example: decode("1101") = 13
        """
        return int(cbs, 2)
