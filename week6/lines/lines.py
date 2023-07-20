import sys

if len(sys.argv) == 2:
    if sys.argv[1][-2:] == "py":
        try:
            with open(sys.argv[1]) as file:
                nlines = 0
                for line in file:
                    if not line.lstrip().startswith('#') and line.lstrip() != '':
                        nlines += 1
                print(nlines)
        except FileNotFoundError:
            sys.exit("File not found")
    elif sys.argv[1][-2:] != "py":
        sys.exit("Not a python file")
elif len(sys.argv) > 2:
    sys.exit("Too few command-line arguments")
elif len(sys.argv) < 2:
    sys.exit("Too many command-line arguments")