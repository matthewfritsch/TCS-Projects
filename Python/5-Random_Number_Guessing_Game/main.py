import random

print("Welcome to my number guessing game!")
print("Your random number will exist between 1 and 100")
print("You've got 6 guesses, good luck!")
choice = 0
number = random.randint(1,100)
guesses = 6
while guesses > 0 and choice != number:
    choice = int(input("Make your choice: "))
    guesses = guesses-1
    if choice > number:
        print("You guessed too high!")
    elif(choice < number):
        print("You guessed too low!")
    
if choice == number:
    print("You got the number!")
else:
    print("You ran out of guesses! The number was ", number)