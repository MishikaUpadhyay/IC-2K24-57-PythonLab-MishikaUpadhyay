# Menu driven program

while True:
    print("\n1. Check Prime Number")
    print("2. Check Armstrong Number")
    print("3. Check Palindrome Number")
    print("4. Check Perfect Number")
    print("5. Fibonacci Series")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        num = int(input("Enter a number: "))
        count = 0

        for i in range(1, num + 1):
            if num % i == 0:
                count = count + 1

        if count == 2:
            print("Prime number")
        else:
            print("Not a prime number")

    elif choice == 2:
        num = int(input("Enter a number: "))
        temp = num
        total = 0
        digits = len(str(num))

        while temp > 0:
            digit = temp % 10
            total = total + digit ** digits
            temp = temp // 10

        if total == num:
            print("Armstrong number")
        else:
            print("Not an Armstrong number")

    elif choice == 3:
        num = input("Enter a number: ")

        if num == num[::-1]:
            print("Palindrome number")
        else:
            print("Not a palindrome number")

    elif choice == 4:
        num = int(input("Enter a number: "))
        total = 0

        for i in range(1, num):
            if num % i == 0:
                total = total + i

        if total == num and num > 0:
            print("Perfect number")
        else:
            print("Not a perfect number")

    elif choice == 5:
        n = int(input("Enter number of terms: "))
        a = 0
        b = 1

        for i in range(n):
            print(a, end=" ")
            a, b = b, a + b
        print()

    elif choice == 6:
        print("Thank you!")
        break

    else:
        print("Invalid choice")
