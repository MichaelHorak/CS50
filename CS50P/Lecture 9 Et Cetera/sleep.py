# print out number of sheep

# def main():
#     n = int(input("What's n? "))
#     for i in range(n):
#         print("🐑" * i)
#
#
# if __name__ == "__main__":
#     main()

# V2
# def main():
#     n = int(input("What's n? "))
#     for s in sheep(n):
#         print(s)
#
#
# def sheep(n):
#     flock = []
#     for i in range(n):
#         flock.append("🐑" * i)
#     return flock
#
#
# if __name__ == "__main__":
#     main()

# V3 generators, yield
def main():
    n = int(input("What's n? "))
    for s in sheep(n):
        print(s)


def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()

# v4 iterators
