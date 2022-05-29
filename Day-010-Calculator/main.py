import art

print(art.logo)


def add(n1, n2):
    return n1 + n2


def subtract(n1, n2):
    return n1 - n2


def multiply(n1, n2):
    return n1 * n2


def divide(n1, n2):
    return n1 / n2


operations = {
    '+': add,
    '-': subtract,
    '*': multiply,
    '/': divide
}


def calculator():
    calculation_continue = True
    user_choice = ''

    num1 = float(input("\nEnter the First number?: "))
    print('\n')
    for operator in operations:
        print(operator)

    while calculation_continue:

        operation_choice = input("\nSelect an operation: ")
        num2 = float(input("\nEnter the next number?: "))

        answer = operations[operation_choice](num1, num2)

        print(f"\n{num1} {operation_choice} {num2} = {answer}\n")

        user_choice = input(
            f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ")

        if user_choice == 'y':
            num1 = answer
        else:
            calculation_continue = False
            print('\n')
            calculator()


calculator()
