import random


def main():
    level = get_level()
    # Randomly generates ten(10) math problems formatted as X + Y =, wherein
    # each of X and Y is a non-negative integer with digits.
    # No need to support operations other than addition (+).
    score = simulate_game(level)
    print("Score: ", score)


def simulate_round(x, y):
    count_tries = 1
    while count_tries <= 3:
        try:
            answer = int(input(f"{x} + {y} = "))
            if answer == (x + y):
                return True
            else:
                count_tries += 1
                print("EEE")
        except ValueError:
            count_tries += 1
            print("EEE")
    print(f"{x} + {y} = {x+y}")
    return False


# simulate game
def simulate_game(level):
    count_round = 1
    score = 0
    while count_round <= 10:
        x, y = generate_integer(level)
        response = simulate_round(x, y)
        if response:
            score += 1
        count_round += 1
    return score


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1, 2, 3]:
                break
        except ValueError:
            pass
    return level
    # Prompts the user for a level, n
    # If the user does not input 1, 2, or 3, the program should prompt again.


def generate_integer(level):
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
    return x, y


if __name__ == "__main__":
    main()
