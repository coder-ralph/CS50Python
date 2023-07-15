def calculate_fuel_percentage(fraction):
    try:
        x, y = map(int, fraction.split('/'))
        if x > y:
            return None
        percentage = (x / y) * 100
        return round(percentage)
    except (ValueError, ZeroDivisionError):
        return None


def main():
    while True:
        fraction = input("Fraction: ")
        percentage = calculate_fuel_percentage(fraction)

        if percentage is not None:
            if percentage <= 1:
                print("E")
            elif percentage >= 99:
                print("F")
            else:
                print(f"{percentage}%")
            break
        else:
            print("Invalid fraction.")


if __name__ == "__main__":
    main()
