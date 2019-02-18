print("Welcome to my basic, two number calculator.")

number1 = int(input("Please enter your first number "))
operator = input("Please type your operator (+,-,*,/) ")
number2 = int(input("Please enter your second number "))

if operator == "+":
    print(number1 + number2)
elif operator == "-":
    print(number1 - number2)
elif operator == "*":
    print(number1 * number2)
elif operator == "/":
    print(number1 / number2)
else:
    print("That was not an operator we have!")