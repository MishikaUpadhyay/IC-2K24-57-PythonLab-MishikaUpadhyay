# Program to perform matrix operations

matrix = []

print("Enter 9 elements for a 3x3 matrix:")

# Taking matrix input
for i in range(3):
    row = []
    for j in range(3):
        num = int(input("Enter element: "))
        row.append(num)
    matrix.append(row)

# Display matrix
print("\nOriginal Matrix:")
for row in matrix:
    print(row)

# Sum of all elements
total = 0
for row in matrix:
    for num in row:
        total = total + num

print("Sum of all elements:", total)

# Sum of diagonal elements
diagonal = 0
for i in range(3):
    diagonal = diagonal + matrix[i][i]

print("Sum of diagonal elements:", diagonal)

# Maximum and minimum
largest = matrix[0][0]
smallest = matrix[0][0]

for row in matrix:
    for num in row:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num

print("Maximum element:", largest)
print("Minimum element:", smallest)

# Transpose of matrix
print("Transpose of matrix:")

for i in range(3):
    for j in range(3):
        print(matrix[j][i], end=" ")
    print()
