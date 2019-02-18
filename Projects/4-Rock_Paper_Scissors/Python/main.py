import random
print("Welcome to Rock, Paper, Scissors! Your opponent is the computer!")

user = input("Choose 'rock', 'paper', or 'scissors': ")
number = random.randint(1,3)
computer = ""
if number == 1:
    computer = "rock"
elif number == 2:
    computer = "paper"
else:
    computer = "scissors"

if user == computer:
    print("It was a tie!")
elif user == "rock":
    if computer == "paper":
        print("You lost, CPU chose paper!")
    elif computer == "scissors":
        print("You won, CPU chose scissors!")
elif user == "paper":
    if computer == "scissors":
        print("You lost, CPU chose scissors!")
    elif computer == "rock":
        print("You won, CPU chose rock!")
elif user == "scissors":
    if computer == "rock":
        print("You lost, CPU chose rock!")
    elif computer == "paper":
        print("You won, CPU chose paper!")
else:
    print("That was not an option!")