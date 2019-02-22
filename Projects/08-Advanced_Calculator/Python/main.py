user = input("Please type in an equation (\"2+2\") here:")
num1 = 0
num2 = 0
op = ""
foundop = False
for letter in user:
    if letter.isdigit() and not foundop:
        num1 = num1*10 + int(letter)
    elif letter.isdigit() and foundop:
        num2 = num2*10 + int(letter)
    elif (letter == "+" or letter == "-" or letter == "*" or letter == "/"):
        op = letter
        foundop = True
if op == "+":
    print(num1, op, num2, "=", num1+num2)
elif op == "-":
    print(num1, op, num2, "=", num1-num2)
elif op == "*":
    print(num1, op, num2, "=", num1*num2)
elif op == "/":
    print(num1, op, num2, "=", num1/num2)
else:
    print("Your operator choice was not an operator this calculator can do.")