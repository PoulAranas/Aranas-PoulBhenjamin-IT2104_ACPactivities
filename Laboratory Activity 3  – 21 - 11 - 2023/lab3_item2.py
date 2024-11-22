def is_perfect_number(number):
    if number <= 0:
        return False
    divisors = [i for i in range(1, number) if number % i == 0]
    return sum(divisors) == number

def main():
    user_input = input("Enter a number: ")
    if not user_input.isdigit():
        print("Please enter a valid integer.")
        return

    number = int(user_input)
    if is_perfect_number(number):
        print(f"{number} is a perfect number.")
    else:
        print(f"{number} is not a perfect number.")

if __name__ == "__main__":
    main()