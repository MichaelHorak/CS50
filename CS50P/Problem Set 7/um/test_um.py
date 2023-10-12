from um import count
import pytest


def main():
    test_beginningend()
    test_special_chars()
    test_caps()


def test_beginningend():
    assert count('um') == 1
    assert count('Humble') == 0


def test_special_chars():
    assert count('um?') == 1
    assert count('album?') == 0


def test_caps():
    assert count('UM, thank you') == 1
    assert count('uM, thank you') == 1
    assert count('um, thank you') == 1
    assert count('UMNO, thank you') == 0
    assert count('hum, thank you') == 0


if __name__ == "__main__":
    main()
