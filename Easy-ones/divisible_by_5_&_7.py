from platform import java_ver


def divisible_by_5and7(num):
    result = []
    for i in range(num):
        if i%5 == 0 and i%7 == 0:
            result.append(i)
    return result

num = int(input("Enter your number: "))
result = divisible_by_5and7(num)
print(result)