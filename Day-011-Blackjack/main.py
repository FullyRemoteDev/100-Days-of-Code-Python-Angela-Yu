############### Our Blackjack House Rules #####################

# The deck is unlimited in size.
# There are no jokers.
# The Jack/Queen/King all count as 10.
# The the Ace can count as 11 or 1.
# Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
# The cards in the list have equal probability of being drawn.
# Cards are not removed from the deck as they are drawn.
# The computer is the dealer.


import art
import random


def deal_card():
    cards_deck = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = int(random.choice(cards_deck))
    return random_card


def calc_score(cards_list):
    sum_cards = sum(cards_list)
    if sum_cards == 21 and len(cards_list) == 2:
        return 0

    if 11 in cards_list and sum_cards > 21:
        cards_list.remove(11)
        cards_list.append(1)
        sum_cards = sum(cards_list)
        return sum_cards
    else:
        return sum_cards


def win_lose(player_score, computer_score):
    if player_score > 21 and computer_score > 21:
        return "\nYour value is more than 21. You Lose. 👎✌"
    elif player_score == computer_score:
        return "\nDraw. 🤝"
    elif computer_score == 0:
        return "\nComputer has a Blackjack. You Lose. 👎"
    elif player_score == 0:
        return "\nYou have a Blackjack. You Win! 👍👏"
    elif player_score > 21:
        return "\nYour value is more than 21. You Lose. 👎"
    elif computer_score > 21:
        return "\nYou Win! Computer value is more than 21. 👍"
    elif player_score > computer_score:
        return "\nYou Win! 👍"
    else:
        return "\nYou Lose. 👎"


def main_game():

    print(art.logo)

    game_over = False

    player_hand = []
    computer_hand = []

    for _ in range(2):
        player_hand.append(deal_card())
        computer_hand.append(deal_card())

    while not game_over:
        player_score = calc_score(player_hand)
        computer_score = calc_score(computer_hand)
        print(
            f"\n\tYour cards: {player_hand}, current score: {sum(player_hand)}")
        print(f"\n\tComputer's first card: {computer_hand[0]}\n")

        if player_score == 0 or computer_score == 0 or player_score > 21:
            game_over = True
        else:
            new_card_choice = input(
                "\nType 'y' to get another card, type 'n' to pass: ")
            if new_card_choice == 'y':
                player_hand.append(deal_card())
            else:
                game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_hand.append(deal_card())
        computer_score = calc_score(computer_hand)

    print(
        f"\n\tYour final hand: {player_hand}, final value: {sum(player_hand)}")
    print(
        f"\t Computer's final hand: {computer_hand}, final value: {sum(computer_hand)}")
    result = win_lose(player_score, computer_score)
    print(result)


while input(
        "\nDo you want to play a game of Blackjack? Type 'y' or 'n': ") == 'y':
    main_game()
