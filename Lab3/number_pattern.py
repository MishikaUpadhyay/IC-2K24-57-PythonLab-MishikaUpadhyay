# Program to print concentric number square pattern

n = int(input("Enter the number: "))

size = 2 * n - 1

for row in range(size):
    for column in range(size):
        distance = min(row, column, size - 1 - row, size - 1 - column)
        value = n - distance
        print(value, end=" ")
    print()
