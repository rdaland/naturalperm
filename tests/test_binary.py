from naturalperm.binary import BinaryMorphism


def test_binary_morphism_encoder():
    assert BinaryMorphism.encode(0) == '0'
    assert BinaryMorphism.encode(1) == '1'
    assert BinaryMorphism.encode(2) == '10'


def test_binary_morphism_decoder():
    assert BinaryMorphism.decode('0') == 0
    assert BinaryMorphism.decode('1') == 1
    assert BinaryMorphism.decode('10') == 2


def test_binary_inverses():
    for n in range(1, 101):
        assert BinaryMorphism.decode(BinaryMorphism.encode(n)) == n
