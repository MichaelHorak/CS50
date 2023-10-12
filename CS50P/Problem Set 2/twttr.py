def main():
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    # prompts the user for a str of text
    keyword = input("Enter a word to shorten: ")

    # and then outputs that same text but with all vowels
    for letter in keyword:
        if letter in vowels:
            keyword = keyword.replace(letter, "")
    # (A, E, I, O, and U) omitted, whether inputted in uppercase or lowercase
    print(keyword)


main()
