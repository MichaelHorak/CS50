def main():
    vanity = input("Input a vanity plate: ")
    is_valid(vanity)


def is_valid(x):
    # is_valid returns True if s meets all requirements
    # and False if it does not.
    if start(x) and max_char(x) and mid_num(x) and no_periods(x) and first_no(x):
        print('Valid')
    else:
        print('Invalid')


def start(x):
    # -All vanity plates must start with at least two letters.
    if len(x) < 2:
        return False
    else:
        char0 = x[0].isdigit()
        char1 = x[1].isdigit()
        if char0 and char1:
            return False
        else:
            return True


def max_char(x):
    # -vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if 1 < len(x) < 7:
        return True
    else:
        return False


def mid_num(x):
    vlist = []
    for i in range(2, len(x)):
        if x[i].isdigit():
            vlist.append('digit')
        else:
            vlist.append('letter')
    if '\'digit\', \'letter\'' in str(vlist):
        return False
    else:
        return True


def no_periods(x):
    forbid_chars = ['.', ' ', '?', ',', '!', '\"', '\'', '–', '[', ']', '(', ')', '–', '—', '...', ':', ';']
    nplist = []
    # -No periods, spaces, or punctuation marks are allowed.
    for i in range(0, len(x)):
        if x[i] in forbid_chars:
            nplist.append('False')
        else:
            nplist.append('True')
    if 'False' in str(nplist):
        return False
    else:
        return True


def first_no(x):
    # The first number used cannot be a ‘0’.”
    nolist = []
    for i in range(2, len(x)):
        if x[i].isdigit():
            nolist.append(x[i])
            if int(nolist[0]) > 0:
                return True
            else:
                return False
        else:
            return True


main()
