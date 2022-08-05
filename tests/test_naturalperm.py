import pytest
from naturalperm import __version__
from naturalperm.naturalperm import (
    int_to_binary_string,
    binary_string_to_int,
    int_to_prime_factorization,
    prime_factorization_to_int,
    encode_primefac_as_binary_string,
    decode_binary_string_as_primefac,
    natperm,
    natperminv,
)

SOME_BIGINT = 600851475143
BIGINT_FACTORS = [71, 839, 1471, 6857]

# illustrate module paths
def test_version():
    assert __version__ == '0.1.0'


def test_int_to_binary_string():
    assert int_to_binary_string(4) == '100'
    with pytest.raises(ValueError):
        int_to_binary_string('4')


def test_binary_string_to_int():
    assert binary_string_to_int('100') == 4
    assert binary_string_to_int('0100') == 4
    with pytest.raises(ValueError):
        binary_string_to_int('1.1')


def test_int_to_prime_factorization():
    assert int_to_prime_factorization(SOME_BIGINT) == BIGINT_FACTORS


def test_prime_factorization_to_int():
    assert prime_factorization_to_int(BIGINT_FACTORS) == SOME_BIGINT


def test_encode_primefac_as_binary_string():
    assert encode_primefac_as_binary_string([]) == '0'
    assert encode_primefac_as_binary_string([2, 2, 3]) == '1011'


def test_decode_binary_string_as_primefac():
    assert decode_binary_string_as_primefac('0') == []
    assert decode_binary_string_as_primefac('1011') == [2, 2, 3]


def test_natperm__basic():
    assert natperm(1) == 1
    with pytest.raises(ValueError):
        natperm(0)


def test_natperminv__basic():
    assert natperminv(1) == 1
    with pytest.raises(ValueError):
        natperminv(0)


def test_natperm_and_natperminv_are_inverses():
    for i in range(1, 100):
        assert natperminv(natperm(i)) == i
        assert natperminv(natperm(i)) == i
