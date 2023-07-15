def create_grocery_list():
    grocery_list = {}

    try:
        while True:
            item = input("").lower()

            if item:
                if item in grocery_list:
                    grocery_list[item] += 1
                else:
                    grocery_list[item] = 1

    except EOFError:
        pass

    return grocery_list


def print_grocery_list(grocery_list):
    sorted_items = sorted(grocery_list.keys())

    for item in sorted_items:
        count = grocery_list[item]
        print(f"{count} {item.upper()}")


if __name__ == "__main__":
    grocery_list = create_grocery_list()
    print_grocery_list(grocery_list)
