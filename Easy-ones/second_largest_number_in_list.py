# Example -  10 5 15 20 5
input_numbers = input("Enter a list of numbers separated by spaces ")
# list_numbers = input_numbers.split(" ")
numbers_list = [int(x) for x in input_numbers.split()]
sorted_list = sorted(numbers_list)
second_largest_number = sorted_list[-2]
print(f"The second largest number is {second_largest_number}")