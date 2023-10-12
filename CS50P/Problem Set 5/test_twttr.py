from twttr import shorten


def test_caps():
    assert shorten('MISSISSIPPI') == 'MSSSSPP'


def test_potatoes():
    assert shorten("potatoes") == 'ptts'


def test_cs50():
    assert shorten('CS50') == 'CS50'

def test_punctuation():
    assert shorten('?!?.,') == '?!?.,'