# 1
# print("hello, world")

# 2
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("X is not an integer")
#
# print(f"x is {x}")

# 3
# try:
#     x = int(input("What's x? "))
# except ValueError:
#     print("x is not an integer")
# else:
#     print(f"x is {x}")

# 4
# while True:
#     try:
#         x = int(input("What's x? "))
#     except ValueError:
#         print("x is not an integer")
#     else:
#         break
#
# print(f"x is {x}")

# 5
# while True:
#     try:
#         x = int(input("What's x? "))
#         break
#     except ValueError:
#         print("x is not an integer")
#
# print(f"x is {x}")

# 6
# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             break
#
#     return x
#
# main()

# 7
# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             x = int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#         else:
#             return x
#
#
# main()

# 8
# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             print("x is not an integer")
#
#
# main()

# 9
# def main():
#     x = get_int()
#     print(f"x is {x}")
#
#
# def get_int():
#     while True:
#         try:
#             return int(input("What's x? "))
#         except ValueError:
#             pass
#
#
# main()

# 10
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")


def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            pass


main()
