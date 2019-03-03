print("Welcome to the Magic Dates program")

month = int(input("Please enter in the number of a month (Jan is 1, Feb is 2...): "))
day = int(input("Please enter in the number of a day during that month: "))
year = int(input("Please enter in the last two digits of a year: "))

if month*day == year:
    print("That is a magic date!")
else:
    print("That is not a magic date!")