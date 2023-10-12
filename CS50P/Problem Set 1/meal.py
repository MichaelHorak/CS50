def main():
    time = input("Enter time: ")
    convert(time)

    if 7 <= c_result <= 8:
        print("breakfast time")
    elif 12 <= c_result <= 13:
        print("lunch time")
    elif 18 <= c_result <= 19:
        print("dinner time")
    else:
        return None


def convert(time):
    y = time.split(":")

    a = float(y[0])

    b = y[1]
    b = float(b)
    b = b / 60

    c_result = a + b

    return c_result

if __name__ == "__main__":
    main()
