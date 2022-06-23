import random
import art
import game_data


def random_data():
    """Randomly select a dict from game_data.py list and return it"""
    return random.choice(game_data.data)


def format_data(data_dict):
    """Format the sentence to display to the user"""
    return f"{data_dict['name']}, a {data_dict['description']}, from {data_dict['country']}"


def compare_choice(user_choice, followers_a, followers_b):
    """Compare the user guess with the correct answer"""
    if user_choice == 'a':
        user_data = followers_a
    elif user_choice == 'b':
        user_data = followers_b

    if followers_a > followers_b:
        winning_data = followers_a
    elif followers_a < followers_b:
        winning_data = followers_b

    if user_data == winning_data:
        return True


def game_logic():
    # Display game art
    print(art.logo)

    user_score = 0
    game_over = False
    data_a = random_data()
    data_b = random_data()

    while not game_over:
        data_a = data_b
        data_b = random_data()

        while data_a == data_b:
            data_b = random_data()

        print(f"Compare A: {format_data(data_a)}")
        # Revealing the follower count for testing
        # print(f"Hint: Follower count is {data_a['follower_count']} millions.")
        print(art.vs)
        print(f"Compare B: {format_data(data_b)}")
        # Revealing the follower count for testing
        # print(f"Hint: Follower count is {data_b['follower_count']} millions.")

        # Prompt the user asking for their choice
        user_choice = input(
            "\nWho has more followers? Type 'A' or 'B': ").lower()

        followers_a = data_a['follower_count']
        followers_b = data_b['follower_count']

        user_correct = compare_choice(user_choice, followers_a, followers_b)

        if user_correct:
            # If the user got it correct, continue
            user_score += 1
            print(f"\nYou are right! Current score: {user_score}.\n")
        else:
            # If the user got it wrong, the game is over
            game_over = True
            print(f"\nYou got it wrong. Final score: {user_score}\n")


# Main game
game_logic()
