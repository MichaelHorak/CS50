def main():
    print_square(3)


def print_square(size):

    # for each row in square
    for i in range(size):
            print_row(size)


def print_row(width):
    print("#" * width)
# def print_column(height):
#     print("#\n" * height, end="")

# def print_row(width):
#     print("?" * width)


main()
