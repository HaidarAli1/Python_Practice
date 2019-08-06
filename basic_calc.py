def addition(num1, num2):
    answer = num1+num2
    return answer


def subtraction(num1, num2):
    answer = num1-num2
    return answer


def multiplication(num1, num2):
    answer = num1*num2
    return answer


def division(num1, num2):
    answer = num1 / num2
    return answer


def exponents(num1, num2):
    answer = 1
    for index in range(num2):
        answer = answer * num1
    return answer


try:
    user_input = str(input("What operation would you like to use: "))
    user_input.lower()

    if user_input == "square" or user_input == "exponent" or user_input == "base":
        number_1 = float(input("What is the base: "))
        number_2 = int(input("What is the exponent: "))
        print(exponents(number_1, number_2))
        escape = 2
    else:
        number_1 = float(input("What is your first number: "))
        number_2 = float(input("What is your second number: "))

        if user_input == "addition" or user_input == "add" or user_input == "+":
            print("\n", addition(number_1, number_2))
        elif user_input == "subtraction" or user_input == "minus" or user_input == "-":
            print("\n", subtraction(number_1, number_2))
        elif user_input == "multiplication" or user_input == "multiply" or user_input == "x" or user_input == "*":
            print("\n", multiplication(number_1, number_2))
        elif user_input == "division" or user_input == "divide" or user_input == "/":
            print("\n", division(number_1, number_2))
        else:
            print("Invalid Operator.")

except ValueError:
    print("Invalid Input.")
