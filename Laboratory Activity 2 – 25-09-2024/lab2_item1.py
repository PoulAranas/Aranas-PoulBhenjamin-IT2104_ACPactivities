def check_palindrome(number):
    reversed_number = str(number)[::-1]
    if str(number) == reversed_number:
        return f"{number} is a Palindrome"
    else:
        return f"{number} is Not a Palindrome"

number = int(input("Enter an integer: "))
print(check_palindrome(number))