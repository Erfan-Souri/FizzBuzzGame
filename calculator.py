# This is a simple calculator using functions in python

def add(n1, n2):
    """Adds two numbers"""
    return n1 + n2


def subtract(n1, n2):
    """Subtracts two numbers"""
    return n1 - n2


def multiply(n1, n2):
    """Multiplies two numbers"""
    return n1 * n2


def divide(n1, n2):
    """Divides two numbers"""
    return n1 / n2


operators = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}


def calculation():
    num1 = float(input("What's the first number? "))

    calculation_continue = True
    while calculation_continue:

        for symbol in operators:
            print(symbol)
        operation_symbol = str(input("Pick an operator from shown operators above: "))

        num2 = float(input("What's the next number? "))

        # Getting the operator and numbers from user and printing the result
        calculation_function = operators[operation_symbol]
        answer = calculation_function(num1, num2)

        print(f"{num1} {operation_symbol} {num2} = {answer}")

        should_continue = input(f"Would you like to continue with result of {answer}? type 'y' for yes or 'n' for no "
                                f"and start new calculation.\nType 'exit' to exit the program ").lower()
        if should_continue == "exit":
            exit()
        elif should_continue == "n":
            calculation()
        else:
            num1 = answer


calculation()
