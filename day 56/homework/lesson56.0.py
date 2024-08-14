def basic_math(operation, value1, value2):
    if operation == '+':
        return value1 + value2
    elif operation == '-':
        return value1 - value2
    elif operation == '*':
        return value1 * value2
    elif operation == '/':
        if value2 != 0:
            return value1 / value2
        else:
            return 'Error: Division by zero'
    else:
        return 'Error: Invalid operation'


print(basic_math('+', 4, 7))  # Output: 11
print(basic_math('-', 15, 18))  # Output: -3
print(basic_math('*', 5, 5))  # Output: 25
print(basic_math('/', 49, 7)) # Output: 7