def main():
    nutrition = input("Item: ")
    # enter fruit & switch to lowercase
    nutrition = nutrition.lower()

    fruit_cal(nutrition)


def fruit_cal(x):
    # match with fruit & return calories
    match x:
        case "apple":
            print("Calories: 130")
        case "avocado" | "cantaloupe" | "honeydew melon" | "pineapple" | "strawberries" | "tangerine":
            print("Calories: 50")
        case "banana":
            print("Calories: 110")
        case "grapefruit" | "nectarine" | "peach":
            print("Calories: 60")
        case "grapes" | "kiwifruit":
            print("Calories: 90")
        case "lemon":
            print("Calories: 15")
        case "lime":
            print("Calories: 20")
        case "orange" | "watermelon":
            print("Calories: 80")
        case "pear" | "sweet cherries":
            print("Calories: 100")
        case "plums":
            print("Calories: 70")


main()
