import re


def main():
    print(count(input("Text: ")))


def count(s):
    matches = re.findall(r"(\b[uU][mM]\b)+", s)
    return len(matches)
# input str
# output int number of times 'um' appears case insensitively
# hello, um, world
# 1
# yummy
# 0
# um
# 1
# um?
# 1
# Um, thanks for the album
# 1
# Um, thanks, um...
# 2

# re comes with findall
# \b is a boundary between \w and \W


if __name__ == "__main__":
    main()
