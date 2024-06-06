import random


def guess_the_number():
    print("Welcome to 'Guess the Number' game!")
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guessed_correctly = False

    while not guessed_correctly:
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        attempts += 1

        if user_guess < number_to_guess:
            print("Too low! Try again.")
        elif user_guess > number_to_guess:
            print("Too high! Try again.")
        else:
            guessed_correctly = True
            print(f"Congratulations! You guessed the number {number_to_guess} in {attempts} attempts.")


# Run the game
guess_the_number()
