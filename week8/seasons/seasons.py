from datetime import date
import sys
import inflect

p = inflect.engine()

def main():
    try:
        year, month, day = input("Date of Birth: ").split("-")
    except ValueError:
        sys.exit("Invalid Date")

    print(minutes_lived(year, month, day))

def minutes_lived(year, month, day):
    try:
        dt = date(int(year), int(month), int(day))
    except ValueError:
        return "Invalid Date"
    tday = date.today()
    diff = tday - dt
    minutes = int(diff.total_seconds() / 60)
    msg = p.number_to_words(minutes, andword="") + " minutes"
    return msg.capitalize()


if __name__ == "__main__":
    main()