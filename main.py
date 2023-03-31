from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
            't', 'u', 'v', 'w', 'x', 'y', 'z']


# encrypts user message by shifting letters forward in alphabet by user_shift letters
def encrypt(user_text, user_shift):
    encrypted_word = []

    for letter in user_text:
        new_letter_index = alphabet.index(letter) + user_shift

        if new_letter_index > 25:
            new_letter_index = abs(new_letter_index - 26)

        encrypted_word.append(alphabet[new_letter_index])

    encrypted_word = ''.join(encrypted_word)
    print(f"The encrypted message is: {encrypted_word}.")
    return encrypted_word


# decrypts user message by shifting letters backward in alphabet by user_shift letters
def decrypt(user_text, user_shift):
    decrypted_word = []

    for letter in user_text:
        new_letter_index = alphabet.index(letter) - user_shift

        if new_letter_index < 0:
            new_letter_index = abs(new_letter_index + 26)

        decrypted_word.append(alphabet[new_letter_index])

    decrypted_word = ''.join(decrypted_word)
    print(f"The decrypted message is: {decrypted_word}.")
    return decrypted_word


def caesar_cipher():

    print(logo)

    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    new_word = []

    for letter in text:

        if direction == "encode":
            new_letter_index = alphabet.index(letter) + shift

            if new_letter_index > 25:
                new_letter_index = abs(new_letter_index - 26)

            new_word.append(alphabet[new_letter_index])
        elif direction == "decode":
            new_letter_index = alphabet.index(letter) - shift

            if new_letter_index < 0:
                new_letter_index = abs(new_letter_index + 26)

            new_word.append(alphabet[new_letter_index])
        else:
            print("Invalid option. Exiting program.")
            return

    new_word = ''.join(new_word)

    if direction == "encode":
        print(f"Your encoded word is: {new_word}")
    else:
        print(f"Your decoded word is: {new_word}")


caesar_cipher()
