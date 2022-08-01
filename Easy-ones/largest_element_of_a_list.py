# function to get the largest number
def get_largest(array):
    # here's array is a parameter which is passed as arguement when this funciton is called(13 number line.)
    largest = array[0]
    for each_number in array:
        # applying the condition
        if largest < each_number:
            largest = each_number
    # returning the largest number from the function
    return largest
        
nums = [0,13,15,30,50,54,93, 108,309,33,304]
largest_number = get_largest(nums)
print("The largest number of your list is ", largest_number)