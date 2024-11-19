Correct_Pass = "12345"  # This is the password

while True:
    Input_Pass = input("Input the passkey: ")
    if Input_Pass == Correct_Pass:
        print("Access granted") # If the user types in the password, the programs ends.
        break
    else:
        print("Access denied") # If the user types in the wrong password, the user has to type it in again.