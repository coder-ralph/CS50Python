def main():
    name = input("Enter your name: ")
    print("Welcome to the Quiz, {}!".format(name))
    print("Answer the following questions:")
    score = run_quiz()
    update_leaderboard(name, score)
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
        },
        {
            "question": "What is the chemical symbol for gold?",
            "options": {
                "a": "Ag",
                "b": "Hg",
                "c": "Au",
                "d": "Pt"
            },
            "answer": "c"
        },
        {
            "question": "Which country is known as the Land of the Rising Sun?",
            "options": {
                "a": "China",
                "b": "Japan",
                "c": "South Korea",
                "d": "Thailand"
            },
            "answer": "b"
        },
        {
            "question": "What is the largest continent on Earth?",
            "options": {
                "a": "North America",
                "b": "Asia",
                "c": "Africa",
                "d": "Europe"
            },
            "answer": "b"
        },
        {
            "question": "Who wrote the play Romeo and Juliet?",
            "options": {
                "a": "William Shakespeare",
                "b": "Arthur Miller",
                "c": "Oscar Wilde",
                "d": "George Bernard Shaw"
            },
            "answer": "a"
        },
        {
            "question": "What is the tallest mountain in the world?",
            "options": {
                "a": "Mount Everest",
                "b": "K2",
                "c": "Kangchenjunga",
                "d": "Makalu"
            },
            "answer": "a"
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
    print("Score: {}/10".format(score))


def update_leaderboard(name, score):
    leaderboard = load_leaderboard()
    leaderboard.append({"name": name, "score": score})
    leaderboard.sort(key=lambda x: x["score"], reverse=True)
    save_leaderboard(leaderboard)


def load_leaderboard():
    try:
        with open("leaderboard.txt", "r") as file:
            leaderboard = eval(file.read())
            return leaderboard
    except FileNotFoundError:
        return []


def save_leaderboard(leaderboard):
    with open("leaderboard.txt", "w") as file:
        file.write(str(leaderboard))


if __name__ == "__main__":
    main()
