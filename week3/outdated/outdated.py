from datetime import datetime

def convert_date(date_str):
    try:
        date = datetime.strptime(date_str, "%m/%d/%Y")
        return date.strftime("%Y-%m-%d")
    except ValueError:
        try:
            date = datetime.strptime(date_str, "%B %d, %Y")
            return date.strftime("%Y-%m-%d")
        except ValueError:
            return None

def main():
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]

    while True:
        date_str = input("Date: ").strip()
        iso_date = convert_date(date_str)

        if iso_date:
            print(iso_date)
            break
        else:
            print("")

if __name__ == "__main__":
    main()
