# def main():
#     yell(["This", "is", "CS50"])
#
#
# def yell(words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
#
#
# if __name__ == "__main__":
#     main()


# V2
# def main():
#     yell("This", "is", "CS50")
#
#
# def yell(*words):
#     uppercased = []
#     for word in words:
#         uppercased.append(word.upper())
#     print(*uppercased)
#
#
# if __name__ == "__main__":
#     main()

# V3 map
# def main():
#     yell("This", "is", "CS50")
#
#
# def yell(*words):
#     uppercased = map(str.upper, words)
#     print(*uppercased)
#
#
# if __name__ == "__main__":
#     main()

# V4 list comprehensions
def main():
    yell("This", "is", "CS50")


def yell(*words):
    uppercased = [word.upper() for word in words]
    print(*uppercased)


if __name__ == "__main__":
    main()
    