from naturalperm.primefac import PrimeFacMorphism


def test_primefac_morphism_encoder():
    assert PrimeFacMorphism.encode(1) == '1'
    assert PrimeFacMorphism.encode(2) == '10'
    assert PrimeFacMorphism.encode(3) == '11'
    assert PrimeFacMorphism.encode(4) == '100'
    assert PrimeFacMorphism.encode(5) == '101'
    assert PrimeFacMorphism.encode(6) == '1000'
    assert PrimeFacMorphism.encode(7) == '111'
    assert PrimeFacMorphism.encode(27) == '100011'


def test_primefac_morphism_decoder():
    assert PrimeFacMorphism.decode('1') == 1
    assert PrimeFacMorphism.decode('10') == 2
    assert PrimeFacMorphism.decode('11') == 3
    assert PrimeFacMorphism.decode('100') == 4
    assert PrimeFacMorphism.decode('101') == 5
    assert PrimeFacMorphism.decode('1000') == 6
    assert PrimeFacMorphism.decode('111') == 7
    assert PrimeFacMorphism.decode('100011') == 27


def test_primefac_inverses():
    for n in range(1, 101):
        assert PrimeFacMorphism.decode(PrimeFacMorphism.encode(n)) == n
