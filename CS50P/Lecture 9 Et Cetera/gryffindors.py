# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
#
# gryffindors = [
#     student["name"] for student in students if student["house"] == "Gryffindor"
# ]
#
# for gryffindor in sorted(gryffindors):
#     print(gryffindor)

# V2 filter
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
#
#
# def is_gryffindor(s):
#     return s["house"] == "Gryffindor"
#
#
# gryffindors = filter(is_gryffindor, students)
#
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# V3
# students = [
#     {"name": "Hermione", "house": "Gryffindor"},
#     {"name": "Harry", "house": "Gryffindor"},
#     {"name": "Ron", "house": "Gryffindor"},
#     {"name": "Draco", "house": "Slytherin"},
# ]
#
#
# gryffindors = filter(lambda s: s["house"] == "Gryffindor", students)
#
#
# for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
#     print(gryffindor["name"])

# V4 dictionary comprehensions
# students = ["Hermione", "Harry", "Ron"]
#
# gryffindors = []
#
# for student in students:
#     gryffindors.append({"name": student, "house": "Gryffindor"})
#
# print(gryffindors)

# V5
# students = ["Hermione", "Harry", "Ron"]
#
# gryffindors = [{"name": student, "house": "Gryffindor"} for student in students]
#
# print(gryffindors)

# V6 dictionary comprehension
# students = ["Hermione", "Harry", "Ron"]
#
# gryffindors = {student: "Gryffindor" for student in students}
#
# print(gryffindors)

# V7
# students = ["Hermione", "Harry", "Ron"]
#
# for i in range(len(students)):
#     print(i + 1, students[i])

# V8 enumerate
students = ["Hermione", "Harry", "Ron"]

for i, student in enumerate(students):
    print(i + 1, student)

# V9 generators
