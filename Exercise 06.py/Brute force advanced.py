Correct_Pass = "12345" # This is the password

Attempts = 0 #Intial attempts
Max_Attempts = 5 #Maximum attempts

while Attempts < Max_Attempts:
    Entered_Pass = input("Input the passkey: ")
    if Entered_Pass == Correct_Pass:
        print("Access granted") # If the user types in the correct password, the program ends.
        break
    else:
        Attempts +=1
        Remaining_Attempts = Max_Attempts - Attempts #The number of attempts decrement by 1
        if Remaining_Attempts > 0:
            print(f"Access denied. You have {Remaining_Attempts} attempts left.") # If the password typeing in is wrong, the number of attempts decrease by 1.
        else:
            print("Acces denied, you have no attempts. Also, the authorities have been alerted.") # When all attempts are gone, the authorities will be alerted.