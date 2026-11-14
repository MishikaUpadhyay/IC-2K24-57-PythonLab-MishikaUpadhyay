# Program to print different star patterns

# 1. Solid Square
n = 4
for i in range(n):
    print("* " * n)

print()

# 2. Solid Triangle
for i in range(1, n + 1):
    print("* " * i)

print()

# 3. Equilateral Triangle
for i in range(1, n + 1):
    print(" " * (n - i) + "*" * (2 * i - 1))

print()

# 4. Square Triangle
for i in range(1, n + 1):
    print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))

print()

# 5. Diamond Pattern
for i in range(1, n + 1):
    print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))

for i in range(n - 2, -1, -1):
    print("*" * (n - i) + " " * (2 * i - 1) + "*" * (n - i))

print()

# 6. Hollow Diamond Box
for i in range(n):
    stars = "*" * (n - i)
    spaces = " " * (2 * i)
    print(stars + spaces + stars)

for i in range(n - 2, -1, -1):
    stars = "*" * (n - i)
    spaces = " " * (2 * i)
    print(stars + spaces + stars)
