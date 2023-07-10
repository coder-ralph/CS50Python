def convert_to_snake_case(variable_name):
    snake_case_name = ""
    for char in variable_name:
        if char.isupper():
            snake_case_name += "_" + char.lower()
        else:
            snake_case_name += char
    return snake_case_name.lstrip("_")


def main():
    variable_name = input("camelCase: ")
    snake_case_name = convert_to_snake_case(variable_name)
    print("snake_case:", snake_case_name)


if __name__ == "__main__":
    main()
