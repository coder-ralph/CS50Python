import random


def main():
    level = get_level()
    score = 0

    for _ in range(10):
        x, y, correct_answer = generate_problem(level)
        question = f"{x} + {y} = "

        for _ in range(3):
            answer = input(question)
            try:
                answer = int(answer)
                if answer == correct_answer:
                    score += 1
                    break
            except ValueError:
                pass
            print("EEE")

        if answer != correct_answer:
            print(f"{question}{correct_answer}")

    print("Score:", score)


def get_level():
    while True:
        level = input("Level: ")
        if level in ["1", "2", "3"]:
            return int(level)


def generate_problem(level):
    x = generate_integer(level)
    y = generate_integer(level)
    correct_answer = x + y
    return x, y, correct_answer


def generate_integer(level):
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")


if __name__ == "__main__":
    main()
