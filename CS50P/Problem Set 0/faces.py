def convert(to):
    to = to.replace(':)', '🙂')
    to = to.replace(':(', '🙁')
    print(to)


def main():
    convert(input("Please enter a string: "))


main()
