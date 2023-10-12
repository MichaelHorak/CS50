def main():
    vanity = input("Input a vanity plate: ")
    if is_valid(vanity):
        print("Valid")
    else:
        print("Invalid")


def is_valid(x):
    # -All vanity plates must start with at least two letters.
    if len(x) < 2:
        start = False
    else:
        char0 = x[0].isdigit()
        char1 = x[1].isdigit()
        if char0 or char1:
            start = False
        else:
            start = True
    # -vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.
    if 1 < len(x) < 7:
        max_char = True
    else:
        max_char = False
    # -Numbers cannot be used in the middle of a plate; they must come at the end.
    vlist = []
    for i in range(2, len(x)):
        if x[i].isdigit():
            vlist.append('digit')
        else:
            vlist.append('letter')
    if '\'digit\', \'letter\'' in str(vlist):
        mid_num = False
    else:
        mid_num = True
    forbid_chars = ['.', ' ', '?', ',', '!', '\"', '\'', '–', '[', ']', '(', ')', '–', '—', '...', ':', ';']
    nplist = []
    # -No periods, spaces, or punctuation marks are allowed.
    for i in range(0, len(x)):
        if x[i] in forbid_chars:
            nplist.append('False')
        else:
            nplist.append('True')
    if 'False' in str(nplist):
        no_periods = False
    else:
        no_periods = True
    # The first number used cannot be a ‘0’
    nolist = []
    for i in range(2, len(x)):
        if x[i].isdigit():
            nolist.append(x[i])

    if len(nolist) == 0:
        first_no = True
    else:
        if int(nolist[0]) == 0:
            first_no = False
        else:
            first_no = True
    # is_valid returns True if s meets all requirements
    # and False if it does not.
    if start and max_char and mid_num and no_periods and first_no:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
