# 02 : GUESS THE NUMBER (COMPUTER)

# In Guess the Number Python's Project we use random module, build functions,
# work with while loops and conditionals, and get user input.

import random

def guess(x: int):
    random_number = random.randint(1, x)
    attempts = 0 
    guess = 0

    while guess != random_number:
        try:
            guess = int(input(f"Guess a number between 1 to {x}: "))
            attempts += 1

            if guess < 1 or guess > x: 
                print(f"Please guess a number between 1 and {x}.")
            elif guess < random_number:
                print("Too low! Try again.")
            elif guess > random_number:
                print("Too high! Try again.")

        except ValueError:
            print("Invalid input! Please enter a number.")

    print(f"🎉 Congrats! You guessed {random_number} in {attempts} attempts!")

guess(10)
