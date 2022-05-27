import art

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
cipher_run = True

print(f'\n {art.logo} \n')


def caesar(input_text, shift_number, direction_type):
    return_text = ''
    new_position = ''
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            if direction_type == 'encode':
                if position > (25 - shift_number):
                    new_position = shift_number - (26 - position)
                else:
                    new_position = position + shift_number
            elif direction_type == 'decode':
                if position < shift_number:
                    new_position = 26 - (shift_number - position)
                else:
                    new_position = position - shift_number
            return_text += alphabet[new_position]
        else:
            return_text += char
    print(f"\nThe {direction_type}d text is {return_text}\n")


while cipher_run == True:
    direction = input(
        "\nType 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # If the user enters a shift that is greater than the number of letters in the alphabet
    if shift >= 26:
        shift %= 26

    caesar(text, shift, direction)

    # If the user want to restart the cipher program
    user_choice = input(
        "\nDo you want to use the cipher program again? Type 'yes' or 'no': ").lower()
    if user_choice == 'yes':
        cipher_run = True
    elif user_choice == 'no':
        print('\nThank you!\n')
        cipher_run = False
