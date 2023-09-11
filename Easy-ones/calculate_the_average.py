inputed_numbers = input("Enter some numbers separated by spaces to get the average numbers. Ex: 10 20 30 40 50 300. Enter here - ")

numbers = inputed_numbers.split(" ")
# num_list = [int(x) for x in inputed_numbers.split()]
# print(num_list)

total = 0
for number in numbers :
    total += float(number)

average = total / len(numbers)
print(f"The average is : {average}")