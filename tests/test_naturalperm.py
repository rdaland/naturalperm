import pytest
import itertools
from naturalperm import __version__
from naturalperm.naturalperm import (
    benc,
    bdec,
    penc,
    pdec,
    natperm,
    natperminv,
)

SOME_BIGINT = 600851475143
BIGINT_FACTORS = [71, 839, 1471, 6857]

# illustrate module paths
def test_version():
    assert __version__ == '0.1.0'

def strip_leading_zeros(binstr: str) -> str:
    if len(binstr) == 1:
        return binstr
    try:
        return binstr[binstr.index('1'):]
    except ValueError:
        return '0'

def test_strip_leading_zeros():
    assert strip_leading_zeros('0') == '0'
    assert strip_leading_zeros('01') == '1'
    assert strip_leading_zeros('00') == '0'
    assert strip_leading_zeros('00000') == '0'
    

class TestBinaryTransformer:
    def test_benc(self):
        assert benc(1) == '0'
        assert benc(2) == '1'
        assert benc(3) == '10'

    def test_bdec(self):
        assert bdec('0') == 1
        assert bdec('1') == 2
        assert bdec('10') == 3

    def test_benc_and_bdec_are_inverses(self):
        for i in range(1, 100 + 1):
            assert bdec(benc(i)) == i
        for bintuple in itertools.product('01', repeat=8):
            binstr = strip_leading_zeros(''.join(bintuple))
            assert benc(bdec(binstr)) == binstr


class TestPrimeTransformer:
    def test_penc(self):
        with pytest.raises(ValueError):
            penc(0)
        assert penc(1) == '0'
        assert penc(2) == '1'
        assert penc(3) == '10'

    def test_pdec(self):
        assert pdec('0') == 1
        assert pdec('1') == 2
        assert pdec('10') == 3

    def test_penc_and_pdec_are_inverses(self):
        for i in range(1, 100 + 1):
            assert pdec(penc(i)) == i
        for primtuple in itertools.product('01', repeat=8):
            primstr = strip_leading_zeros(''.join(primtuple))
            assert penc(pdec(primstr)) == primstr


class TestNaturalPermutation:
    def test_natperm__basic(self):
        assert natperm(1) == 1
        with pytest.raises(ValueError):
            natperm(0)

    def test_natperminv__basic(self):
        assert natperminv(1) == 1
        with pytest.raises(ValueError):
            natperminv(0)

    def test_natperm_and_natperminv_are_inverses(self):
        for i in range(1, 100 + 1):
            assert natperminv(natperm(i)) == i
            assert natperminv(natperm(i)) == i
