# v 1H __init__
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError('Invalid house')
#         self.name = name
#         self.house = house
#
#
# def main():
#     student = get_student()
#     print(f"{student.name} from {student.house}")
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
#
#
# if __name__ == "__main__":
#     main()
#

# V2 X __str__
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError('Invalid house')
#         self.name = name
#         self.house = house
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#
# def main():
#     student = get_student()
#     print(student)
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
#
#
# if __name__ == "__main__":
#     main()

# V3 adding our own methods
# class Student:
#     def __init__(self, name, house, patronus):
#         if not name:
#             raise ValueError("Missing name")
#         if house not in ['Gryffindor', 'Hufflepuff', 'Ravenclaw', 'Slytherin']:
#             raise ValueError('Invalid house')
#         self.name = name
#         self.house = house
#         self.patronus = patronus
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     def charm(self):
#         match self.patronus:
#             case "Stag":
#                 return "🦌"
#             case "Otter":
#                 return "🦦"
#             case "Jack Russell terrier":
#                 return "🐶"
#             case _:
#                 return "🪄"
#
#
# def main():
#     student = get_student()
#     print("Expecto Patronum!")
#     print(student.charm())
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     patronus = input("Patronus: ")
#     return Student(name, house, patronus)
#
#
# # if __name__ == "__main__":
# #     main()
#
# # V4 properties @property GETTER & SETTER
# class Student:
#     def __init__(self, name, house):
#         if not name:
#             raise ValueError("Missing name")
#         self.name = name
#         self.house = house
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     # Getter
#     @property
#     def house(self):
#         return self._house
#
#     # Setter
#     @house.setter
#     def house(self, house):
#         if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
#             raise ValueError("Invalid house")
#         self._house = house
#
#
# def main():
#     student = get_student()
#     print(student)
#
#
# def get_student():
#     name = input("Name: ")
#     house = input("House: ")
#     return Student(name, house)
#
#
# if __name__ == "__main__":
#     main()

# V5
class Student:
    def __init__(self, name, house):
        self.name = name
        self.house = house

    def __str__(self):
        return f"{self.name} from {self.house}"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if not name:
            raise ValueError("Missing name")
        self._name = name

    @property
    def house(self):
        return self._house

    # Setter
    @house.setter
    def house(self, house):
        if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
            raise ValueError("Invalid house")
        self._house = house


def main():
    student = get_student()
    print(student)


def get_student():
    name = input("Name: ")
    house = input("House: ")
    return Student(name, house)


if __name__ == "__main__":
    main()

# V6 simplifying @classmethod
# class Student:
#     def __init__(self, name, house):
#         self.name = name
#         self.house = house
#
#     def __str__(self):
#         return f"{self.name} from {self.house}"
#
#     @classmethod
#     def get(cls):
#         name = input('Name: ')
#         house = input('House: ')
#         return cls(name, house)
#
#
# def main():
#     student = Student.get()
#     print(student)
#
#
# if __name__ == "__main__":
#     main()

# inheritance