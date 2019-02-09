print("Welcome to my text adventure game")

playing = True
while playing:
    print("You wake up in a forest, with no other signs of human life in sight. You don't remember arriving here, and do not recognize where you are.")
    print("You're right on top of a trail, which leads three different ways that you must choose from:")
    print("1. Enter the nearby cave")
    print("2. Follow the dirt trail over a hill")
    print("3. Walk deeper into the forest.")
    choice = int(input("Please type the number for your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input("That was not among your options, go ahead and try again: "))

    if choice == 1:
        print("You enter the cave, to find a bear is comfortably laying down, its head on its hands.")
        print("Instinctually, you choose to:")
        print("1. Attack the bear")
        print("2. Sneak past the bear")
        print("3. Try to befriend the bear")
        choice = int(input("Please type the number for your choice: "))

        while choice > 3 or choice < 1:
            choice = int(input("That was not among your options, go ahead and try again: "))
        if choice == 1:
            print("What were you thinking? You can't fight a bear! You were eaten!")
        elif choice == 2:
            print("The bear is definitely not asleep, it sees you tiptoeing around, gets up, and attacks! You were eaten!")
        elif choice == 3:
            print("The bear, eerily enough, seems quite docile. He starts walking out of the cave with you, and directs you all the way back home!")
    elif choice == 2:
        print("You follow the dirt trail, which leads you over top a small yet, steep hill. Behind the hill is a horse, which appears to be waiting for you.")
        print("Instinctually, you choose to:")
        print("1. Feed the horse")
        print("2. Ride the horse")
        print("3. Leave the hill")
        choice = int(input("Please type the number for your choice: "))

        while choice > 3 or choice < 1:
            choice = int(input("That was not among your options, go ahead and try again: "))
        if choice == 1:
            print("The horse was not waiting to be fed, so it gets spooked and kicks you! You're knocked out!")
        elif choice == 2:
            print("The horse was waiting for you to hop on, and as you did, it ran you straight to your home!")
        elif choice == 3:
            print("You leave the hill and, along the way, lose track of where you are. You get so lost that you never seem to make it out of the forest.")
    else:
        print("You walk deeper into the forest, and see some people who are all around a bonfire, staring right into it.")
        print("Instinctually, you choose to:")
        print("1. Attack the people")
        print("2. Talk to the people")
        print("3. Run away from the people")
        choice = int(input("Please type the number for your choice: "))

        while choice > 3 or choice < 1:
            choice = int(input("That was not among your options, go ahead and try again: "))
        if choice == 1:
            print("There are so many people here, and they all attack you right back at the same time. You fall unconscious!")
        elif choice == 2:
            print("As a person sees you approaching, they all begin screaming and chasing you. They were too fast, and you fall unconscious!")
        elif choice == 3:
            print("You understood that these people were kind of scary, and when you begin running away you start to recognize where you are! You make it out of the forest back to your home!")
    playing = "y" == input("Would you like to play again? [y/n]: ")
