def main():
    fraction = input("Fraction: ")
    percentage = convert(fraction)
    result = gauge(percentage)
    print(result)


def convert(fraction):
    while True:
        try:
            arr = fraction.split("/")
            x = int(arr[0])
            y = int(arr[1])
            if y == 0:
                raise ZeroDivisionError
            if x > y:
                raise ValueError
            percentage = int(round((x / y) * 100, 0))
            return percentage
            # percentage = x/y
            # return percentage
        except ValueError:
            raise
        except ZeroDivisionError:
            raise
    # expects a str in X/Y format as input, wherein each of X and Y is an integer,
    # and returns that fraction as a percentage rounded to the nearest int between
    # 0 and 100, inclusive.
    #
    # If X and/or Y is not an integer, or if X is greater than Y, then convert should raise a ValueError
    # If Y is 0, then convert should raise a ZeroDivisionError


def gauge(percentage):
    percentage = int(percentage)
    # expects an int and returns a str that is:
    if percentage >= 99:
        result = "F"
        # if 99 % or more remains, output F instead to indicate that the tank is essentially full.
        # "F" if that int is greater than or equal to 99,
    elif percentage > 1:
        result = str(percentage) + '%'
        # "Z%" otherwise wherein Z is that same int
    else:
        result = "E"
        # "E" if that int is less than or equal to 1,
    return result


if __name__ == "__main__":
    main()
