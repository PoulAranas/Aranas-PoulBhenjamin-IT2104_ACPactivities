while True:
        total_amount = float(input("Enter the total purchase amount: "))

        if total_amount > 5000:
            discount_rate = 0.10
        else:
            discount_rate = 0.05

        discount = total_amount * discount_rate
        final_price = total_amount - discount

        print(f"Initial Purchase Amount: {total_amount:.2f}")
        print(f"Discount: {discount:.2f}")
        print(f"Final Price: {final_price:.2f}")

        try_again = input("Do you want to try again? (yes/no): ").lower()
        if try_again != 'yes':
            print("Thank you!")
            break