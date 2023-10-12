# reading CSV
# with open("students.csv") as file:
#     for line in file:
#         row = line.rstrip().split(",")
#         print(f"{row[0]} is in {row[1]}")

# v2
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         print(f"{name} is in {house}")

# v3 sorting by sentences
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         students.append(f"{name} is in {house}")
#
# for student in sorted(students):
#     print(student)

# v4 sorting using dictionary
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {}
#         student["name"] = name
#         student["house"] = house
#         students.append(student)
#
# for student in students:
#     print(f"{student['name']} is in {student['house']}")

# v5 sorting using dictionary, sorting by function
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# def get_name(student):
#     return student["name"]
#
#
# for student in sorted(students, key=get_name, reverse=True):
#     print(f"{student['name']} is in {student['house']}")

# v6 sorting using dictionary, sorting by ANONYMOUS function
# students = []
#
# with open("students.csv") as file:
#     for line in file:
#         name, house = line.rstrip().split(",")
#         student = {"name": name, "house": house}
#         students.append(student)
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is in {student['house']}")

# v7 house>home list reader
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.reader(file)
#     for row in reader:
#         students.append({"name": row[0], "home": row[1]})
#
#     # for name, home in reader:
#     #     students.append("name": name, "home": home})
#
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# v8 using dictionary reader
# import csv
#
# students = []
#
# with open("students.csv") as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         students.append({"name": row["name"], "home": row["home"]})
#
# for student in sorted(students, key=lambda student: student["name"]):
#     print(f"{student['name']} is from {student['home']}")

# v9 inserting data into a csv file
# import csv
#
# name = input("What's your name? ")
# home = input("Where's your home? ")
#
# with open("students.csv", "a") as file:
#     writer = csv.writer(file)
#     writer.writerow([name, home])

# v10 inserting data into a csv file using a dict writer
import csv

name = input("What's your name? ")
home = input("Where's your home? ")

with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})
