def slow_down(input_str):
    return input_str.replace(" ", "...")

user_input = input("Enter a text: ")
modified_input = slow_down(user_input)
print(modified_input)
