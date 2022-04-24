import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Write your code below this line 👇

rps_ascii = [rock, paper, scissors]
player_choice = int(
    input('What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: '))
computer_choice = random.randint(0, 2)

if player_choice > 2 or player_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(f'\nYou chose: {rps_ascii[player_choice]}')
    print(f'\nComputer chose: {rps_ascii[computer_choice]}')

    if player_choice == computer_choice:
        print('\nDraw\n')
    elif player_choice == 0 and computer_choice == 1:
        print('\nYou Lose.\n')
    elif player_choice == 0 and computer_choice == 2:
        print('\nYou Win!\n')
    elif player_choice == 1 and computer_choice == 0:
        print('\nYou Win!\n')
    elif player_choice == 1 and computer_choice == 2:
        print('\nYou Lose.\n')
    elif player_choice == 2 and computer_choice == 0:
        print('\nYou Lose.\n')
    elif player_choice == 2 and computer_choice == 1:
        print('\nYou Win!\n')

    # Other Logic:
    #
    # if user_choice == 0 and computer_choice == 2:
    #         print("You win!")
    #     elif computer_choice == 0 and user_choice == 2:
    #         print("You lose")
    #     elif computer_choice > user_choice:
    #         print("You lose")
    #     elif user_choice > computer_choice:
    #         print("You win!")
    #     elif computer_choice == user_choice:
    #         print("It's a draw")
