import random

# Generate a random number between 1 and 100
number = random.randint(1, 100)

print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 100")

guess = int(input("Enter your guess: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")

elif guess < number:
    print("Too low! The correct number was", number)

else:
    print("Too high! The correct number was", number)
