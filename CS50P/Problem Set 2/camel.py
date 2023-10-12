def main():
    camel = input("Enter name of a variable in camelCase: ")
    snake = ""

    for char in range(0, len(camel)):
        if camel[char].isupper():
            snake = snake + '_' + camel[char].lower()
        else:
            snake = snake + camel[char]
    print(snake)

main()

