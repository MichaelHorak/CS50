# WRITING

# names = []
#
# for _ in range(3):
#     names.append(input("What's your name? "))
#
# for name in sorted(names):
#     print(f"hello, {name}")

# v2
# name = input("What's your name? ")
#
# file = open("names.txt", "w")
# file.write(name)
# file.close()

# v3
# name = input("What's your name? ")
#
# file = open("names.txt", "a")
# file.write(f"{name}\n")
# file.close()

# v4
# name = input("What's your name? ")
#
# with open("names.txt", "a") as file:
#     file.write(f"{name}\n")

# READING
# v5
# with open("names.txt", "r") as file:
#     lines = file.readlines()
#
# for line in lines:
#     print("hello,", line.rstrip())

# v6 read better
# with open("names.txt", "r") as file:
#     for line in file:
#         print("hello,", line.strip())

# v7 sort it
# names = []
#
# with open("names.txt") as file:
#     for line in file:
#         names.append(line.rstrip())
#
# for name in sorted(names):
#     print(f"hello, {name}")

# v8 sort it easily
names = []

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
