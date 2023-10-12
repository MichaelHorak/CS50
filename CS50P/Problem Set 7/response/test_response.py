from response import email_check


def main():
    test_at_symbol()
    test_suffix()
    test_prefix()


def test_at_symbol():
    assert email_check('horakm@ymail.com') == 'Valid'
    assert email_check('horakm@@ymail.com') == 'Invalid'
    assert email_check('horakm@@@ymail.com') == 'Invalid'
    assert email_check('horakmymail.com') == 'Invalid'


def test_suffix():
    assert email_check('malan@harvard.edu') == 'Valid'
    assert email_check('malan@harvardedu') == 'Invalid'
    assert email_check('malan@harvard..edu') == 'Invalid'


def test_prefix():
    assert email_check('horak.michael@icloud.com') == 'Valid'
    assert email_check('@icloud.com') == 'Invalid'


if __name__ == "__main__":
    main()
