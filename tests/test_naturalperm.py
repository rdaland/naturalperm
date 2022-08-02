import pytest
from naturalperm import __version__
from naturalperm.naturalperm import (
    bit_to_int,
    int_to_binary_string,
    binary_string_to_int,
)

# illustrate module paths
def test_version():
    assert __version__ == '0.1.0'


def test_bit_to_int():
    assert bit_to_int('0') == 0
    assert bit_to_int('1') == 1
    with pytest.raises(ValueError):
        bit_to_int(0)
    with pytest.raises(ValueError):
        bit_to_int('00')
    with pytest.raises(ValueError):
        bit_to_int('2')


def test_int_to_binary_string():
    assert int_to_binary_string(4) == '100'
    with pytest.raises(ValueError):
        int_to_binary_string('4')


def test_binary_string_to_int():
    assert binary_string_to_int('100') == 4
    assert binary_string_to_int('0100') == 4
    with pytest.raises(ValueError):
        binary_string_to_int('1.1')

