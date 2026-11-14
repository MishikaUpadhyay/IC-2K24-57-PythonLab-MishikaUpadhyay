import random
number = random.randint(1, 10)
attempts = 3
print("Guess a number between 1 and 10")
for i in range(attempts):
    guess = int(input("Enter your guess: "))

    if guess == number:
        print("Correct! You won.")
        break
    elif guess < number:
        print("Too low!")
    else:
        print("Too high!")
else:
    print("Game over! The number was", number)
