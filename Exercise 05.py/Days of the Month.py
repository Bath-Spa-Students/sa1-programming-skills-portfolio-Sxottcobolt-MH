Month_Days = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31   
} # This dictionary contains the month number, corresponding with the number of days per month.

Month = int(input("Enter the month from 1 to 12: ")) #The user inputs a number from 1 to 12.
if 1 <= Month <= 12:
    print(f"The month {Month} has {Month_Days[Month]} days. ")  #The if else statement is used if the user types a number outside 1-12.
else:
    print("Invalid. Please enter a month from 1 to 12.")