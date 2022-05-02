from art import logo

print(logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {'+': add, '-': subtract, '*': multiply, '/': divide}


def calculator():
    continue_calculating = 'y'
    num1 = float(input("What's the first number?: "))
    for operation in operations:
        print(operation)

    while continue_calculating == 'y':
        operation = input("Pick an operation: ")
        num2 = float(input("What's the next number?: "))
        answer = operations[operation](num1, num2)
        print(f"{num1} {operation} {num2} = {answer}")
        continue_calculating = input(f"Type 'y' to continue calculating with {answer}? "
                                     f"Or 'n' to start a new calculation "
                                     f"and 'e' to exit application. ").lower()
        if continue_calculating == 'y':
            num1 = answer
        elif continue_calculating == 'n':
            calculator()
        else:
            exit()


calculator()
