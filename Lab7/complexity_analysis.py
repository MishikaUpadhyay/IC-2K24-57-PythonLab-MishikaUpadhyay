# Program to demonstrate time complexity

# O(1) - Constant Time
def constant_time(n):
    print("First element:", n[0])


# O(n) - Linear Time
def linear_time(n):
    for i in n:
        print(i)


# O(n^2) - Quadratic Time
def quadratic_time(n):
    for i in n:
        for j in n:
            print(i, j)


# O(log n) - Logarithmic Time
def logarithmic_time(n):
    while n > 1:
        print(n)
        n = n // 2


numbers = [10, 20, 30, 40]

print("Constant Time:")
constant_time(numbers)

print("\nLinear Time:")
linear_time(numbers)

print("\nQuadratic Time:")
quadratic_time(numbers)

print("\nLogarithmic Time:")
logarithmic_time(16)
