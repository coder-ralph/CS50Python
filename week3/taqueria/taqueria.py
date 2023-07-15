MENU = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}


def place_order():
    order_total = 0.00

    try:
        while True:
            item = input("Item: ").title()

            if item not in MENU:
                continue

            item_price = MENU[item]
            order_total += item_price

            print(f"Total: ${order_total:.2f}")

    except EOFError:
        pass


if __name__ == "__main__":
    place_order()
