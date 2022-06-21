import random
import art

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5


# Check User's guess with Computer's guess
def check_guess(user_guess, computer_pick, user_attempts):
    if user_guess == computer_pick:
        print(f"\nYou guessed it correctly. It was {computer_pick}.\n")
    elif user_guess > computer_pick:
        print("Your guess is high.")
        user_attempts -= 1
        return user_attempts
    elif user_guess < computer_pick:
        print("Your guess is low.")
        user_attempts -= 1
        return user_attempts


# Set number of attempts for the user to guess
def set_difficulty():
    user_difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
    if user_difficulty == 'easy':
        return EASY_ATTEMPTS
    elif user_difficulty == 'hard':
        return HARD_ATTEMPTS


print(art.logo)
print("\nWelcome to the Number Guessing Game!")
print("\nI'm thinking of a number between 1 and 100.")
computer_pick = random.randint(1, 100)

# Display the Computer's pick for testing
print(f"\nThe guessed number is: {computer_pick}")

user_attempts = set_difficulty()

user_guess = 0
while user_guess != computer_pick:
    print(
        f"\nYou have {user_attempts} attempts remaining to guess the number.")
    user_guess = int(input("\nMake a guess: ").strip())

    user_attempts = check_guess(user_guess, computer_pick, user_attempts)

    if user_attempts == 0:
        print("\nYour attempts are over. You Lose.\n")
        break
    elif user_guess != computer_pick:
        print("Try again.")
