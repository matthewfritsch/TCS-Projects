print("We will start by printing all previous information in the file!\n")

file1 = open("myFile.txt", "r")
for line in file1:
    print(line, end="")
print("\nThat completes the information in the file.")

file1.close()
choice = input("Would you like to rewrite, or add to the file?\n('r' or 'a'): ")
while not (choice == "a" or choice == "r"):
    choice = input("Would you like to rewrite, or add to the file?\n('r' or 'a'): ")

if choice == "r":
    file2 = open("myFile.txt", "w")
    user = input("Start by typing something to go into the file, or 'stop' to end.\nEnter here: ")
    while not user=="stop":
        file2.write(user + "\n")
        user = input("Enter here: ")
    file2.close()
else:
    file2 = open("myFile.txt", "a")
    user = input("Start by typing something to go into the file, or 'stop' to end.\nEnter here: ")
    while not user=="stop":
        file2.append(user + "\n")
        user = input("Enter here: ")
    file2.close()
print("All done! Run again to see changes!")