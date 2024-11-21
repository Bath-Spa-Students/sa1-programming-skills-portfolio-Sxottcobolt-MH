def tell_even_odd(num): # Defining the function.
    if num % 2 == 0:             # The function is made to differentiate between odd and even numbers.
        return f"The number {num} is even."
    else:
        return f"The number {num} is odd"
    
def main():
    Input = int(input("Enter a number of your choosing: "))# The user will input a number, any number, no specified range.
    output = tell_even_odd(Input)
    print(output)
if __name__ == "__main__": # Calling out the function
    main()