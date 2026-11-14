# Program to print Fibonacci series
n = int(input("Enter number of terms: "))

a = 0
b = 1

print("Fibonacci series using loop:")

for i in range(n):
    print(a, end=" ")
    c = a + b
    a = b
    b = c
  
# Fibonacci using recursion
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print("\nFibonacci series using recursion:")

for i in range(n):
    print(fibonacci(i), end=" ")
