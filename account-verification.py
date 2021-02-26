#python account system using CSV read and write.
#main start file

import sys
import random

acc = False
found = False
while acc == False:
    username=input("username: ")
    password=input("password: ")
    file=open("C:/dev/py auth/auth-users.csv", "r+")
    for line in file:
        details=line.split(",")
        if details[0]==username and details [1]==password +"\n":
            print("account found")
            found = True
            acc = True
    if found == False:
        print ("account not found" +"\n")
        answer=input("Would you like to make an account with the details given? (Y/n)")
        if answer=="Y" or answer=="y":
            file.write(username+","+password)
            print("Account saved")
            acc = True
        elif answer=="N" or answer=="n":
            print("")
        else:
            print("Unexpected Value")
file.close()

if acc == True:
    import snake
    execfile('snake.py')
