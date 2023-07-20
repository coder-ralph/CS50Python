import tabulate
import sys
import csv

if len(sys.argv) == 2:
    if sys.argv[1][-3:] != "csv":
        try:
            with open(sys.argv[1]) as file:
                reader = csv.DictReader(file)
                print(tabulate.tabulate(reader, headers="keys", tablefmt="grid"))
        except FileNotFoundError:
            sys.exit("File not found")
    else:
        sys.exit("not a csv file")
elif len(sys.argv) < 2:
    sys.exit("too few command-line arguments")
elif len(sys.argv) > 2:
    sys.exit("too many command-line arguments")
        
                