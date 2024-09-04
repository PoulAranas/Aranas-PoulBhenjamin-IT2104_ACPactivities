char1, char2 = input("Enter two space-separated characters: ").split()

ascii1 = ord(char1)
ascii2 = ord(char2)

greater_char = max(char1, char2)

print("--------------------------")
print(f"The character with greater value is: {greater_char} ")
print("--------------------------")
print("Showig ASCII Values: ")
print(f"{char1} : {ascii1}")
print(f"{char2} : {ascii2}")
