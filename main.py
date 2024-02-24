import random
from art import logo
print(logo)
def guess_number():
    print("I am thinking of a number between 1 and 100.")
    global difficulty_level
    difficulty_level = input("Choose a difficulty: type 'easy' or 'hard': ").lower()
    if difficulty_level == "easy":
        attempts = 10
    elif difficulty_level == "hard":
        attempts = 5
    else:
        print("Invalid difficulty choice. Please type 'easy' or 'hard'.")
        return

    number_to_guess = random.randint(1, 100)

    print(f"You have {attempts} attempts remaining to guess the number.")

    while attempts > 0:
        guess = int(input("Make a guess: "))

        if guess > number_to_guess:
            print("Too high, guess again.")
        elif guess < number_to_guess:
            print("Too low, guess again.")
        else:
            print(f"Congratulations! You guessed the number {number_to_guess} correctly!")
            break

        attempts -= 1
        print(f"You have {attempts} attempts remaining to guess the number.")

    if attempts == 0:
        print(f"Sorry, you've run out of attempts. The correct number was {number_to_guess}.")

guess_number()
