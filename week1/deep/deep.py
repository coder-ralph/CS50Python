def check_great_question(answer):
    answer = answer.replace("-", "")

    if answer.lower() == "42" or answer.lower() == "fortytwo":
        return "Yes"
    else:
        return "No"

user_answer = input("What is the answer to the Great Question of Life, the Universe, and Everything? ")
result = check_great_question(user_answer)
print(result)
