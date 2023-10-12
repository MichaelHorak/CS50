from validators import email


def main():
    print(email_check(input("What's your email address? ")))


def email_check(email_address):
    if email(email_address):
        return 'Valid'
    else:
        return 'Invalid'


if __name__ == "__main__":
    main()
