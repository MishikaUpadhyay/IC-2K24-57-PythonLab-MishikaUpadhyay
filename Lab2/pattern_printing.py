n = int(input("Enter number of rows: "))
# Pattern 1: Right triangle
print("Pattern 1:")
for i in range(1, n + 1):
    print("* " * i)

# Pattern 2: Inverted triangle
print("\nPattern 2:")
for i in range(n, 0, -1):
    print("* " * i)

# Pattern 3: Number triangle
print("\nPattern 3:")
for i in range(1, n + 1):
    for j in range(1, i + 1):
        print(j, end=" ")
    print()
