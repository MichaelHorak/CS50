import re
import sys


def main():
    print(validate(input("IPv4 Address: ")))
    # ip = input("IPv4 Address: ")
    # print(validate(ip))
    # validate(ip)


def validate(ip):
    group = []
    val = []
    if matches := re.search(r"^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$", ip):
        for i in range(1, 5):
            group.append((int(matches.group(i))))

        for i in range(0, 4):
            if group[i] > 255:
                # print(f"{group[i]} is false")
                val.append(False)
            else:
                # print(f"{group[i]} is true")
                val.append(True)

    try:
        if val[0] and val[1] and val[2] and val[3]:
            return True
        else:
            return False

    except IndexError:
        # sys.exit('Index Error, IP is false')
        return False

    # use re.search
    # for re.search use group capturing
    # use regex
    # use raw string r"harvard\.edu"


if __name__ == "__main__":
    main()

# don't forget to test the code with test_numb3rs.py
# two or more functions
