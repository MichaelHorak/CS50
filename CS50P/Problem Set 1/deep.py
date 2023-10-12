answer = input("Enter the answer to the Great Question of Live, the Universe and Everything: ")

match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _:
        print("No")
