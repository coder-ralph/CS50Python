def main():
    time = input("What time is it? ")
    hours = convert(time)

    meal_time = ""

    if 7.0 <= hours < 8.0:
        meal_time = "breakfast time"
    elif 12.0 <= hours < 13.0:
        meal_time = "lunch time"
    elif 18.0 <= hours < 19.0:
        meal_time = "dinner time"

    if meal_time:
        print(meal_time)


def convert(time):
    hours, minutes = time.split(":")0227
    hours = float(hours)
    minutes = float(minutes) / 60
    return hours + minutes


if __name__ == "__main__":
    main()
