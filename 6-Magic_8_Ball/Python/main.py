import random

print("Welcome to the magic 8 ball!")

input("Ask your question, and receive a yes/no style answer: ")

answers = ["Yes","It is certain","Without a doubt","You may rely on it","As I see it, yes","Most likely","It is decidedly so","Outlook good.", "Yes-definitely", "Signs point to yes.", "Reply hazy, try again.", "Ask again later.", "Better not tell you now.", "Cannot predict now.", "Concentrate and ask again.", "Don't count on it.", "My reply is no.", "My sources say no.", "Outlook not so good.", "Very doubtful."]
number = random.randint(0,19)

print(answers[number])