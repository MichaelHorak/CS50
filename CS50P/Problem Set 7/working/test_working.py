from working import convert
import pytest


def main():
    test_am()
    test_correct_time()
    test_correct_hour()
    test_correct_minute()
    test_correct_format()


def test_am():
    with pytest.raises(ValueError):
        convert('13 AM to 5 PM')
    # assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    # assert convert('13 AM to 5 PM') == ValueError


def test_correct_time():
    assert convert('9 AM to 5 PM') == '09:00 to 17:00'
    assert convert('9:00 AM to 5:00 PM') == '09:00 to 17:00'
    assert convert('10 PM to 8 AM') == '22:00 to 08:00'
    assert convert('10:30 PM to 8:50 AM') == '22:30 to 08:50'


def test_correct_hour():
    with pytest.raises(ValueError):
        convert('15:30 AM to 5:00 PM')
# printing hours off by one
# printing minutes off by five
# not raising ValueError when user omits " to "
# not raising ValueError for out-of-range times


def test_correct_minute():
    with pytest.raises(ValueError):
        convert('11:77 AM to 4:99 PM')


def test_correct_format():
    with pytest.raises(ValueError):
        convert('5 AM - 1 PM')


if __name__ == "__main__":
    main()
