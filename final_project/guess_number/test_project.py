import pytest
from project import run_quiz


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
        }
    ]

    # Simulate user input for the sample questions
    user_inputs = ["b", "c", "d", "a", "d"] # Correct answers

    # Patch the input function to simulate user input
    monkeypatch.setattr('builtins.input', lambda _: user_inputs.pop(0))

    # Run the quiz with simulated user input
    score = run_quiz()

    # Calculated score
    assert score == 5


if __name__ == "__main__":
    pytest.main()
