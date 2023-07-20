from validator_collection import checkers


def main():
    print(validate(input("What's your email address? ")))


def validate(email):
    if checkers.is_email(email):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
