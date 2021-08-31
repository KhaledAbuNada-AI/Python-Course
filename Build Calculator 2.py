def addition(num1, num2):
    result = num1 + num2
    return result


def subtraction(num1, num2):
    result = num1 - num2
    return result


def multiplication(num1, num2):
    result = num1 * num2
    return result


def division(num1, num2):
    result = num1 / num2
    return result


def modulus(num1, num2):
    result = num1 % num2
    return result


def exponent(num1, num2):
    result = num1 ** num2
    return result

num1 = float(input("Enter Your Num1: "))
operator = input("Enter Your Operators: ")
num2 = float(input("Enter Your Num2: "))

if operator == "+":
    print(addition(num1, num2))
elif operator == "-":
    print(subtraction(num1, num2))
elif operator == "*":
    print(multiplication(num1, num2))
elif operator == "/":
    print(division(num1, num2))
elif operator == "%":
    print(modulus(num1, num2))
elif operator == "**":
    print(exponent(num1, num2))
else:
    print("Wrong operator please try again")