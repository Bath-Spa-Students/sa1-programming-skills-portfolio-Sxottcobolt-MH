ThisList = ["Jake", "Zac", "Ian", "Ron", "Sam", "Dave"]
print(ThisList)
User_Input = input("Enter a name from this list: ")
if  User_Input in ThisList:
    print("Valid")
else:
    print("Invalid")

#The user is asked to input any of these names from this list, which has been printed.
#If the user enters a name that is not of this list, the program will print Invalid.