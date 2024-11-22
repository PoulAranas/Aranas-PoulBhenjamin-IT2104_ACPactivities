def roman_to_integer(roman):
    roman_values = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }
    total = 0
    prev_value = 0
    for char in reversed(roman.upper()):
        current_value = roman_values.get(char, 0)
        if current_value == 0:
            return f"Invalid Roman numeral: '{roman}'"
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    return total

def main():
    roman = input("Enter a Roman numeral: ")
    result = roman_to_integer(roman)
    print(f"The integer value of '{roman}' is: {result}")

if __name__ == "__main__":
    main()