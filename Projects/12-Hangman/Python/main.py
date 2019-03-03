import random

def makeGuess(text, usedLetters):
    user = input(text)
    while not (len(user) == 1) or user in usedLetters:
        print("Please type one, new letter!")
        user = input(text)
    usedLetters.append(user)
    return user

def printDashes(dashes):
    for letter in dashes:
        print(letter + " ", end="")
    print()

def findInWord(word, guess, dashes):
    dash = dashes
    for i in range(len(word)):
        if str(word[i]) == guess:
            dash = dash[:i] + guess + dash [i+1:]
            wasFound = True
    printDashes(dash)
    return dash

def runGame():
    print("Welcome to hangman, here is your word:")
    words = open("words_alpha.txt", "r")
    usedLetters = []
    guesses = 6
    guess = ""
    word = ""
    dashes = ""
    for i in range(random.randint(0, 369962)):
        words.readline()
    for letter in words.readline():
        if letter.isalpha():
            word = word + letter
    for letter in word:
        dashes = dashes+"_"
    printDashes(dashes)

    while guesses > 0 and not dashes == word:
        guess = makeGuess("Make your guess: ", usedLetters)
        found = findInWord(word, guess, dashes)
        if found == dashes:
            print("Not found.")
            guesses=guesses-1
        else:
            dashes = found
        
    if dashes == word:
        print("You won!")
    else:
        print("You lost! Good try! Your word was", word)

runGame()