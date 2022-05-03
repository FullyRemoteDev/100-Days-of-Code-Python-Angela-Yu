import random
import hangman_art
import hangman_words

# Update the word list to use the 'word_list' from hangman_words.py
# Delete this line: word_list = ["aardvark", "baboon", "camel"]
# word_list = ["aardvark", "baboon", "camel"]
# Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word = random.choice(hangman_words.word_list)
word_length = len(random_word)
game_over = False

# Create a variable called 'lives' to keep track of the number of lives left.
# Set 'lives' to equal 6.
player_lives = 6

# Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo)

# Testing code
print(f"\nFor Testing, the word is {random_word}.\n")


# Create an empty List called display.
# For each letter in the chosen_word, add a "_" to 'display'.
# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 "_" representing each letter to guess.
guess_display = []
for i in range(word_length):
    guess_display.append("_")


# Use a while loop to let the user guess again. The loop should only stop once the user has guessed all the letters in the chosen_word and 'display' has no more blanks ("_"). Then you can tell the user they've won.

while not game_over:

    # Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
    player_guess = input("\nGuess a letter: ").lower()

    # If the user has entered a letter they've already guessed, print the letter and let them know.
    if player_guess in guess_display:
        print(f"\nYou've already guessed {player_guess}.\n")
        continue

    # Check guessed letter
    # Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
    # Loop through each position in the chosen_word;
    # If the letter at that position matches 'guess' then reveal that letter in the display at that position.
    # e.g. If the user guessed "p" and the chosen word was "apple", then display should be ["_", "p", "p", "_", "_"].
    for position in range(word_length):
        char = random_word[position]
        if player_guess == char:
            guess_display[position] = char

    # If guess is not a letter in the chosen_word,
    # Then reduce 'lives' by 1.
    # If lives goes down to 0 then the game should stop and it should print "You lose."
    if player_guess not in random_word:
        player_lives -= 1
        # If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(
            f"\nYou guessed {player_guess}, which is not in the word. You lose a life. You have {player_lives} lives remaining.\n")
        if player_lives == 0:
            game_over = True
            print("\nYou Lose.")

    # Print 'display' and you should see the guessed letter in the correct position and every other letter replace with "_".
    # Join all the elements in the list and turn it into a String.
    print(f"\n{' '.join(guess_display)}\n")

    # Check if user has got all letters.
    if "_" not in guess_display:
        game_over = True
        print("\nYou Win!")

    # Print the ASCII art from 'stages' that corresponds to the current number of 'lives' the user has remaining.
    # Import the stages from hangman_art.py
    print(hangman_art.stages[player_lives])
