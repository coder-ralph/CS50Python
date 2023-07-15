import pytest
from project import run_quiz, load_leaderboard


def test_run_quiz(monkeypatch):
    # Define sample quiz questions and answers
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

    # Simulate user input for the sample questions
    user_inputs = ["b", "c", "d", "a", "d", "c", "b", "b", "a", "a"]  # Correct answers

    # Patch the input function to simulate user input
    monkeypatch.setattr('builtins.input', lambda _: user_inputs.pop(0))

    # Run the quiz with simulated user input
    score = run_quiz()

    # Calculated score
    assert score == 10


def test_leaderboard():
    leaderboard = load_leaderboard()
    assert isinstance(leaderboard, list)


if __name__ == "__main__":
    pytest.main()
