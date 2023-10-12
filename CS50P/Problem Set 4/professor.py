import random


def main():
    get_level()
    # Randomly generates ten(10) math problems formatted as X + Y =, wherein
    # each of X and Y is a non-negative integer with digits.
    # No need to support operations other than addition (+).

    i = 0
    score = 0
    while i < 10:
        i += 1
        # counter i for 10 problems
        attempt = 0
        # counter for attempts
        generate_integer(level)
        print(f"{x} + {y} =", end=' ')
        result = x + y

        while True:
            try:
                z = int(input())
                if result == z:
                    score += 1
                    break
                else:
                    raise ValueError
            except ValueError:
                attempt += 1
                if attempt < 3:
                    print("EEE")
                    print(f"{x} + {y} =", end=' ')
                    pass
                else:
                    print("EEE")
                    print(f"{x} + {y} = {result}")
                    break
    print(f"Score: {score}")


def get_level():
    while True:
        try:
            global level
            level = int(input("Level: "))
            if 0 < level < 4:
                break
        except ValueError:
            pass
    # Prompts the user for a level, n
    # If the user does not input 1, 2, or 3, the program should prompt again.


def generate_integer(level):
    global x, y
    if level == 1:
        x = random.randint(0, 9)
        y = random.randint(0, 9)
    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10, 99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100, 999)
    # generate_integer returns a randomly generated non-negative
    # integer with level digits or raises a ValueError if level is not 1, 2, or 3:


if __name__ == "__main__":
    main()
