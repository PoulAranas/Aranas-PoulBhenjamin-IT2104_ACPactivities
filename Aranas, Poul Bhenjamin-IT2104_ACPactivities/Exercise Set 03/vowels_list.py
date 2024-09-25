input_string = input("Enter a String: ")
vowels = "aeiouAEIOU"
vowels_in_string = [char for char in input_string if char in vowels]
print(vowels_in_string)