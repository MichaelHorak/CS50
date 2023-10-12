from numb3rs import validate


def main():
    test_255()
    test_1000()
    test_str()
    test_1()
    test_2()
    test_3()
    test_4()


def test_255():
    assert validate('255.255.255.255') == True
    assert validate('256.255.255.255') == False


def test_1000():
    assert validate('1.2.3.1000') == False
    assert validate('1.0.0.0') == True


def test_str():
    assert validate('cat') == False


def test_1():
    assert validate('999.11.223.4') == False
    assert validate('99.11.223.4') == True


def test_2():
    assert validate('245.256.255.255') == False
    assert validate('245.244.244.244') == True


def test_3():
    assert validate('172.23.1000.1') == False
    assert validate('172.23.100.1') == True


def test_4():
    assert validate('6.6.6.6666') == False
    assert validate('6.66.66.6') == True


if __name__ == "__main__":
    main()
