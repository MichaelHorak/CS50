import random

# Prompts the user for a level
while True:
    try:
        level = int(input("Level: "))
        # If the user does not input a positive integer, the program should prompt again.
        if level > 0:
            break
    except ValueError:
        pass

print(level)
# Randomly generates an integer between 1 and n
# , inclusive, using the random module.
guess_no = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))

        if guess > 0:
            if guess > guess_no:
                print('Too large!')
            elif guess < guess_no:
                print('Too small!')
            else:
                print('Just right!')
                break

    except ValueError:
        pass
# Prompts the user to guess that integer.
# If the guess is not a positive integer,
# the program should prompt the user again.
#
#     If the guess is smaller than that integer, the program should output Too small! and prompt the user again.
#     If the guess is larger than that integer, the program should output Too large! and prompt the user again.
#     If the guess is the same as that integer, the program should output Just right! and exit.
