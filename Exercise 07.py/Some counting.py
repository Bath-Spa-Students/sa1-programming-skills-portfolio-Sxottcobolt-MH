Option_A = 1
Option_B = 2
Option_C = 3
Option_D = 4
Option_E = 5

print(Option_A)
print(Option_B)
print(Option_C)
print(Option_D)
print(Option_E) #The 5 options are displayed, so that the user can see what the 5 are.

Selection = input("Select from any of these 5 options for counting: ") # The program asks the user what option they want to select.

if Selection == "1": # 1st option, 0 to 50, in increments of 1
    for x in range(0, 51, 1):
        print (x)
elif Selection == "2": # 2nd option, 50 to 0, in decrements of 1
    for x in range(51, 0, -1):
        print(x)
elif Selection == "3": # 3rd option, 30 to 50, in increments of 1
    for x in range(30, 51, 1):
        print(x)
elif Selection == "4": # 4th option, 50 to 10, in decrements of 2
    for x in range(50, 8, -2):
     print(x)
elif Selection == "5": # 5th option, 100 to 200, in increments of 5
    for x in range(100, 205, 5):
     print(x)
else:
    print("Nothing, ok") # That is if the user doesn't select any of the options. Also ends the program.