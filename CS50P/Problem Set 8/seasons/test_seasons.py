from seasons import validate
import pytest


def main():
    test_valid_input()
    test_validate()


def test_valid_input():
    with pytest.raises(SystemExit):
        validate('January 1, 1999')
    #     validate('January 1, 1999')


def test_validate():
    assert validate('1999-01-01') == (1999, 1, 1)
    assert validate('1901-12-03') == (1901, 12, 3)
    assert validate('2003-09-11') == (2003, 9, 11)


if __name__ == "__main__":
    main()
