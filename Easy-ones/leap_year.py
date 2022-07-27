# Getting the year from the user.
year = input("Enter the year you want to know that is leap year or not: ")

# turning the string into number.
year = int(year)

# checking
if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("This is a leaf year.")
        else:
            print("This is not a leaf year.")
    else:
        print("This is a leap year.")
else: 
    print("This is not a leap year.")