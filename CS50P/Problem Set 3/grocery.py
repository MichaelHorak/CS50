grocery_list = {}
while True:
    try:
        item = input("").upper()
        if item in grocery_list:
            # increase amount by 1
            grocery_list[item] += 1
        else:
            grocery_list[item] = 1
            # add item to dictionary
    except EOFError:
        sorted_dict = dict(sorted(grocery_list.items()))
        for i in sorted_dict:
            print(sorted_dict[i], i)
        break

# implement a program that prompts the user for items,
# one per line,
# until the user inputs control-d (which is a common way of ending one’s input to a program).
# Then output the user’s grocery list in all uppercase,
# sorted alphabetically by item,
# prefixing each line with the number of times the user inputted that item.
# No need to pluralize the items. Treat the user’s input case-insensitively.
