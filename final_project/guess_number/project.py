def main():
    name = input("Enter your name: ")
    print("Welcome to the Quiz, {}!".format(name))
    print("Answer the following questions:")
    score = run_quiz()
    display_result(name, score)


def run_quiz():
    score = 0
    questions = [
        {
            "question": "What is the capital of France?",
            "options": {
                "a": "London",
                "b": "Paris",
                "c": "Berlin",
                "d": "Madrid"
            },
            "answer": "b"
        },
        {
            "question": "Which planet is closest to the Sun?",
            "options": {
                "a": "Mars",
                "b": "Jupiter",
                "c": "Mercury",
                "d": "Venus"
            },
            "answer": "c"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "options": {
                "a": "Atlantic Ocean",
                "b": "Indian Ocean",
                "c": "Arctic Ocean",
                "d": "Pacific Ocean"
            },
            "answer": "d"
        },
        {
            "question": "Who painted the Mona Lisa?",
            "options": {
                "a": "Leonardo da Vinci",
                "b": "Pablo Picasso",
                "c": "Vincent van Gogh",
                "d": "Claude Monet"
            },
            "answer": "a"
        },
        {
            "question": "What is the currency of Japan?",
            "options": {
                "a": "Yuan",
                "b": "Dollar",
                "c": "Euro",
                "d": "Yen"
            },
            "answer": "d"
        }
    ]

    for question in questions:
        print(question["question"])
        for option, answer in question["options"].items():
            print("{}: {}".format(option, answer))

        user_answer = input("Your answer: ").lower()
        if user_answer == question["answer"]:
            score += 1

    return score


def display_result(name, score):
    print("Quiz completed! Here's the result:")
    print("Player: {}".format(name))
    print("Score: {}/5".format(score))


if __name__ == "__main__":
    main()
