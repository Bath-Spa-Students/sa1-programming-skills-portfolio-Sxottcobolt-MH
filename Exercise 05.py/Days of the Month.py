Months = { 
    "1": 31,
    "2": 28,
    "3": 30,
    "4": 30,
    "5": 31,
    "6": 29,
    "7": 31,
    "8": 31,
    "9": 30,
    "10": 31,
    "11": 30,
    "12": 31}
#This dictionary has the month numbers stored as a string value, whereas the days in said month is sotred as interger


Calender = input("Enter the Month no. ")
if Calender == "1":
    print(Months["1"])
elif Calender == "2":
    print(Months["2"])
elif Calender == "3":
    print(Months["3"])
elif Calender == "4":
    print(Months["4"])
elif Calender == "5":
    print(Months["5"])
elif Calender == "6":
    print(Months["6"])
elif Calender == "7":
    print(Months["7"])
elif Calender == "8":
    print(Months["8"])
elif Calender == "9":
    print(Months["9"])
elif Calender == "10":
    print(Months["10"])
elif Calender == "11":
    print(Months["11"])
elif Calender == "12":
    print(Months["12"])
else:
    print("None")

#This program makes use of a if, elif, else statement, to print out the number of days, according to what month number
#the user has inputted in.
