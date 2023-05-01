import random

# Generate a random number between 1 and 1000
number = random.randint(1, 1000)

# Set the number of guesses to 0
guesses = 0

# Loop until the user guesses the correct number
while True:
    # Ask the user to guess a number
    guess = int(input("Guess a number between 1 and 1000: "))

    # Increment the number of guesses
    guesses += 1

    # Check if the guess is correct
    if guess == number:
        print("Congratulations! You guessed the number in", guesses, "guesses.")
        break
    elif guess < number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")100