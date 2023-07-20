import sys
import csv

if len(sys.argv) == 3:
    if sys.argv[1][-3:] == "csv":
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                with open(sys.argv[2], "w") as file2:
                    writer = csv.DictWriter(file2, fieldnames=["first", "last", "house"])
                    writer.writeheader()
                    for row in reader:
                        row["first"] = row.pop("name")
                        last_name, first_name = row["first"].split(",")
                        row["first"] = first_name
                        row["last"] = last_name
                        writer.writerow(row)
        except FileNotFoundError:
            sys.exit(f"Could not read {sys.argv[1]}")
    else:
        sys.exit("not a csv file")
elif len(sys.argv) < 3:
    sys.exit("too few command-line arguments")
elif len(sys.argv) > 3:
    sys.exit("too many command-line arguments")
    