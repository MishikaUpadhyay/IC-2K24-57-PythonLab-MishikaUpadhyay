# Program to print a hollow diamond pattern
n = int(input("Enter an odd number: "))
if n % 2 == 0:
    print("Please enter an odd number.")

else:
    mid = n // 2

    for i in range(n):
        outer_spaces = abs(mid - i)
        inner_spaces = 2 * (mid - outer_spaces) - 1

        print(" " * outer_spaces, end="")
        print("*", end="")

        if inner_spaces > 0:
            print(" " * inner_spaces, end="")
            print("*", end="")

        print()
