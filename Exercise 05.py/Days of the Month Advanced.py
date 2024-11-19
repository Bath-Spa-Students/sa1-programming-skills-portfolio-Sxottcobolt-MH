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
}

Month = int(input("Enter the month from 1 to 12: "))  # Same as the normal one, but now a funciton is used, for the leap year.
if 1 <= Month <= 12:
    if Month == 2:
        Year = (int(input("Input the year: ")))
        def is_leap_year(Year): # Leap year function
            if (Year % 4 == 0  and Year % 100 != 0) or (Year % 400 == 0):
                return True
            return False
        if is_leap_year(Year):
            Month_Days[2] = 29
            print(f"February in the year {Year} has {Month_Days[Month]} days. ")
        else:
            print("Invalid. Please enter a month from 1 to 12.")
    print(f"The month {Month} has {Month_Days[Month]} days. ")
else:
    print("Invalid. Please enter a month from 1 to 12.")