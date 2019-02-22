print("Welcome to my restaurant!")
print("The menu is listed below:\n")
menu = {"Pancakes":6.99,"Turkey Sandwich":7.99,"A slice of pizza":2.99,"Buffalo Wings":9.99,"Chocolate Milkshake":3.99}
bill = 0
ordering = True 
while ordering:
    for food, price in menu.items():
        print(food, "-", price)
    user = input("What would you like to order?\nChoose here: ")
    cost = 0
    for food, price in menu.items():
        if food == user:
            cost = price
            break
    if cost == 0:
        print("That doesn't appear to be on the menu, please try again!")
    else:
        quantity = int(input("Very good choice. How many would you like?\nChoose here: "))
        price = price * quantity
        bill = bill + price
        ordering = ("y" == input("That will cost: $"+ str(price)+".\nWould you like anything else? (Y/N)\nChoose here: ").lower())
print("Your total is", bill)