def main():
    word = input('Input: ')
    result = shorten(word)
    print(f"Output: {result}")


# shorten expects a str as input and returns the same str but with all vowels(A, E, I, O, and U)
# omitted for both uppercase and lowercase
def shorten(word):
    result = ''
    for letter in word:
        if not letter.lower() in ['a', 'e', 'i', 'o', 'u']:
            result += letter
    return result


if __name__ == "__main__":
    main()
