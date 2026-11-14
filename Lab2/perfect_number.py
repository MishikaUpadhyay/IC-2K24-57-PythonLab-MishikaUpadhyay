num = int(input("Enter a number: "))

sum = 0

for i in range(1, num):
    if num % i == 0:
        sum = sum + i

if sum == num and num>0:
    print("Perfect number")
else:
    print("Not a perfect number")


limit = int(input("Enter the limit: "))

print("Perfect numbers up to", limit, "are:")

for n in range(1, limit+1):
    total = 0

    for i in range(1, n):
        if n % i == 0:
            total = total + i

    if total == n and n > 0:
        print(n, end=" ")
