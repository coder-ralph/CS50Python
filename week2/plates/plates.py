def has_minimum_length(s):
    return len(s) >= 2


def has_maximum_length(s):
    return len(s) <= 6


def has_valid_number_placement(s):
    if s[-1].isnumeric():
        return s[1:-1].isalpha() and s[0] != '0'
    return True


def has_valid_characters(s):
    return s.isalnum()


def is_valid(s):
    return (
        has_minimum_length(s)
        and has_maximum_length(s)
        and has_valid_number_placement(s)
        and has_valid_characters(s)
    )


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


if __name__ == "__main__":
    main()
