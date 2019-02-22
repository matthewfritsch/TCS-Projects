file1 = open("foldernames.txt","r")

foldernames = []
for line in file1:
    current = ""
    for letter in line:
        if not letter == "\n":
            current = current+letter
    foldernames.append(current)

import os, sys
x = 14
for name in foldernames:
    os.mkdir("/Users/matthewfritsch/Programming/GithubTCSP/TCS-Projects/Projects/"+str(x)+"-"+name, 777)
    #print("Users/matthewfritsch/Programming/GithubTCSP/TCS-Projects/Projects/"+str(x)+"-"+name)
    x=x+1
