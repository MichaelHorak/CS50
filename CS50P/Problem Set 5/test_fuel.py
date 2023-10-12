from fuel import convert, gauge
import pytest


def main():
    test_ints()
    test_value_err()
    test_zero_div()
    test_e()
    test_per()
    test_f()

def test_ints():
    assert convert('1/2') == 50


# raising ValueError in convert
def test_value_err():
    with pytest.raises(ValueError):
        assert convert('cat/dog')


# raising ZeroDivisionError in convert
def test_zero_div():
    with pytest.raises(ZeroDivisionError):
        assert convert('4/0')


# labeling 1% as E in gauge
def test_e():
    assert gauge(1) == 'E'


# printing % in gauge
def test_per():
    assert gauge(50) == '50%'


# labeling 99% as F in gauge
def test_f():
    assert gauge(99) == 'F'


if __name__ == "__main__":
    main()
