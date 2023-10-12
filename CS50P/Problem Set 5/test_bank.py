from bank import value


def main():
    test_0()


def test_0():
    assert value('hello') == 0
    assert value('HELLO') == 0


def test_20():
    assert value('How do you do') == 20


def test_100():
    assert value('Praise the lord') == 100
