names = ["Jesus","Ivan","Harriet","Goofman","Ferris","Erica","David","Charlie","Andrew","Bob"]

print(names)
sorted = False
while not sorted:
    sorted = True
    for i in range(len(names)-1):
        if names[i] > names[i+1]:
            sorted = False
            temp = names[i+1]
            names[i+1] = names[i]
            names[i] = temp
        
print(names)