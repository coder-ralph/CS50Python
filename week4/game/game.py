import random

def get_level():
    while True:
        level = input("Level: ")
        try:
            level = int(level)
            if level > 0:
                return level
        except ValueError:
            pass
        print("Please enter a positive integer.")

def get_guess():
    while True:
        guess = input("Guess: ")
        try:
            guess = int(guess)
            if guess > 0:
                return guess
        except ValueError:
            pass
        print("Please enter a positive integer.")

def main():
    level = get_level()
    answer = random.randint(1, level)

    while True:
        guess = get_guess()

        if guess < answer:
            print("Too small!")
        elif guess > answer:
            print("Too large!")
        else:
            print("Just right!")
            break

if __name__ == "__main__":
    main()
