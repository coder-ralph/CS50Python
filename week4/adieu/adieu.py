import inflect

def bid_adieu(names):
    p = inflect.engine()
    count = len(names)
    farewell = "Adieu, adieu, to "
    
    if count == 1:
        farewell += names[0]
    elif count == 2:
        farewell += f"{names[0]} and {names[1]}"
    else:
        farewell += ", ".join(names[:-1])
        farewell += f", and {names[-1]}"
    
    return farewell

def main():
    names = []
    try:
        while True:
            name = input()
            names.append(name)
    except EOFError:
        farewell = bid_adieu(names)
        print(farewell)

if __name__ == "__main__":
    main()
