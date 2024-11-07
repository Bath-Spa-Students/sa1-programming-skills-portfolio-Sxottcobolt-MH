name = str(input("Enter name: "))
hometown = str(input("Enter hometown: "))
age = int(input("Enter age: "))

try:
    age = int(age)
except ValueError:
    print('That is not number')

Info = {
    "name" : "Adam",
    "hometown" : "Miridf",
    "age" : 17
}

print(*Info.values(), sep='\n')

# In here, instead of just hardcoding the values, the user is required to enter it.
# If the user were to enter a string value instead of a integer value for their age, an acknowledgement will be printed,
# saying that it was not a number.