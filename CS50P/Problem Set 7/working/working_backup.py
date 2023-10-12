import re
import sys


def main():
    print(convert(input("Hours: ")))


def convert(s):
    try:
        x = re.search(r"^([0-9]{1,2})(?::|)([0-9]{2}|)(?: )([AMP]{2})(?: )(?:to)(?: )([0-9]{1,2})(?::|)([0-9]{2}|)(?: )([AMP]{2})", s)
        h1 = int(x.group(1))
        # assigning first hour value to the variable
        # print(h1)
        if x.group(2):
            # if 1st min var contains a value
            m1 = int(x.group(2))
            # validate first min var
            validate_mins(m1)
            if m1 < 10:
                m1 = '0' + str(m1)
        else:
            m1 = str('00')
        f1 = x.group(3)
        h2 = int(x.group(4))
        # assigning second hour value to the variable
        # print(h2)
        if x.group(5):
            # if 2nd min var contains a value
            m2 = int(x.group(5))
            # validate second min var
            validate_mins(m2)
            if m2 < 10:
                m2 = '0' + str(m2)
        else:
            m2 = str('00')
        f2 = x.group(6)
        validate_hours(h1)
        validate_hours(h2)
        # validating both hour values

        # AM / PM
        # PM + 12
        # < 10 ^ > 10
        # for both times
        if f1 == 'AM':
            if h1 < 10:
                h1 = '0' + str(h1)
            elif h1 == 12:
                h1 = '00'
        else:
            # f1 = PM
            if h1 == 12:
                h1 = '12'
            else:
                h1 = h1 + 12

        if f2 == 'AM':
            if h2 < 10:
                h2 = '0' + str(h2)
            elif h2 == 12:
                h2 = '00'
        else:
            # f2 = PM
            if h2 == 12:
                h2 = '12'
            else:
                h2 = (h2 + 12)

        result = str(h1) + ':' + str(m1) + ' to ' + str(h2) + ':' + str(m2)

        # return x.groups()
        return result
    except ValueError:
        sys.exit('ValueError')
    except AttributeError:
        sys.exit('ValueError')

#     9:00 AM to 5:00 PM
#       error 13:00 PM to 5:00 PM
#       error 12:60 PM to 5:00 PM
#       ('9', '00', 'AM', '5', '00', 'PM')
#     9 AM to 5 PM
#       ('9', '', 'AM', '5', '', 'PM')
# Raise a ValueError instead if the input to convert is not in either of
# those formats or if either time is invalid (e.g., 12:60 AM, 13:00 PM,
# etc.).


def validate_hours(hours):
    if hours < 13:
        pass
    else:
        raise ValueError


def validate_mins(mins):
    if mins > 59:
        raise ValueError


if __name__ == "__main__":
    main()
