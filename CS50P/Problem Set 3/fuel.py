def main():
    get_data()


def get_data():
    while True:
        try:
            get_xy = input("Fraction: ")
            # In a file called fuel.py, implement a program that prompts the user for a fraction,
            # formatted as X/Y,

            arr = get_xy.split("/")
            x = int(arr[0])
            y = int(arr[1])
            # wherein each of X and Y is an integer,
            # If, though, X or Y is not an integer,

            if x > y:
                raise ValueError
            # X is greater than Y,

            if y == 0:
                raise ZeroDivisionError
            # or Y is 0,

        except ValueError:
            pass
        except ZeroDivisionError:
            pass

        # instead prompt the user again.
        # (It is not necessary for Y to be 4.)
        # Be sure to catch any exceptions like ValueError
        # or ZeroDivisionError.

        else:
            print_result(x, y)
            break


def print_result(a, b):
    print(f"{a}/{b}")
    x = int(round((a/b) * 100, 0))

    if x >= 99:
        print("F")
        # if 99 % or more remains, output F instead to indicate that the tank is essentially full.
    elif x > 1:
        print(f"{x}%")
    else:
        print("E")


main()


# and then outputs, as a
# percentage rounded to the nearest integer, how much fuel is in the tank. If, though,
# 1% or less remains, output E instead to indicate that the tank is essentially empty.
# And
#
