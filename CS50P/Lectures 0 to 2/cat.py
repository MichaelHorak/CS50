# i = 0
# while i < 3:
#     print('meow')
#     i += 1
#
# for _ in range(99):
#     print("meow")


# while True:
#     n = int(input("What's n? "))
#     if n > 0:
#         break
#
# for _ in range(n):
#     print('meow')

# print("meow\n" * n, end="")

def main():
    number = get_number()
    meow(number)


def meow(n):
    for _ in range(n):
        print("meow")


def get_number():
    while True:
        n = int(input("What's n? "))
        if n > 0:
            return n


main()
