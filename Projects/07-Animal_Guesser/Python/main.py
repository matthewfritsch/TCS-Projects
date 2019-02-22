import random, os

print("Welcome to my Animal Guessing Game")

options = ["horse","lion","tiger","cow","flamingo","dog","dolphin","cheetah","pelican","chicken","monkey","leopard","rat","elephant","panda"]

toGuess = options[random.randint(0,len(options))]
chances = 3
userGuess = ""
hints = []

directory = os.path.join(os.path.dirname(__file__), "animals/"+toGuess)

file1 = open(directory, "r")
for line in file1:
    hints.append(line)

while chances > 0 and toGuess != userGuess:
    chances = chances-1
    print(hints[2-chances])
    userGuess = input("Enter guess here: ")

if toGuess == userGuess:
    print("You win!")
else:
    print("You lost! The animal was ", toGuess)