import random

secret_number = random.randint(1, 10)

print("=== Guess the Number Game ===")
print("I have chosen a number between 1 and 10.")

attempts = 0

while True:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess < secret_number:
        print("Too low!\n")

    elif guess > secret_number:
        print("Too high!\n")

    else:
        print("\nCongratulations!")
        print("You guessed the number.")
        print("Attempts:", attempts)
        break
