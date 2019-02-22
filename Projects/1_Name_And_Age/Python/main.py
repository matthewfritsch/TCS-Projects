print("Hello, and welcome to my first program")
#name = "Matthew Fritsch"
#age = 20
#These lines are important for letting the student understand variables
name = input("Please type in your name: ")
age = int(input("Please type in your age: "))
print(name, "is", age, "years old!")

name2 = "Peter Parker"
age2 = 17
print(name2, "is", age2, "years old!")

if(age > age2):
    print(name, "is older than", name2)
elif(age < age2):
    print(name, "is younger than", name2)
else:
    print(name,"and",name2,"are the same age!")