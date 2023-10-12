def main():
    x = input("Greeting: ")
    y = x.lower()
    greeting = y.strip()
    result = value(greeting)
    print(f"${result}")


def value(greeting):
    result = ''
    greeting = greeting.lower()
    if greeting.startswith("hello"):
        result = 0
    elif greeting.startswith("h"):
        result = 20
    else:
        result = 100
    return result

    # if 'hello' in greeting:
    #     return 0
    # elif 'h' == greeting[0]:
    #     return 20
    # else:
    #     return 100


if __name__ == "__main__":
    main()
