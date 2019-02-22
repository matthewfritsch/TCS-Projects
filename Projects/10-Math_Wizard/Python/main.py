import random, time

print("Welcome! I am the great Math Wizard! I will test your knowledge of 20 randomized questions!")
print("If you are ready, please choose an operator:")
op = input("Choose +, -, *, or /: ")

while(not(op == "+" or op == "-" or op == "*" or op == "/")):
    print("That was not a choice!")
    op = input("Choose +, -, *, or /: ")

print("Okay then, prepare yourself!")
time.sleep(2)
for i in range(3):
    print(3-i)
    time.sleep(1)
print("Go!")
score = 20
for i in range(20):
    num1 = random.randint(1,20)
    num2 = random.randint(1,20)
    correct = 0
    if op == "+":
        correct = num1+num2
    elif op == "-":
        correct = num1-num2
    elif op == "*":
        correct = num1*num2
    else:
        correct = num1/num2
    answer = float(input(str(num1) + op + str(num2) + "="))
    if answer == correct:
        print("Correct!")
    else:
        score = score-1
        print("Incorrect!")

print("Your total score was:", score)