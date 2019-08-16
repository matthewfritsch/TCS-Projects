print("Welcome to the Supermarket!")
print("Our market has these available aisles: ")
aisles = {"protein": ["eggs", "almonds", "chicken", "oats", "greek yogurt", "beef"], "dairy": ["milk", "butter", "cheese", "clotted cream", "cream cheese", "cream"], "frozen items": ["ice cream", "waffle", "chicken nuggets", "pizza", "movie night dinner"], "fruits": ["grapefruit", "pineapple", "strawberries", "apples", "grapes", "bananas"], "vegetables": ["broccoli", "carrots", "green beans", "asparagus", "lettuce", "spinach"], "candy and sweets": ["Kit Kat", "Chocolate", "Cookies", "Brownies", "Pie", "MnMs"]}

def printAisles():
    print(end=" - ")
    for aisle in aisles:
        print(aisle, end=" - ")
    print()

printAisles()
choice = input("Choose your aisle: ")
if choice in aisles:
    print("You are in the", choice,"aisle.")
    grocery = ""
    while grocery != "done" or grocery != "back":
        print("Your options are: ")