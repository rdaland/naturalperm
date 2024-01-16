from naturalperm.binary import BinaryMorphism


def test_binary_morphism_encoder():
    assert BinaryMorphism.encode(1) == '1'
    assert BinaryMorphism.encode(2) == '10'
    assert BinaryMorphism.encode(13) == '1101'


def test_binary_morphism_decoder():
    assert BinaryMorphism.decode('1') == 1
    assert BinaryMorphism.decode('10') == 2
    assert BinaryMorphism.decode('1101') == 13


def test_binary_inverses():
    for n in range(1, 101):
        assert BinaryMorphism.decode(BinaryMorphism.encode(n)) == n
