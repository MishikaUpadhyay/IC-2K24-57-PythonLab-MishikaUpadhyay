def is_prime(num):
    if num < 2:
        return False

    for i in range(2, num):
        if i * i > num:
            break
        if num % i == 0:
            return False

    return True

n = int(input("Enter a number: "))

if is_prime(n):
    print("Prime number")
else:
    print("Not a prime number")

limit = int(input("Enter the limit: "))

print("Prime numbers up to", limit, "are:")

for num in range(2, limit + 1):
    if is_prime(num):
        print(num, end=" ")
