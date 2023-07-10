def calculate_expression(expression):
    x, operator, z = expression.split()
    x = int(x)
    z = int(z)

    if operator == "+":
        result = x + z
    elif operator == "-":
        result = x - z
    elif operator == "*":
        result = x * z
    elif operator == "/":
        result = x / z

    return round(result, 1)

user_expression = input("Expression: ")
result = calculate_expression(user_expression)
formatted_result = "{:.1f}".format(result)
print(formatted_result)
