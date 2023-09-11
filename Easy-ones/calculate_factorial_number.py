input_number = int(input("Enter a positive number to get factorial result: "))
factorial = 1
if input_number < 0 :
    print("Sorry! Enter a positive number again.")
elif input_number == 0:
    print("Factorial of 0 is 1.")
else :
    for i in range(1, input_number + 1):
        factorial *= i

print(f"The factorial of {input_number} is: {factorial}")