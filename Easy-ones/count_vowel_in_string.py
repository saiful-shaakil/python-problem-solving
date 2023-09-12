input_string = input("Enter a string to count vowel in that string: ").lower()
total_vowel = 0
for i in input_string :
    if i == "a" or i == "e" or i == "i" or i == "o" or i == "u":
        total_vowel += 1
    else :
        pass

print(f"The total vowel in your string is : {total_vowel}")