print("The computer going to give you the prime number between your starting number and end number.")
starting_number = int(input("Enter your starting number: "))
end_number = int(input("Enter your end number: "))

prime_numbers_list = []

for num in range(starting_number, end_number + 1) :
    if num > 1 :
        is_prime = True
        
        for i in range(2, int(num ** 0.5) + 1) :
            if num % i == 0 :
                is_prime = False
                break
        if is_prime :
            prime_numbers_list.append(num)

print(f"Prime numbers in the range ({starting_number}, {end_number}): {prime_numbers_list}")