# Program to check palindrome number
#num

num = int(input("Enter a number: "))

temp = num
reverse = 0

while temp > 0:
    digit = temp % 10
    reverse = reverse * 10 + digit
    temp = temp // 10

if num == reverse:
    print("Palindrome number")
else:
    print("Not a palindrome number")


# Checking palindrome using string

text = input("Enter a word: ")

if text == text[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome string")
