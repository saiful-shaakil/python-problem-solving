def get_total(array):
    sum = 0
    for element in array:
        sum = sum + element
    return sum

nums = [10,20,30,40]

total = get_total(nums)
print("The total number of this array is ", total)