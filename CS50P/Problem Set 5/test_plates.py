from plates import is_valid


def main():
    test_start()
    test_max_chars()
    test_min()
    test_middle_numbers()
    test_first_no()
    test_no_special_chars()


def test_start():
    assert is_valid('VANI') == True
    assert is_valid('AB') == True
    assert is_valid('T2flah') == False
    assert is_valid('22XO') == False
    assert is_valid('3') == False
    assert is_valid('A') == False
    assert is_valid('86') == False
    # All vanity plates must start with at least two letters


def test_max_chars():
    assert is_valid('MAXSIX') == True
    assert is_valid('SEVENEL') == False
# “… vanity plates may contain a maximum of 6 characters (letters or numbers)


def test_min():
    assert is_valid('XY') == True
    assert is_valid('F') == False
# and a minimum of 2 characters.


def test_middle_numbers():
    assert is_valid('END60') == True
    assert is_valid('MID6LE') == False
# Numbers cannot be used in the middle of a plate;
# they must come at the end.


def test_first_no():
    assert is_valid('FIR1') == True
    assert is_valid('FIR012') == False
# The first number used cannot be a ‘0’


def test_no_special_chars():
    assert is_valid('HI2023') == True
    assert is_valid('HiWor!') == False
    assert is_valid('HI.wo') == False
    assert is_valid('HI wo') == False
    assert is_valid('HIwo?') == False
# “No periods, spaces, or punctuation marks are allowed.”


if __name__ == "__main__":
    main()
