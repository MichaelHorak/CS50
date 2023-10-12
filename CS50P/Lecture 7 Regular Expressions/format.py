import re

name = input("What's your name? ").strip()
# V1
# if "," in name:
#     last, first = name.split(", ")
#     name = f"{first} {last}"
# print(f"hello, {name}")

# V2 using re.search
# matches = re.search(r"^(.+), (.+)$", name)
# if matches:
#     last, first = matches.groups()
#     name = f"{first} {last}"
# print(f"hello, {name}")

# V3 matches.groups
# matches = re.search(r"^(.+), *(.+)$", name)
# if matches:
#     name = matches.group(2) + " " + matches.group(1)
# print(f"hello, {name}")

# V4 := walrus operator assign operator & ask if
if matches := re.search(r"^(.+), *(.+)$", name):
    name = matches.group(2) + " " + matches.group(1)
print(f"hello, {name}")
