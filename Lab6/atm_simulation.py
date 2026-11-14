# Program to simulate an ATM

pin = 1234
balance = 5000
attempts = 3
transactions = 0

# PIN verification
while attempts > 0:
    entered_pin = int(input("Enter your PIN: "))

    if entered_pin == pin:
        print("Login successful!")
        break
    else:
        attempts = attempts - 1
        print("Incorrect PIN. Attempts left:", attempts)

if attempts == 0:
    print("Your account is locked.")

else:
    while transactions < 3:
        print("\n1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")

        choice = int(input("Enter your choice: "))

        if choice == 1:
            print("Current Balance:", balance)

        elif choice == 2:
            amount = int(input("Enter deposit amount: "))

            if amount > 0:
                balance = balance + amount
                transactions = transactions + 1
                print("Money deposited successfully.")
            else:
                print("Invalid amount.")

        elif choice == 3:
            amount = int(input("Enter withdrawal amount: "))

            if amount <= 0:
                print("Invalid amount.")
            elif amount > balance:
                print("Insufficient balance.")
            else:
                balance = balance - amount
                transactions = transactions + 1
                print("Please collect your cash.")

        elif choice == 4:
            print("Thank you for using our ATM.")
            break

        else:
            print("Invalid choice.")

    if transactions == 3:
        print("Transaction limit reached.")
